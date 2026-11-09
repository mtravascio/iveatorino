#!/usr/bin/env python3
"""Genera le pagine del sito IVE a Torino.

Uso:  python3 build.py      (oppure ./publish.sh per pubblicare)

Scrive le pagine in docs/, che è la cartella pubblicata da GitHub Pages.
Immagini e CSS stanno in docs/assets/ e NON vengono toccati: si modificano lì.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "docs")   # cartella pubblicata da GitHub Pages

SITE = "IVE a Torino"
WA = "https://whatsapp.com/channel/0029Vb6V2S27Noa7Re3MLe0u"
CAL = ("https://script.google.com/macros/s/"
       "AKfycbzdeOyxCEVWRphI1P3eCbvoeGcSKrlUnJ_9xuvQpjoVHb_Cqe-H3EEqznvLJ4WXOYSK4A/exec")
PET = "https://petizione.iveatorino.it/"
PRE = "https://preghiere.iveatorino.it/"
MAIL = "info@iveatorino.it"
MAPS = "https://maps.google.com/?q=Via+Baltimora+85+10137+Torino"

NAV = [
    ("index.html", "Home"),
    ("comunita.html", "Comunità"),
    ("adorazione.html", "Adorazione"),
    ("preghiera.html", "Preghiera"),
    ("orari.html", "Orari"),
    ("eventi.html", "Eventi"),
    ("formazione.html", "Formazione"),
    ("contatti.html", "Contatti"),
]

HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.iveatorino.it/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="IVE a Torino">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.iveatorino.it/assets/img/crest.png">
<meta name="theme-color" content="#7C2434">
<link rel="icon" href="assets/img/crest.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Open+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Salta al contenuto</a>
"""

TOPBAR = f"""<div class="topbar">
  <div class="wrap">
    <div>Parrocchia Maria Madre della Chiesa <span class="dot">·</span><span class="hide-s">Via Baltimora 85, Torino</span></div>
    <div><a href="{MAPS}" target="_blank" rel="noopener">Come arrivare</a><span class="dot">·</span><a href="mailto:{MAIL}">{MAIL}</a></div>
  </div>
</div>
"""

