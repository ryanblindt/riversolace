import json, os, datetime
ROOT='/workspace/real_estate/ellijay_str/site'
SITE="https://stayatriversolace.com/"
BOOK="https://bookings-slidingrockcabins.escapia.com/Unit/Details/31096#availTab"
TODAY=datetime.date.today().isoformat()
def btn(l,c="btn"): return f'<a class="{c}" href="{BOOK}" target="_blank" rel="noopener">{l}</a>'
DRIVE=[("Tallahassee","338","6.9"),("Panama City","364","7.4"),("Pensacola","398","7.6"),("Gainesville","408","7.6"),("Jacksonville","423","7.8"),("Orlando","515","9.4"),("Tampa","533","9.8"),("Miami","739","13.6"),("Atlanta (for reference)","78","1.6")]
drive_rows="".join(f"<tr><td>{c}</td><td>{m} mi</td><td>about {h} hrs</td></tr>" for c,m,h in DRIVE)
cabin='''<section class="section alt"><div class="wrap narrow"><p class="eyebrow">Where to stay</p><h2>River Solace, right on the Ellijay River</h2>
<p>River Solace is a private 2-bedroom, 2-bath log cabin on the Ellijay River for up to 4 adults. Soak in the private hot tub on the deck, fish right off the porch, cook on the gas grill and eat on the covered porch, then end the night at the fire pit by the river. Dogs are welcome with no pet fee, and the TV includes the NFL package for game days.</p>
<p>'''+btn("Check open dates")+''' <a class="btn btn-ghost" href="/">See the cabin</a></p>
<p class="fine">Reservations are handled by Sliding Rock Cabins.</p></div></section>'''
P=[
("florida-to-north-georgia-mountains","North Georgia Mountain Getaway from Florida | River Solace, Ellijay",
 "Driving to the North Georgia mountains from Florida: drive times from Jacksonville, Orlando, Tampa, Tallahassee, Gainesville and the Panhandle to Ellijay, plus trip tips.",
 "Mountain getaway from Florida","A North Georgia mountain getaway from Florida",
 "Ellijay sits in the North Georgia foothills, close enough to Florida for a long-weekend drive and far enough to trade beach heat for cool mountain air, rivers and apple country.",
 f'''<section class="section"><div class="wrap narrow"><h2>Drive times from Florida to Ellijay</h2>
<p>Approximate driving distance and time to Ellijay, GA, without stops or traffic. Calculated with OpenStreetMap routing (OSRM) from each city center; your map app will give the best live estimate.</p>
<div class="table-wrap"><table class="drive"><thead><tr><th>From</th><th>Distance</th><th>Drive time</th></tr></thead><tbody>{drive_rows}</tbody></table></div>
<p class="fine">Most Florida routes head north toward Atlanta and then up GA-515 (the Zell Miller Mountain Parkway) into Ellijay. Atlanta-area traffic is the biggest variable; many drivers time their pass through the city outside rush hour.</p>
<h2>Why Floridians head for Ellijay</h2>
<ul class="rules"><li><strong>Real seasons:</strong> apple season in September and October, fall color from mid-October into early November, and cool winter nights made for a hot tub and a fire.</li>
<li><strong>Rivers instead of crowds:</strong> Ellijay is quieter than the busiest mountain towns, with the Ellijay and Cartecay rivers running through the area.</li>
<li><strong>Easy day trips:</strong> downtown Blue Ridge, orchards on Highway 52, wineries and the Chattahoochee National Forest are all nearby.</li></ul>
<h2>Tips for the drive</h2>
<ul class="rules"><li>Leave early or split the drive; the last stretch is mountain roads, and the cabin is reached by gravel roads, so arrive in daylight if you can.</li>
<li>Pack layers. Mountain mornings and evenings run much cooler than Florida, especially from October through April.</li>
<li>Fall weekends, especially the two Georgia Apple Festival weekends in October, book up early.</li></ul></div></section>'''),
("ellijay-apple-festival-orchards","Ellijay Apple Festival & Apple Orchards Guide | River Solace",
 "Georgia Apple Festival in Ellijay: dates, hours and admission, plus the apple orchards on Highway 52 in Georgia's Apple Capital. Stay riverfront at River Solace.",
 "Apple Festival & orchards","Ellijay Apple Festival and apple orchards",
 "Gilmer County calls itself Georgia's Apple Capital, and every fall the orchards around Ellijay fill with pickers, cider and fried pies.",
 '''<section class="section"><div class="wrap narrow"><h2>The Georgia Apple Festival</h2>
<p>The Georgia Apple Festival is held over two weekends each October at the Ellijay Lions Club Fairgrounds, 1729 South Main Street, Ellijay. It is a joint venture of the Ellijay Lions Club and the Gilmer County Chamber of Commerce, with hundreds of arts and crafts vendors, demonstrations, live music and fair food.</p>
<ul class="rules"><li><strong>2026 dates:</strong> October 10-11 and October 17-18 (the 55th festival).</li>
<li><strong>Hours:</strong> Saturdays 9 am to 6 pm, Sundays 9 am to 5 pm.</li>
<li><strong>Admission:</strong> $10 per person; children under 12 free.</li></ul>
<p class="fine">Source: <a href="https://www.georgiaapplefestival.org/" rel="noopener">georgiaapplefestival.org</a> and <a href="https://ellijaylionsclub.com/apple-festival" rel="noopener">Ellijay Lions Club</a>. Check the official site for next year's dates.</p>
<h2>Apple orchards near Ellijay</h2>
<p>Most of the orchards line Highway 52 East, an easy and scenic drive. A few to know (listed by the <a href="https://www.gilmerchamber.com/explore-the-ellijays/apple-orchards/" rel="noopener">Gilmer County Chamber</a>):</p>
<ul class="rules"><li><strong>B.J. Reece Orchards</strong> (9131 Hwy 52 E): U-pick apples, bakery and farm activities, open daily in September and October.</li>
<li><strong>Hillcrest Orchards</strong> (9696 Hwy 52 E): bakery, farm market and weekend Apple Pickin' Jubilee in season.</li>
<li><strong>Panorama Orchards &amp; Farm Market</strong> (63 Talona Mountain Rd): open year round with 20-plus apple varieties.</li>
<li><strong>Aaron Family Orchards</strong> and <strong>Mack Aaron's Apple House</strong> on Hwy 52 E: roadside apple houses.</li>
<li><strong>Mercier Orchards</strong> (Blue Ridge): open year round with U-pick, bakery, market and farm winery.</li></ul>
<p>Apples are harvested from late summer into fall. Varieties change week to week, so call ahead if you want a particular one.</p></div></section>'''),
("fall-colors-ellijay","Fall Colors near Ellijay & Blue Ridge, GA | When Leaves Peak",
 "When do the leaves peak in North Georgia? A guide to fall color around Ellijay and Blue Ridge, with timing by elevation and where to see it. Cabin with hot tub on the river.",
 "Fall colors","Fall colors near Ellijay and Blue Ridge",
 "Fall in the North Georgia mountains starts with apple season and ends with the hills turning red, orange and gold.",
 '''<section class="section"><div class="wrap narrow"><h2>When do the leaves peak?</h2>
<p>Color starts at the highest elevations in early to mid-October and works its way downhill. Mountain towns at lower elevations, like Ellijay and Blue Ridge, typically see their best color from late October into the first week of November. Weather sets the exact schedule every year: drought and early freezes can shorten the season, and a wet late summer can delay and intensify it.</p>
<p>For live reports, follow Georgia State Parks' <a href="https://gastateparks.org/LeafWatch" rel="noopener">Leaf Watch</a>, which posts color updates each fall starting in October.</p>
<h2>Planning a fall trip</h2>
<ul class="rules"><li><strong>Late September to early October:</strong> apple picking in full swing, cooler mornings, fewer crowds.</li>
<li><strong>Mid-October:</strong> the Georgia Apple Festival weekends and early color up high. The busiest time to book.</li>
<li><strong>Late October to early November:</strong> often the best color around Ellijay and Blue Ridge, with lighter crowds after the festival.</li></ul>
<h2>Ways to see the color</h2>
<ul class="rules"><li>Drive Highway 52 East through apple country.</li>
<li>Ride the Blue Ridge Scenic Railway from downtown Blue Ridge along the Toccoa River.</li>
<li>Hike in the Chattahoochee National Forest or visit nearby state parks such as Fort Mountain and Amicalola Falls.</li>
<li>Or simply watch the trees along the river from the hot tub on the deck.</li></ul></div></section>'''),
("things-to-do-ellijay-blue-ridge","Things to Do in Ellijay & Blue Ridge, GA | River Solace Guide",
 "Things to do in Ellijay and Blue Ridge, Georgia: apple orchards, wineries, river tubing, Carters Lake, the Blue Ridge Scenic Railway, hiking and downtown shopping.",
 "Things to do","Things to do in Ellijay and Blue Ridge",
 "Ellijay and Blue Ridge sit side by side in the North Georgia mountains. Here is what to do when you can pull yourself away from the porch.",
 '''<section class="section"><div class="wrap"><div class="cards">
<article><h3>Apple orchards</h3><p>U-pick apples, fried pies and cider donuts along Highway 52 East, mostly late summer through fall. <a href="/guides/ellijay-apple-festival-orchards/">Orchard guide</a>.</p></article>
<article><h3>Wineries</h3><p>North Georgia wine country surrounds Ellijay, with vineyards and tasting rooms such as Cartecay Vineyards and Engelheim Vineyards nearby.</p></article>
<article><h3>Rivers</h3><p>Fish from the deck at River Solace on the Ellijay River, or tube and paddle the Cartecay River in the warm months with local outfitters.</p></article>
<article><h3>Carters Lake</h3><p>A deep, undeveloped mountain lake run by the U.S. Army Corps of Engineers, with boating, a marina and lakeside trails.</p></article>
<article><h3>Blue Ridge</h3><p>Shops and restaurants downtown, Lake Blue Ridge, and the Blue Ridge Scenic Railway, which runs along the Toccoa River to McCaysville on the Tennessee line.</p></article>
<article><h3>Hiking &amp; waterfalls</h3><p>Trails across the Chattahoochee National Forest, plus Fort Mountain State Park and Amicalola Falls State Park within driving distance.</p></article>
<article><h3>Downtown Ellijay</h3><p>The historic square has local shops, antiques and restaurants, and hosts seasonal events, including the Georgia Apple Festival weekends in October.</p></article>
<article><h3>Game day</h3><p>The TV at River Solace includes the NFL package, so Sundays can be football on the couch and dinner on the porch.</p></article>
<article><h3>Winter &amp; holidays</h3><p>Quieter months mean easier dates, crisp nights, the gas log fireplace and the hot tub. A cozy Christmas or New Year's cabin trip.</p></article>
</div><p class="fine">Hours and seasons change; check each business before you go.</p></div></section>'''),
("riverfront-cabin-hot-tub-north-georgia","Riverfront Cabin with Hot Tub in North Georgia | River Solace",
 "Looking for a riverfront cabin with a hot tub in North Georgia? River Solace in Ellijay has a private hot tub on the deck, a fire pit by the river and fishing from the porch.",
 "Riverfront cabin with hot tub","A riverfront cabin with a hot tub in North Georgia",
 "Plenty of North Georgia cabins have a hot tub. Fewer sit right on the water. River Solace has both.",
 '''<section class="section"><div class="wrap narrow"><h2>What makes River Solace different</h2>
<ul class="rules"><li><strong>On the Ellijay River:</strong> waterfront at the end of a private road, with a big covered porch facing the water.</li>
<li><strong>Private hot tub on the deck:</strong> soak with the river running just below.</li>
<li><strong>Fire pit by the river:</strong> plus a gas grill and picnic table with extra lighting.</li>
<li><strong>Porch dining and fishing:</strong> eat outside and cast a line right off the porch.</li>
<li><strong>Two king beds, two baths:</strong> sized for two couples or a quiet trip for two. Adults only, up to 4 guests, 25 and older.</li>
<li><strong>Dog friendly:</strong> fenced yard, no pet fee, no breed or weight limits.</li>
<li><strong>Cozy inside:</strong> gas log fireplace, full kitchen, fast Wi-Fi, and a TV with the NFL package.</li></ul>
<p>It is a good fit for anniversaries, couples' weekends, fall leaf trips and winter escapes. It is not a party house: no events, and quiet is the point.</p></div></section>'''),
]
STYLE='<style>.table-wrap{overflow-x:auto}.drive{width:100%;border-collapse:collapse;margin:12px 0}.drive th,.drive td{text-align:left;padding:8px 10px;border-bottom:1px solid rgba(90,62,43,.15)}.btn-ghost{background:transparent;color:inherit;border:1px solid currentColor}.crumbs{font-size:.85rem;margin-bottom:.6em}.guide-hero{padding:56px 0 24px}</style>'
def head(title,desc,url,extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="index, follow, max-image-preview:large">
<title>{title.replace("&","&amp;")}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#2f4a3a">
<meta property="og:type" content="article">
<meta property="og:site_name" content="River Solace">
<meta property="og:title" content="{title.replace("&","&amp;")}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}img/og-image.jpg">
<meta property="og:image:alt" content="River Solace log cabin on the bank of the Ellijay River">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}img/og-image.jpg">
<link rel="icon" href="/logo/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/logo/apple-touch-icon.png">
<link rel="stylesheet" href="/styles.css">
{STYLE}
{extra}
</head>
<body>
<header class="topbar" id="top">
  <a class="brand" href="/" aria-label="River Solace home"><img src="/logo/logo-emblem-256.webp" alt="River Solace logo" width="44" height="38"><span>River Solace</span></a>
  <nav class="nav" aria-label="Sections"><a href="/#stay">The Cabin</a><a href="/#amenities">Amenities</a><a href="/#gallery">Photos</a><a href="/guides/">Guides</a></nav>
  {btn("Book Now","btn btn-sm")}
