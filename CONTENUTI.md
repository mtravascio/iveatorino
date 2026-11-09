# Cosa scrivere, pagina per pagina

Note editoriali per completare il sito. Non serve sapere nulla di informatica: ogni
punto dice **cosa manca**, **dove si mette** e **chi lo può decidere**.

---

## 1. La comunità (pagina `comunita.html`)

Oggi il testo è volutamente generico: dice cosa è l'IVE e come vive la parrocchia, ma
non racconta la storia torinese. Mancano:

- da quando l'Istituto è a Torino e chi lo ha portato;
- i nomi dei padri e dei seminaristi che ci sono stati e che ci sono (con il loro consenso);
- due o tre fatti concreti: la scuola parentale, i campi estivi, le ordinazioni
  sacerdotali, i lavori in chiesa;
- una foto di gruppo, se esiste.

Chi lo decide: il superiore della comunità. Il testo si scrive nella costante
`COMUNITA` dentro `build.py`.

## 2. Orari (pagine `orari.html`, `adorazione.html`, home)

**Da sciogliere subito:** l'adorazione del venerdì risulta alle **8:00** sul poster
della chiesa e alle **9:00** sul calendario online. Va scelta una versione sola.

Poi vanno verificati, riga per riga, questi valori presi dalla tabella affissa:

| | Messa | Adorazione | Confessioni | Ufficio |
|---|---|---|---|---|
| Lunedì | — | — | — | — |
| Martedì | 18:30 | — | su appuntamento | Segreteria 17:00–18:00 |
| Mercoledì | 8:00 · 18:30 | 17:30 | 17:45–18:20 | Segreteria 17:00–18:00 · Don 19:15–20:00 |
| Giovedì | 8:00 · 18:30 | 17:30 | 17:45–18:20 | Don 11:00–12:30 · Segreteria 17:00–18:00 |
| Venerdì | 18:30 | 9:00–18:00 | 17:45–18:20 | Segreteria 17:00–18:00 |
| Sabato e vigilie | 18:30 | 17:30 | — | — |
| Domenica e feste | 10:30 · 18:30 | 17:30 | 17:45–18:20 | — |

Quando gli orari cambiano (estate, feste, lavori) vanno aggiornati in **quattro punti**
elencati nel `README.md`, altrimenti le pagine si contraddicono.

## 3. Foto

Il sito oggi non ha nessuna fotografia della chiesa: la copertina è un fondo grafico
con lo stemma. Servono:

- **una copertina** orizzontale della chiesa (navata o altare), almeno 2000 px di
  larghezza, senza persone riconoscibili;
- **tre o quattro scatti** della vita della comunità: adorazione, un incontro, i
  ragazzi del catechismo, la sagrestia, i lavori;
- **i volti solo con liberatoria** firmata; per i minori serve il consenso di entrambi
  i genitori. Senza liberatoria si fotografano le mani, le spalle, i dettagli.

Formato: JPG, lato lungo almeno 2000 px, sotto i 300 KB per foto.

## 4. Eventi (pagina `eventi.html`)

La locandina di «L'universo: caso o progetto?» è al suo posto. Dopo l'11 dicembre va
spostata nell'archivio e sostituita con il cartellone successivo. Per ogni evento
servono: titolo, date, orario, luogo, una riga di descrizione, se serve iscrizione.

## 5. Newsletter e contatti

Il pulsante iscrive al gruppo Google «IVE a Torino – Newsletter della Comunità»
(`groups.google.com/g/iveatorino`). Nell'elenco «Ultimi numeri» ci sono i due invii
dell'8 novembre 2026: quando ne esce uno nuovo, si aggiorna quella lista (titolo e
data, due righe in `build.py`, costante `CONTATTI`).

Chi gestisce il gruppo può verificare che l'iscrizione via email
(`iveatorino+subscribe@googlegroups.com`) sia aperta anche a chi non ha un account
Google.

## 6. Privacy (pagina `privacy.html`)

È una bozza corretta ma da far validare: servono il titolare esatto del trattamento,
i tempi di conservazione dei dati della petizione e l'indicazione di un responsabile,
se c'è. Meglio farla leggere a chi segue le questioni legali della parrocchia o della
diocesi.

## 7. Cose che potrebbero esserci, e oggi non ci sono

- **La rivista**: la newsletter di novembre annuncia «Cristo in Tutto». Una pagina con
  i numeri in PDF (uno per uscita, con copertina e indice) darebbe senso alla voce
  «rivista» che oggi sul vecchio sito è vuota.
- **Il bollettino settimanale**, se esiste in PDF.
- **Come diventare volontari**: chi apre la chiesa, chi tiene l'adorazione, chi
  accoglie i ragazzi.
- **Le app della comunità** (`app.regeomaria.net`) sono già linkate nel piè di pagina:
  si potrebbe dedicare loro uno spazio, se servono a chi arriva sul sito.

---

## Promemoria per chi scrive

- Frasi corte, voce attiva, niente gergo ecclesiastico quando si può evitare.
- I numeri in cifre, gli orari sempre con i minuti (`18:30`, non `18.30`).
- Mai informazioni solo dentro un'immagine: la tabella degli orari in foto, per
  esempio, non si legge da telefono e Google non la capisce.
- Ogni immagine ha bisogno di una descrizione vera, non di «foto».
