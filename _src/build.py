#!/usr/bin/env python3
"""Builds the static site into ../ .

    python3 _src/build.py

Everything it writes is plain HTML with no runtime dependencies, which is both
the fastest a page can be and the only thing GitHub Pages needs to serve.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from posts import POSTS  # noqa: E402
from layout import (  # noqa: E402
    APP_STORE,
    BASE,
    Page,
    app_schema,
    breadcrumb_schema,
    e,
    faq_schema,
    post_schema,
    website_schema,
    write,
    write_feed,
    write_robots,
    write_sitemap,
)

PRETTY_DATE = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December",
}


def pretty(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{int(d)} {PRETTY_DATE[m]} {y}"


def faq_html(pairs) -> str:
    """Visible FAQ.

    The JSON-LD and the visible text are generated from the same list on
    purpose: structured data that does not match what is on the page is a
    manual action waiting to happen, and Google says so explicitly.
    """
    items = "".join(
        f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in pairs
    )
    return f'<section class="faq"><h2>Common questions</h2>{items}</section>'


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

HOME_FAQ = [
    (
        "Is GLP-1 Tracker free?",
        "Yes. Unlimited logging of shots, food, weight, water and symptoms is free, with no account, along with the full offline food database, barcode scanning, injection site rotation, reminders and the estimated level chart. Premium adds history beyond 90 days, insights, custom macro targets and themes.",
    ),
    (
        "Do I need an account?",
        "No, and there is never a login wall. Everything is stored in a database on your phone.",
    ),
    (
        "Which medications does it support?",
        "Ozempic, Wegovy, Rybelsus, Mounjaro, Zepbound, Saxenda, Victoza and Trulicity, plus a custom option for compounded or vial medication with dosing in syringe units or milligrams.",
    ),
    (
        "Does it work offline?",
        "Yes. The food database — about 98,000 foods — ships inside the app, and barcode lookups check local data first. You can log everything in airplane mode.",
    ),
    (
        "Does it send my health data anywhere?",
        "No. Nothing is uploaded and no analytics service receives a health value. The only network request the app makes is a barcode lookup to Open Food Facts, which sends the barcode and nothing else. Its App Store privacy label is Data Not Collected.",
    ),
    (
        "Can I get my data out?",
        "Yes. Settings → Export your data produces a full backup file plus a spreadsheet per thing for your doctor, and restore brings your history onto a new phone. The export always contains everything, never just the last 90 days.",
    ),
    (
        "Does it tell me what dose to take?",
        "Never. It does not prescribe, recommend or adjust doses, and it cannot assess symptoms. Titration schedules shown in the app are reproductions of the manufacturers' published labelling, for reference. Your prescriber decides your dose.",
    ),
]


def build_home() -> Page:
    body = f"""
<section class="hero">
  <div class="hero-copy">
    <h1>The GLP-1 tracker that actually tracks your food.</h1>
    <p class="lede">Log your shots, your protein, your weight and how you feel. Everything stays on
    your phone — no account, and it works with no signal.</p>
    <p class="cta">
      <a class="btn" href="{APP_STORE}">Download on the App Store</a>
    </p>
    <p class="fine">Free to download. Unlimited logging, offline food search and barcode scanning
    are free forever. iPhone, iOS 15 and later. 12 languages.</p>
  </div>
  <div class="hero-shot">
    <img src="img/screen-today.webp" width="320" height="695"
         alt="The Today screen of GLP-1 Tracker, showing a large protein ring, calorie, carb and fat
              tiles, a water total with quick-add buttons, and the next shot due."
         fetchpriority="high" decoding="async">
  </div>
</section>

<section class="pillars">
  <h2>Four things that are unusual about it</h2>
  <div class="grid">
    <article>
      <h3>A real food database</h3>
      <p>About 98,000 foods from USDA FoodData Central, plus barcode scanning, all of it inside the
      app. The highest-rated GLP-1 app in the category has no food tracking at all, and several of
      the ones that do return figures their users say are wrong.</p>
    </article>
    <article>
      <h3>Protein first, not calories</h3>
      <p>On a GLP-1 you are unlikely to overshoot calories and quite likely to undershoot protein.
      The protein ring is the largest thing on the home screen; calories are a small tile
      underneath. <a href="blog/protein-on-a-glp-1/">Why that inversion matters</a>.</p>
    </article>
    <article>
      <h3>Nothing leaves your phone</h3>
      <p>No account, no server, no analytics receiving a health value. The App Store privacy label
      is <em>Data Not Collected</em>, and it is literally true. You can still export everything
      whenever you want.</p>
    </article>
    <article>
      <h3>No AI guessing at your record</h3>
      <p>Food comes from a database, not a model's best guess. Half-lives come from FDA prescribing
      information, quoted with the label revision. In a category with a measurable AI backlash, we
      would rather be checkable.</p>
    </article>
  </div>