</header>
<main>'''
FOOT=f'''</main>
<footer class="footer">
  <p>River Solace - Ellijay, Georgia - GA STR Host License #002890</p>
  <p class="fine"><a href="/">Home</a> - <a href="/guides/">Trip guides</a> - &copy; 2026 River Solace</p>
</footer>
<div class="mobile-book">{btn("Check Availability","btn btn-block")}</div>
</body>
</html>
'''
urls=[SITE]
for slug,title,desc,short,h1,lead,body in P:
    url=f"{SITE}guides/{slug}/"; urls.append(url)
    ld=[{"@context":"https://schema.org","@type":"Article","headline":h1[0].upper()+h1[1:],"description":desc,"url":url,"image":SITE+"img/og-image.jpg","dateModified":TODAY,"author":{"@type":"Organization","name":"River Solace"},"publisher":{"@type":"Organization","name":"River Solace","url":SITE}},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE},{"@type":"ListItem","position":2,"name":"Guides","item":SITE+"guides/"},{"@type":"ListItem","position":3,"name":short,"item":url}]}]
    extra="".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    html=head(title,desc,url,extra)+f'''
<section class="section guide-hero"><div class="wrap narrow"><p class="crumbs"><a href="/">Home</a> / <a href="/guides/">Guides</a></p><p class="eyebrow">Ellijay, Georgia</p><h1>{h1[0].upper()+h1[1:]}</h1><p class="lead">{lead}</p></div></section>
{body}
{cabin}
'''+FOOT
    os.makedirs(f"{ROOT}/guides/{slug}",exist_ok=True); open(f"{ROOT}/guides/{slug}/index.html","w").write(html)
items="".join(f'<article><h3><a href="/guides/{s}/">{h[0].upper()+h[1:]}</a></h3><p>{d}</p></article>' for s,t,d,sh,h,l,b in P)
hub=head("Ellijay & North Georgia Trip Guides | River Solace","Trip guides for Ellijay and Blue Ridge, Georgia: driving up from Florida, the Apple Festival and orchards, fall colors, things to do, and riverfront cabins with hot tubs.",SITE+"guides/")+f'''
<section class="section guide-hero"><div class="wrap"><p class="eyebrow">Plan your trip</p><h1>Ellijay and North Georgia trip guides</h1><p class="lead">Local know-how for a stay at River Solace on the Ellijay River.</p><div class="cards">{items}</div></div></section>
{cabin}
'''+FOOT
os.makedirs(f"{ROOT}/guides",exist_ok=True); open(f"{ROOT}/guides/index.html","w").write(hub); urls.insert(1,SITE+"guides/")
open(f"{ROOT}/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open(f"{ROOT}/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
print(urls)
