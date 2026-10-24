import json, html
BOOK = "https://bookings-slidingrockcabins.escapia.com/Unit/Details/31096#availTab"
SITE = "https://stayatriversolace.com/"
photos = json.load(open('/workspace/real_estate/ellijay_str/site/_build/photos.json'))

def book(label, cls="btn"):
    return f'<a class="{cls}" href="{BOOK}" target="_blank" rel="noopener">{label}</a>'

gallery = "\n".join(
    f'''<a class="g-item{' g-wide' if i in (0,8,21,34) else ''}" href="img/full/{p["n"]}.jpg" data-webp="img/full/{p["n"]}.webp" data-cap="{html.escape(p["cap"])}" data-i="{i}">
  <picture><source srcset="img/thumb/{p["n"]}.webp" type="image/webp"><img src="img/thumb/{p["n"]}.jpg" alt="{html.escape(p["cap"])}" width="{p["tw"]}" height="{p["th"]}" loading="lazy" decoding="async"></picture></a>'''
    for i, p in enumerate(photos))

amen = [
 ("🌊","On the Ellijay River","Waterfront at the end of a private road"),
 ("♨️","Private hot tub on the deck","Soak with the river running just below"),
 ("🎣","Fish from the deck","Cast a line right off the porch"),
 ("🔥","Riverside fire pit","Gas grill &amp; picnic table with extra lighting"),
 ("🪑","Big covered porch","Four rocking chairs looking out on the water"),
 ("🛏️","Two king beds","Pillow-top king on the main level, king in the loft"),
 ("🛁","Two bathrooms","Spa-quality soap, towels, robes &amp; hair dryers"),
 ("🐕","Dogs welcome","Fenced yard, dog bed, bowls &amp; treats, no pet fee"),
 ("🪵","Gas log fireplace","Cozy living room with a 55&Prime; smart TV"),
 ("📺","Media / reading room","Sofa &amp; TV with FireStick; TV includes NFL package"),
 ("🍳","Full kitchen","Dishwasher, coffee beans, grinder &amp; cookware"),
 ("📶","Free high-speed Wi-Fi","Central heat &amp; air, washer &amp; dryer"),
 ("🎲","Games &amp; books","For slow evenings in"),
]
amen_html = "\n".join(f'<li><span class="a-ico" aria-hidden="true">{e}</span><div><strong>{t}</strong><span>{d}</span></div></li>' for e,t,d in amen)

