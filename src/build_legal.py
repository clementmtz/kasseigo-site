"""Builds legal.html, terms.html and privacy.html for kasseigo.com (French is the reference text).

Usage: python3 site/src/build_legal.py   (writes the three pages into site/)
"""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).parent.parent
FAV = 'img/icon-64.png'

UPDATED_FR = '25 octobre 2026'
UPDATED_EN = '25 October 2026'
NAME = 'Clément Martinez'
MAIL = 'contact@kasseigo.com'

PAGES = {
    'legal': ('Mentions légales', 'Legal notice'),
    'terms': ("Conditions d’utilisation", 'Terms of use'),
    'privacy': ('Politique de confidentialité', 'Privacy policy'),
}

CSS = """
:root{--bg:#f3f0fa;--card:#fff;--ink:#1d1830;--mut:#6c6584;--line:#e6e1f2;--p:#bba6f4;--pt:#efe9fe;--pd:#6a4bc4;--warn:#9a5209;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#1b1628;--card:#241e37;--ink:#f2eefc;--mut:#a8a0c3;--line:#372f51;--p:#c4b2f8;--pt:#30274f;--pd:#c4b2f8;--warn:#eea45d;color-scheme:dark}}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:500 17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--pd)}
:focus-visible{outline:3px solid var(--pd);outline-offset:3px;border-radius:6px}
.wrap{width:min(820px,100% - 32px);margin-inline:auto}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:72px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px;text-decoration:none;color:var(--ink)}
.brand img{width:36px;height:36px}
.lang{display:flex;gap:4px;padding:4px;border-radius:14px;background:var(--card);border:1px solid var(--line)}
.lang button{min-height:36px;min-width:48px;border:0;border-radius:10px;background:none;color:var(--mut);font-weight:700;font-size:14px;line-height:1;font-family:inherit;cursor:pointer}
.lang button[aria-pressed="true"]{background:var(--pt);color:var(--ink)}
nav.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 24px}
nav.tabs a{padding:8px 14px;border-radius:12px;background:var(--card);border:1px solid var(--line);text-decoration:none;color:var(--ink);font-weight:650;font-size:15px}
nav.tabs a[aria-current="page"]{background:var(--pt);border-color:var(--pd)}
main{padding-bottom:48px}
article{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:clamp(24px,5vw,48px)}
h1{font-size:clamp(30px,5vw,42px);line-height:1.1;letter-spacing:-.02em;margin:0 0 8px}
.upd{color:var(--mut);font-size:15px;margin:0 0 28px}
h2{font-size:21px;letter-spacing:-.01em;margin:36px 0 10px}
h2:first-of-type{margin-top:0}
p,li{margin:0 0 10px}
ul{padding-left:22px;margin:0 0 10px}
.box{padding:18px 20px;border-radius:18px;background:var(--pt);margin:0 0 24px}
.box.warn{background:color-mix(in srgb,var(--warn) 12%,var(--card))}
.box p:last-child{margin:0}
dl{display:grid;grid-template-columns:minmax(120px,200px) 1fr;gap:6px 20px;margin:0 0 10px}
dt{color:var(--mut);font-weight:650}
dd{margin:0}
@media (max-width:560px){dl{grid-template-columns:1fr}dd{margin-bottom:8px}}
.note{color:var(--mut);font-size:15px}
footer{padding:0 0 48px;color:var(--mut);font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:8px 20px}
footer a{color:var(--mut)}
.heart{color:#c23a3a}
@media (prefers-color-scheme:dark){.heart{color:#ef7a7a}}
:root[lang="en"] [data-l="fr"],:root[lang="fr"] [data-l="en"]{display:none}
"""

def host(url):
    return url.split('/')[2]

FEEDS = [
    ('Dott', 'Bruxelles / Brussels, Paris', 'gbfs.api.ridedott.com'),
    ('Bolt', 'Bruxelles / Brussels', 'mds.bolt.eu'),
    ('Villo!', 'Bruxelles / Brussels', 'api.cyclocity.fr'),
    ('Voi', 'Paris', 'api.voiapp.io'),
    ('Vélib’ Métropole', 'Paris', 'velib-metropole-opendata.smovengo.cloud'),
]
feeds_li = '\n'.join(f'<li><b>{n}</b> ({c}) · <code>{h}</code></li>' for n, c, h in FEEDS)

