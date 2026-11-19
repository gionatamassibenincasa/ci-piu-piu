// Stile tipografico del compito. Modificare qui, non nel capitolo.
#set page(paper: "a4", margin: (x: 2cm, y: 1.8cm))
#set text(font: ("Liberation Serif", "DejaVu Serif", "Libertinus Serif"), size: 10.5pt)
#set par(justify: false, leading: 0.65em)

#let compito-intestazione(numero: none, titolo: "", template: "worksheet") = {
  set text(size: 12pt, weight: "bold")
  [#titolo]
  v(0.4em)
  set text(size: 9.5pt, weight: "regular")
  [Nome: ................................  Classe: ........  Data: ................]
  v(0.3em)
  line(length: 100%, stroke: 0.8pt)
  v(0.45em)
}

#let testo(contenuto) = {
  set text(size: 10.5pt)
  block(width: 100%, [#contenuto])
}

#let meta-riga(contenuto) = {
  set text(size: 9.5pt, fill: luma(60))
  [#contenuto]
  v(0.45em)
}

#let item-id(contenuto) = {
  set text(size: 8pt, fill: luma(120))
  [#contenuto]
}

#let istruzione-modify(contenuto) = {
  set text(size: 9.5pt, style: "italic")
  [#contenuto]
  v(0.25em)
}

#let codice(contenuto) = {
  block(
    width: 100%,
    inset: 8pt,
    fill: rgb("#f5f5f5"),
    stroke: 0.4pt + luma(180),
    raw(contenuto, block: true, lang: "cpp"),
  )
}

// Quadrato e testo sempre sulla stessa riga (testo lungo va a capo nella colonna destra)
#let scelta(contenuto) = {
  v(0.12em)
  grid(
    columns: (11pt, 1fr),
    column-gutter: 8pt,
    rows: (auto,),
    align: (horizon, top),
    square(size: 9pt, stroke: 0.75pt + luma(30)),
    contenuto,
  )
}

#let spazio-risposta(fase: "predict") = {
  let altezza = if fase == "make" {
    7cm
  } else if fase == "modify" {
    3.5cm
  } else if fase == "investigate" {
    3.5cm
  } else if fase == "predict-mc" {
    0cm
  } else {
    2cm
  }
  if altezza > 0cm {
    v(0.25em)
    block(width: 100%, height: altezza, stroke: 0.6pt + luma(160), fill: rgb("#fafafa"))
    v(0.35em)
  }
}
