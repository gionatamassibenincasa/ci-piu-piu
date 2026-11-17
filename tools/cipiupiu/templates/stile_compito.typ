// Stile tipografico del compito. Modificare qui, non nel capitolo.
#set page(paper: "a4", margin: (x: 2.2cm, y: 2cm))
#set text(font: "Liberation Serif", size: 10.5pt)

#let compito-intestazione(numero: none, titolo: "", template: "worksheet") = {
  set text(size: 15pt, weight: "bold")
  [Compito — Capitolo #numero: #titolo]
  set text(size: 9pt, weight: "regular", fill: gray)
  [Template: #template · Nome: .................... Classe: ...... Data: ..........]
  line(length: 100%, stroke: 0.8pt)
}

#let testo(contenuto) = [#contenuto]
#let codice(contenuto) = raw(contenuto, block: true, lang: "cpp")
#let scelta(contenuto) = box(square(size: 9pt) + h(6pt) + contenuto)

#let spazio-risposta(fase: "predict") = {
  let altezza = if fase == "make" { 9cm } else if fase == "modify" { 6cm } else if fase == "investigate" { 5cm } else { 3cm }
  block(width: 100%, height: altezza, stroke: 0.6pt, fill: rgb("#fafafa"))
}
