"""Builds the French (fr/) and Belgian Dutch (nl/) home pages from the English one (site/index.html).

Usage: python3 site/src/build_i18n.py
The app mock-ups use the app's own translations. Every source string must be found once,
so a change to index.html that breaks a translation stops the build.
"""
import pathlib

SITE = pathlib.Path(__file__).parent.parent

# Strings shared by both translations (head, links); per language below.
COMMON = {
    'fr': [
        ('<html lang="en">', '<html lang="fr">'),
        ('<link rel="canonical" href="https://kasseigo.com/">', '<link rel="canonical" href="https://kasseigo.com/fr/">'),
        ('<meta property="og:url" content="https://kasseigo.com/">', '<meta property="og:url" content="https://kasseigo.com/fr/">'),
        ('<meta property="og:locale" content="en_GB">', '<meta property="og:locale" content="fr_BE">\n<meta property="og:locale:alternate" content="fr_FR">'),
        ('"inLanguage": "en"', '"inLanguage": "fr"'),
        ('"url": "https://kasseigo.com/",\n      "description"', '"url": "https://kasseigo.com/fr/",\n      "description"'),
        ('aria-current="page">EN</a><a href="/fr/" hreflang="fr" lang="fr">FR</a>', '>EN</a><a href="/fr/" hreflang="fr" lang="fr" aria-current="page">FR</a>'),
        ('<nav class="langs" aria-label="Language">', '<nav class="langs" aria-label="Langue">'),
        ('/legal.html?lang=en', '/legal.html'), ('/terms.html?lang=en', '/terms.html'), ('/privacy.html?lang=en', '/privacy.html'), ('/feedback.html?lang=en', '/feedback.html?lang=fr'),
    ],
    'nl': [
        ('<html lang="en">', '<html lang="nl-BE">'),
        ('<link rel="canonical" href="https://kasseigo.com/">', '<link rel="canonical" href="https://kasseigo.com/nl/">'),
        ('<meta property="og:url" content="https://kasseigo.com/">', '<meta property="og:url" content="https://kasseigo.com/nl/">'),
        ('<meta property="og:locale" content="en_GB">', '<meta property="og:locale" content="nl_BE">'),
        ('"inLanguage": "en"', '"inLanguage": "nl-BE"'),
        ('"url": "https://kasseigo.com/",\n      "description"', '"url": "https://kasseigo.com/nl/",\n      "description"'),
        ('aria-current="page">EN</a>', '>EN</a>'),
        ('<a href="/nl/" hreflang="nl-BE" lang="nl">NL</a>', '<a href="/nl/" hreflang="nl-BE" lang="nl" aria-current="page">NL</a>'),
        ('<nav class="langs" aria-label="Language">', '<nav class="langs" aria-label="Taal">'),
        # Legal pages exist in French and English only.
        ('/legal.html?lang=en', '/legal.html'), ('/terms.html?lang=en', '/terms.html'), ('/privacy.html?lang=en', '/privacy.html'), ('/feedback.html?lang=en', '/feedback.html?lang=nl'),
    ],
}

