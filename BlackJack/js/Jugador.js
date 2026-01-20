export class Jugador {
  constructor(nombre, selectorZona, idPuntos, idCartas) {
    this.nombre = nombre;
    this.puntos = 0;

    this.zonaVisual = document.querySelector(selectorZona);
    this.spanPuntos = document.getElementById(idPuntos);
    this.divCartas = document.getElementById(idCartas);
  }

  recibirCarta(carta) {
    this.puntos += carta.puntos;
    this.spanPuntos.innerText = this.puntos;
    this.pintarCarta(carta);
  }

  pintarCarta(carta) {
    const img = document.createElement("img");

    img.src = `img/${carta.valor}${carta.palo}.png`;

    img.classList.add("cartas-blackjack");

    img.alt = `${carta.valor} de ${carta.palo}`;
    this.divCartas.appendChild(img);
  }

  activarTurno(esSuTurno) {
    if (esSuTurno) {
      this.zonaVisual.classList.add("activo");
    } else {
      this.zonaVisual.classList.remove("activo");
    }
  }

  reiniciar() {
    this.puntos = 0;
    this.spanPuntos.innerText = 0;
    this.divCartas.innerHTML = "";

    this.activarTurno(false);
  }
}