# ---------------------------------------------------------------- Legal notice
LEGAL_FR = f"""
<h2>Éditeur</h2>
<dl>
<dt>Éditeur</dt><dd>{NAME}, particulier, agissant à titre personnel et non professionnel</dd>
<dt>Résidence</dt><dd>Belgique</dd>
<dt>Statut</dt><dd>Aucune entreprise, aucun numéro d’entreprise (BCE) ni de TVA : KasseiGo est un projet personnel, gratuit et sans but lucratif.</dd>
<dt>Contact</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
<dt>Responsable de la publication</dt><dd>{NAME}</dd>
</dl>

<h2>Hébergement</h2>
<dl>
<dt>Site kasseigo.com</dt><dd>GitHub Pages, service de GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis · <a href="https://github.com">github.com</a></dd>
<dt>Fichiers des villes</dt><dd>Publiés sur GitHub (GitHub, Inc., même adresse), dépôt <code>clementmtz/kasseigo-packs</code></dd>
<dt>Formulaire de retour</dt><dd>Cloudflare Workers et Cloudflare Turnstile, services de Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis ; tickets enregistrés dans un dépôt privé sur GitHub</dd>
<dt>Nom de domaine</dt><dd>Enregistré auprès d’OVH SAS, 2 rue Kellermann, 59100 Roubaix, France · <a href="https://www.ovhcloud.com">ovhcloud.com</a></dd>
<dt>Application</dt><dd>Distribuée par Apple (App Store, TestFlight) ; une version Android est prévue.</dd>
</dl>

<h2>Objet</h2>
<p>KasseiGo est une application d’aide à l’itinéraire pour les vélos et trottinettes partagés à Bruxelles et à Paris. Le site kasseigo.com la présente. L’application et le site sont gratuits, sans compte, sans publicité et sans mesure d’audience.</p>

<h2>Propriété intellectuelle</h2>
<p>Le nom KasseiGo, le logo, les textes, la présentation, les images, le site et l’application (y compris son code source et son moteur d’itinéraire) sont la propriété de {NAME}. <b>Le projet n’est pas open source</b> : tous droits réservés. Toute reproduction, représentation, adaptation, extraction ou diffusion, totale ou partielle, sans autorisation écrite préalable est interdite, sauf dans les limites prévues par la loi.</p>
<p>Restent la propriété de leurs titulaires, et soumis à leurs propres licences :</p>
<ul>
<li>les données cartographiques d’<b>OpenStreetMap</b>, © les contributeurs d’OpenStreetMap, disponibles sous licence <a href="https://opendatacommons.org/licenses/odbl/">Open Database License (ODbL)</a> ;</li>
<li>les tuiles de carte d’<b>OpenFreeMap</b>, fondées sur OpenStreetMap ;</li>
<li>les données des véhicules, stations, places et zones, publiées par chaque opérateur dans son flux public GBFS ;</li>
<li>les briques logicielles tierces utilisées par l’application (notamment Flutter, Rust et MapLibre), sous leurs licences respectives.</li>
</ul>

<h2>Marques et absence d’affiliation</h2>
<p>Dott, Bolt, Voi, Villo! et Vélib’ sont des marques de leurs propriétaires respectifs. Elles sont citées uniquement pour indiquer les services dont KasseiGo affiche les données publiques. <b>KasseiGo est indépendant</b> : il n’est ni affilié, ni partenaire, ni soutenu, ni autorisé par ces opérateurs, par les villes de Bruxelles ou de Paris, ni par Apple ou Google.</p>

<h2>Responsabilité</h2>
<p>Les informations du site et de l’application sont fournies à titre indicatif, gratuitement et sans garantie. Les règles d’utilisation et les limites de responsabilité sont détaillées dans les <a href="terms.html">conditions d’utilisation</a>.</p>

<h2>Liens externes</h2>
<p>Le site et l’application peuvent renvoyer vers des sites ou applications tiers (opérateurs, sources de données). L’éditeur n’en contrôle ni le contenu ni la disponibilité et n’en est pas responsable.</p>

<h2>Données personnelles</h2>
<p>Voir la <a href="privacy.html">politique de confidentialité</a>. Le site ne dépose aucun cookie et n’utilise aucun traceur ; seule la page de retour utilise le contrôle anti-robot Cloudflare Turnstile.</p>

<h2>Signalement</h2>
<p>Pour signaler un contenu, une erreur ou une atteinte à vos droits : <a href="feedback.html">formulaire de retour</a> ou <a href="mailto:{MAIL}">{MAIL}</a>.</p>

<h2>Droit applicable</h2>
<p>Les présentes mentions sont régies par le droit belge. En cas de différence entre la version française et la version anglaise, la version française fait foi.</p>
"""

LEGAL_EN = f"""
<h2>Publisher</h2>
<dl>
<dt>Publisher</dt><dd>{NAME}, a private individual acting in a personal, non-professional capacity</dd>
<dt>Residence</dt><dd>Belgium</dd>
<dt>Status</dt><dd>No company, no enterprise (BCE/KBO) or VAT number: KasseiGo is a personal, free, non-profit project.</dd>
<dt>Contact</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
<dt>Publication manager</dt><dd>{NAME}</dd>
</dl>

<h2>Hosting</h2>
<dl>
<dt>Website kasseigo.com</dt><dd>GitHub Pages, a service of GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States · <a href="https://github.com">github.com</a></dd>
<dt>City files</dt><dd>Published on GitHub (GitHub, Inc., same address), repository <code>clementmtz/kasseigo-packs</code></dd>
<dt>Feedback form</dt><dd>Cloudflare Workers and Cloudflare Turnstile, services of Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, United States; tickets stored in a private GitHub repository</dd>
<dt>Domain name</dt><dd>Registered with OVH SAS, 2 rue Kellermann, 59100 Roubaix, France · <a href="https://www.ovhcloud.com">ovhcloud.com</a></dd>
<dt>App</dt><dd>Distributed by Apple (App Store, TestFlight); an Android version is planned.</dd>
</dl>

<h2>Purpose</h2>
<p>KasseiGo is a route-planning aid for shared bikes and e-scooters in Brussels and Paris. The website kasseigo.com presents it. The app and the website are free, with no account, no ads and no audience measurement.</p>

<h2>Intellectual property</h2>
<p>The KasseiGo name, logo, texts, layout, images, website and app (including its source code and routing engine) are the property of {NAME}. <b>The project is not open source</b>: all rights reserved. Any reproduction, representation, adaptation, extraction or distribution, in whole or in part, without prior written permission is forbidden, except within the limits set by law.</p>
<p>The following remain the property of their owners and are subject to their own licences:</p>
<ul>
<li><b>OpenStreetMap</b> map data, © OpenStreetMap contributors, available under the <a href="https://opendatacommons.org/licenses/odbl/">Open Database License (ODbL)</a>;</li>
<li><b>OpenFreeMap</b> map tiles, based on OpenStreetMap;</li>
<li>vehicle, station, parking and zone data, published by each operator in its public GBFS feed;</li>
<li>third-party software components used by the app (including Flutter, Rust and MapLibre), under their respective licences.</li>
</ul>

<h2>Trademarks and no affiliation</h2>
<p>Dott, Bolt, Voi, Villo! and Vélib’ are trademarks of their respective owners. They are named only to show which services’ public data KasseiGo displays. <b>KasseiGo is independent</b>: it is not affiliated with, partnered with, endorsed or authorised by these operators, the cities of Brussels or Paris, Apple or Google.</p>

<h2>Liability</h2>
<p>Information on the website and in the app is provided for guidance only, free of charge and without warranty. Rules of use and limits of liability are set out in the <a href="terms.html">terms of use</a>.</p>

<h2>External links</h2>
<p>The website and the app may link to third-party websites or apps (operators, data sources). The publisher does not control their content or availability and is not responsible for them.</p>

<h2>Personal data</h2>
<p>See the <a href="privacy.html">privacy policy</a>. The website sets no cookies and uses no trackers; only the feedback page uses the Cloudflare Turnstile anti-robot check.</p>

<h2>Reporting</h2>
<p>To report content, an error or an infringement of your rights: <a href="feedback.html">feedback form</a> or <a href="mailto:{MAIL}">{MAIL}</a>.</p>

<h2>Governing law</h2>
<p>This notice is governed by Belgian law. If the French and English versions differ, the French version prevails.</p>
"""