def header(active):
    links = "".join(
        f'<a href="{href}"{" class=\"on\"" if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<header>
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <img src="assets/img/crest.png" alt="Stemma dell'Istituto del Verbo Incarnato">
      <span><b>IVE a Torino</b><small>Istituto del Verbo Incarnato</small></span>
    </a>
    <button class="burger" aria-label="Apri il menu" aria-expanded="false" onclick="const m=document.getElementById('menu');m.classList.toggle('open');this.setAttribute('aria-expanded',m.classList.contains('open'))">
      <span></span><span></span><span></span>
    </button>
    <nav class="links" id="menu">
      {links}
      <a class="cta" href="{WA}">Canale WhatsApp</a>
    </nav>
  </div>
</header>
"""

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html">
          <img src="assets/img/crest.png" alt="" style="width:40px;height:40px">
          <span><b>IVE a Torino</b><small>Istituto del Verbo Incarnato</small></span>
        </a>
        <p style="margin-top:18px;max-width:34ch">Amici e terziari dell'Istituto del Verbo Incarnato a Torino. La chiesa di riferimento è Maria Madre della Chiesa, via Baltimora 85.</p>
      </div>
      <div>
        <h4>Dove siamo</h4>
        <ul>
          <li>Via Baltimora 85<br>10137 Torino</li>
          <li><a href="{MAPS}" target="_blank" rel="noopener">Indicazioni stradali</a></li>
        </ul>
      </div>
      <div>
        <h4>Link utili</h4>
        <ul>
          <li><a href="{PET}">Petizione</a></li>
          <li><a href="{PRE}">Preghiere per i Padri</a></li>
          <li><a href="https://app.regeomaria.net">Le nostre app</a></li>
          <li><a href="privacy.html">Privacy e cookie</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <div>© 2026 IVE a Torino</div>
      <div>Via Baltimora 85 · 10137 Torino</div>
    </div>
  </div>
</footer>
</body>
</html>
"""

def page(slug, title, desc, active, body, hero_title=None, hero_sub=None):
    out = HEAD.format(title=title, desc=desc, slug=slug)
    out += TOPBAR + header(active) + "<main id=\"main\">\n"
    if hero_title:
        out += f"""<div class="page-hero">
  <div class="wrap">
    <p class="eyebrow">IVE a Torino</p>
    <h1>{hero_title}</h1>
    {f'<p class="sub">{hero_sub}</p>' if hero_sub else ''}
  </div>
</div>
"""
    out += body + "\n</main>\n" + FOOTER
    return out


HOME = f"""
<div class="hero" id="top">
  <div class="hero-copy">
    <img class="hero-crest" src="assets/img/crest.png" alt="Stemma dell'Istituto del Verbo Incarnato">
    <p class="eyebrow">Torino · Maria Madre della Chiesa</p>
    <h1>Una comunità che resta</h1>
    <p>Amici e terziari dell'Istituto del Verbo Incarnato a Torino: l'Adorazione eucaristica che continua ogni venerdì, la preghiera per i padri, la petizione perché tornino nella diocesi. Dopo la loro partenza, la comunità non si è sciolta.</p>
    <div class="actions">
      <a class="btn btn-primary" href="orari.html">Orari e Adorazione</a>
      <a class="btn btn-ghost" href="{PET}">La Petizione</a>
    </div>
  </div>
  <figure class="hero-photo">
    <img src="assets/img/loreto.jpg" alt="La Santa Casa di Loreto: l'altare con l'immagine della Madonna e l'iscrizione «Hic Verbum caro factum est»">
    <figcaption>La Santa Casa di Loreto</figcaption>
  </figure>
</div>

<div class="facts">
  <div class="wrap">
    <div class="card">
      <div class="fact">
        <div class="k">Adorazione eucaristica</div>
        <p class="v">Ogni venerdì<br>9:00 – 18:00</p>
        <div class="n">Primo giovedì del mese: dalle 22:00 alla sera del venerdì</div>
      </div>
      <div class="fact">
        <div class="k">Sante Messe</div>
        <p class="v">18:30 feriale<br>10:30 e 18:30 domenica</p>
        <div class="n">Confessioni 17:45 – 18:20</div>
      </div>
      <div class="fact">
        <div class="k">Prossimo appuntamento</div>
        <p class="v">«L'universo:<br>caso o progetto?»</p>
        <div class="n">Venerdì 13 novembre, ore 21:00</div>
        <a class="more" href="eventi.html">Tutti gli eventi</a>
      </div>
    </div>
  </div>
</div>

<section id="comunita">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Chi siamo</p>
      <h2>Laici legati all'Istituto del Verbo Incarnato</h2>
      <p class="lead">Siamo amici e terziari dell'IVE: laici — famiglie, giovani, professionisti — che si riconoscono nel carisma dell'Incarnazione e che hanno condiviso per anni la vita della parrocchia di Maria Madre della Chiesa, in via Baltimora. La comunità è affidata a Maria Santissima di Loreto, la cui Santa Casa è il segno dell'Incarnazione.</p>
      <p>Da settembre 2025 i padri non sono più a Torino. La comunità non si è sciolta: l'Adorazione del venerdì continua, un gruppo prega per i sacerdoti e i seminaristi dell'Istituto e i fedeli laici hanno chiesto al Cardinale Repole che la Famiglia Religiosa torni nella diocesi.</p>
      <p>Questo sito raccoglie gli orari della chiesa, le iniziative e i canali con cui restare in contatto. Se è la prima volta che ci incontri, comincia dall'Adorazione: è il cuore di tutto il resto.</p>
      <a class="btn btn-line" href="comunita.html">Conosci la comunità</a>
    </div>
    <aside class="identity">
      <img class="identity-mark" src="assets/img/crest.png" alt="Stemma dell'Istituto del Verbo Incarnato">
      <p class="kicker">La chiesa</p>
      <h3>Maria Madre della Chiesa</h3>
      <p class="addr">Via Baltimora 85<br>10137 Torino</p>
      <hr>
      <dl>
        <dt>Adorazione</dt><dd>venerdì 9:00 – 18:00</dd>
        <dt>Messe</dt><dd>18:30 · domenica 10:30 e 18:30</dd>
        <dt>Confessioni</dt><dd>17:45 – 18:20</dd>
      </dl>
      <a class="btn btn-line" href="contatti.html">Come arrivare</a>
    </aside>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Tre porte d'ingresso</p>
    <h2 style="margin-bottom:44px">Da dove cominciare</h2>
    <div class="doors">
      <a class="door" href="adorazione.html">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17M3.5 12h17"/></svg>
        <h3>Adorazione</h3>
        <p>Il calendario delle ore di adorazione e la prenotazione dei turni, aggiornati ogni mese.</p>
        <span class="go">Calendario e turni</span>
      </a>
      <a class="door" href="{PET}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16M6 20V9l6-4 6 4v11"/><path d="M10 20v-5h4v5"/></svg>
        <h3>La Petizione</h3>
        <p>L'appello dei fedeli laici perché la Famiglia Religiosa dell'IVE torni nella diocesi di Torino: il testo, le firme, gli articoli.</p>
        <span class="go">Leggi e firma</span>
      </a>
      <a class="door" href="{PRE}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/></svg>
        <h3>Preghiere per i Padri</h3>
        <p>Sussidi e preghiere per sostenere spiritualmente i sacerdoti e i seminaristi dell'Istituto.</p>
        <span class="go">Materiale e preghiere</span>
      </a>
    </div>
  </div>
</section>

<section class="hours">
  <div class="wrap split" style="align-items:start">
    <div>
      <p class="eyebrow">Ogni settimana</p>
      <h2>Orari della chiesa</h2>
      <p class="lead">Parrocchia Maria Madre della Chiesa, via Baltimora 85. La chiesa è aperta per la preghiera personale negli orari di Adorazione.</p>
      <p><a class="btn btn-primary" href="orari.html">Tutti gli orari</a></p>
      <p class="note">Le preghiere comunitarie di devozione e gli orari supplementari di Adorazione si concordano con il sacerdote.</p>
    </div>
    <div>
      <table class="sched">
        <caption class="kicker">Orario ordinario</caption>
        <thead><tr><th></th><th>S. Messa</th><th>Adorazione</th><th>Confessioni</th></tr></thead>
        <tbody>
          <tr><td>Lunedì</td><td class="off">—</td><td class="off">—</td><td class="off">—</td></tr>
          <tr><td>Martedì</td><td>18:30</td><td class="off">—</td><td>su richiesta</td></tr>
          <tr><td>Mercoledì</td><td>8:00 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td></tr>
          <tr><td>Giovedì</td><td>8:00 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td></tr>
          <tr><td>Venerdì</td><td>18:30</td><td class="ad">9:00 – 18:00</td><td>17:45 – 18:20</td></tr>
          <tr><td>Sabato</td><td>18:30</td><td class="ad">17:30</td><td class="off">—</td></tr>
          <tr><td>Domenica</td><td>10:30 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td></tr>
        </tbody>
      </table>
      <p class="scrollhint">Scorri per vedere tutte le colonne →</p>
    </div>
  </div>
</section>

<section id="eventi">
  <div class="wrap">
    <p class="eyebrow">Vita della comunità</p>
    <h2 style="margin-bottom:52px">Prossimi appuntamenti</h2>
    <div class="event">
      <img src="assets/img/evento.jpg" alt="Locandina dell'incontro «L'universo: caso o progetto?»">
      <div>
        <p class="kicker">Cinque serate · Ingresso libero</p>
        <h3>«L'universo: caso o progetto?»</h3>
        <p>Cinque serate in anteprima per indagare le leggi della natura, la scienza e il codice segreto alla radice di ciò che esiste. Un percorso aperto a tutti, credenti e non.</p>
        <div class="when">
          <div><b>13 · 20 · 27 novembre</b>e 4 · 11 dicembre</div>
          <div><b>Ore 21:00</b>Parrocchia M2C, via Baltimora 85</div>
        </div>
        <p style="margin-top:18px"><a class="btn btn-line" href="eventi.html">Dettagli</a></p>
      </div>
    </div>
  </div>
</section>

<section class="tight" id="rivista">
  <div class="wrap rivista">
    <figure class="poster" style="max-width:320px">
      <img src="assets/img/rivista-cristo-in-tutto.jpg" alt="Copertina del primo numero della rivista «Cristo in Tutto», novembre 2026">
      <figcaption>«Cristo in Tutto», n. 1 — novembre 2026</figcaption>
    </figure>
    <div>
      <p class="eyebrow">La rivista</p>
      <h2>«Cristo in Tutto»</h2>
      <p class="lead">«Omnia in Christo instauranda»: è uscito il primo numero della rivista del Terzo Ordine. Ansia, Santa Messa, ateismo moderno, il Politico di Gand: quattro articoli per ricapitolare tutto in Cristo.</p>
      <p><a class="btn btn-line" href="formazione.html">Tutti i materiali di formazione</a></p>
    </div>
  </div>
</section>

<section class="quote tight">
  <div class="wrap">
    <p class="eyebrow" style="text-align:center">Il motto dell'Istituto</p>
    <blockquote>«Hic Verbum caro factum est»</blockquote>
    <p class="motto-it">E il Verbo si fece carne e venne ad abitare in mezzo a noi</p>
    <cite>Gv 1,14</cite>
  </div>
</section>

<section class="band tight" id="petizione">
  <div class="wrap">
    <div>
      <h2>I padri tornino a Torino</h2>
      <p>Dopo la partenza della Famiglia Religiosa dell'IVE, i fedeli laici hanno chiesto al Cardinale Repole il suo ritorno nella diocesi. Puoi leggere il testo, le testimonianze e aggiungere la tua firma.</p>
    </div>
    <div class="actions">
      <a class="btn btn-white" href="{PET}">Firma la petizione</a>
      <a class="btn btn-ghost" href="{PET}testimonianze">Testimonianze</a>
    </div>
  </div>
</section>

<section class="tight" id="contatti">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Restiamo in contatto</p>
      <h2>Un canale solo per gli avvisi importanti</h2>
      <p class="lead">Sul canale WhatsApp pubblichiamo orari straordinari, variazioni e iniziative. La newsletter arriva una volta al mese: niente pubblicità, solo la vita della comunità.</p>
      <p><a href="{WA}" class="btn btn-primary">Iscriviti al canale WhatsApp</a></p>
    </div>
    <div class="cardpanel">
      <p class="kicker">Newsletter</p>
      <h3>Una email al mese</h3>
      <p>La vita della comunità, gli appuntamenti, il notiziario. Nessuna pubblicità, disdetta con un clic.</p>
      <a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:6px" href="https://groups.google.com/g/iveatorino" target="_blank" rel="noopener">Iscriviti alla newsletter</a>
      <p class="fine">Si apre Google Gruppi: serve un account Google e un clic su «Partecipa al gruppo». In alternativa scrivi a <a href="mailto:iveatorino+subscribe@googlegroups.com?subject=Iscrizione%20newsletter">iveatorino+subscribe@googlegroups.com</a>.</p>
    </div>
  </div>
</section>
"""

COMUNITA = f"""
<section>
  <div class="wrap split" style="align-items:start">
    <div class="prose">
      <p class="eyebrow">Chi siamo</p>
      <h2>Una famiglia religiosa, e i laici che la portano nel cuore</h2>
      <p class="lead">L'Istituto del Verbo Incarnato è una famiglia religiosa della Chiesa cattolica, presente in diversi paesi. A Torino ha animato per anni la parrocchia di Maria Madre della Chiesa: qui i padri hanno celebrato, confessato, accompagnato famiglie e giovani.</p>
      <p>Il nome dice il programma: il Verbo si è fatto carne. Per questo la spiritualità dell'Istituto passa dalle cose concrete — l'Eucaristia, le persone, il lavoro, la casa — e non da un'idea astratta. È la stessa spiritualità che i terziari cercano di vivere nel mondo, nelle proprie famiglie e nei propri lavori.</p>
      <p>Da settembre 2025 i padri non sono più a Torino: la Famiglia Religiosa ha lasciato la diocesi. La comunità laicale che si era formata attorno a loro non si è sciolta. Continua a ritrovarsi, tiene viva l'Adorazione del venerdì, prega per i sacerdoti e i seminaristi dell'Istituto e chiede al Cardinale Repole che possano tornare.</p>
      <h3>Che cosa trovi qui</h3>
      <ul class="ticks">
        <li>L'Adorazione eucaristica del venerdì, con il calendario e i turni</li>
        <li>Gli orari della chiesa di Maria Madre della Chiesa</li>
        <li>La preghiera per i padri e i seminaristi dell'Istituto</li>
        <li>Gli incontri e le iniziative aperte a tutti</li>
        <li>La petizione dei fedeli laici per il ritorno dell'IVE in diocesi</li>
      </ul>
    </div>
    <aside class="sidecard">
      <p class="kicker">In breve</p>
      <dl>
        <dt>Dove</dt><dd>Via Baltimora 85, 10137 Torino</dd>
        <dt>Chi</dt><dd>Amici e terziari dell'Istituto del Verbo Incarnato</dd>
        <dt>Chiesa</dt><dd>Maria Madre della Chiesa</dd>
        <dt>Contatti</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
        <dt>Canale</dt><dd><a href="{WA}">WhatsApp</a></dd>
      </dl>
      <a class="btn btn-primary" style="width:100%;justify-content:center" href="contatti.html">Come arrivare</a>
    </aside>
  </div>
</section>

<section class="tight">
  <div class="wrap split">
    <div>
      <p class="eyebrow">La patrona</p>
      <h2>Maria Santissima di Loreto</h2>
      <p class="lead">La comunità è affidata a Maria Santissima di Loreto. La Santa Casa venerata nel santuario marchigiano è, secondo la tradizione, la casa di Nazareth dove l'angelo annunciò a Maria l'Incarnazione del Verbo.</p>
      <p>Accanto a quella casa si leggono le parole che l'Istituto ha preso come motto — <i>Hic Verbum caro factum est</i>, «qui il Verbo si è fatto carne» — e che dicono il modo in cui questa comunità legge la propria vita: Dio che entra nella storia, in una casa, in un quartiere, dentro le giornate di chi ci passa.</p>
      <p>Non è una devozione ornamentale. È il motivo per cui l'Adorazione resta il centro della giornata e per cui la parrocchia è casa prima che struttura.</p>
    </div>
    <figure style="margin:0">
      <img src="assets/img/loreto.jpg" alt="La Santa Casa di Loreto con l'iscrizione «Hic Verbum caro factum est»" style="border:1px solid var(--line)">
      <figcaption>La Santa Casa di Loreto, dove il Verbo si è fatto carne.</figcaption>
    </figure>
  </div>
</section>

<section class="quote tight">
  <div class="wrap">
    <p class="eyebrow" style="text-align:center">Il motto dell'Istituto</p>
    <blockquote>«Hic Verbum caro factum est»</blockquote>
    <p class="motto-it">E il Verbo si fece carne e venne ad abitare in mezzo a noi</p>
    <cite>Gv 1,14</cite>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">La vita di ogni giorno</p>
    <h2 style="margin-bottom:40px">Tre cose che ci tengono insieme</h2>
    <div class="doors">
      <div class="door">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17M3.5 12h17"/></svg>
        <h3>L'Eucaristia</h3>
        <p>Il centro della giornata: la Messa, l'Adorazione, la preghiera davanti al Santissimo.</p>
      </div>
      <div class="door">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 4v6c0 4-3 7-7 8-4-1-7-4-7-8V7z"/></svg>
        <h3>La formazione</h3>
        <p>La <i>Guida del terziario</i>, gli incontri e lo studio: la vocazione laicale dentro il carisma dell'Incarnazione.</p>
      </div>
      <div class="door">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 6.5h17v11h-17z"/><path d="M3.5 7l8.5 6 8.5-6"/></svg>
        <h3>La richiesta</h3>
        <p>La petizione al Cardinale Repole perché la Famiglia Religiosa torni nella diocesi di Torino.</p>
      </div>
    </div>
  </div>
</section>
"""

ADORAZIONE = f"""
<section>
  <div class="wrap split" style="align-items:start">
    <div class="prose">
      <p class="eyebrow">Adorazione eucaristica</p>
      <h2>Il cuore della giornata</h2>
      <p class="lead">Ogni venerdì la chiesa resta aperta dalle 9:00 alle 18:00 con il Santissimo esposto; una volta al mese l'Adorazione si prolunga dalla sera del giovedì fino al venerdì pomeriggio.</p>
      <p>Per questa comunità l'Adorazione del venerdì è il punto fermo della settimana. Per coprire tutte le ore serve qualcuno in chiesa in ogni momento: si può prenotare un'ora — o più — dal calendario online.</p>
      <h3>Come funziona</h3>
      <ol class="steps">
        <li><b>Scegli l'ora</b> sul calendario e vedi subito quali sono ancora libere.</li>
        <li><b>Prenota</b> con il tuo nome: la casella si colora e gli altri sanno che quell'ora è coperta.</li>
        <li><b>Vieni in chiesa</b> a quell'ora, anche solo per venti minuti: l'importante è che ci sia qualcuno.</li>
      </ol>
      <p class="note">Se non puoi più venire, cancella la prenotazione: quell'ora torna disponibile per qualcun altro.</p>
      <p><a class="btn btn-primary" href="{CAL}">Apri il calendario</a></p>
      <p class="note">Durante l'ora di Adorazione puoi recitare il Rosario seguendo l'audio: <a href="preghiera.html">le quattro corone</a>.</p>
    </div>
    <aside class="sidecard">
      <p class="kicker">Orari</p>
      <dl>
        <dt>Ogni venerdì</dt><dd>9:00 – 18:00</dd>
        <dt>Primo giovedì del mese</dt><dd>dalle 22:00 del giovedì alle 18:00 del venerdì</dd>
        <dt>Dove</dt><dd>Chiesa di Maria Madre della Chiesa, via Baltimora 85</dd>
      </dl>
      <a class="btn btn-primary" style="width:100%;justify-content:center" href="{CAL}">Prenota un'ora</a>
    </aside>
  </div>
</section>

<section class="hours">
  <div class="wrap">
    <p class="eyebrow">La settimana</p>
    <h2>Adorazione e confessioni</h2>
    <div class="tablewrap">
      <table class="sched">
        <caption class="kicker">Orario ordinario</caption>
        <thead><tr><th></th><th>Adorazione</th><th>Confessioni</th><th>S. Messa</th></tr></thead>
        <tbody>
          <tr><td>Mercoledì</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td>8:00 · 18:30</td></tr>
          <tr><td>Giovedì</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td>8:00 · 18:30</td></tr>
          <tr><td>Venerdì</td><td class="ad">9:00 – 18:00</td><td>17:45 – 18:20</td><td>18:30</td></tr>
          <tr><td>Sabato</td><td class="ad">17:30</td><td class="off">—</td><td>18:30</td></tr>
          <tr><td>Domenica</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td>10:30 · 18:30</td></tr>
        </tbody>
      </table>
      <p class="scrollhint">Scorri per vedere tutte le colonne →</p>
    </div>
    <p class="note">La domenica le confessioni seguono l'orario feriale. Per un colloquio in altri momenti scrivi a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap split" style="align-items:center">
    <div class="prose">
      <p class="eyebrow">La locandina</p>
      <h2>Un'ora davanti al Santissimo</h2>
      <p class="lead">L'Adorazione non è un servizio da organizzare: è tempo davanti a Dio. La locandina della comunità lo ricorda ogni anno, e le ore da coprire sono ancora tante.</p>
      <p><a class="btn btn-primary" href="{CAL}">Prenota la tua ora</a></p>
      <p class="note">Gli orari aggiornati sono quelli qui sopra: venerdì 9:00 – 18:00, primo giovedì del mese dalle 22:00.</p>
    </div>
    <figure class="poster" style="max-width:420px">
      <img src="assets/img/locandina-adorazione.jpg" alt="Locandina dell'Adorazione eucaristica continua: l'ostensorio con il Santissimo">
      <figcaption>Adorazione eucaristica continua · Maria Madre della Chiesa</figcaption>
    </figure>
  </div>
</section>
"""

ORARI = f"""
<section>
  <div class="wrap">
    <p class="eyebrow">Ogni settimana</p>
    <h2>Orari della chiesa</h2>
    <p class="lead" style="max-width:60ch">Parrocchia Maria Madre della Chiesa, via Baltimora 85. Gli orari possono cambiare nelle feste e in estate: in quel caso lo trovi sul canale WhatsApp.</p>
    <div class="tablewrap">
      <table class="sched big">
        <thead><tr><th></th><th>S. Messa</th><th>Adorazione</th><th>Confessioni</th><th>Ufficio</th></tr></thead>
        <tbody>
          <tr><td>Lunedì</td><td class="off">—</td><td class="off">—</td><td class="off">—</td><td class="off">—</td></tr>
          <tr><td>Martedì</td><td>18:30</td><td class="off">—</td><td>su appuntamento</td><td>Segreteria 17:00 – 18:00</td></tr>
          <tr><td>Mercoledì</td><td>8:00 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td>Segreteria 17:00 – 18:00<br>Don 19:15 – 20:00</td></tr>
          <tr><td>Giovedì</td><td>8:00 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td>Don 11:00 – 12:30<br>Segreteria 17:00 – 18:00</td></tr>
          <tr><td>Venerdì</td><td>18:30</td><td class="ad">9:00 – 18:00<br><span class="tiny">continua</span></td><td>17:45 – 18:20</td><td>Segreteria 17:00 – 18:00</td></tr>
          <tr><td>Sabato e vigilie</td><td>18:30</td><td class="ad">17:30</td><td class="off">—</td><td class="off">—</td></tr>
          <tr><td>Domenica e feste</td><td>10:30 · 18:30</td><td class="ad">17:30</td><td>17:45 – 18:20</td><td class="off">—</td></tr>
        </tbody>
      </table>
      <p class="scrollhint">Scorri per vedere tutte le colonne →</p>
    </div>
    <p class="note">Il martedì le confessioni si prenotano al campanello dell'ufficio o si chiedono al sacerdote. Le preghiere comunitarie di devozione e gli orari supplementari di Adorazione si concordano con il don. Per un appuntamento scrivi a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
    <p><a class="btn btn-primary" href="adorazione.html">Calendario dell'Adorazione</a></p>
  </div>
</section>

<section class="hours">
  <div class="wrap split" style="align-items:start">
    <div>
      <p class="eyebrow">Prima di venire</p>
      <h2>Tre cose utili</h2>
      <p class="lead">La chiesa si raggiunge in tram o in auto; il parcheggio è in cortile.</p>
      <p><a class="btn btn-line" href="contatti.html">Come arrivare</a></p>
    </div>
    <div class="prose">
      <h3>Adorazione</h3>
      <p>Il venerdì la chiesa resta aperta dalle 9:00 alle 18:00 con l'Adorazione continua. Negli altri giorni il Santissimo è esposto dalle 17:30, prima della Messa serale.</p>
      <h3>Confessioni</h3>
      <p>Mercoledì, giovedì e venerdì dalle 17:45 alle 18:20; la domenica lo stesso orario. Il martedì si prenotano al campanello dell'ufficio.</p>
      <h3>Feste ed estate</h3>
      <p>Gli orari delle solennità vengono pubblicati sul canale WhatsApp e sul bollettino parrocchiale.</p>
    </div>
  </div>
</section>
"""

EVENTI = f"""
<section>
  <div class="wrap">
    <p class="eyebrow">Vita della comunità</p>
    <h2>Prossimi appuntamenti</h2>
    <div class="event" style="margin-top:52px">
      <img src="assets/img/evento.jpg" alt="Locandina dell'incontro «L'universo: caso o progetto?»">
      <div>
        <p class="kicker">Cinque serate · Ingresso libero · Ore 21:00</p>
        <h3>«L'universo: caso o progetto?»</h3>
        <p>Cinque serate in anteprima per indagare le leggi della natura, la scienza e il codice segreto alla radice di ciò che esiste. Un percorso aperto a tutti, credenti e non, a cura della parrocchia con gli amici di «Verso l'Alto».</p>
        <div class="when">
          <div><b>13 · 20 · 27 novembre</b>e 4 · 11 dicembre</div>
          <div><b>Parrocchia M2C</b>Via Baltimora 85, Torino</div>
        </div>
        <p class="note">Non serve iscrizione. Per informazioni: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="hours">
  <div class="wrap">
    <p class="eyebrow">Ogni settimana</p>
    <h2>Appuntamenti fissi</h2>
    <div class="doors" style="margin-top:36px">
      <div class="door">
        <h3>Adorazione</h3>
        <p>Venerdì 9:00 – 18:00; primo giovedì del mese dalle 22:00.</p>
        <a class="go" href="adorazione.html">Calendario</a>
      </div>
      <div class="door">
        <h3>Messe</h3>
        <p>Feriale 18:30; domenica 10:30 e 18:30.</p>
        <a class="go" href="orari.html">Tutti gli orari</a>
      </div>
      <div class="door">
        <h3>Confessioni</h3>
        <p>Ogni giorno feriale 17:45 – 18:20, e su richiesta.</p>
        <a class="go" href="orari.html">Dettagli</a>
      </div>
    </div>
  </div>
</section>

<section class="hours">
  <div class="wrap">
    <p class="eyebrow">Terzo Ordine · Eventi nazionali</p>
    <h2>Novembre 2026</h2>
    <p class="lead" style="max-width:64ch;margin-bottom:14px">Due appuntamenti del Terzo Ordine Secolare aperti anche agli amici, a Montefiascone (VT), nel santuario di San Flaviano.</p>
    <div class="twoup">
      <figure class="poster">
        <img src="assets/img/locandina-ritiro.jpg" alt="Locandina del Ritiro di Formazione Nazionale del Terzo Ordine, 20-22 novembre 2026">
        <figcaption><b>Ritiro di Formazione Nazionale</b>20 – 22 novembre 2026 · Montefiascone (VT)</figcaption>
      </figure>
      <figure class="poster">
        <img src="assets/img/locandina-cristo-re.jpg" alt="Locandina della Solennità di Cristo Re, 22 novembre 2026, Montefiascone">
        <figcaption><b>Solennità di Cristo Re</b>22 novembre 2026 · Seminario «Marco Antonio Barbarigo»</figcaption>
      </figure>
    </div>
    <p class="note" style="margin-top:26px">Iscrizioni e quota: i riferimenti sono in locandina. Per organizzarci con l'andata da Torino scrivi a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Archivio</p>
    <h2 style="margin-bottom:18px">Appuntamenti passati</h2>
    <p class="lead" style="max-width:62ch">Le locandine e i resoconti degli incontri già svolti restano qui, così chi arriva dopo può farsi un'idea di cosa si fa in parrocchia.</p>
    <p class="note">Nessun evento archiviato: è lo spazio da riempire con le prime tre o quattro schede.</p>
  </div>
</section>
"""

CONTATTI = f"""
<section>
  <div class="wrap split" style="align-items:start">
    <div class="prose">
      <p class="eyebrow">Contatti</p>
      <h2>Dove trovarci</h2>
      <p class="lead">Chiesa e parrocchia di Maria Madre della Chiesa, via Baltimora 85, 10137 Torino.</p>
      <p>Per informazioni su orari, sacramenti, catechismo o iniziative scrivi a <a href="mailto:{MAIL}">{MAIL}</a>. Per gli avvisi urgenti (variazioni di orario, feste, eventi) il canale WhatsApp è il mezzo più rapido.</p>
      <p><a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps</a></p>
      <h3>Newsletter</h3>
      <p>Una volta al mese, la vita della comunità. Per iscriverti basta un account Google: si apre il gruppo, si clicca «Partecipa al gruppo», fine.</p>
      <p><a class="btn btn-primary" href="https://groups.google.com/g/iveatorino" target="_blank" rel="noopener">Iscriviti alla newsletter</a></p>
      <p class="fine">Senza account Google puoi iscriverti scrivendo a <a href="mailto:iveatorino+subscribe@googlegroups.com?subject=Iscrizione%20newsletter">iveatorino+subscribe@googlegroups.com</a>. Per scrivere alla redazione: <a href="mailto:newsletter@iveatorino.it">newsletter@iveatorino.it</a>.</p>
    </div>
    <aside class="sidecard">
      <p class="kicker">Recapiti</p>
      <dl>
        <dt>Indirizzo</dt><dd>Via Baltimora 85<br>10137 Torino</dd>
        <dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
        <dt>WhatsApp</dt><dd><a href="{WA}">Canale «IVE a Torino»</a></dd>
        <dt>Siti</dt><dd><a href="{PET}">Petizione</a> · <a href="{PRE}">Preghiere</a></dd>
      </dl>
    </aside>
  </div>
</section>

<section class="hours tight">
  <div class="wrap">
    <p class="eyebrow">Ultimi numeri</p>
    <h2 style="margin-bottom:26px">Il notiziario della comunità</h2>
    <div class="issues">
      <a class="issue" href="https://groups.google.com/g/iveatorino" target="_blank" rel="noopener">
        <span class="date">8 novembre 2026</span>
        <span class="ttl">Nasce la nuova rivista: «Cristo in Tutto»</span>
        <span class="desc">Notiziario di novembre: la nuova rivista della comunità, «Omnia in Christo instauranda».</span>
      </a>
      <a class="issue" href="https://groups.google.com/g/iveatorino" target="_blank" rel="noopener">
        <span class="date">8 novembre 2026</span>
        <span class="ttl">Cronache IVE dal Mondo</span>
        <span class="desc">Egitto e Tanzania: «Andate in tutto il mondo e predicate il vangelo».</span>
      </a>
    </div>
    <p class="note">Tutti i numeri restano nell'archivio del gruppo; l'iscrizione serve a riceverli per email.</p>
  </div>
</section>

<section class="hours tight">
  <div class="wrap">
    <div class="map">
      <iframe title="Mappa: via Baltimora 85, Torino"
        src="https://www.openstreetmap.org/export/embed.html?bbox=7.6325%2C45.0415%2C7.6465%2C45.0495&amp;layer=mapnik&amp;marker=45.0455489%2C7.6395122"
        loading="lazy"></iframe>
    </div>
    <p class="note">La chiesa è in via Baltimora 85, zona Santa Rita. Per il percorso più comodo usa «Indicazioni stradali», oppure apri la posizione in OpenStreetMap: <a href="https://www.openstreetmap.org/?mlat=45.0455489&amp;mlon=7.6395122#map=17/45.04555/7.63951">vedi sulla mappa</a>.</p>
  </div>
</section>
"""

PRIVACY = f"""
<section class="tight">
  <div class="wrap prose">
    <p class="eyebrow">Informazioni legali</p>
    <h1 style="font-size:2.4rem">Privacy e cookie</h1>
    <p class="lead">Questa pagina spiega quali dati raccogliamo attraverso il sito e come vengono trattati.</p>
    <h3>Titolare del trattamento</h3>
    <p>Amici e terziari dell'Istituto del Verbo Incarnato a Torino — chiesa di Maria Madre della Chiesa, via Baltimora 85, 10137 Torino. Contatto: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
    <h3>Quali dati raccogliamo</h3>
    <ul class="ticks">
      <li><b>Newsletter</b>: l'indirizzo email che ci comunichi iscrivendoti al gruppo Google «IVE a Torino». Serve solo a inviarti gli aggiornamenti; puoi cancellarti in qualsiasi momento.</li>
      <li><b>Petizione</b>: nome e cognome, città ed eventuale messaggio, raccolti sul sito <a href="{PET}">petizione.iveatorino.it</a> per presentare l'appello all'Autorità ecclesiastica.</li>
      <li><b>Navigazione</b>: questo sito non usa cookie propri, non profila e non vende dati. La mappa è servita da OpenStreetMap, che non imposta cookie di profilazione.</li>
    </ul>
    <h3>Base giuridica e diritti</h3>
    <p>Il trattamento si basa sul consenso (newsletter) e sull'interesse legittimo a sostenere l'appello (petizione). Puoi chiedere accesso, rettifica o cancellazione scrivendo a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
    <h3>Conservazione</h3>
    <p>I dati della newsletter restano finché non chiedi la cancellazione; quelli della petizione per il tempo necessario alla sua presentazione.</p>
    <p class="note">Bozza da far verificare prima della pubblicazione: aggiungere eventuale responsabile del trattamento, tempi esatti e riferimenti al registro delle attività.</p>
  </div>
</section>
"""

VIRTUS = [
    ("virtus-01-esame-particolare.pdf", "Virtus 1", "L'esame particolare e il difetto dominante", "", 76),
    ("virtus-03-duc-in-altum.pdf", "Virtus 3", "«Duc in altum!»", "Essenza e formazione della magnanimità", 40),
    ("virtus-04-educazione-e-grazia.pdf", "Virtus 4", "Da lupi ad agnelli", "Educazione e grazia", 48),
    ("virtus-07-crisi-di-paternita.pdf", "Virtus 7", "Crisi di paternità", "Il padre assente", 72),
    ("virtus-10-cammino-del-perdono.pdf", "Virtus 10", "Il cammino del perdono", "", 160),
    ("virtus-13-maturita-secondo-cristo.pdf", "Virtus 13", "La maturità secondo Cristo", "L'uomo alla luce del Discorso della Montagna", 134),
    ("virtus-14-meditazioni-dio-padre.pdf", "Virtus 14", "Meditazioni su Dio Padre", "", 88),
    ("virtus-15-superficialita-e-frivolo.pdf", "Virtus 15", "La superficialità e la sindrome del frivolo", "", 64),
    ("virtus-16-educare-la-volonta.pdf", "Virtus 16", "Educare la volontà", "", 164),
    ("virtus-17-confidate-nel-signore.pdf", "Virtus 17", "«Confidate sempre nel Signore»", "Psicologia e spiritualità della fiducia · Salmo 62,9", 68),
    ("virtus-18-maturare-la-personalita.pdf", "Virtus 18", "Maturare la personalità", "", 100),
    ("virtus-20-l-accidia.pdf", "Virtus 20", "L'accidia", "Appunti psicologici e spirituali sul «male della delusione»", 99),
]

DOCS = [
    ("esercizi-spirituali.pdf", "Spiritualità", "Esercizi Spirituali", "Il testo di Sant'Ignazio di Loyola: le annotazioni, le quattro settimane, le regole del discernimento.", 76),
    ("catechismo-maggiore-pio-x.pdf", "Catechismo", "Il Catechismo Maggiore di San Pio X", "Le quattro parti della dottrina cristiana: il Credo, l'orazione, i comandamenti, i sacramenti.", 127),
    ("guida-del-terziario.pdf", "Terzo Ordine", "Essere una nuova incarnazione del Verbo", "Manuale del Terzo Ordine Secolare dell'Istituto del Verbo Incarnato.", 55),
    ("rege-o-maria.pdf", "Mariologia", "Rege O Maria", "", 150),
]


def doc_grid(items, cols=3):
    """Schede PDF: dimensione calcolata dal file, non scritta a mano."""
    cards = []
    for fname, label, title, sub, pages in items:
        path = os.path.join(OUT, "assets", "pdf", fname)
        size = "%.1f MB" % (os.path.getsize(path) / 1048576.0)
        sub_html = '<p class="sub">%s</p>' % sub if sub else ""
        cards.append(
            '      <article class="doc">\n'
            '        <p class="n">%s</p>\n'
            '        <h3>%s</h3>\n'
            '        %s\n'
            '        <p class="meta">%d pagine · %s</p>\n'
            '        <a class="dl" href="assets/pdf/%s" target="_blank" rel="noopener">Apri il PDF</a>\n'
            '      </article>' % (label, title, sub_html, pages, size.replace(".", ","), fname)
        )
    cls = 'docs' if cols == 3 else 'docs c%d' % cols
    return '<div class="%s">\n' % cls + "\n".join(cards) + "\n    </div>"


FORMAZIONE = f"""
<section class="tight">
  <div class="wrap">
    <div class="prose" style="max-width:74ch">
      <p class="eyebrow">Formazione</p>
      <h2>I libri della comunità</h2>
      <p class="lead">La formazione dei terziari e degli amici dell'Istituto passa da pochi testi scelti: la collana <em>Virtus</em> di p. Miguel Ángel Fuentes, i documenti del Terzo Ordine, il catechismo della tradizione. Sono tutti qui, da leggere o scaricare.</p>
      <p>Sono file PDF: si aprono nel browser e restano consultabili anche senza connessione, una volta scaricati. Non serve registrarsi.</p>
    </div>
  </div>
</section>

<section class="hours">
  <div class="wrap">
    <p class="eyebrow">Collana Virtus</p>
    <h2 style="margin-bottom:10px">Formazione umana e spirituale</h2>
    <p class="note" style="max-width:66ch;margin-bottom:34px">Dodici volumi di p. Miguel Ángel Fuentes, IVE — Ediciones IVE. Psicologia e vita interiore: il difetto dominante, la volontà, la maturità, il perdono, l'accidia.</p>
    {doc_grid(VIRTUS)}
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Documenti</p>
    <h2 style="margin-bottom:34px">Manuali e sussidi</h2>
    {doc_grid(DOCS, 2)}
    <p class="note" style="margin-top:26px">I testi sono pubblicati con il permesso dell'Istituto del Verbo Incarnato. Se un file non si apre o trovi un errore, scrivi a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
  </div>
</section>

<section class="hours">
  <div class="wrap split" style="align-items:center">
    <div class="prose">
      <p class="eyebrow">La rivista</p>
      <h2>«Cristo in Tutto»</h2>
      <p class="lead">«Omnia in Christo instauranda» — tutto ricapitolare in Cristo. Il primo numero è uscito il 1° novembre 2026.</p>
      <p>In questo numero:</p>
      <ul class="ticks">
        <li>Il grande male del secolo: l'ansia</li>
        <li>Il tesoro della Santa Messa</li>
        <li>Introduzione all'ateismo moderno</li>
        <li>L'annunciazione del Politico di Gand</li>
      </ul>
      <p><a class="btn btn-line" href="assets/img/rivista-indice.jpg" target="_blank" rel="noopener">Sfoglia l'indice</a></p>
      <p class="note">Per ricevere i prossimi numeri iscriviti alla newsletter della comunità.</p>
    </div>
    <figure class="poster" style="max-width:340px">
      <img src="assets/img/rivista-cristo-in-tutto.jpg" alt="Copertina del primo numero della rivista «Cristo in Tutto», novembre 2026">
      <figcaption>«Cristo in Tutto», n. 1 — novembre 2026</figcaption>
    </figure>
  </div>
</section>
"""

ROSA = [
    ("rosario-gaudiosi.mp3", "Misteri gaudiosi", "Lunedì e sabato", "26:13",
     "Dall'Annunciazione al ritrovamento di Gesù nel tempio: la gioia degli inizi."),
    ("rosario-luminosi.mp3", "Misteri luminosi", "Giovedì", "26:24",
     "La vita pubblica del Signore: dal battesimo al Giordano all'istituzione dell'Eucaristia."),
    ("rosario-dolorosi.mp3", "Misteri dolorosi", "Martedì e venerdì", "26:05",
     "La Passione: dall'agonia nell'orto alla morte in croce."),
    ("rosario-gloriosi.mp3", "Misteri gloriosi", "Mercoledì e domenica", "26:01",
     "Dalla Risurrezione all'incoronazione di Maria: la vittoria che apre il cielo."),
]


def audio_rows(items):
    """Righe con lettore audio: nessun preload, così la pagina resta leggera."""
    out = []
    for fname, title, days, dur, desc in items:
        path = os.path.join(OUT, "assets", "audio", fname)
        size = "%.1f MB" % (os.path.getsize(path) / 1048576.0)
        out.append(
            '      <article class="audio-row">\n'
            '        <div>\n'
            '          <p class="k">%s · %s</p>\n'
            '          <h3>%s</h3>\n'
            '          <p>%s</p>\n'
            '        </div>\n'
            '        <div class="player">\n'
            '          <audio controls preload="none" src="assets/audio/%s"></audio>\n'
            '          <p class="note">%s · <a href="assets/audio/%s" download>scarica l\'MP3</a></p>\n'
            '        </div>\n'
            '      </article>' % (title, dur, title, desc, fname, size.replace(".", ","), fname)
        )
    return '\n'.join(out)


PREGHIERA = f"""
<section class="tight">
  <div class="wrap">
    <div class="prose" style="max-width:74ch">
      <p class="eyebrow">Preghiera</p>
      <h2>Il Santo Rosario</h2>
      <p class="lead">Le quattro corone, registrate per intero: misteri gaudiosi, luminosi, dolorosi e gloriosi. Un modo semplice per recitare il Rosario durante l'ora di Adorazione, o in famiglia la sera.</p>
      <p>Si può ascoltare direttamente da questa pagina — l'audio parte con un clic, senza scaricare tutto in anticipo — oppure salvare il file e portarlo con sé, dove la connessione non arriva.</p>
    </div>
  </div>
</section>

<section class="hours">
  <div class="wrap">
    <p class="eyebrow">Le quattro corone</p>
    <h2 style="margin-bottom:8px">I misteri di oggi</h2>
    <p class="note" style="max-width:64ch;margin-bottom:18px">Ogni registrazione dura circa ventisei minuti. La tradizione assegna i misteri ai giorni della settimana; chi preferisce può seguirne altri.</p>
    <div class="audio-list">
{audio_rows(ROSA)}
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap split" style="align-items:start">
    <div class="prose">
      <p class="eyebrow">Come si recita</p>
      <h2>Una corona, cinque misteri</h2>
      <p>Si comincia con il segno della croce e il Credo, poi un Padre nostro, tre Ave Maria e il Gloria. Seguono i cinque misteri del giorno: per ciascuno si annuncia il mistero, si recita un Padre nostro, dieci Ave Maria e il Gloria. Si chiude con la Salve Regina e la preghiera per il Santo Padre.</p>
      <p>Durante l'Adorazione del venerdì il Rosario si può recitare in chiesa, seguendo l'audio anche a bassa voce; in famiglia funziona bene la sera, quando tutti sono in casa.</p>
      <p><a class="btn btn-line" href="{PRE}">Preghiere per i padri</a></p>
    </div>
    <aside class="sidecard">
      <p class="kicker">In chiesa</p>
      <dl>
        <dt>Adorazione</dt><dd>venerdì 9:00 – 18:00</dd>
        <dt>Primo giovedì</dt><dd>dalle 22:00 del giovedì alle 18:00 del venerdì</dd>
        <dt>Dove</dt><dd>Maria Madre della Chiesa, via Baltimora 85</dd>
      </dl>
      <a class="btn btn-primary" style="width:100%;justify-content:center" href="adorazione.html">Calendario dell'Adorazione</a>
    </aside>
  </div>
</section>

<section class="hours tight">
  <div class="wrap">
    <p class="note">Registrazioni audio: Radio Maria. Se trovi un file che non si apre, scrivi a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
  </div>
</section>
"""

PAGES = [
    ("index.html", "IVE a Torino — Amici e terziari dell'Istituto del Verbo Incarnato",
     "La comunità laicale di amici e terziari dell'Istituto del Verbo Incarnato a Torino: Adorazione eucaristica, orari della chiesa di Maria Madre della Chiesa, petizione per il ritorno dei padri.",
     "index.html", HOME, None, None),
    ("comunita.html", "La comunità — IVE a Torino",
     "Gli amici e i terziari dell'Istituto del Verbo Incarnato a Torino: chi sono, cosa fanno dopo la partenza dei padri, perché chiedono il loro ritorno nella diocesi.",
     "comunita.html", COMUNITA, "La comunità", "Amici e terziari dell'IVE, dopo la partenza dei padri."),
    ("adorazione.html", "Adorazione eucaristica — IVE a Torino",
     "Orari e calendario dell'Adorazione eucaristica a Maria Madre della Chiesa, Torino: ogni venerdì dalle 9:00 alle 18:00, primo giovedì del mese.",
     "adorazione.html", ADORAZIONE, "Adorazione eucaristica", "Ogni venerdì il Santissimo è esposto dalle 9:00 alle 18:00."),
    ("preghiera.html", "Preghiera — IVE a Torino",
     "Il Santo Rosario in audio (misteri gaudiosi, luminosi, dolorosi e gloriosi) e le preghiere della comunità IVE a Torino.",
     "preghiera.html", PREGHIERA, "Preghiera", "Il Rosario in audio, per l'Adorazione e per la famiglia."),
    ("orari.html", "Orari e Messe — IVE a Torino",
     "Orari di Sante Messe, Adorazione e confessioni della parrocchia Maria Madre della Chiesa, via Baltimora 85, Torino.",
     "orari.html", ORARI, "Orari e Messe", "Parrocchia Maria Madre della Chiesa, via Baltimora 85."),
    ("eventi.html", "Eventi — IVE a Torino",
     "Gli appuntamenti della comunità IVE a Torino: incontri, serate culturali, liturgie e iniziative aperte a tutti.",
     "eventi.html", EVENTI, "Eventi", "Le iniziative aperte a tutti, dentro e fuori la parrocchia."),
    ("formazione.html", "Formazione — IVE a Torino",
     "La Collana Virtus di p. Miguel Ángel Fuentes, il Catechismo di San Pio X, il Manuale del Terzo Ordine e la rivista «Cristo in Tutto»: i testi della comunità IVE a Torino.",
     "formazione.html", FORMAZIONE, "Formazione", "I libri, i manuali e i sussidi della comunità."),
    ("contatti.html", "Contatti — IVE a Torino",
     "Dove trovarci: via Baltimora 85, Torino. Email, canale WhatsApp e newsletter della comunità IVE a Torino.",
     "contatti.html", CONTATTI, "Contatti", "Via Baltimora 85, 10137 Torino."),
    ("privacy.html", "Privacy e cookie — IVE a Torino",
     "Informativa sul trattamento dei dati personali del sito iveatorino.it.",
     "privacy.html", PRIVACY, None, None),
]

SITE_URL = "https://www.iveatorino.it"


def write_sitemap(pages):
    """sitemap.xml valido secondo lo schema sitemaps.org 0.9."""
    from datetime import date
    today = date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, title, desc, active, body, ht, hs in pages:
        loc = SITE_URL + "/" if slug == "index.html" else SITE_URL + "/" + slug
        if slug == "index.html":
            freq, pri = "weekly", "1.0"
        elif slug in ("privacy.html",):
            freq, pri = "yearly", "0.3"
        elif slug in ("contatti.html", "formazione.html", "preghiera.html"):
            freq, pri = "monthly", "0.7"
        else:
            freq, pri = "monthly", "0.8"
        out.append("  <url>")
        out.append("    <loc>%s</loc>" % loc)
        out.append("    <lastmod>%s</lastmod>" % today)
        out.append("    <changefreq>%s</changefreq>" % freq)
        out.append("    <priority>%s</priority>" % pri)
        out.append("  </url>")
    out.append("</urlset>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


def write_robots():
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)


def main():
    os.makedirs(OUT, exist_ok=True)
    for slug, title, desc, active, body, ht, hs in PAGES:
        html_out = page(slug, title, desc, active, body, ht, hs)
        with open(os.path.join(OUT, slug), "w", encoding="utf-8") as fh:
            fh.write(html_out)
    write_sitemap(PAGES)
    write_robots()
    print("Generati:", ", ".join(p[0] for p in PAGES), "+ sitemap.xml, robots.txt")

if __name__ == "__main__":
    main()
