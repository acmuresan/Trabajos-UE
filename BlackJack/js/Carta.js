import { FIGURAS } from "./constants.js";

export class Carta {
  constructor(valor, palo) {
    this.valor = valor;
    this.palo = palo;

    this.puntos = this.calcularPuntos(valor);
  }

  calcularPuntos(valor) {
    if (valor === "A") {
      return 1;
    }

    if (FIGURAS.includes(valor)) {
      return 11;
    }

    return parseInt(valor);
  }
}
