"""Blog content.

WRITING RULES, which are the app's safety rules applied to prose:

  * Never recommend, adjust or imply a dose. Not "most people start at 0.25",
    not "you should be on". Explain mechanics; the prescriber decides.
  * Never diagnose or triage. Severe or persistent symptoms go to a clinician.
  * Every clinical number is attributable — an FDA label, a named guideline —
    or it is described as what it is, a general figure.
  * The competitor quotes are real, harvested reviews, quoted with the app they
    were left on. They are evidence, not marketing.

Each post is (slug, title, description, date, image, body, faq).
"""

POSTS = [
    # ----------------------------------------------------------------------
    (
        "what-4313-glp1-app-reviews-say",
        "What 4,313 GLP-1 app reviews actually say people need",
        "We read every App Store review of 27 GLP-1 tracking apps. Here is what people praise, what makes them angry, and the four things they ask for most.",
        "2026-09-16",
        "img/blog-reviews.jpg",
        """
<p class="lede">We harvested <strong>4,313 App Store reviews across 27 GLP-1 tracking apps</strong>
from the US and UK storefronts, then read the complaints and the praise separately. This is what
the people using these apps say, in their own words, rather than what app makers think they want.</p>

<p>A note on method, because it changes the numbers. One app in the set is a 2010
WeightWatchers-style tracker with 89,971 ratings that bolted GLP-1 features on later. Its reviews
are overwhelmingly about billing disputes that have nothing to do with GLP-1 tracking, and leaving
it in skews every theme. The headline figures below are the <strong>3,656 reviews of GLP-1-native
trackers</strong>, with that one held out.</p>

<h2>Price is a third of every complaint</h2>

<p>Of 662 reviews at three stars or below, <strong>32.9% are about price or the paywall</strong>.
Not "it is expensive" — that would be ordinary. The pattern is people who could not evaluate the
app before being asked to pay for it:</p>

<blockquote>
<p>"You immediately have to pay $70. There is no option to try it for free. Why am I paying $70 if
I don't even know if it works for me yet?"</p>
<p>"Downloaded because there's supposed to be free functionality, but the app would not let me do
ANYTHING unless I subscribed."</p>
<p>"I was hoping there was a limited functionality free version to try… you literally can't track
ANYTHING without the membership, not even weight."</p>
</blockquote>

<p>And from the highest-rated app in the category, repeatedly, a narrower version of the same
complaint — that the feature people came for is the one behind the wall:</p>

<blockquote>
<p>"The free version doesn't contain the most useful thing about the app, which is the estimated
medication levels."</p>
</blockquote>

<h2>The second most praised thing is simplicity</h2>

<p>Across 2,994 reviews at four stars or above, weight and progress tracking is praised most
(37.1%) and <strong>simplicity is second at 32.7%</strong>. That is a remarkable number for
something no app markets itself on.</p>

<p>It is also the thing the category keeps destroying. A recurring shape in the two-star reviews is
a long-time user describing an app they loved before an update reorganised it. If you are choosing
a tracker, an app that has resisted the urge to redesign is worth more than one with a longer
feature list.</p>

<h2>Four things people ask for, in order</h2>

<p>414 reviews contain an explicit feature request. Counted:</p>

<table>
<thead><tr><th>Request</th><th>Reviews</th></tr></thead>
<tbody>
<tr><td>Water tracking</td><td>39</td></tr>
<tr><td>Better charts and trends</td><td>38</td></tr>
<tr><td>A real food database</td><td>33</td></tr>
<tr><td>Apple Health</td><td>19</td></tr>
<tr><td>A home screen widget</td><td>16</td></tr>
<tr><td>Export for a doctor</td><td>15</td></tr>
</tbody>
</table>

<p>Water is the clear leader, and the reviews explain why: people treat water, protein and fibre as
one thing. The happiest reviewers of one competitor repeat almost the same sentence — "helps me
track water, protein and fiber". Dehydration is also a real and common concern on these
medications, which is a conversation for your prescriber rather than an app.</p>

<h2>The angriest reviews in the entire set are about lost data</h2>

<p>Data loss is only 4.2% of complaints by volume, but it produces the most furious writing in the
corpus, and it happened to the category leader:</p>

<blockquote>
<p>"Updated the app this evening and have lost all my previous jab records and weight loss
progress. Absolutely gutted."</p>
<p>"Thanks for the update it's wiped out my history for last 18 months 🤬🤬"</p>
<p>"Love the app but when I got a new phone there's no way to transfer all your data. The app just
keeps making you start over. So I canceled my subscription."</p>
</blockquote>

<p>If you are picking a tracker, this is the question worth asking before you commit a year of
your history to it: <em>can I get my data out?</em> An app that cannot export is an app you can
only leave by starting over.</p>

<h2>There is an AI backlash</h2>

<p>5.4% of complaints mention AI features, and essentially all of them are negative — inaccurate
food recognition, chatbots that replace things that used to be buttons, and in one case an AI
suggestion a reviewer described as unsafe. In a category built on numbers people are putting into
their own medical record, "the computer guessed" is not a feature.</p>

<blockquote>
<p>"The AI identification of food gives you its best guess. No meal planning component and the
GLP-1 tracking is a prediction of average daily reminder of medicine. No science behind it."</p>
</blockquote>

<h2>Food tracking is where these apps are weakest</h2>

<p>Food is 16.5% of complaints, second only to price, and the failure comes in two shapes. Some
apps have no food tracking at all:</p>

<blockquote>
<p>"This app doesn't do anything I can't already do with MyFitnessPal. No food tracking, minimal
features, and not worth the subscription price."</p>
</blockquote>

<p>Others have it, and the data is wrong:</p>

<blockquote>
<p>"My can of tuna has 20g of protein and it came up 16g."</p>
<p>"I'm finding very few of my food items in the search, and when I scan them, it almost always
comes up with incorrect [data]."</p>
</blockquote>

<p>This matters more on a GLP-1 than it would otherwise. Appetite drops sharply, total intake falls
with it, and <a href="../protein-on-a-glp-1/">protein is the number most people are told to
protect</a>. A protein figure that is 20% wrong is not a rounding error when you are eating
900 calories a day.</p>

<h2>What we took from this</h2>

<p>We build <a href="../../index.html">GLP-1 Tracker</a>, so treat this section as interested
rather than neutral. The research changed what we built: water tracking, export and restore, and
Apple Health all shipped because of these numbers, not because we thought of them. Logging stays
free — all of it, with no account — because a third of the complaints in this category are from
people who were never allowed to try the thing before paying for it.</p>

<p>The raw data and the scripts that produced it live in our repository. We would rather the
numbers were checkable than impressive.</p>
""",
        [
            (
                "How many GLP-1 app reviews were analysed?",
                "4,313 App Store reviews across 27 apps, harvested from the US and UK storefronts on both most-recent and most-helpful sort. Headline figures use the 3,656 reviews of GLP-1-native trackers, excluding one general weight-loss app whose billing complaints skew every theme.",
            ),
            (
                "What do people complain about most in GLP-1 tracking apps?",
                "Price and paywalls, at 32.9% of all reviews of three stars or below. The specific pattern is being asked to pay before being able to evaluate the app at all.",
            ),
            (
                "What feature do GLP-1 app users ask for most?",
                "Water tracking, mentioned in 39 of the 414 reviews containing an explicit feature request, followed by better charts (38) and a real food database (33).",
            ),
        ],
    ),
    # ----------------------------------------------------------------------
    (
        "protein-on-a-glp-1",
        "Protein on a GLP-1: why it is the number to watch",
        "Appetite falls fast on a GLP-1. Why protein is the number most people are told to protect, and how to track it without counting every meal.",
        "2026-09-16",
        "img/blog-protein.jpg",
        """
<p class="lede">Most food trackers put calories at the top because most people using them are
trying to eat fewer of them. On a GLP-1, eating less is the part that is already happening. The
harder problem is what you eat within a much smaller total — and protein is the number most people
are told to protect.</p>

<h2>Why the usual advice inverts</h2>

<p>GLP-1 receptor agonists slow gastric emptying and reduce appetite. That is the mechanism, and it
works: intake drops, often sharply, often without much conscious effort. The consequence is that a
calorie ceiling stops being the binding constraint. You are very unlikely to overshoot. You are
quite likely to undershoot on protein, because protein-dense food is also the food that feels
heaviest when you have no appetite.</p>

<p>Weight lost is not all fat. Some of it is lean mass, and the proportion depends partly on
protein intake and resistance training. This is well-established nutrition science that long
predates these medications, and it is the reason clinicians talking about GLP-1 courses talk about
protein so much.</p>

<p><strong>What we are not going to do here is give you a number.</strong> Protein targets depend
on your body, your goal, your kidney function and what else is going on, and the person who should
set yours is your prescriber or a dietitian. What follows is about the mechanics of tracking it.</p>

<h2>Where the general figures come from</h2>

<p>You will see roughly 1.2–2.0 g of protein per kilogram of body weight quoted in general
nutrition guidance for people losing weight or maintaining muscle, with the higher end associated
with an energy deficit and resistance training. Those are population-level figures from nutrition
literature, not a prescription, and a clinician's number for you beats any of them.</p>

<p>Our app suggests a starting figure so the ring on the home screen has a denominator on day one.
It uses 1.6 g per kilogram, applied to your goal weight where you have set one, with a floor at 75%
of your current weight so an ambitious goal does not produce an implausibly small number. You can
see that explanation inside the app, next to the number, by tapping "Why this number?" — and you
can change it to whatever you were actually told.</p>

<h2>Tracking it without tracking everything</h2>

<p>The common failure with food logging is that it is exhausting, so people do it perfectly for
nine days and then stop. A few things make it survivable:</p>

<ul>
<li><strong>Log the protein sources, not the meal.</strong> If you are watching one number, you do
not need to itemise the salad. The yoghurt, the chicken, the shake — those are the entries that
move the figure.</li>
<li><strong>Scan the things you eat repeatedly.</strong> Most people eat a surprisingly small
rotation. Scanning a barcode once and re-logging it afterwards takes seconds.</li>
<li><strong>Check the database against the label.</strong> Food data varies in quality, and it is
worth spot-checking a few of your regulars. Reviews of GLP-1 apps are full of people finding
protein figures that are simply wrong — one reviewer of a competing app found a tuna can listed at
16 g against a label that said 20 g. We use USDA FoodData Central and real barcode data, and it
still pays to look.</li>
<li><strong>Accept partial days.</strong> A log with gaps is still more useful than no log. The
trend is the point.</li>
</ul>

<h2>The other two numbers people watch alongside it</h2>

<p>In the review corpus we analysed, the happiest users of GLP-1 apps repeat one phrase almost
word for word: they track "water, protein and fiber". Those three travel together for a reason.
Appetite suppression cuts fluid intake along with food, and fibre intake tends to fall with total
volume — which matters given how commonly constipation comes up in these reviews. Whether any of
that applies to you is a question for your clinician, not a tracker.</p>

<h2>What this looks like in the app</h2>

<p>Protein is the largest thing on our home screen and calories are a small tile underneath it.
That is a deliberate inversion of how almost every food app is laid out, and it is the single
clearest expression of what the app is for. Logging food, scanning barcodes and setting your own
protein target are free, with no account.</p>

<p><a class="btn" href="https://apps.apple.com/app/id6805192887">Get GLP-1 Tracker on the App
Store</a></p>
""",
        [
            (
                "Why is protein important on a GLP-1 medication?",
                "Appetite and total intake fall sharply on a GLP-1, and weight lost includes some lean mass as well as fat. Protein intake, alongside resistance training, is associated with preserving lean mass during weight loss. Your protein target should be set by your prescriber or a dietitian.",
            ),
            (
                "How much protein should I eat on Ozempic or Mounjaro?",
                "That is a question for your prescriber or a dietitian, and depends on your body, your goal and your kidney function. General nutrition guidance for people losing weight quotes roughly 1.2 to 2.0 g per kilogram of body weight, but those are population figures rather than advice for any individual.",
            ),
            (
                "Do I have to log every meal to track protein?",
                "No. Logging only the protein sources — the yoghurt, the chicken, the shake — moves the number that matters, and a log with gaps is far more useful than a log you abandon.",
            ),
        ],
    ),
    # ----------------------------------------------------------------------
    (
        "injection-site-rotation",
        "Injection site rotation: a system you will actually keep to",
        "Rotating injection sites is standard guidance for subcutaneous injections. The hard part is remembering where you went last time. Here is a simple way to do it.",
        "2026-09-16",
        "img/blog-rotation.jpg",
        """
<p class="lede">Every set of instructions that comes with a subcutaneous injection pen says to
rotate your injection site. Almost nobody is told <em>how</em> to keep track, and after a few
months of weekly shots most people are relying on a vague memory of "the left one, I think".</p>

<h2>Why the guidance exists</h2>

<p>Repeatedly injecting the same spot is associated with local skin and tissue changes, which is
why rotation appears in the patient instructions for these products. The manufacturer's
instructions for use that came with your pen or vial are the authority here — read them, and ask
your prescriber or pharmacist if anything is unclear. Nothing on this page replaces them.</p>

<p>What we can be useful about is the bookkeeping.</p>

<h2>The sites, and why a list beats a habit</h2>

<p>The usual subcutaneous sites for these medications are the abdomen, the front of the thigh and
the back of the upper arm, avoiding the area immediately around the navel and any skin that is
bruised, tender, scarred or hardened. Within a region there is a lot of usable area, which is
exactly why people drift back to the same square inch: there is no landmark, so the hand goes where
it went last time.</p>

<p>A written record fixes this in a way that intention does not. Two approaches work:</p>

<ul>
<li><strong>A fixed cycle.</strong> Decide an order — left abdomen, right abdomen, left thigh,
right thigh, and so on — and follow it. Simple, and it fails the first time you miss a week and
lose your place.</li>
<li><strong>Least-recently-used.</strong> Record where each shot went, and next time pick whichever
site you have not used for longest. Self-correcting, because a missed week cannot put you out of
sequence.</li>
</ul>

<p>The second is what our app does. When you log a shot, it suggests the site you have gone
longest without using, based on the ones you have actually recorded. It is a convenience, not a
medical instruction — you can tap a different one, and nothing in the app will argue with you.</p>

<h2>What to record</h2>

<p>The useful minimum is the date and the site. If you also record how the site felt afterwards,
you have something concrete to show a clinician if you ever need to, which is easier than
reconstructing three months from memory. Injection site reactions are one of the symptoms our app
lets you log against your dose history, for exactly that reason.</p>

<h2>A note on what a tracker cannot do</h2>

<p>An app can tell you where you last injected. It cannot look at your skin. If a site is
painful, hard, persistently red, or changing, that is a conversation with your prescriber or
pharmacist, and it is not one an app should be having with you. Ours deliberately does not try —
when you log a severe symptom it says plainly that it cannot assess symptoms and points you at
your clinician.</p>

<h2>Rotation in the app</h2>

<p>Logging a shot takes one screen: the amount, the date and time, and the site, with the
least-recently-used one already suggested. It is free, there is no account, and your history stays
on your phone.</p>

<p><a class="btn" href="https://apps.apple.com/app/id6805192887">Get GLP-1 Tracker on the App
Store</a></p>
""",
        [
            (
                "Where can GLP-1 medications be injected?",
                "The usual subcutaneous sites are the abdomen, the front of the thigh and the back of the upper arm, avoiding the area immediately around the navel and any skin that is bruised, tender, scarred or hardened. Follow the instructions for use that came with your pen or vial, and ask your prescriber or pharmacist if anything is unclear.",
            ),
            (
                "How do I keep track of injection site rotation?",
                "Record the date and site of every shot, then choose whichever site you have gone longest without using. That least-recently-used approach is self-correcting, unlike a fixed cycle, which breaks the first time you miss a week.",
            ),
            (
                "Does GLP-1 Tracker suggest an injection site?",
                "Yes. When you log a shot it suggests the site you have gone longest without using, based on the shots you have recorded. It is a convenience rather than a medical instruction, and you can pick any site you like.",
            ),
        ],
    ),
    # ----------------------------------------------------------------------
    (
        "vial-dosing-units-and-milligrams",
        "Vials and syringe units: why the number on your syringe is not milligrams",
        "A pen tells you milligrams; a vial tells you units. What each means, and why your vial's concentration is the number that connects them.",
        "2026-09-16",
        "img/blog-vial.jpg",
        """
<p class="lede">A pen tells you milligrams. A vial and syringe tell you units. They are not the
same number and they are not interchangeable, and the thing that connects them — the concentration
of what is in your vial — is printed on the vial rather than being a property of the drug.</p>

<p><strong>Read this as background, not as instructions.</strong> What you draw up is set by your
prescriber and by the vial in your hand. If the arithmetic below does not match what you were told,
what you were told is right and you should ask your prescriber or pharmacist. This page exists
because a lot of people move from a pen to a compounded vial and are handed two different units
with no explanation of how they relate.</p>

<h2>The three numbers</h2>

<dl>
<dt>Milligrams (mg)</dt>
<dd>The amount of drug. This is the number your prescriber talks in, and the number a pen is
labelled with.</dd>

<dt>Concentration (mg/mL)</dt>
<dd>How much drug is dissolved in each millilitre of liquid in <em>your</em> vial. Compounded
vials come in different concentrations, so this is not a fact about the medication — it is a fact
about the specific vial, printed on the specific label.</dd>

<dt>Syringe units</dt>
<dd>Marks on the barrel of an insulin syringe. On the common U-100 syringe, <strong>one unit is
0.01 mL</strong> — that is a measure of volume, and it says nothing at all about how much drug is
in that volume.</dd>
</dl>

<h2>How they connect</h2>

<p>Because a U-100 unit is 0.01 mL, the volume you draw and the amount of drug in it are related
by the concentration:</p>

<p class="formula">milligrams = units × 0.01 × concentration (mg/mL)</p>

<p>Which means the same mark on the same syringe delivers different amounts from different vials.
Twenty units is 0.2 mL either way. From a 2.5 mg/mL vial that is 0.5 mg; from a 5 mg/mL vial the
identical 20 units is 1 mg. <strong>Twice the drug, same number on the syringe.</strong></p>

<p>This is the whole reason the distinction matters, and it is why "I take twenty units" is not a
dose anybody else can interpret without also knowing your vial.</p>

<h2>Where this goes wrong</h2>

<ul>
<li><strong>Switching vials.</strong> A new vial at a different concentration changes the number of
units for the same dose. The unit count you memorised belongs to the old vial.</li>
<li><strong>Syringes that are not U-100.</strong> The 0.01 mL per unit figure is specific to U-100.
Check what you have.</li>
<li><strong>Repeating a unit count between people.</strong> Advice in a forum expressed in units is
meaningless without the concentration, and potentially dangerous if the concentrations differ.</li>
</ul>

<p>If any of those apply to you, the answer is your prescriber or pharmacist, not arithmetic from a
blog post.</p>

<h2>What a tracker can honestly do here</h2>

<p>It can record what you did, in both numbers, so your history means something months later. Our
app lets you enter a dose in either milligrams or syringe units and shows the other as you type,
using the concentration you recorded for that course. That is a conversion, not a recommendation:
the app never proposes an amount, never prefills one from your recorded strength, and never
advances you along a schedule.</p>

<p>If you have not recorded a concentration for a compounded vial, it will not guess one. It asks
for milligrams instead, because inventing a concentration would mean inventing a number in your
own medical record.</p>

<h2>A word on compounded medication</h2>

<p>Compounded semaglutide and tirzepatide are not the branded products and do not carry the same
published pharmacokinetic data. Our app reproduces the manufacturers' published half-lives for the
branded medications — from the FDA prescribing information, with the label revision recorded
alongside each value — and for a compounded course it says plainly that it cannot know, because
the compound is not a published product. An estimate presented confidently would be worse than no
estimate.</p>

<p><a class="btn" href="https://apps.apple.com/app/id6805192887">Get GLP-1 Tracker on the App
Store</a></p>
""",
        [
            (
                "How many milligrams is one unit on an insulin syringe?",
                "It depends entirely on the concentration of your vial. On a U-100 syringe one unit is 0.01 mL of volume, so milligrams = units × 0.01 × the vial's concentration in mg/mL. The same 20 units delivers 0.5 mg from a 2.5 mg/mL vial and 1 mg from a 5 mg/mL vial.",
            ),
            (
                "Why do vials use units when pens use milligrams?",
                "A syringe measures volume, and its unit marks are a volume scale. A pen is labelled by the amount of drug it delivers. The concentration printed on your vial is what converts between the two, and it varies between vials.",
            ),
            (
                "Can GLP-1 Tracker convert between units and milligrams?",
                "Yes. You can enter a dose in either and it shows the other as you type, using the concentration you recorded for that course. It is a conversion only — the app never suggests, prefills or adjusts a dose.",
            ),
        ],
    ),
    # ----------------------------------------------------------------------
    (
        "keep-your-glp1-data-when-you-change-phones",
        "Getting your GLP-1 history onto a new phone",
        "Losing a year of injection history to a new phone is a common complaint. How to avoid it, and what to ask before trusting an app with your log.",
        "2026-09-16",
        "img/blog-export.jpg",
        """
<p class="lede">Of all the reviews we read across 27 GLP-1 tracking apps, the angriest are not
about price or bugs. They are from people who lost their history.</p>

<blockquote>
<p>"Thanks for the update it's wiped out my history for last 18 months 🤬🤬"</p>
<p>"Love the app but when I got a new phone there's no way to transfer all your data. The app just
keeps making you start over. So I canceled my subscription."</p>
</blockquote>

<p>A GLP-1 course runs for months or years. The log is the only record of what you took, when, and
how you felt — and it is often the thing you want in front of you at an appointment. It is worth
ten minutes of thought before you have accumulated a year of it.</p>

<h2>The question to ask before you commit</h2>

<p>Not "does it sync", but <strong>"can I get a file out?"</strong> Those are different promises.
Sync ties your history to an account and a company; if either goes away, so does the data. A file
is yours regardless.</p>

<p>The two useful forms are:</p>

<ul>
<li><strong>A spreadsheet (CSV)</strong> — for a human. This is what you send a doctor, and a
request for exactly this appears fifteen times in the reviews we read, almost always phrased as
"export for my doctor".</li>
<li><strong>A full backup file</strong> that the app itself can read back. This is what actually
survives a new phone. A CSV of your shots is readable, but it will not restore your course
settings, your targets or your symptom history.</li>
</ul>

<p>An app that offers neither is one you can only leave by starting over.</p>

<h2>The privacy trade-off, stated honestly</h2>

<p>Apps that keep everything on your device — ours included — are more private and
<em>more</em> exposed to this particular failure, not less. There is no server holding a copy,
because there is no server. If the phone goes in a river, the file you exported is the only
recovery there is.</p>

<p>That is a real cost of local-first design and we would rather say so than pretend otherwise.
The mitigation is that exporting is free, takes two taps, and produces a file you control.</p>

<h2>A routine that takes about a minute</h2>

<ol>
<li>Export whenever something changes that you would mind losing — a new course, a dose change, or
just once a month.</li>
<li>Save it somewhere that is not only on the phone. Files, iCloud Drive, a cloud drive, an email
to yourself. Anywhere the phone is not the only copy.</li>
<li><strong>Before</strong> you set up a new phone, not after.</li>
<li>On the new phone, install the app and restore from the file.</li>
</ol>

<h2>How it works in our app</h2>

<p>Settings → Export your data produces a JSON backup plus a CSV per thing — shots, weight, food,
water, symptoms — and hands them to the normal iOS share sheet, so you choose where they go.
Nothing is uploaded; the file leaves only because you sent it somewhere.</p>

<p>Restore takes the JSON back. It offers to add to what is on the phone or to replace it, and it
matches entries by content rather than by internal id — which means restoring the same file twice
does not double your history. That sounds like a detail and is the difference between a restore
and a mess.</p>

<p>The export contains <strong>everything</strong>, not the ninety days a free account can browse.
The free tier limits what you can look at inside the app. It has never limited what you can take
out of it, and it never will.</p>

<p><a class="btn" href="https://apps.apple.com/app/id6805192887">Get GLP-1 Tracker on the App
Store</a></p>
""",
        [
            (
                "How do I move my GLP-1 tracking history to a new phone?",
                "Export a full backup file from the old phone before you switch, save it somewhere other than the phone itself, then restore it on the new one. A CSV alone is not enough — it is readable by a person but will not restore your course settings, targets and symptom history.",
            ),
            (
                "Can I export my GLP-1 log for my doctor?",
                "In GLP-1 Tracker, yes: Settings → Export your data produces a spreadsheet for each of shots, weight, food, water and symptoms, plus a full backup file, handed to the normal iOS share sheet. It includes your whole history, not just the last ninety days.",
            ),
            (
                "Is my data uploaded anywhere?",
                "No. GLP-1 Tracker keeps everything in a database on your phone. The only time a file leaves the device is when you export it and choose where to send it.",
            ),
        ],
    ),
    # ----------------------------------------------------------------------
    (
        "estimated-medication-level-chart",
        "What an 'estimated level' chart is, and what it is not",
        "Several GLP-1 apps draw a curve of medication in your system. The arithmetic behind it, why it is an estimate, and where it stops meaning much.",
        "2026-09-16",
        "img/blog-level.jpg",
        """
<p class="lede">It is the feature people in this category like most, and the one most likely to be
misread. A curve showing medication "in your system" looks like a measurement. It is not one. It is
arithmetic on the dates you typed in.</p>

<h2>The arithmetic</h2>

<p>Every one of these curves is built from one idea: a drug leaves the body at a rate proportional
to how much is left, so the amount remaining halves over a fixed period. That period is the
<strong>half-life</strong>, and for the branded GLP-1 medications it is published in the FDA
prescribing information — section 12.3, the same document your pharmacist works from. Semaglutide's
is about a week, which is why those products are weekly.</p>

<p>From that, the contribution of a single dose at any later moment is:</p>

<p class="formula">remaining = dose × 2<sup>−(time since dose ÷ half-life)</sup></p>

<p>and the curve is the sum of that across every dose you have logged. That is the whole model. It
is a single-compartment decay, the simplest pharmacokinetic model there is.</p>

<h2>What it is genuinely good for</h2>

<ul>
<li><strong>Seeing the accumulation.</strong> If you dose weekly and the half-life is about a week,
you are injecting before the previous dose has cleared. The curve makes the ramp-up over the first
several weeks visible, which surprises people.</li>
<li><strong>Making sense of the shape of a week.</strong> Plenty of people notice that days two and
six feel different. A decay curve is a reasonable thing to hold that observation against.</li>
<li><strong>Seeing what a missed or late shot did.</strong> The dip is obvious.</li>
</ul>

<h2>What it is not</h2>

<p>It is not a blood level. Nothing in your phone is measuring anything. We label ours "Estimated
level" everywhere, never "blood level", and we put a footnote under every chart saying it is a
simplified estimate based on published half-life, that individual results vary, and that it is not
a medical measurement. That is not legal throat-clearing; a curve drawn confidently invites
decisions it cannot support.</p>

<p>Specifically, the model ignores absorption — it treats a dose as arriving instantly, when in
reality it enters over hours — as well as individual variation in clearance, body weight, kidney
function, and everything else a real pharmacokinetic model accounts for. The published half-life is
a population figure, not yours.</p>

<p>And the thing it must never be used for: <strong>deciding what to inject or when.</strong> A
curve is not a reason to move a dose. That decision belongs to your prescriber, every time.</p>

<h2>Where it stops being meaningful at all</h2>

<p>Compounded semaglutide and tirzepatide have no published half-life, because the compound is not
a published product. Any app drawing a confident curve for a compounded vial is applying a number
it does not have. Ours draws the curve — people find the shape useful — but says plainly in the
footnote that this medication has no published half-life and the curve is a rough illustration
only. An estimate presented as if it were sourced is worse than no estimate.</p>

<h2>Why ours is free</h2>

<p>The clearest single finding from reading 4,313 reviews in this category was how often people
complain about paying for the feature they came for. From the highest-rated app in the category,
more than once:</p>

<blockquote>
<p>"The free version doesn't contain the most useful thing about the app, which is the estimated
medication levels."</p>
</blockquote>

<p>Ours is in the free tier, along with unlimited logging, the full offline food database and
barcode scanning, injection site rotation and reminders. No account.</p>

<p><a class="btn" href="https://apps.apple.com/app/id6805192887">Get GLP-1 Tracker on the App
Store</a></p>
""",
        [
            (
                "Is an estimated medication level chart a blood level?",
                "No. Nothing in a phone measures anything in your body. The curve is arithmetic applied to the doses and dates you logged, using the half-life published in the medication's prescribing information. It is an estimate, individual results vary, and it is not a medical measurement.",
            ),
            (
                "How is the estimated level calculated?",
                "Each dose decays by half every half-life, so its remaining contribution is dose × 2^(−time since dose ÷ half-life), and the curve is the sum across every dose logged. It is a single-compartment decay model and ignores absorption time and individual variation.",
            ),
            (
                "Does the chart work for compounded semaglutide?",
                "Only as a rough illustration. Compounded products have no published half-life because they are not published products, so any app drawing a confident curve for one is using a number it does not have. GLP-1 Tracker says so in the footnote rather than implying a source it does not have.",
            ),
        ],
    ),
]
