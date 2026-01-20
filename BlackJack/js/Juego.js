import { Baraja } from "./Baraja.js";
import { Jugador } from "./Jugador.js";

export class Juego {
  constructor() {
    this.baraja = new Baraja();

    this.banca = new Jugador(
      "Banca",
      ".zona.banca",
      "puntos-banca",
      "cartas-banca"
    );

    this.usuario = new Jugador(
      "Jugador",
      ".zona.jugador",
      "puntos-jugador",
      "cartas-jugador"
    );

    this.divControles = document.getElementById("controles");
    this.btnPedir = document.getElementById("btn-pedir");
    this.btnPlantarse = document.getElementById("btn-plantarse");
    this.asignarEventos();
  }

  asignarEventos() {
    this.btnPedir.addEventListener("click", () => this.turnoUsuarioPedir());
    this.btnPlantarse.addEventListener("click", () =>
      this.turnoUsuarioPlantarse()
    );
  }

  async iniciar() {
    this.baraja.mezclar();
    this.banca.reiniciar();
    this.usuario.reiniciar();

    const { value: nombre } = await Swal.fire({
      title: "♠️♣️ Blackjack ♦️♥️",
      input: "text",
      inputLabel: "Introduce tu nombre",
      allowOutsideClick: false,
      confirmButtonText: "¡A Jugar!",
      inputValidator: (value) => {
        if (!value) return "¡Necesitas un nombre!";
      },
    });

    this.usuario.nombre = nombre;
    document.getElementById("nombre-jugador").innerText = nombre;

    this.jugarBanca();
  }

  jugarBanca() {
    this.banca.activarTurno(true);
    this.usuario.activarTurno(false);

    this.divControles.style.display = "none";

    Swal.fire({
      icon: "info",
      title: "Turno de la Banca",
      text: "La banca está jugando...",
      timer: 1500,
      showConfirmButton: false,
    });

    this.bancaRobarRecursivo();
  }

  bancaRobarRecursivo() {
    if (this.banca.puntos >= 17) {
      this.finTurnoBanca();
      return;
    }

    const carta = this.baraja.sacar();

    this.banca.recibirCarta(carta);

    setTimeout(() => {
      this.bancaRobarRecursivo();
    }, 1000);
  }

  finTurnoBanca() {
    if (this.banca.puntos > 21) {
      this.finalizarPartida(
        "¡ La banca se ha pasado ! GANASTE !!🎉",
        "success"
      );
    } else {
      this.jugarUsuario();
    }
  }

  jugarUsuario() {
    this.banca.activarTurno(false);
    this.usuario.activarTurno(true);

    this.divControles.style.display = "block";

    Swal.fire({
      toast: true,
      position: "top-end",
      icon: "success",
      title: `Tu turno, ${this.usuario.nombre}`,
      showConfirmButton: false,
      timer: 2000,
    });
  }

  turnoUsuarioPedir() {
    const carta = this.baraja.sacar();

    this.usuario.recibirCarta(carta);

    if (this.usuario.puntos > 21) {
      this.finalizarPartida("Te has pasado de 21. PERDISTE ☠️", "error");
    }
  }

  turnoUsuarioPlantarse() {
    this.calcularGanador();
  }

  calcularGanador() {
    const ptsU = this.usuario.puntos;
    const ptsB = this.banca.puntos;

    let mensaje, icono;

    if (ptsU > ptsB) {
      mensaje = `¡GANASTE! ${ptsU} a ${ptsB}`;
      icono = "success";
    } else if (ptsU === ptsB) {
      mensaje = `EMPATE a ${ptsU} puntos`;
      icono = "warning";
    } else {
      mensaje = `PERDISTE. La banca gana ${ptsB} a ${ptsU}`;
      icono = "error";
    }

    this.finalizarPartida(mensaje, icono);
  }

  finalizarPartida(mensaje, icono) {
    this.divControles.style.display = "none";

    this.usuario.activarTurno(false);

    Swal.fire({
      title: mensaje,
      icon: icono,
      confirmButtonText: "Jugar otra vez",
      allowOutsideClick: false,
    }).then((result) => {
      if (result.isConfirmed) {
        location.reload();
      }
    });
  }
}
