"""Shared layout, SEO head and structured data for the GLP-1 Tracker site.

WHY A GENERATOR AND NOT TEN HAND-WRITTEN FILES. Every page needs a unique
title, description, canonical, Open Graph block and JSON-LD. Maintained by hand
across a growing blog that decays immediately: one page ends up with the site
title, another with last month's description, and two share a canonical. The
head is assembled from one function so it cannot drift.

Output is plain static HTML with no build step at serve time — GitHub Pages
serves it as-is, which is also the fastest thing a page can be.
"""
from __future__ import annotations

import html
import os
from dataclasses import dataclass, field
from datetime import date

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

# Trailing slash matters: every canonical and sitemap URL is built from this.
BASE = "https://tanzil114.github.io/glp1-tracker"

SITE_NAME = "GLP-1 Tracker"
APP_STORE = "https://apps.apple.com/app/id6805192887"
AUTHOR = "GLP-1 Tracker"

# The App Store listing and lib/app/legal_urls.dart both point at these exact
# filenames. Apple rejected this app once over a broken legal link (guideline
# 3.1.2). Do not "tidy" them into directories.
FROZEN_PATHS = ("privacy.html", "support.html")

OUT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


@dataclass
class Page:
    """One output page, with everything the head needs to be correct."""

    path: str          # "index.html" or "blog/protein-on-glp-1/index.html"
    title: str         # <title>, and og:title
    description: str   # meta description, and og:description
    body: str          # the <main> contents
    # Social image, relative to the site root. Every page gets one; a page
    # without an og:image is a link that pastes into a chat as a grey box.
    image: str = "og/default.jpg"
    # Blog posts only. Drives BlogPosting JSON-LD and the RSS feed.
    published: str | None = None
    updated: str | None = None
    # Extra JSON-LD blocks, already serialised.
    schema: list[str] = field(default_factory=list)
    # Excluded from sitemap and feed (404).
    indexable: bool = True
    nav: str = ""      # which nav item is current

    @property
    def url(self) -> str:
        """The canonical URL. Directory pages drop their index.html."""
        if self.path == "index.html":
            return f"{BASE}/"
        if self.path.endswith("/index.html"):
            return f"{BASE}/{self.path[: -len('index.html')]}"
        return f"{BASE}/{self.path}"

    @property
    def depth(self) -> int:
        """How many directories deep, so relative asset links work."""
        return self.path.count("/")


def e(text: str) -> str:
    """Escape for an HTML attribute or text node."""
    return html.escape(text, quote=True)


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------

def app_schema() -> str:
    """The app itself.

    DELIBERATELY NO aggregateRating. The app has no ratings yet, and inventing
    one is both dishonest and the exact thing Google strips a rich result for.
    It goes in when there are real reviews to count.
    """
    return """{
  "@context": "https://schema.org",
  "@type": "MobileApplication",
  "name": "GLP-1 Tracker",
  "operatingSystem": "iOS 15.0",
  "applicationCategory": "HealthApplication",
  "applicationSubCategory": "Medication tracker",
  "url": "%(base)s/",
  "downloadUrl": "%(store)s",
  "installUrl": "%(store)s",
  "inLanguage": ["en","de","es","fr","it","pt","nl","sv","da","ja","ko","ar"],
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Free to download. Unlimited logging of shots, food, weight and symptoms, full offline food search and barcode scanning, and the estimated level chart are free with no account."
  },
  "featureList": [
    "Log injections with dose, date and injection site",
    "Injection site rotation suggestions",
    "Estimated medication level chart from published half-lives",
    "Offline food database with barcode scanning",
    "Protein-first daily tracking",
    "Weight with a smoothed trend line",
    "Side effect logging against dose history",
    "Vial and compounded dosing in syringe units or milligrams",
    "Water tracking",
    "Export and restore your own data"
  ],
  "publisher": { "@type": "Organization", "name": "GLP-1 Tracker" }
}""" % {"base": BASE, "store": APP_STORE}


def website_schema() -> str:
    return """{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "GLP-1 Tracker",
  "url": "%(base)s/",
  "inLanguage": "en"
}""" % {"base": BASE}


def faq_schema(pairs: list[tuple[str, str]]) -> str:
    items = ",\n".join(
        """    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": { "@type": "Answer", "text": %s }
    }"""
        % (_json_str(q), _json_str(a))
        for q, a in pairs
    )
    return (
        '{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n'
        '  "mainEntity": [\n%s\n  ]\n}' % items
    )


def post_schema(page: Page) -> str:
    return """{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": %(title)s,
  "description": %(desc)s,
  "image": "%(base)s/%(img)s",
  "datePublished": "%(pub)s",
  "dateModified": "%(upd)s",
  "author": { "@type": "Organization", "name": "%(author)s", "url": "%(base)s/" },
  "publisher": { "@type": "Organization", "name": "%(author)s", "url": "%(base)s/" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "%(url)s" },
  "isAccessibleForFree": true,
  "inLanguage": "en"
}""" % {
        "title": _json_str(page.title),
        "desc": _json_str(page.description),
        "base": BASE,
        "img": page.image,
        "pub": page.published,
        "upd": page.updated or page.published,
        "author": AUTHOR,
        "url": page.url,
    }


def breadcrumb_schema(trail: list[tuple[str, str]]) -> str:
    items = ",\n".join(
        '    { "@type": "ListItem", "position": %d, "name": %s, "item": "%s" }'
        % (i + 1, _json_str(name), url)
        for i, (name, url) in enumerate(trail)
    )
    return (
        '{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n'
        '  "itemListElement": [\n%s\n  ]\n}' % items
    )