# ---------------------------------------------------------------- Terms of use
TERMS_FR = f"""
<div class="box warn"><p><b>En bref.</b> KasseiGo est une aide gratuite, fournie telle quelle par un particulier. Ses informations peuvent être fausses ou dépassées. Vous restez seul responsable de votre conduite, de votre sécurité, du respect du code de la route et des règles de l’opérateur. Le code de la route, la signalisation et les règles de l’opérateur priment toujours sur l’application.</p></div>

<h2>1. Objet et acceptation</h2>
<p>Les présentes conditions encadrent l’utilisation de l’application KasseiGo et du site kasseigo.com (ensemble, « le service »), édités par {NAME}, particulier résidant en Belgique (voir les <a href="legal.html">mentions légales</a>). En installant ou en utilisant le service, vous acceptez ces conditions. Si vous ne les acceptez pas, n’utilisez pas le service.</p>

<h2>2. Description du service</h2>
<p>KasseiGo aide à se déplacer en vélo ou en trottinette partagés à Bruxelles et à Paris. Il affiche les véhicules, stations et emplacements publiés par les opérateurs, calcule un itinéraire (marche jusqu’au véhicule, trajet, stationnement, marche jusqu’à la destination) en tenant compte du revêtement des rues et des zones des opérateurs, et propose un guidage.</p>
<p>KasseiGo <b>ne loue, ne réserve, ne déverrouille et ne facture aucun véhicule</b>. La location se fait uniquement dans l’application de l’opérateur, selon ses propres conditions. Utiliser KasseiGo ne crée aucun lien contractuel entre vous et un opérateur, ni entre l’éditeur et un opérateur.</p>

<h2>3. Gratuité, absence de compte, version bêta</h2>
<ul>
<li>Le service est <b>gratuit</b> : aucun abonnement, aucun achat intégré, aucune publicité.</li>
<li>Il ne demande <b>aucun compte</b> ni aucune inscription.</li>
<li>Il est proposé dans le cadre d’un projet personnel, en version bêta. Il peut comporter des erreurs, des interruptions ou des fonctions incomplètes.</li>
<li>L’éditeur peut à tout moment, sans préavis ni indemnité, modifier, suspendre ou arrêter tout ou partie du service, notamment une ville, un opérateur ou une fonction.</li>
</ul>

<h2>4. Accès</h2>
<p>Le service nécessite un appareil compatible. Certaines fonctions (véhicules en temps réel, téléchargement des villes, carte) nécessitent une connexion à Internet ; les frais de connexion restent à votre charge. La disponibilité du service dépend aussi de services tiers (opérateurs, OpenStreetMap, OpenFreeMap, GitHub, Apple) que l’éditeur ne contrôle pas.</p>

<h2>5. Informations indicatives, sans garantie</h2>
<p>Toutes les informations du service sont <b>indicatives</b>. Elles peuvent être inexactes, incomplètes, retardées ou dépassées, en particulier :</p>
<ul>
<li>les rues, revêtements, pistes cyclables, sens de circulation, escaliers et adresses, issus d’OpenStreetMap, base de données collaborative mise à jour une fois par semaine dans l’application ;</li>
<li>la position et la disponibilité des véhicules, l’état de leur batterie, les stations, les places libres et les zones (lentes, interdites, de stationnement), issues des flux publics des opérateurs, qui peuvent être erronés, en retard ou indisponibles ; certains opérateurs ne publient pas les places libres ;</li>
<li>les durées, distances et heures d’arrivée, qui sont des estimations ;</li>
<li>les travaux, fermetures, événements, conditions météo et dangers temporaires, que le service ne connaît pas.</li>
</ul>
<p>Un itinéraire proposé peut emprunter une voie inadaptée, fermée, dangereuse ou interdite à votre véhicule au moment où vous passez. Un emplacement de stationnement affiché peut être plein, supprimé ou ne pas être accepté par l’opérateur. Le service est une <b>aide supplémentaire</b> : il ne remplace ni votre attention, ni votre jugement, ni la signalisation, ni les informations de l’opérateur.</p>

<h2>6. Votre responsabilité et votre sécurité</h2>
<p>Vous utilisez le service librement et sous votre seule responsabilité. En particulier, vous vous engagez à :</p>
<ul>
<li>respecter le code de la route du pays où vous circulez, la signalisation, les instructions des agents et les règles locales, qui priment sur toute indication de l’application ;</li>
<li>respecter les conditions générales et les règles de l’opérateur du véhicule (âge minimum, zones, vitesse, stationnement, nombre de personnes, fin de location) ;</li>
<li>ne pas manipuler votre téléphone en roulant : réglez votre trajet à l’arrêt, utilisez un support adapté si vous le consultez, et arrêtez-vous dans un endroit sûr pour toute manipulation ;</li>
<li>adapter votre conduite à la circulation, à l’état de la chaussée, à la météo et à votre propre état, et ne pas conduire sous l’influence de l’alcool, de drogues ou de médicaments qui altèrent la vigilance ;</li>
<li>vérifier l’état du véhicule avant de l’utiliser et porter les équipements de protection recommandés (casque notamment) ;</li>
<li>ne pas utiliser le service à des fins illégales ou d’une manière qui pourrait vous mettre en danger ou mettre en danger d’autres personnes.</li>
</ul>
<p>Les amendes, frais de stationnement, pénalités, frais de location ou de déplacement du véhicule facturés par un opérateur ou une autorité restent entièrement à votre charge, même si vous avez suivi une indication du service.</p>

<h2>7. Limitation de responsabilité</h2>
<p>Le service est fourni gratuitement, <b>« tel quel » et « selon disponibilité »</b>, sans aucune garantie, expresse ou implicite, notamment d’exactitude, d’exhaustivité, de disponibilité, d’absence d’erreur ou d’adéquation à un usage particulier.</p>
<p>Dans toute la mesure permise par la loi, l’éditeur ne peut être tenu responsable d’aucun dommage, direct ou indirect, matériel ou immatériel, résultant de l’utilisation ou de l’impossibilité d’utiliser le service, ou d’une information qu’il affiche, notamment : accident, chute, blessure, dommage à un véhicule, à un bien ou à un tiers, amende, pénalité ou frais d’un opérateur, perte de temps, retard, trajet manqué, perte de données, ou dommage causé par un service tiers.</p>
<p>Cette limitation ne s’applique pas dans les cas où la loi interdit d’exclure ou de limiter la responsabilité, notamment en cas de faute intentionnelle (dol) de l’éditeur.</p>

<h2>8. Services tiers</h2>
<p>Le service affiche des données fournies par des tiers (opérateurs, OpenStreetMap, OpenFreeMap) et peut ouvrir l’application d’un opérateur à votre demande. Ces tiers agissent sous leur seule responsabilité et selon leurs propres conditions et politiques de confidentialité. L’éditeur n’est pas responsable de leurs contenus, de leurs services, de leur disponibilité ni de leurs pratiques.</p>

<h2>9. Licence d’utilisation et propriété intellectuelle</h2>
<p>L’éditeur vous accorde un droit personnel, gratuit, non exclusif, non transférable et révocable d’utiliser l’application pour vos déplacements, à des fins privées et non commerciales. Le service et son code ne sont pas open source et restent la propriété de l’éditeur (voir les <a href="legal.html">mentions légales</a>).</p>
<p>Sauf dans les limites expressément autorisées par la loi, il est interdit de copier, modifier, décompiler, désassembler ou tenter d’obtenir le code source de l’application ; de la revendre, la louer ou la redistribuer ; d’extraire ses données de manière automatisée ou massive ; de contourner ses protections ; ou de l’utiliser pour fournir un service concurrent ou commercial.</p>

<h2>10. Données personnelles</h2>
<p>Le service fonctionne sans compte et l’éditeur ne collecte pas vos données. Les détails figurent dans la <a href="privacy.html">politique de confidentialité</a>.</p>

<h2>11. Modification des conditions</h2>
<p>L’éditeur peut modifier ces conditions à tout moment, notamment pour suivre l’évolution du service ou de la loi. La date de mise à jour figure en haut de cette page. Continuer à utiliser le service après une modification vaut acceptation des nouvelles conditions.</p>

<h2>12. Dispositions générales</h2>
<p>Si une clause de ces conditions est jugée nulle ou inapplicable, elle est réputée non écrite et les autres clauses restent en vigueur. Le fait de ne pas se prévaloir d’une clause ne vaut pas renonciation à s’en prévaloir plus tard. En cas de différence entre la version française et la version anglaise, la version française fait foi.</p>

<h2>13. Droit applicable et litiges</h2>
<p>Ces conditions sont régies par le droit belge, sous réserve des règles impératives qui vous protègent dans votre pays de résidence. En cas de difficulté, écrivez d’abord à <a href="mailto:{MAIL}">{MAIL}</a> pour chercher une solution amiable. À défaut, le litige sera porté devant les juridictions compétentes selon les règles légales.</p>

<h2>14. Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>
"""