reviews = [
 ("It was so nice to be able to fish off the porch in the mornings and enjoy peace and quiet.","Dawn R.","Oct 2025"),
 ("We have stayed at this property about 7 times now. It is just a perfect getaway for the 2 of us. It feels like home.","Denise M.","Sep 2025"),
 ("Beautiful, immaculate cabin along a babbling stream&hellip; HIGHLY recommend this cabin, perhaps our favorite of all time.","Raymond N.","May 2026"),
]
rev_html = "\n".join(f'<figure class="review"><blockquote>&ldquo;{q}&rdquo;</blockquote><figcaption>&mdash; {n}, {d}</figcaption></figure>' for q,n,d in reviews)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="index, follow, max-image-preview:large">
<title>River Solace | Dog-Friendly Riverfront Log Cabin in Ellijay, GA</title>
<meta name="description" content="River Solace is a private, adults-only 2-bedroom, 2-bath log cabin on the Ellijay River in North Georgia. Private hot tub on the deck, riverside fire pit, fishing from the deck, and dogs welcome with no pet fee.">
<link rel="canonical" href="{SITE}">
<meta name="theme-color" content="#2f4a3a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="River Solace">
<meta property="og:title" content="River Solace | Riverfront Log Cabin in Ellijay, GA">
<meta property="og:description" content="A private, dog-friendly log cabin for up to 4 adults, right on the Ellijay River. Private hot tub on the deck, riverside fire pit and fishing from the deck.">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="River Solace log cabin on the bank of the Ellijay River">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="River Solace | Riverfront Log Cabin in Ellijay, GA">
<meta name="twitter:description" content="Private, dog-friendly riverfront log cabin for up to 4 adults in North Georgia.">
<meta name="twitter:image" content="{SITE}img/og-image.jpg">
<link rel="icon" href="logo/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="logo/favicon-32.png">
<link rel="apple-touch-icon" href="logo/apple-touch-icon.png">
<link rel="preload" as="image" href="img/hero-mobile.webp" media="(max-width: 767px)">
<link rel="preload" as="image" href="img/hero-desktop.webp" media="(min-width: 768px)">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{json.dumps({
 "@context":"https://schema.org","@type":"VacationRental","name":"River Solace",
 "description":"Private, adults-only, dog-friendly 2-bedroom, 2-bath log cabin on the Ellijay River with a private hot tub on the deck and a riverside fire pit.",
 "image":SITE+"img/og-image.jpg","url":SITE,
 "address":{"@type":"PostalAddress","addressLocality":"Ellijay","addressRegion":"GA","addressCountry":"US"},
 "containsPlace":{"@type":"Accommodation","numberOfBedrooms":2,"numberOfBathroomsTotal":2,"occupancy":{"@type":"QuantitativeValue","maxValue":4}},
 "petsAllowed":True,
 "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in ["Private hot tub","Riverfront","Fire pit","Covered porch","Gas grill","Fireplace","Free Wi-Fi","Full kitchen","Washer and dryer"]]})}</script>
</head>
<body>
<header class="topbar" id="top">
  <a class="brand" href="#top" aria-label="River Solace home">
    <img src="logo/logo-emblem-256.webp" alt="" width="44" height="38">
    <span>River Solace</span>
  </a>
  <nav class="nav" aria-label="Sections">
    <a href="#stay">The Cabin</a><a href="#amenities">Amenities</a><a href="#gallery">Photos</a><a href="#area">Area</a><a href="#rules">Rules</a><a href="guides/">Guides</a>
  </nav>
  {book("Book Now","btn btn-sm")}
</header>

<section class="hero">
  <picture class="hero-bg">
    <source media="(max-width: 767px)" srcset="img/hero-mobile.webp" type="image/webp">
    <source media="(max-width: 767px)" srcset="img/hero-mobile.jpg">
    <source srcset="img/hero-desktop.webp" type="image/webp">
    <img src="img/hero-desktop.jpg" alt="River Solace's deck and covered porch right on the bank of the Ellijay River" fetchpriority="high" width="1920" height="1028">
  </picture>
  <div class="hero-bar">
    <div class="hero-text">
      <p class="hero-title">Riverfront log cabin &middot; Ellijay, GA</p>
      <p class="hero-sub">2 BR &middot; 2 BA &middot; 4 adults &middot; dogs welcome &middot; hot tub</p>
    </div>
    <div class="hero-cta">
      {book("Check Availability","btn btn-hero")}
      <span class="fine hero-fine">Reservations handled by Sliding Rock Cabins</span>
    </div>
  </div>
</section>

<main>
<section class="section intro" id="stay">
  <div class="wrap two-col">
    <div>
      <picture><source srcset="logo/logo-riversolace.webp" type="image/webp"><img class="intro-logo" src="logo/logo-riversolace.png" alt="River Solace &mdash; Ellijay, Georgia" width="640" height="587" loading="lazy"></picture>
      <p class="eyebrow">Welcome to River Solace</p>
      <h1>Your own quiet bend of the river</h1>
      <p>At the quiet end of a gravel road outside Ellijay, River Solace is a full-log cabin set right on the bank of the Ellijay River. There are no neighbors on top of you here, and the river does most of the talking.</p>
      <p>Mornings start with fresh-ground coffee in a rocker on the big covered porch, or with a fishing line dropped straight off the deck. Later, fire up the gas grill, eat at the picnic table, and finish the evening around the stone fire pit by the water, then slip into the private hot tub on the deck.</p>
      <p>Inside it&rsquo;s all warm logs and easy comfort: a gas log fireplace, a pillow-top king downstairs, a second king in the loft, two baths, and a snug media and reading room. The cabin sleeps four adults (guests 25 and up). Dogs are family here, with a fenced yard, a welcome kit for them, and never a pet fee.</p>
      <p class="note">Good to know: the last stretch is on gravel mountain roads. Four-wheel drive isn&rsquo;t required, but take it slow and steady.</p>
    </div>
    <figure class="intro-photo">
      <picture><source srcset="img/full/rs-05.webp" type="image/webp"><img src="img/full/rs-05.jpg" alt="Deck seating over the river" loading="lazy" width="1366" height="768"></picture>
    </figure>
  </div>
</section>

<section class="section alt" id="amenities">
  <div class="wrap">
    <p class="eyebrow">What&rsquo;s here</p>
    <h2>Amenities</h2>
    <ul class="amenities">
{amen_html}
    </ul>
    <div class="layout">
      <div><h3>Main level</h3><p>King pillow-top bed &middot; full bath with tub/shower &middot; living room with fireplace &middot; full kitchen &middot; media/reading room</p></div>
      <div><h3>Upstairs loft</h3><p>King bed &middot; bathroom &middot; TV with FireStick</p></div>
      <div><h3>Outside</h3><p>Covered riverfront porch &middot; private hot tub on the deck &middot; fire pit by the water &middot; gas grill &amp; picnic table &middot; fenced dog yard</p></div>
    </div>
    <p class="pawnote">&#128062; Dog guests get a welcome kit too: dog bed, bowls, treats, toys and muddy-paw towels. (No cats, please.)</p>
  </div>
</section>

<section class="section" id="gallery">
  <div class="wrap">
    <p class="eyebrow">Take a look around</p>
    <h2>Photo gallery</h2>
    <div class="gallery">
{gallery}
    </div>
  </div>
</section>

<section class="section reviews-sec" id="reviews">
  <div class="wrap">
    <p class="eyebrow">Guests keep coming back</p>
    <h2>Loved by our guests</h2>
    <div class="rating">
      <span class="score">9.4</span>
      <div><strong>Exceptional</strong><span>9.4 out of 10 from 209 reviews on Vrbo</span></div>
    </div>
    <div class="review-grid">
{rev_html}
    </div>
    <p class="fine center">Excerpts from guest reviews posted on Sliding Rock Cabins&rsquo; River Solace page.</p>
  </div>
</section>

<section class="section alt" id="area">
  <div class="wrap">
    <p class="eyebrow">Out &amp; about</p>
    <h2>Exploring Ellijay</h2>
    <p class="lead">Ellijay is a small mountain town in the North Georgia foothills, known as Georgia&rsquo;s Apple Capital. There&rsquo;s plenty to do when you can pull yourself away from the porch.</p>
    <div class="cards">
      <article><h3>&#127822; Apple orchards</h3><p>From late summer through fall, family orchards around Ellijay open for apple picking, cider, fried pies and farm markets.</p></article>
      <article><h3>&#127863; Wineries</h3><p>The surrounding hills are dotted with vineyards and tasting rooms. A relaxed afternoon of tastings is an easy drive away.</p></article>
      <article><h3>&#128758; Rivers &amp; outdoors</h3><p>Fish right at the cabin on the Ellijay River, or float, tube and paddle the nearby Cartecay River. The Chattahoochee National Forest offers trails and waterfalls.</p></article>
      <article><h3>&#9968;&#65039; Blue Ridge</h3><p>The mountain town of Blue Ridge, with its shops, restaurants, scenic railway and lake, makes a great day trip.</p></article>
      <article><h3>&#127979; Downtown Ellijay</h3><p>Stroll the historic square for local shops, antiques and restaurants, plus seasonal events like the Georgia Apple Festival each October.</p></article>
    </div>
    <p class="guide-links"><strong>Trip guides:</strong> <a href="guides/florida-to-north-georgia-mountains/">Mountain getaway from Florida</a> &middot; <a href="guides/ellijay-apple-festival-orchards/">Apple Festival &amp; orchards</a> &middot; <a href="guides/fall-colors-ellijay/">Fall colors</a> &middot; <a href="guides/things-to-do-ellijay-blue-ridge/">Things to do</a> &middot; <a href="guides/riverfront-cabin-hot-tub-north-georgia/">Riverfront cabin with hot tub</a></p>
  </div>
</section>

<section class="section" id="rules">
  <div class="wrap narrow">
    <p class="eyebrow">Before you book</p>
    <h2>House rules</h2>
    <ul class="rules">
      <li><strong>Adults only:</strong> up to 4 guests, all age 25 or older.</li>
      <li><strong>Dogs welcome:</strong> no pet fee, no breed or weight limits. No cats.</li>
      <li><strong>No parties or events:</strong> River Solace is a quiet retreat; please respect the neighbors and the river.</li>
      <li><strong>Getting here:</strong> gravel mountain roads; drive with care.</li>
    </ul>
    <p class="fine">Full policies, rates and cancellation terms are shown when you book.</p>
  </div>
</section>

<section class="cta" id="book">
  <div class="wrap narrow center">
    <img src="logo/logo-emblem-256.webp" alt="" width="120" height="104" loading="lazy">
    <h2>Ready for a little river time?</h2>
    <p>Check open dates and reserve River Solace directly.</p>
    {book("Book Your Stay","btn btn-lg")}
    <p class="fine">Reservations handled by Sliding Rock Cabins</p>
  </div>
</section>
</main>

<footer class="footer">
  <p>River Solace &middot; Ellijay, Georgia &middot; GA STR Host License #002890</p>
  <p class="fine"><a href="guides/">Ellijay &amp; North Georgia trip guides</a></p>
  <p class="fine">Additional photos courtesy of Sliding Rock Cabins &middot; &copy; 2026 River Solace</p>
</footer>

<div class="mobile-book">{book("Check Availability","btn btn-block")}</div>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button class="lb-close" aria-label="Close">&times;</button>
  <button class="lb-prev" aria-label="Previous photo">&#8249;</button>
  <figure><picture><source id="lb-webp" type="image/webp"><img id="lb-img" alt=""></picture><figcaption id="lb-cap"></figcaption></figure>
  <button class="lb-next" aria-label="Next photo">&#8250;</button>
</div>
<script src="main.js" defer></script>
</body>
</html>
'''
open('/workspace/real_estate/ellijay_str/site/index.html','w').write(page)
print("ok", len(page))