def _json_str(value: str) -> str:
    """A JSON string literal that is also safe inside a <script> element."""
    import json

    return json.dumps(value).replace("</", "<\\/")


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------

NAV = (
    ("index.html", "Home", ""),
    ("blog/", "Blog", "blog"),
    ("support.html", "Support", "support"),
    ("privacy.html", "Privacy", "privacy"),
)


def render(page: Page) -> str:
    up = "../" * page.depth
    nav_html = "".join(
        '<a href="{href}"{cur}>{label}</a>'.format(
            href=up + (href if href != "index.html" or page.depth else "index.html"),
            cur=' aria-current="page"' if key and key == page.nav else "",
            label=label,
        )
        for href, label, key in NAV
    )

    schema_html = "".join(
        '\n<script type="application/ld+json">%s</script>' % s for s in page.schema
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(page.title)}</title>
<meta name="description" content="{e(page.description)}">
<link rel="canonical" href="{page.url}">
<meta name="robots" content="{'index,follow,max-image-preview:large' if page.indexable else 'noindex,follow'}">
<meta name="theme-color" content="#0b3d3a">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="{'article' if page.published else 'website'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{e(page.title)}">
<meta property="og:description" content="{e(page.description)}">
<meta property="og:url" content="{page.url}">
<meta property="og:image" content="{BASE}/{page.image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(page.title)}">
<meta name="twitter:description" content="{e(page.description)}">
<meta name="twitter:image" content="{BASE}/{page.image}">
<link rel="icon" href="{up}icon.png" type="image/png">
<link rel="apple-touch-icon" href="{up}icon.png">
<link rel="alternate" type="application/rss+xml" title="{SITE_NAME} blog" href="{BASE}/feed.xml">
<link rel="stylesheet" href="{up}style.css">{schema_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="site">
  <a class="brand" href="{up}index.html">
    <img src="{up}icon.png" width="44" height="44" alt="">
    <span>GLP-1 Tracker</span>
  </a>
  <nav aria-label="Main">{nav_html}</nav>
</header>
<main id="main">
{page.body}
</main>
<footer class="site">
  <p><a class="btn small" href="{APP_STORE}">Get it on the App Store</a></p>
  <p class="fine"><strong>This is a log, not medical advice.</strong> GLP-1 Tracker is for people
  already prescribed a GLP-1 medication by a clinician. It does not prescribe, recommend or adjust
  doses, and it cannot assess symptoms. Your prescriber decides your dose. Talk to them about
  anything that concerns you.</p>
  <p class="fine">Nutrition data from USDA FoodData Central. Barcode data from
  Open Food Facts (ODbL). Ozempic, Wegovy, Rybelsus, Mounjaro, Zepbound, Saxenda, Victoza and
  Trulicity are trademarks of their respective owners; this app is not affiliated with, endorsed
  by, or sponsored by any of them.</p>
  <p class="fine"><a href="{up}index.html">Home</a> · <a href="{up}blog/">Blog</a> ·
  <a href="{up}support.html">Support</a> · <a href="{up}privacy.html">Privacy</a> ·
  <a href="{BASE}/feed.xml">RSS</a></p>
</footer>
</div>
</body>
</html>
"""


def write(page: Page) -> None:
    dest = os.path.join(OUT, page.path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(render(page))


# --------------------------------------------------------------------------
# sitemap / robots / feed
# --------------------------------------------------------------------------

def write_sitemap(pages: list[Page]) -> None:
    today = date.today().isoformat()
    urls = []
    for p in pages:
        if not p.indexable:
            continue
        lastmod = p.updated or p.published or today
        # The home page is the entry point; posts are the long tail.
        priority = "1.0" if p.path == "index.html" else (
            "0.8" if p.path.startswith("blog/") else "0.5"
        )
        urls.append(
            f"  <url>\n    <loc>{p.url}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <priority>{priority}</priority>\n  </url>"
        )
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(body)


def write_robots() -> None:
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(
            "User-agent: *\n"
            "Allow: /\n"
            # The generator lives in the published repo so a future session can
            # find it. It is not content and should not be indexed.
            "Disallow: /_src/\n"
            f"\nSitemap: {BASE}/sitemap.xml\n"
        )


def write_feed(posts: list[Page]) -> None:
    """RSS 2.0. Small, and the thing aggregators and readers actually take."""
    from email.utils import format_datetime
    from datetime import datetime, timezone

    def rfc822(iso: str) -> str:
        return format_datetime(
            datetime.fromisoformat(iso).replace(tzinfo=timezone.utc)
        )

    items = "\n".join(
        f"""  <item>
    <title>{e(p.title.rsplit(" — ", 1)[0])}</title>
    <link>{p.url}</link>
    <guid isPermaLink="true">{p.url}</guid>
    <pubDate>{rfc822(p.published)}</pubDate>
    <description>{e(p.description)}</description>
  </item>"""
        for p in posts
    )
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{SITE_NAME}</title>
  <link>{BASE}/</link>
  <atom:link href="{BASE}/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Practical writing about tracking a GLP-1 course, from the people who build the app.</description>
  <language>en</language>
{items}
</channel>
</rss>
"""
    with open(os.path.join(OUT, "feed.xml"), "w", encoding="utf-8") as fh:
        fh.write(body)