TERMS_EN = f"""
<div class="box warn"><p><b>In short.</b> KasseiGo is a free aid, provided as is by a private individual. Its information may be wrong or out of date. You alone remain responsible for how you ride, for your safety, and for following the highway code and the operator’s rules. The highway code, road signs and the operator’s rules always take precedence over the app.</p></div>

<h2>1. Purpose and acceptance</h2>
<p>These terms govern the use of the KasseiGo app and the kasseigo.com website (together, “the service”), published by {NAME}, a private individual living in Belgium (see the <a href="legal.html">legal notice</a>). By installing or using the service, you accept these terms. If you do not accept them, do not use the service.</p>

<h2>2. What the service does</h2>
<p>KasseiGo helps you get around on shared bikes and e-scooters in Brussels and Paris. It shows the vehicles, stations and parking spots published by operators, plans a route (walk to the vehicle, ride, parking, walk to the destination) taking street surfaces and operator zones into account, and offers turn-by-turn guidance.</p>
<p>KasseiGo <b>does not rent, reserve, unlock or charge for any vehicle</b>. Rental only happens in the operator’s own app, under its own terms. Using KasseiGo creates no contract between you and an operator, nor between the publisher and an operator.</p>

<h2>3. Free, no account, beta</h2>
<ul>
<li>The service is <b>free</b>: no subscription, no in-app purchases, no ads.</li>
<li>It requires <b>no account</b> and no sign-up.</li>
<li>It is offered as a personal project, in beta. It may contain errors, interruptions or incomplete features.</li>
<li>The publisher may at any time, without notice or compensation, change, suspend or stop all or part of the service, including a city, an operator or a feature.</li>
</ul>

<h2>4. Access</h2>
<p>The service requires a compatible device. Some features (live vehicles, city downloads, map) need an Internet connection; connection costs are yours. The service also depends on third-party services (operators, OpenStreetMap, OpenFreeMap, GitHub, Apple) that the publisher does not control.</p>

<h2>5. Information for guidance only, no warranty</h2>
<p>All information in the service is <b>for guidance only</b>. It may be inaccurate, incomplete, delayed or out of date, in particular:</p>
<ul>
<li>streets, surfaces, cycle tracks, one-way streets, stairs and addresses, taken from OpenStreetMap, a collaborative database updated once a week in the app;</li>
<li>vehicle positions and availability, battery levels, stations, free places and zones (slow, no-ride, parking), taken from operators’ public feeds, which may be wrong, late or unavailable; some operators do not publish free places;</li>
<li>durations, distances and arrival times, which are estimates;</li>
<li>roadworks, closures, events, weather and temporary hazards, which the service does not know about.</li>
</ul>
<p>A suggested route may use a road that is unsuitable, closed, dangerous or forbidden to your vehicle when you get there. A parking spot shown may be full, removed or not accepted by the operator. The service is an <b>additional aid</b>: it does not replace your attention, your judgement, road signs or the operator’s information.</p>

<h2>6. Your responsibility and safety</h2>
<p>You use the service freely and at your own risk. In particular, you agree to:</p>
<ul>
<li>follow the highway code of the country you ride in, road signs, instructions from officers and local rules, which take precedence over anything the app shows;</li>
<li>follow the terms and rules of the vehicle’s operator (minimum age, zones, speed, parking, number of riders, ending the rental);</li>
<li>not handle your phone while riding: set up your trip while stopped, use a suitable mount if you look at it, and stop in a safe place for any interaction;</li>
<li>adapt your riding to traffic, road conditions, weather and your own condition, and not ride under the influence of alcohol, drugs or medication that affects alertness;</li>
<li>check the vehicle before use and wear recommended protective equipment (a helmet in particular);</li>
<li>not use the service for illegal purposes or in a way that could endanger you or others.</li>
</ul>
<p>Fines, parking fees, penalties, rental or relocation fees charged by an operator or an authority remain entirely yours, even if you followed something the service showed.</p>

<h2>7. Limitation of liability</h2>
<p>The service is provided free of charge, <b>“as is” and “as available”</b>, without any warranty, express or implied, including of accuracy, completeness, availability, freedom from errors or fitness for a particular purpose.</p>
<p>To the fullest extent permitted by law, the publisher is not liable for any damage, direct or indirect, material or immaterial, arising from the use of or inability to use the service, or from any information it shows, including: accident, fall, injury, damage to a vehicle, property or third party, fine, penalty or operator fee, lost time, delay, missed trip, loss of data, or damage caused by a third-party service.</p>
<p>This limitation does not apply where the law forbids excluding or limiting liability, in particular in case of the publisher’s intentional misconduct (fraud).</p>

<h2>8. Third-party services</h2>
<p>The service displays data supplied by third parties (operators, OpenStreetMap, OpenFreeMap) and may open an operator’s app at your request. These third parties act under their sole responsibility and their own terms and privacy policies. The publisher is not responsible for their content, services, availability or practices.</p>

<h2>9. Licence and intellectual property</h2>
<p>The publisher grants you a personal, free, non-exclusive, non-transferable and revocable right to use the app for your own trips, for private, non-commercial purposes. The service and its code are not open source and remain the publisher’s property (see the <a href="legal.html">legal notice</a>).</p>
<p>Except within the limits expressly allowed by law, you may not copy, modify, decompile, disassemble or try to obtain the app’s source code; resell, rent or redistribute it; extract its data automatically or in bulk; circumvent its protections; or use it to provide a competing or commercial service.</p>

<h2>10. Personal data</h2>
<p>The service works without an account and the publisher does not collect your data. Details are in the <a href="privacy.html">privacy policy</a>.</p>

<h2>11. Changes to these terms</h2>
<p>The publisher may change these terms at any time, in particular to follow changes in the service or the law. The date of the last update is shown at the top of this page. Continuing to use the service after a change means you accept the new terms.</p>

<h2>12. General provisions</h2>
<p>If any clause of these terms is held void or unenforceable, it is deemed unwritten and the other clauses remain in force. Not enforcing a clause does not waive the right to enforce it later. If the French and English versions differ, the French version prevails.</p>

<h2>13. Governing law and disputes</h2>
<p>These terms are governed by Belgian law, subject to the mandatory rules that protect you in your country of residence. If there is a problem, first write to <a href="mailto:{MAIL}">{MAIL}</a> to look for an amicable solution. Failing that, the dispute will be brought before the courts that have jurisdiction under the law.</p>

<h2>14. Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>
"""

