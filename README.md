# IVE a Torino — sito

Sito della comunità dell'Istituto del Verbo Incarnato a Torino.
Stato aggiornato al **9 novembre 2026**.

## Dov'è, adesso

| | |
|---|---|
| Repository | https://github.com/mtravascio/iveatorino (pubblico) |
| Sito | **https://www.iveatorino.it** — per ora serve in HTTP, il certificato HTTPS è in attesa |
| Anteprima GitHub | https://mtravascio.github.io/iveatorino/ (reindirizza al dominio) |
| Dominio | `iveatorino.it`, DNS su Squarespace |
| Pagine | 7: home, comunità, adorazione, orari, eventi, contatti, privacy |

## Come funziona

Le pagine HTML sono **generate** da `build.py`: lì stanno tutti i testi, i menu e la
struttura. La cartella `assets/` contiene foglio di stile e immagini e non viene mai
toccata dalla generazione.

```
build.py             testi e struttura (unica fonte di verità)
publish.sh           rigenera, committa e pubblica su GitHub
index.html           home
comunita.html        chi siamo
adorazione.html      adorazione e calendario
orari.html           messe, adorazione, confessioni, ufficio
eventi.html          appuntamenti
contatti.html        recapiti, mappa, newsletter
privacy.html         informativa
assets/css/style.css
assets/img/          crest.png (stemma), evento.jpg (locandina)
CNAME                www.iveatorino.it — lo usa GitHub Pages, non cancellarlo
.nojekyll            dice a GitHub di non processare i file con Jekyll
```

## Modificare i testi

1. Apri `build.py` e cerca il testo da cambiare: sono tutti in chiaro, in italiano.
2. `python3 build.py`
3. Guarda il risultato aprendo `index.html`, poi `./publish.sh "cosa hai cambiato"`.

**Attenzione:** puoi anche modificare direttamente gli `.html`, ma il successivo
`python3 build.py` li sovrascrive. O usi il generatore, o lavori solo sugli HTML, non
entrambi.

### Gli orari compaiono in quattro punti

Se cambi un orario vanno aggiornati tutti, altrimenti il sito si contraddice:

- `HOME`, blocco `<div class="facts">` — i tre riquadri in cima
- `HOME`, tabella `class="sched"` — la tabella riassuntiva
- `ORARI`, tabella `class="sched big"` — la pagina completa
- `ADORAZIONE` — riquadro laterale e tabella

La fonte è la tabella affissa in chiesa: il sito la trascrive.

### Aggiungere una pagina

In fondo a `build.py` c'è la lista `PAGES`: ogni voce è
`(file, titolo, descrizione, voce di menu, contenuto, titolo hero, sottotitolo)`.
Si aggiunge una costante con il contenuto, una voce in `PAGES` e una in `NAV`; poi
`python3 build.py`.

### Aggiungere una foto

1. Metti il file in `assets/img/` — orizzontale, almeno 2000 px di larghezza, JPG sotto i 300 KB.
2. Richiamala dove serve in `build.py`:
   `<img src="assets/img/nome.jpg" alt="descrizione vera della foto">`
3. L'`alt` non è un dettaglio: serve a chi non vede l'immagine e ai motori di ricerca.

## Pubblicare

```bash
cd "IVE a Torino/sito"
./publish.sh "Aggiornati gli orari di novembre"
```

GitHub Pages ricostruisce in 20–40 secondi. Controllo: *Settings → Pages* sul
repository, oppure aprire il sito in incognito.

## Dominio e DNS

DNS su **Squarespace** (nameserver `ns-cloud-a1..a4.googledomains.com`). Stato attuale:

| Record | Valore | Note |
|---|---|---|
| `CNAME www` | `mtravascio.github.io` | cambiato il 9/11/2026, TTL 1h |
| `A @` | 198.185.159.144/145, 198.49.23.144/145 | ancora Squarespace: fa 302 su `www` |
| `MX` | `mx1`/`mx2.forwardemail.net` | **non toccare**: è la posta |
| `TXT` | SPF forwardemail, verifica Google | **non toccare** |

Quindi `iveatorino.it` → 302 → `www.iveatorino.it` → GitHub. Funziona, con un salto in più.

### Passaggio definitivo (per togliere Squarespace di mezzo)

1. `A @`: togliere i quattro IP Squarespace e mettere `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   (IPv6 facoltativo: `2606:50c0:8000::153`, `…:8001::153`, `…:8002::153`, `…:8003::153`).
2. Su GitHub, *Settings → Pages → Custom domain*: mettere `iveatorino.it` (senza `www`).
3. Il file `CNAME` lo aggiorna GitHub da solo; poi aspettare il nuovo certificato.

### Tornare indietro

Basta rimettere i record com'erano:

- `CNAME www` → `ghs.googlehosted.com` (Google Sites riprende a rispondere)
- `A @` → `198.49.23.144`, `198.49.23.145`, `198.185.159.144`, `198.185.159.145`

Il vecchio sito Google Sites non è stato cancellato: resta nel pannello Sites.

## HTTPS

Il certificato lo emette GitHub, ma solo dopo che i suoi resolver vedono il nuovo
CNAME; il record precedente aveva TTL 4 ore, quindi l'attesa può durare qualche ora.
Quando il certificato è emesso va attivato *Enforce HTTPS* in *Settings → Pages*.
Fino a quel momento `https://www.iveatorino.it` mostra un avviso di sicurezza, mentre
`http://` funziona normalmente.

## Problemi tipici

| Sintomo | Causa | Rimedio |
|---|---|---|
| Vedo ancora il sito vecchio | cache DNS dell'operatore | provare in 4G o con DNS 1.1.1.1, oppure aspettare la scadenza del TTL |
| Avviso di sicurezza in HTTPS | certificato non ancora emesso | usare `http://`, aspettare |
| 404 su tutte le pagine | Pages su branch sbagliato o `CNAME` cancellato | *Settings → Pages*: branch `main`, cartella `/` |
| Il sito non si aggiorna dopo il push | build Pages fallita | controllare *Actions* / *Pages* e ricostruire |
| Il sito sparisce dopo un push | è stato cancellato `CNAME` | ricrearlo con dentro `www.iveatorino.it` |

## Cosa manca

Vedi `CONTENUTI.md`: orari da confermare, foto vere, testi della storia, privacy da
far validare.
