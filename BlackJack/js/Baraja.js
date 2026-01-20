import { PALOS, FIGURAS } from "./constants.js";
import { Carta } from "./Carta.js";

export class Baraja {
  constructor() {
    this.cartas = [];
    this.generar();
  }

  generar() {
    this.cartas = [];

    // 1. Números (2-10)
    for (let i = 2; i <= 10; i++) {
      for (let palo of PALOS) {
        this.cartas.push(new Carta(i, palo));
      }
    }

    for (let figura of FIGURAS) {
      for (let palo of PALOS) {
        this.cartas.push(new Carta(figura, palo));
      }
    }

    for (let palo of PALOS) {
      this.cartas.push(new Carta("A", palo));
    }
  }

  mezclar() {
    this.cartas.sort(() => Math.random() - 0.5);
  }

  sacar() {
    return this.cartas.pop();
  }
}