# ---------------------------------------------------------------- Privacy policy
PRIVACY_FR = f"""
<div class="box"><p><b>En bref.</b> Pas de compte, pas de publicité, pas de mesure d’audience, pas de rapport de plantage. Votre position est utilisée sur le téléphone et n’est jamais envoyée. L’éditeur ne reçoit aucune donnée vous concernant, sauf les messages que vous choisissez de lui envoyer. Seuls les services contactés pour fonctionner (opérateurs, cartes, fichiers des villes) voient, comme pour toute connexion, l’adresse IP de votre téléphone.</p></div>

<h2>1. Responsable du traitement</h2>
<p>{NAME}, particulier résidant en Belgique, éditeur de KasseiGo · <a href="mailto:{MAIL}">{MAIL}</a>. Cette politique s’applique à l’application KasseiGo et au site kasseigo.com, conformément au règlement général sur la protection des données (RGPD, règlement (UE) 2016/679).</p>

<h2>2. Ce que l’éditeur collecte : rien, sauf ce que vous lui envoyez</h2>
<p>L’application n’envoie vos données à aucun serveur de KasseiGo. L’application ne contient ni compte, ni publicité, ni outil de mesure d’audience, ni outil de rapport de plantage, ni kit de suivi tiers. L’éditeur ne reçoit, ne voit et ne conserve ni votre position, ni vos trajets, ni vos recherches, ni vos favoris. Seuls les messages que vous envoyez vous-même, par le formulaire de retour ou par e-mail, lui parviennent (section 6).</p>

<h2>3. Ce qui reste sur votre téléphone</h2>
<ul>
<li><b>Votre position</b> : utilisée uniquement pendant l’utilisation de l’application, pour trouver les véhicules proches et vous guider. Elle n’est ni enregistrée, ni envoyée. Votre téléphone vous demande l’autorisation ; vous pouvez la retirer à tout moment dans ses réglages.</li>
<li><b>Vos favoris, recherches récentes, zones personnalisées et réglages</b> : enregistrés dans l’espace privé de l’application, protégé par le chiffrement du téléphone. Supprimer l’application les efface.</li>
<li><b>Les fichiers des villes et la carte</b> : rues, lieux et carte hors ligne, gérés dans « Offline cities ».</li>
</ul>
<p>Les itinéraires, les emplacements et la recherche d’adresses sont calculés sur le téléphone : ce que vous cherchez n’est jamais envoyé.</p>

<h2>4. Connexions de l’application et ce qu’elles envoient</h2>
<p>Pour fonctionner, l’application contacte les services suivants, toujours en connexion chiffrée (HTTPS). Comme pour toute connexion à Internet, chacun voit l’adresse IP de votre téléphone et les informations techniques habituelles d’une requête. Ils agissent sous leur propre responsabilité et selon leur propre politique de confidentialité ; l’éditeur n’a pas accès à leurs journaux.</p>
<ul>
<li><b>Flux publics des opérateurs (GBFS)</b> : l’application demande les données de toute la ville (véhicules, stations, places, zones), sans rien envoyer qui vous concerne.
<ul>{feeds_li}</ul></li>
<li><b>Fichiers des villes</b> · GitHub (<code>github.com</code>) : liste des fichiers publiés au démarrage et sur la page « Offline cities », puis fichier d’une ville seulement s’il est nouveau ou mis à jour.</li>
<li><b>Tuiles de carte</b> · OpenFreeMap (<code>tiles.openfreemap.org</code>) : les morceaux de carte de la zone affichée que le téléphone n’a pas encore.</li>
<li><b>Application de l’opérateur</b> : ouverte uniquement quand vous touchez son bouton. Ses propres conditions et sa politique de confidentialité s’appliquent alors.</li>
</ul>
<p>L’application est distribuée par Apple (App Store, TestFlight), qui peut traiter des données selon ses propres conditions, en dehors du contrôle de l’éditeur.</p>

<h2>5. Le site kasseigo.com</h2>
<p>Le site ne dépose aucun cookie, n’utilise aucun traceur ni outil de mesure d’audience et ne charge aucune ressource externe, sauf la page de retour (section 6). Il est hébergé par GitHub Pages (GitHub, Inc., États-Unis), qui peut enregistrer l’adresse IP des visiteurs dans ses journaux, notamment pour la sécurité du service, selon la <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">déclaration de confidentialité de GitHub</a>. L’éditeur n’a pas accès à ces journaux.</p>

<h2>6. Si vous envoyez un retour ou écrivez à l’éditeur</h2>
<p><b>Formulaire de retour</b> (<a href="feedback.html">kasseigo.com/feedback</a>, aussi ouvert depuis l’application) : il transmet le type de retour, votre message, la ville si vous la choisissez, votre adresse e-mail seulement si vous la donnez, la langue de la page et, depuis l’application, la version de l’application et du système du téléphone. Rien d’autre n’est ajouté automatiquement : ni position, ni identifiant.</p>
<ul>
<li>Pour bloquer les robots, la page utilise <b>Cloudflare Turnstile</b> (Cloudflare, Inc., États-Unis), qui analyse des signaux techniques du navigateur, selon la <a href="https://www.cloudflare.com/privacypolicy/">politique de confidentialité de Cloudflare</a>.</li>
<li>Le message est transmis par un service de Cloudflare Workers et enregistré comme ticket dans un dépôt <b>privé</b> sur GitHub (GitHub, Inc., États-Unis), accessible uniquement à l’éditeur.</li>
<li>Finalité : corriger les erreurs, améliorer le service et, si vous avez donné votre e-mail, vous répondre. Base : l’intérêt légitime à traiter les retours reçus.</li>
<li>Les tickets sont conservés le temps nécessaire à leur traitement et à leur suivi, puis supprimés. Ils ne sont jamais vendus ni transmis à d’autres tiers. Vous pouvez demander leur suppression à tout moment.</li>
</ul>
<p><b>Par e-mail</b> : si vous écrivez à <a href="mailto:{MAIL}">{MAIL}</a>, votre adresse e-mail et le contenu de votre message sont utilisés uniquement pour vous répondre et assurer le suivi de votre demande, sur la base de l’intérêt légitime à répondre aux messages reçus. Ils sont conservés le temps nécessaire à ce suivi, puis supprimés, et ne sont jamais vendus ni transmis à des tiers. La messagerie est hébergée par OVH SAS (France).</p>

<h2>7. Transferts hors de l’Union européenne</h2>
<p>Certains services cités (notamment GitHub, Inc. et Cloudflare, Inc.) sont situés hors de l’Union européenne. Les données qu’ils traitent (adresse IP, données techniques de connexion et, pour les retours, le contenu du message) le sont sous leur propre responsabilité, selon leurs propres garanties.</p>

<h2>8. Vos droits</h2>
<p>Vous disposez des droits d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité. Comme l’éditeur ne détient aucune donnée issue de l’application, ces droits s’exercent surtout pour un retour ou un échange d’e-mails, à <a href="mailto:{MAIL}">{MAIL}</a>. Pour les données traitées par les services tiers cités, adressez-vous à eux directement.</p>
<p>Vous pouvez introduire une réclamation auprès de l’<b>Autorité de protection des données</b>, rue de la Presse 35, 1000 Bruxelles, Belgique · <a href="https://www.autoriteprotectiondonnees.be">autoriteprotectiondonnees.be</a>, ou auprès de l’autorité de votre pays de résidence (en France, la CNIL · <a href="https://www.cnil.fr">cnil.fr</a>).</p>

<h2>9. Mineurs</h2>
<p>Le service ne collecte sciemment aucune donnée sur quiconque, mineur compris. La location des véhicules est soumise à l’âge minimum fixé par chaque opérateur.</p>

<h2>10. Sécurité</h2>
<p>Toutes les connexions de l’application sont chiffrées (HTTPS ; les connexions non chiffrées sont refusées). Chaque fichier de ville est vérifié (taille et empreinte SHA-256) avant utilisation. Les liens issus des flux ne s’ouvrent que vers une page sécurisée (https) ou l’application de l’opérateur.</p>

<h2>11. Modifications</h2>
<p>Cette politique peut évoluer avec l’application. La date de mise à jour figure en haut de la page. En cas de différence entre la version française et la version anglaise, la version française fait foi.</p>
"""

