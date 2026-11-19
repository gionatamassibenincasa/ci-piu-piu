// Stile tipografico del compito. Modificare qui, non nel capitolo.
#set page(paper: "a4", margin: (x: 2cm, y: 1.8cm))
#set text(font: ("Liberation Serif", "DejaVu Serif", "Libertinus Serif"), size: 10.5pt)
#set par(justify: false, leading: 0.65em)

#let compito-intestazione(numero: none, titolo: "", template: "worksheet") = {
  set text(size: 13pt, weight: "bold")
  [Compito — Cap. #numero]
  set text(size: 11pt, weight: "bold")
  [#titolo]
  v(0.35em)
  set text(size: 9pt, weight: "regular", fill: luma(80))
  [Template: #template · Nome: ........................ Classe: ...... Data: ............]
  v(0.25em)
  line(length: 100%, stroke: 0.8pt)
  v(0.4em)
}

#let testo(contenuto) = {
  set text(size: 10.5pt)
  [#contenuto]
}

#let meta-riga(contenuto) = {
  set text(size: 9.5pt, fill: luma(60))
  [#contenuto]
  v(0.5em)
}

#let item-id(contenuto) = {
  set text(size: 8pt, fill: luma(120))
  [#contenuto]
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

#let scelta(contenuto) = {
  v(0.15em)
  box(square(size: 9pt) + h(6pt) + contenuto)
}

#let spazio-risposta(fase: "predict") = {
  let altezza = if fase == "make" {
    8cm
  } else if fase == "modify" {
    5.5cm
  } else if fase == "investigate" {
    4.5cm
  } else if fase == "predict-mc" {
    1.2cm
  } else {
    2.5cm
  }
  v(0.3em)
  block(width: 100%, height: altezza, stroke: 0.6pt + luma(160), fill: rgb("#fafafa"))
  v(0.4em)
}