TEXT = {
    'fr': [
        ('<title>KasseiGo: shared bike &amp; e-scooter app for Brussels and Paris</title>',
         '<title>KasseiGo : appli vélos et trottinettes partagés à Bruxelles et Paris</title>'),
        ('content="Free app for shared bikes and e-scooters in Brussels and Paris: routes around cobblestones and no-ride zones, straight to a parking spot. No account, no ads."',
         'content="Appli gratuite pour vélos et trottinettes partagés à Bruxelles et Paris : itinéraires sans pavés, zones des opérateurs respectées, jusqu’à une place de stationnement. Sans compte, sans pub."'),
        ('<meta property="og:title" content="KasseiGo: ride smooth, park right">',
         '<meta property="og:title" content="KasseiGo : roulez en douceur, garez-vous juste">'),
        ('<meta property="og:description" content="Free app for shared bikes and e-scooters in Brussels and Paris: around cobblestones and no-ride zones, to a real parking spot.">',
         '<meta property="og:description" content="Appli gratuite pour vélos et trottinettes partagés à Bruxelles et Paris : sans pavés, sans zones interdites, jusqu’à une vraie place de stationnement.">'),
        ('"description": "Route-planning app for shared bikes and e-scooters in Brussels and Paris: avoids cobblestones, follows operator slow and no-ride zones, and guides you to a parking spot."',
         '"description": "Appli d’itinéraire pour vélos et trottinettes partagés à Bruxelles et Paris : évite les pavés, suit les zones lentes et interdites des opérateurs et guide jusqu’à une place de stationnement."'),
        ('<a class="btn btn-primary" href="#get">Get the app</a>', '<a class="btn btn-primary" href="#get">Obtenir l’appli</a>'),
        ('<span class="free"><b>FREE</b>No subscription, no in-app purchases</span>', '<span class="free"><b>GRATUIT</b>Sans abonnement ni achat intégré</span>'),
        ('<h1>Ride smooth.<br><span>Park right.</span></h1>', '<h1>Roulez en douceur.<br><span>Garez-vous juste.</span></h1>'),
        ('<p class="lead">The guide for shared bikes and e-scooters in Brussels and Paris (Dott, Bolt, Voi, Villo!, Vélib’). KasseiGo takes you around cobblestones and no-ride zones, and ends your trip at a real parking spot.</p>',
         '<p class="lead">Le guide des vélos et trottinettes partagés à Bruxelles et à Paris (Dott, Bolt, Voi, Villo!, Vélib’). KasseiGo vous fait éviter les pavés et les zones interdites, et termine votre trajet sur une vraie place de stationnement.</p>'),
        ('<a class="btn btn-primary" href="#get">Join the iPhone beta</a>', '<a class="btn btn-primary" href="#get">Rejoindre la bêta iPhone</a>'),
        ('<a class="btn btn-ghost" href="#why">Why KasseiGo</a>', '<a class="btn btn-ghost" href="#why">Pourquoi KasseiGo</a>'),
        ('<li>Free</li><li>No account</li><li>No ads</li><li>No tracking</li>', '<li>Gratuit</li><li>Sans compte</li><li>Sans pub</li><li>Sans pistage</li>'),
        ('alt="Home screen: shared vehicles around you on the map, and a “Where to?” search."',
         'alt="Écran d’accueil : les véhicules partagés autour de vous sur la carte, et la recherche « Where to? »."'),
        ('alt="Trip preview: 12 min to Place Eugène Flagey, with the departure and the parking spot already chosen."',
         'alt="Aperçu du trajet : 12 min jusqu’à la place Eugène Flagey, départ et place de stationnement déjà choisis."'),
        ('<h2>Built for the vehicle under your feet.</h2>', '<h2>Pensé pour le véhicule sous vos pieds.</h2>'),
        ('<p class="mut">Regular map apps know cars and bikes. They don’t know cobblestones, operator zones, or where you’re allowed to leave a scooter.</p>',
         '<p class="mut">Les applis de cartes classiques connaissent les voitures et les vélos. Elles ignorent les pavés, les zones des opérateurs et les endroits où l’on peut laisser une trottinette.</p>'),
        ('<h3>You decide how much it shakes</h3>', '<h3>Vous décidez à quel point ça secoue</h3>'),
        ('<p>Every street is rated by its surface. Set the roughest one you accept, and each trip shows how many metres of cobbles are left. <em>Kassei</em> is Brussels for cobblestone.</p>',
         '<p>Chaque rue est classée selon son revêtement. Choisissez le plus inconfortable que vous acceptez, et chaque trajet indique combien de mètres de pavés il reste. <em>Kassei</em>, c’est un pavé en bruxellois.</p>'),
        ('<h3>Zones, before they surprise you</h3>', '<h3>Les zones, avant qu’elles vous surprennent</h3>'),
        ('<p>Your operator’s slow and no-ride zones are part of the route. Choose to go around them or cross on foot, and see exactly where it happens.</p>',
         '<p>Les zones lentes et interdites de votre opérateur font partie de l’itinéraire. Choisissez de les contourner ou de les traverser à pied, et voyez exactement où ça se passe.</p>'),
        ('<h3>Know where you’ll park</h3>', '<h3>Sachez où vous garer</h3>'),
        ('<p>Pick your drop-off spot before you leave, with its free places when the operator publishes them. Guidance takes you straight there.</p>',
         '<p>Choisissez votre place avant de partir, avec le nombre de places libres quand l’opérateur le publie. Le guidage vous y mène directement.</p>'),
        ('<h3>Honest when walking wins</h3>', '<h3>Honnête quand la marche gagne</h3>'),
        ('<p>Every trip is compared with walking. When your feet are faster, KasseiGo says so and saves you the unlock fee. The vehicle stays one tap away.</p>',
         '<p>Chaque trajet est comparé à la marche. Quand vos pieds vont plus vite, KasseiGo le dit et vous évite les frais de déverrouillage. Le véhicule reste à portée de doigt.</p>'),
        ('<b>Free, for real</b><span>No subscription, no in-app purchases, no ads.</span>', '<b>Gratuit, vraiment</b><span>Sans abonnement, sans achat intégré, sans publicité.</span>'),
        ('<b>Every operator, one map</b><span><i>Brussels:</i> Dott, Bolt, Villo!<br><i>Paris:</i> Dott, Voi, Vélib’</span>',
         '<b>Tous les opérateurs, une seule carte</b><span><i>Bruxelles :</i> Dott, Bolt, Villo!<br><i>Paris :</i> Dott, Voi, Vélib’</span>'),
        ('<b>Switch operator mid-trip</b><span>Battery low? Change operator from Trip options; zones, parking and route follow.</span>',
         '<b>Changez d’opérateur en route</b><span>Batterie faible ? Changez d’opérateur depuis « Trip options » : zones, stationnement et itinéraire suivent.</span>'),
        ('<h2>Your trips are nobody’s business.</h2>', '<h2>Vos trajets ne regardent que vous.</h2>'),
        ('<p>Your location, trips, favourites and zones stay on your phone. Address search runs on the phone too. The network is only used for live vehicles, city packs and map tiles.</p>',
         '<p>Votre position, vos trajets, vos favoris et vos zones restent sur votre téléphone, tout comme la recherche d’adresses. Le réseau ne sert qu’aux véhicules en temps réel, aux fichiers des villes et aux tuiles de la carte.</p>'),
        ('<ul class="nos"><li>Free</li><li>No account</li><li>No ads</li><li>No telemetry</li></ul>', '<ul class="nos"><li>Gratuit</li><li>Sans compte</li><li>Sans pub</li><li>Sans télémétrie</li></ul>'),
        ('<h2>Your next ride, without the bumps.</h2>', '<h2>Votre prochain trajet, sans les secousses.</h2>'),
        ('<p class="mut">Free, in English, French and Dutch. In beta on iPhone, Android is on the way.</p>', '<p class="mut">Gratuit, en français, néerlandais et anglais. En bêta sur iPhone, Android arrive bientôt.</p>'),
        ('<div class="cta"><a class="btn btn-primary" href="#">Join the iPhone beta</a></div>', '<div class="cta"><a class="btn btn-primary" href="#">Rejoindre la bêta iPhone</a></div>'),
        ('<span><b>Brussels</b> · Dott, Bolt, Villo!</span>', '<span><b>Bruxelles</b> · Dott, Bolt, Villo!</span>'),
        ('<span>© 2026 KasseiGo · independent, not affiliated with any operator.</span>', '<span>© 2026 KasseiGo · indépendant, sans lien avec aucun opérateur.</span>'),
        ('>Legal notice</a> · <a href="/terms.html">Terms of use</a> · <a href="/privacy.html">Privacy</a>', '>Mentions légales</a> · <a href="/terms.html">Conditions d’utilisation</a> · <a href="/privacy.html">Confidentialité</a>'),
        ('>Feedback</a></span>', '>Envoyer un retour</a></span>'),
        ('<span>Map data © OpenStreetMap contributors · Tiles by OpenFreeMap</span>', '<span>Données cartographiques © contributeurs OpenStreetMap · Tuiles OpenFreeMap</span>'),
        ('<span>Made with <span class="heart" role="img" aria-label="love">♥</span> in Brussels</span>', '<span>Fait avec <span class="heart" role="img" aria-label="amour">♥</span> à Bruxelles</span>'),
    ],
    'nl': [
        ('<title>KasseiGo: shared bike &amp; e-scooter app for Brussels and Paris</title>',
         '<title>KasseiGo: app voor deelfietsen en deelsteps in Brussel en Parijs</title>'),
        ('content="Free app for shared bikes and e-scooters in Brussels and Paris: routes around cobblestones and no-ride zones, straight to a parking spot. No account, no ads."',
         'content="Gratis app voor deelfietsen en elektrische deelsteps in Brussel en Parijs: routes zonder kasseien, met de zones van de operator, tot aan een parkeerplek. Zonder account, zonder reclame."'),
        ('<meta property="og:title" content="KasseiGo: ride smooth, park right">',
         '<meta property="og:title" content="KasseiGo: rij zonder schokken, parkeer correct">'),
        ('<meta property="og:description" content="Free app for shared bikes and e-scooters in Brussels and Paris: around cobblestones and no-ride zones, to a real parking spot.">',
         '<meta property="og:description" content="Gratis app voor deelfietsen en deelsteps in Brussel en Parijs: om kasseien en verboden zones heen, tot aan een echte parkeerplek.">'),
        ('"description": "Route-planning app for shared bikes and e-scooters in Brussels and Paris: avoids cobblestones, follows operator slow and no-ride zones, and guides you to a parking spot."',
         '"description": "Routeplanner voor deelfietsen en elektrische deelsteps in Brussel en Parijs: vermijdt kasseien, volgt de trage en verboden zones van de operator en leidt je naar een parkeerplek."'),
        ('<a class="btn btn-primary" href="#get">Get the app</a>', '<a class="btn btn-primary" href="#get">Download de app</a>'),
        ('<span class="free"><b>FREE</b>No subscription, no in-app purchases</span>', '<span class="free"><b>GRATIS</b>Geen abonnement of aankopen</span>'),
        ('<h1>Ride smooth.<br><span>Park right.</span></h1>', '<h1>Rij zonder schokken.<br><span>Parkeer correct.</span></h1>'),
        ('<p class="lead">The guide for shared bikes and e-scooters in Brussels and Paris (Dott, Bolt, Voi, Villo!, Vélib’). KasseiGo takes you around cobblestones and no-ride zones, and ends your trip at a real parking spot.</p>',
         '<p class="lead">De gids voor deelfietsen en elektrische deelsteps in Brussel en Parijs (Dott, Bolt, Voi, Villo!, Vélib’). KasseiGo leidt je om kasseien en verboden zones heen, en eindigt je rit op een echte parkeerplek.</p>'),
        ('<a class="btn btn-primary" href="#get">Join the iPhone beta</a>', '<a class="btn btn-primary" href="#get">Doe mee aan de iPhone-bèta</a>'),
        ('<a class="btn btn-ghost" href="#why">Why KasseiGo</a>', '<a class="btn btn-ghost" href="#why">Waarom KasseiGo</a>'),
        ('<li>Free</li><li>No account</li><li>No ads</li><li>No tracking</li>', '<li>Gratis</li><li>Geen account</li><li>Geen reclame</li><li>Geen tracking</li>'),
        ('alt="Home screen: shared vehicles around you on the map, and a “Where to?” search."',
         'alt="Startscherm: de deelvoertuigen rondom jou op de kaart, en de zoekbalk “Where to?”."'),
        ('alt="Trip preview: 12 min to Place Eugène Flagey, with the departure and the parking spot already chosen."',
         'alt="Overzicht van de rit: 12 min naar het Flageyplein, met vertrekpunt en parkeerplek al gekozen."'),
        ('<h2>Built for the vehicle under your feet.</h2>', '<h2>Gemaakt voor het voertuig onder je voeten.</h2>'),
        ('<p class="mut">Regular map apps know cars and bikes. They don’t know cobblestones, operator zones, or where you’re allowed to leave a scooter.</p>',
         '<p class="mut">Gewone kaartapps kennen auto’s en fietsen. Ze kennen geen kasseien, geen zones van operatoren en weten niet waar je een step mag achterlaten.</p>'),
        ('<h3>You decide how much it shakes</h3>', '<h3>Jij beslist hoeveel het schudt</h3>'),
        ('<p>Every street is rated by its surface. Set the roughest one you accept, and each trip shows how many metres of cobbles are left. <em>Kassei</em> is Brussels for cobblestone.</p>',
         '<p>Elke straat krijgt een score voor haar wegdek. Kies het ruwste wegdek dat je aanvaardt, en elke rit toont hoeveel meter kasseien er nog overblijft. Vandaar de naam: elke Brusselaar kent de <em>kassei</em>.</p>'),
        ('<h3>Zones, before they surprise you</h3>', '<h3>Zones, nog voor ze je verrassen</h3>'),
        ('<p>Your operator’s slow and no-ride zones are part of the route. Choose to go around them or cross on foot, and see exactly where it happens.</p>',
         '<p>De trage en verboden zones van je operator zitten in de route. Kies of je ze omzeilt of te voet doorkruist, en zie precies waar dat gebeurt.</p>'),
        ('<h3>Know where you’ll park</h3>', '<h3>Weet waar je parkeert</h3>'),
        ('<p>Pick your drop-off spot before you leave, with its free places when the operator publishes them. Guidance takes you straight there.</p>',
         '<p>Kies je parkeerplek voor je vertrekt, met het aantal vrije plaatsen als de operator dat publiceert. De begeleiding brengt je er rechtstreeks naartoe.</p>'),
        ('<h3>Honest when walking wins</h3>', '<h3>Eerlijk als wandelen wint</h3>'),
        ('<p>Every trip is compared with walking. When your feet are faster, KasseiGo says so and saves you the unlock fee. The vehicle stays one tap away.</p>',
         '<p>Elke rit wordt vergeleken met wandelen. Ben je te voet sneller, dan zegt KasseiGo het en bespaar je de ontgrendelkosten. Het voertuig blijft één tik verwijderd.</p>'),
        ('<b>Free, for real</b><span>No subscription, no in-app purchases, no ads.</span>', '<b>Echt gratis</b><span>Geen abonnement, geen in-app aankopen, geen reclame.</span>'),
        ('<b>Every operator, one map</b><span><i>Brussels:</i> Dott, Bolt, Villo!<br><i>Paris:</i> Dott, Voi, Vélib’</span>',
         '<b>Alle operatoren, één kaart</b><span><i>Brussel:</i> Dott, Bolt, Villo!<br><i>Parijs:</i> Dott, Voi, Vélib’</span>'),
        ('<b>Switch operator mid-trip</b><span>Battery low? Change operator from Trip options; zones, parking and route follow.</span>',
         '<b>Wissel onderweg van operator</b><span>Batterij bijna leeg? Wissel van operator via “Trip options”: zones, parkeren en route volgen mee.</span>'),
        ('<h2>Your trips are nobody’s business.</h2>', '<h2>Je ritten gaan niemand iets aan.</h2>'),
        ('<p>Your location, trips, favourites and zones stay on your phone. Address search runs on the phone too. The network is only used for live vehicles, city packs and map tiles.</p>',
         '<p>Je locatie, ritten, favorieten en zones blijven op je telefoon, net als het zoeken naar adressen. Het netwerk dient alleen voor live voertuigen, stadsbestanden en kaarttegels.</p>'),
        ('<ul class="nos"><li>Free</li><li>No account</li><li>No ads</li><li>No telemetry</li></ul>', '<ul class="nos"><li>Gratis</li><li>Geen account</li><li>Geen reclame</li><li>Geen telemetrie</li></ul>'),
        ('<h2>Your next ride, without the bumps.</h2>', '<h2>Je volgende rit, zonder schokken.</h2>'),
        ('<p class="mut">Free, in English, French and Dutch. In beta on iPhone, Android is on the way.</p>', '<p class="mut">Gratis, in het Nederlands, Frans en Engels. In bèta op iPhone, Android komt eraan.</p>'),
        ('<div class="cta"><a class="btn btn-primary" href="#">Join the iPhone beta</a></div>', '<div class="cta"><a class="btn btn-primary" href="#">Doe mee aan de iPhone-bèta</a></div>'),
        ('<span><b>Brussels</b> · Dott, Bolt, Villo!</span><span><b>Paris</b> · Dott, Voi, Vélib’</span>', '<span><b>Brussel</b> · Dott, Bolt, Villo!</span><span><b>Parijs</b> · Dott, Voi, Vélib’</span>'),
        ('<span>© 2026 KasseiGo · independent, not affiliated with any operator.</span>', '<span>© 2026 KasseiGo · onafhankelijk, niet verbonden aan een operator.</span>'),
        ('>Legal notice</a> · <a href="/terms.html">Terms of use</a> · <a href="/privacy.html">Privacy</a>', '>Juridische vermeldingen</a> · <a href="/terms.html">Gebruiksvoorwaarden</a> · <a href="/privacy.html">Privacy</a> (FR/EN)'),
        ('<span>Map data © OpenStreetMap contributors · Tiles by OpenFreeMap</span>', '<span>Kaartgegevens © OpenStreetMap-bijdragers · Kaarttegels van OpenFreeMap</span>'),
        ('<span>Made with <span class="heart" role="img" aria-label="love">♥</span> in Brussels</span>', '<span>Gemaakt met <span class="heart" role="img" aria-label="liefde">♥</span> in Brussel</span>'),
    ],
}