PRIVACY_EN = f"""
<div class="box"><p><b>In short.</b> No account, no ads, no analytics, no crash reports. Your location is used on the phone and never sent. The publisher receives no data about you, except the messages you choose to send. Only the services contacted to make the app work (operators, maps, city files) see, as with any connection, your phone’s IP address.</p></div>

<h2>1. Data controller</h2>
<p>{NAME}, a private individual living in Belgium, publisher of KasseiGo · <a href="mailto:{MAIL}">{MAIL}</a>. This policy covers the KasseiGo app and the kasseigo.com website, under the General Data Protection Regulation (GDPR, Regulation (EU) 2016/679).</p>

<h2>2. What the publisher collects: nothing, except what you send</h2>
<p>The app sends your data to no KasseiGo server. The app has no account, no ads, no analytics, no crash reporting and no third-party tracking SDK. The publisher does not receive, see or keep your location, trips, searches or favourites. Only the messages you send yourself, through the feedback form or by email, reach the publisher (section 6).</p>

<h2>3. What stays on your phone</h2>
<ul>
<li><b>Your location</b>: used only while the app is in use, to find nearby vehicles and guide you. It is neither stored nor sent. Your phone asks for permission; you can withdraw it at any time in its settings.</li>
<li><b>Your favourites, recent searches, custom zones and settings</b>: stored in the app’s private space, protected by the phone’s encryption. Deleting the app erases them.</li>
<li><b>City files and the map</b>: streets, places and offline map, managed in “Offline cities”.</li>
</ul>
<p>Routes, parking spots and address search are computed on the phone: what you search for is never sent.</p>

<h2>4. App connections and what they send</h2>
<p>To work, the app contacts the following services, always over an encrypted connection (HTTPS). As with any Internet connection, each one sees your phone’s IP address and the usual technical details of a request. They act under their own responsibility and privacy policies; the publisher has no access to their logs.</p>
<ul>
<li><b>Operators’ public feeds (GBFS)</b>: the app asks for the data of the whole city (vehicles, stations, places, zones), sending nothing about you.
<ul>{feeds_li}</ul></li>
<li><b>City files</b> · GitHub (<code>github.com</code>): the list of published files at start-up and on the “Offline cities” page, then a city’s file only when it is new or updated.</li>
<li><b>Map tiles</b> · OpenFreeMap (<code>tiles.openfreemap.org</code>): the map pieces of the area shown that the phone does not have yet.</li>
<li><b>Operator app</b>: opened only when you tap its button. Its own terms and privacy policy then apply.</li>
</ul>
<p>The app is distributed by Apple (App Store, TestFlight), which may process data under its own terms, outside the publisher’s control.</p>

<h2>5. The kasseigo.com website</h2>
<p>The website sets no cookies, uses no trackers or analytics and loads no external resources, except the feedback page (section 6). It is hosted on GitHub Pages (GitHub, Inc., United States), which may log visitors’ IP addresses, in particular for the security of the service, under the <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>. The publisher has no access to these logs.</p>

<h2>6. If you send feedback or write to the publisher</h2>
<p><b>Feedback form</b> (<a href="feedback.html">kasseigo.com/feedback</a>, also opened from the app): it sends the type of feedback, your message, the city if you choose one, your email address only if you give it, the page language and, from the app, the app and phone system versions. Nothing else is added automatically: no location, no identifier.</p>
<ul>
<li>To block robots, the page uses <b>Cloudflare Turnstile</b> (Cloudflare, Inc., United States), which analyses technical signals from the browser, under the <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare privacy policy</a>.</li>
<li>The message goes through a Cloudflare Workers service and is stored as a ticket in a <b>private</b> GitHub repository (GitHub, Inc., United States), accessible to the publisher only.</li>
<li>Purpose: fixing errors, improving the service and, if you gave your email, replying to you. Basis: the legitimate interest in handling the feedback received.</li>
<li>Tickets are kept as long as needed to handle and follow them up, then deleted. They are never sold or passed on to other third parties. You can ask for their deletion at any time.</li>
</ul>
<p><b>By email</b>: if you write to <a href="mailto:{MAIL}">{MAIL}</a>, your email address and message are used only to reply and follow up on your request, on the basis of the legitimate interest in answering messages received. They are kept as long as needed for that follow-up, then deleted, and are never sold or passed on to third parties. The mailbox is hosted by OVH SAS (France).</p>

<h2>7. Transfers outside the European Union</h2>
<p>Some of the services listed (GitHub, Inc. and Cloudflare, Inc. in particular) are located outside the European Union. The data they process (IP address, technical connection data and, for feedback, the message content) is processed under their own responsibility and safeguards.</p>

<h2>8. Your rights</h2>
<p>You have the rights of access, rectification, erasure, restriction, objection and portability. Since the publisher holds no data from the app, these rights mainly apply to feedback or an email exchange, at <a href="mailto:{MAIL}">{MAIL}</a>. For data processed by the third-party services listed, contact them directly.</p>
<p>You can lodge a complaint with the Belgian <b>Data Protection Authority</b> (Autorité de protection des données), rue de la Presse 35, 1000 Brussels, Belgium · <a href="https://www.dataprotectionauthority.be">dataprotectionauthority.be</a>, or with the authority of your country of residence (in France, the CNIL · <a href="https://www.cnil.fr">cnil.fr</a>).</p>

<h2>9. Minors</h2>
<p>The service knowingly collects no data about anyone, minors included. Vehicle rental is subject to the minimum age set by each operator.</p>

<h2>10. Security</h2>
<p>All app connections are encrypted (HTTPS; plain connections are refused). Each city file is checked (size and SHA-256 hash) before use. Links from the feeds only open if they lead to a secure page (https) or to the operator app.</p>

<h2>11. Changes</h2>
<p>This policy may change with the app. The date of the last update is shown at the top of the page. If the French and English versions differ, the French version prevails.</p>
"""