</section>

<section class="feature">
  <img src="img/screen-doses.webp" width="280" height="608" loading="lazy" decoding="async"
       alt="The Doses screen, showing an estimated medication level curve, a plain count of doses
            taken, and a shot history.">
  <div>
    <h2>Your shots, and what they add up to</h2>
    <p>Every injection with its dose, date and site, and a suggested site each time based on
    wherever you have gone longest without using. An estimated level chart drawn from the
    half-life published in the manufacturer's own labelling — free, where the category leader
    charges for it.</p>
    <p>Adherence is shown as a plain count, never a streak and never a score. Missing a dose is
    often a medical decision, and gamifying that would be wrong.</p>
    <p><a href="blog/estimated-medication-level-chart/">What the estimated level curve is, and what
    it is not</a></p>
  </div>
</section>

<section class="feature reverse">
  <img src="img/screen-vial.webp" width="280" height="608" loading="lazy" decoding="async"
       alt="Logging a dose from a vial, showing the same dose expressed in both milligrams and
            syringe units.">
  <div>
    <h2>Vials and compounded doses, in the units you actually use</h2>
    <p>Enter a dose in milligrams or in syringe units and see the other as you type, using the
    concentration on your vial. It is a conversion and nothing more — the app never proposes an
    amount, never prefills one, and never advances you along a schedule.</p>
    <p><a href="blog/vial-dosing-units-and-milligrams/">Why the number on your syringe is not
    milligrams</a></p>
  </div>
</section>

<section class="feature">
  <img src="img/screen-weight.webp" width="280" height="608" loading="lazy" decoding="async"
       alt="The Weight screen, showing individual weigh-ins and a smoothed trend line.">
  <div>
    <h2>Weight, water and how you feel</h2>
    <p>A smoothed trend line, so one bad morning is not a story. Water with a two-tap quick add —
    the single most requested feature in this whole category. Side effects logged against your dose
    history, so a pattern has somewhere to show up.</p>
    <p>Apple Health can fill the trend from a connected scale, if you want it. It is optional, off
    until you switch it on, and the app works identically without it.</p>
  </div>
</section>

<section class="showreel">
  <h2>Twenty seconds of the actual app</h2>
  <p class="lede">Real screens from the shipped build, not a mock-up.</p>
  <video class="reel" width="1280" height="720" poster="video/hero-poster.webp"
         autoplay muted loop playsinline preload="none"
         aria-label="A silent twenty-second tour of GLP-1 Tracker: the food database, the protein
                     ring on the Today screen, and the estimated medication level chart.">
    <source src="video/hero.mp4" type="video/mp4">
  </video>
</section>

<section class="quiet">
  <h2>Built on 4,313 reviews, not guesses</h2>
  <p>Before deciding what to build, we read every App Store review of 27 GLP-1 tracking apps and
  counted what people actually complain about and ask for. Water tracking, export, and Apple Health
  all shipped because of that, not because we thought of them.</p>
  <p><a href="blog/what-4313-glp1-app-reviews-say/">Read what the reviews say &rarr;</a></p>
</section>

{faq_html(HOME_FAQ)}

<section class="closing">
  <h2>Free, and free to leave</h2>
  <p>Logging is free forever with no account. Your history is yours, exportable in two taps, and
  stays on your phone until you send it somewhere.</p>
  <p><a class="btn" href="{APP_STORE}">Download on the App Store</a></p>
</section>
"""
    return Page(
        path="index.html",
        title="GLP-1 Tracker — shot, food and weight log for Ozempic, Mounjaro and compounded",
        description=(
            "Track GLP-1 shots, protein, water and weight in one app. Offline food database, "
            "barcode scanning and a free estimated level chart. No account."
        ),
        body=body,
        image="og/default.jpg",
        schema=[app_schema(), website_schema(), faq_schema(HOME_FAQ)],
    )


# --------------------------------------------------------------------------
# Blog
# --------------------------------------------------------------------------

def build_posts() -> list[Page]:
    pages: list[Page] = []
    for slug, title, desc, published, image, body, faq in POSTS:
        page = Page(
            path=f"blog/{slug}/index.html",
            title=f"{title} — GLP-1 Tracker",
            description=desc,
            body="",
            image=image,
            published=published,
            nav="blog",
        )
        # Depth-correct the asset paths in the hand-written body.
        rendered = f"""