# The app mock-ups, with the app's own words in each language (lib/l10n in the app).
MOCK = {'fr': [('>No cobbles detected<', '>Aucun pavé détecté<'), ('>Slow zone, 80 m<', '>Zone lente, 80 m<'), ('>Speed limited by Bolt<', '>Vitesse limitée par Bolt<'), ('>Unlock it<', '>Déverrouillez-le<'), ('>In the Bolt app<', '>Dans l’appli Bolt<'), ('>Nearest parking: 60 m <', '>Emplacement le plus proche : 60 m <'), ('<u>Undo</u>', '<u>Annuler</u>'), ('>Surface<', '>Revêtement<'), ('>The least comfortable surface you accept.<', '>Le revêtement le moins confortable que vous acceptez.<'), ('</svg>Smooth<', '</svg>Lisse<'), ('</svg>Slabs<', '</svg>Dalles<'), ('</svg>Cobbles<', '</svg>Pavés<'), ('</svg>Rough<', '</svg>Irrégulier<'), ('>8 min by bike<', '>8 min à vélo<'), ('>9 min by bike<', '>9 min à vélo<'), ('>≈ 2.2 km to the parking spot<', '>≈ 2,2 km jusqu’à l’emplacement<'), ('>≈ 2.4 km to the parking spot<', '>≈ 2,4 km jusqu’à l’emplacement<'), ('>Cobbles, 70 m<', '>Pavés, 70 m<'), ('>Your tolerance: slabs<', '>Votre tolérance : dalles<'), ('>Cycle tracks, 11 % of the trip<', '>Pistes cyclables, 11 % du trajet<'), ('>No-ride zones<', '>Zones interdites<'), ('>Zones where the operator forbids riding: get off and push, or go around.<', '>Zones où l’opérateur interdit de rouler : descendre et pousser, ou contourner.<'), ('>Go around<', '>Contourner<'), ('>Cross on foot<', '>Traverser à pied<'), ('>No-ride zone, 120 m<', '>Zone interdite, 120 m<'), ('>Get off and push<', '>Descendez et poussez<'), ('>Choose a parking spot<', '>Choisir un emplacement<'), ('>Closest to the destination<', '>Les plus proches de la destination<'), ('>Dott parking<', '>Parking Dott<'), ('</svg>Full<', '</svg>Complet<'), ('Walking is faster: 7 min on foot, against 8 min by bike.', 'La marche est plus rapide : 7 min à pied, contre 8 min à vélo.'), ('>Walk</a>', '>Marcher</a>'), ('<em>min on foot</em>', '<em>min à pied</em>'), ('>Arrival at 10:26<', '>Arrivée à 10:26<'), ('Bike: 10 min with the walk to it.', 'Vélo : 10 min avec la marche pour le rejoindre.'), ('>Ride anyway</a>', '>Rouler quand même</a>'), ('</svg>Start</div>', '</svg>Démarrer</div>'), ("'Your tolerance: ' + b.dataset.l", "'Votre tolérance : ' + b.textContent.trim().toLowerCase()")], 'nl': [('>No cobbles detected<', '>Geen kasseien gevonden<'), ('>Slow zone, 80 m<', '>Trage zone, 80 m<'), ('>Speed limited by Bolt<', '>Snelheid beperkt door Bolt<'), ('>Unlock it<', '>Ontgrendel de fiets<'), ('>In the Bolt app<', '>In de Bolt-app<'), ('>Nearest parking: 60 m <', '>Dichtstbijzijnde parkeerplek: 60 m <'), ('<u>Undo</u>', '<u>Ongedaan maken</u>'), ('>Surface<', '>Wegdek<'), ('>The least comfortable surface you accept.<', '>Het minst comfortabele wegdek dat je aanvaardt.<'), ('</svg>Smooth<', '</svg>Glad<'), ('</svg>Slabs<', '</svg>Tegels<'), ('</svg>Cobbles<', '</svg>Kasseien<'), ('</svg>Rough<', '</svg>Ruw<'), ('>8 min by bike<', '>8 min met de fiets<'), ('>9 min by bike<', '>9 min met de fiets<'), ('>≈ 2.2 km to the parking spot<', '>≈ 2,2 km tot de parkeerplek<'), ('>≈ 2.4 km to the parking spot<', '>≈ 2,4 km tot de parkeerplek<'), ('>Cobbles, 70 m<', '>Kasseien, 70 m<'), ('>Your tolerance: slabs<', '>Jouw tolerantie: tegels<'), ('>Cycle tracks, 11 % of the trip<', '>Fietspaden, 11 % van de rit<'), ('>No-ride zones<', '>Verboden zones<'), ('>Zones where the operator forbids riding: get off and push, or go around.<', '>Zones waar de operator rijden verbiedt: afstappen en duwen, of omrijden.<'), ('>Go around<', '>Omrijden<'), ('>Cross on foot<', '>Te voet doorkruisen<'), ('>No-ride zone, 120 m<', '>Verboden zone, 120 m<'), ('>Get off and push<', '>Afstappen en duwen<'), ('>Choose a parking spot<', '>Kies een parkeerplek<'), ('>Closest to the destination<', '>Het dichtst bij de bestemming<'), ('>Dott parking<', '>Dott-parking<'), ('</svg>Full<', '</svg>Vol<'), ('Walking is faster: 7 min on foot, against 8 min by bike.', 'Wandelen is sneller: 7 min te voet, tegenover 8 min met de fiets.'), ('>Walk</a>', '>Wandelen</a>'), ('<em>min on foot</em>', '<em>min te voet</em>'), ('>Arrival at 10:26<', '>Aankomst om 10:26<'), ('Bike: 10 min with the walk to it.', 'Fiets: 10 min, met de wandeling ernaartoe.'), ('>Ride anyway</a>', '>Toch rijden</a>'), ('</svg>Start</div>', '</svg>Starten</div>'), ("'Your tolerance: ' + b.dataset.l", "'Jouw tolerantie: ' + b.textContent.trim().toLowerCase()")]}

src = (SITE / 'index.html').read_text()
for lang in ('fr', 'nl'):
    s = src
    for a, b in COMMON[lang] + TEXT[lang] + MOCK[lang]:
        n = s.count(a)
        if n == 0:
            raise SystemExit(f'{lang}: not found: {a[:90]}')
        s = s.replace(a, b)
    out = SITE / lang / 'index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(s)
    print('ok', out.relative_to(SITE))