DESC = {
    'legal': 'Mentions légales de KasseiGo : éditeur, hébergement, propriété intellectuelle. Legal notice of the KasseiGo app.',
    'terms': 'Conditions d’utilisation de l’application gratuite KasseiGo, pour vélos et trottinettes partagés à Bruxelles et à Paris. Terms of use.',
    'privacy': 'Politique de confidentialité de KasseiGo : pas de compte, pas de publicité, pas de suivi ; votre position reste sur le téléphone. Privacy policy.',
}

CONTENT = {'legal': (LEGAL_FR, LEGAL_EN), 'terms': (TERMS_FR, TERMS_EN), 'privacy': (PRIVACY_FR, PRIVACY_EN)}


def page(key):
    fr_t, en_t = PAGES[key]
    fr, en = CONTENT[key]
    cur = ' aria-current="page"'
    tabs = lambda l: ''.join(
        f'<a href="{k}.html"{cur if k == key else ""}>{t[0] if l == "fr" else t[1]}</a>' for k, t in PAGES.items())
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{fr_t} · KasseiGo</title>
<meta name="description" content="{DESC[key]}">
<link rel="canonical" href="https://kasseigo.com/{key}.html">
<link rel="icon" type="image/png" sizes="64x64" href="{FAV}">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="KasseiGo">
<meta property="og:url" content="https://kasseigo.com/{key}.html">
<meta property="og:title" content="{fr_t} · KasseiGo">
<meta property="og:description" content="{DESC[key]}">
<meta property="og:image" content="https://kasseigo.com/img/og.jpg">
<style>{CSS}</style>
<script>
// French by default; English with #en, ?lang=en or a previous choice.
(function(){{var l='fr';try{{l=localStorage.getItem('kg-lang')||l}}catch(e){{}}
if(/[#?&](lang=)?en\\b/.test(location.hash+location.search))l='en';document.documentElement.lang=l}})();
</script>
</head>
<body>
<header><div class="wrap">
  <a class="brand" href="./"><img src="img/icon-192.png" alt="" width="36" height="36">KasseiGo</a>
  <div class="lang" role="group" aria-label="Langue / Language">
    <button type="button" data-set="fr">FR</button><button type="button" data-set="en">EN</button>
  </div>
</div></header>
<main class="wrap">
  <nav class="tabs" data-l="fr" aria-label="Pages légales">{tabs('fr')}</nav>
  <nav class="tabs" data-l="en" aria-label="Legal pages">{tabs('en')}</nav>
  <article data-l="fr" lang="fr">
    <h1>{fr_t}</h1>
    <p class="upd">Dernière mise à jour : {UPDATED_FR}</p>
    {fr}
  </article>
  <article data-l="en" lang="en">
    <h1>{en_t}</h1>
    <p class="upd">Last updated: {UPDATED_EN}</p>
    {en}
  </article>
</main>
<footer><div class="wrap">
  <a href="./">kasseigo.com</a>
  <a href="feedback.html" data-l="fr">Envoyer un retour</a><a href="feedback.html?lang=en" data-l="en">Send feedback</a>
  <span>© 2026 {NAME}</span>
  <span data-l="fr">Fait avec <span class="heart" role="img" aria-label="amour">♥</span> à Bruxelles</span>
  <span data-l="en">Made with <span class="heart" role="img" aria-label="love">♥</span> in Brussels</span>
</div></footer>
<script>
function setLang(l){{
  var r=document.documentElement;r.lang=l;
  document.querySelectorAll('[data-set]').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.set===l)}});
  try{{localStorage.setItem('kg-lang',l)}}catch(e){{}}
}}
document.querySelectorAll('[data-set]').forEach(function(b){{b.addEventListener('click',function(){{setLang(b.dataset.set)}})}});
setLang(document.documentElement.lang);
</script>
</body>
</html>
"""


for k in PAGES:
    (OUT / f'{k}.html').write_text(page(k))
print('ok', ', '.join(f'{k}.html' for k in PAGES))