<article class="post">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="../../index.html">Home</a> <span aria-hidden="true">/</span>
    <a href="../">Blog</a>
  </nav>
  <h1>{e(title)}</h1>
  <p class="byline"><time datetime="{published}">{pretty(published)}</time> · GLP-1 Tracker</p>
  <img class="post-hero" src="../../{image}" width="1200" height="630" loading="lazy"
       decoding="async" alt="">
  {body}
  {faq_html(faq)}
  <aside class="note">
    <p><strong>A log, not medical advice.</strong> GLP-1 Tracker is for people already prescribed a
    GLP-1 medication. Nothing on this page prescribes, recommends or adjusts a dose, and nothing
    here can assess a symptom. Talk to your prescriber or pharmacist.</p>
  </aside>
</article>
"""
        page.body = rendered
        page.schema = [
            post_schema(page),
            faq_schema(faq),
            breadcrumb_schema(
                [
                    ("Home", f"{BASE}/"),
                    ("Blog", f"{BASE}/blog/"),
                    (title, page.url),
                ]
            ),
        ]
        pages.append(page)
    return pages


def build_blog_index(posts: list[Page]) -> Page:
    cards = "".join(
        f"""
  <article class="card">
    <h2><a href="{p.path[len('blog/'):-len('index.html')]}">{e(p.title.rsplit(' — ', 1)[0])}</a></h2>
    <p class="byline"><time datetime="{p.published}">{pretty(p.published)}</time></p>
    <p>{e(p.description)}</p>
  </article>"""
        for p in posts
    )
    body = f"""
<h1>Writing about tracking a GLP-1 course</h1>
<p class="lede">Practical pieces about the mechanics — protein, injection sites, vial arithmetic,
and what the numbers in a tracker do and do not mean. None of it is medical advice, and all of it
tries to be checkable.</p>
{cards}
"""
    return Page(
        path="blog/index.html",
        title="Blog — GLP-1 Tracker",
        description=(
            "Practical writing about tracking a GLP-1 course: protein targets, injection site "
            "rotation, vial and syringe unit arithmetic, and what an estimated level chart means."
        ),
        body=body,
        image="og/default.jpg",
        nav="blog",
        schema=[
            breadcrumb_schema([("Home", f"{BASE}/"), ("Blog", f"{BASE}/blog/")]),
        ],
    )


# --------------------------------------------------------------------------
# Static pages that already existed, rebuilt into the new layout
# --------------------------------------------------------------------------

def existing_body(filename: str) -> str:
    """The body of a page whose content is hand-written rather than generated.

    Source of truth is `_src/pages/<name>`, NOT the built file. Reading the
    output back in would make the build non-idempotent: the first run wraps the
    content in the new shell, and the second run cannot find the old markers it
    parsed the first time.

    The privacy and support URLs are referenced by the App Store listing and by
    lib/app/legal_urls.dart, and a broken legal link got this app rejected once
    (guideline 3.1.2). The filenames stay exactly as they are; only the shell
    around the content changes.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages", filename)
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip()


def build_404() -> Page:
    return Page(
        path="404.html",
        title="Page not found — GLP-1 Tracker",
        description="That page does not exist.",
        body="""
<h1>That page does not exist</h1>
<p class="lede">The link may be old, or we may have moved something.</p>
<p><a href="index.html">Go to the home page</a> or <a href="blog/">read the blog</a>.</p>
""",
        indexable=False,
    )


# --------------------------------------------------------------------------

def main() -> None:
    posts = build_posts()
    pages = [build_home(), build_blog_index(posts), *posts]

    for filename, title, desc, nav in (
        (
            "privacy.html",
            "Privacy policy — GLP-1 Tracker",
            "GLP-1 Tracker stores everything on your device. No account, no server, no analytics "
            "receiving a health value. Read the full policy.",
            "privacy",
        ),
        (
            "support.html",
            "Support — GLP-1 Tracker",
            "Help with GLP-1 Tracker: contact, common questions, and how to get your data out.",
            "support",
        ),
    ):
        pages.append(
            Page(
                path=filename,
                title=title,
                description=desc,
                body=existing_body(filename),
                nav=nav,
            )
        )

    pages.append(build_404())

    for page in pages:
        write(page)

    write_sitemap(pages)
    write_robots()
    write_feed(sorted(posts, key=lambda p: p.published, reverse=True))

    root = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
    # Serve the files verbatim. Without this GitHub Pages runs Jekyll, which
    # has opinions about directories and would need its own config to be safe.
    open(os.path.join(root, ".nojekyll"), "w").close()

    print(f"built {len(pages)} pages, sitemap, robots.txt and feed.xml")


if __name__ == "__main__":
    main()
