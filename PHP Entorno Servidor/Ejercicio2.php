<?php

$jugador1 = [];
$jugador2 = [];

$suma1 = 0;
$suma2 = 0;

for ($i = 0; $i < 5; $i++) {

    $dado = rand(1, 6);
    $jugador1[] = $dado;

    $suma1 += $dado;
}

for ($i = 0; $i < 5; $i++) {

    $dado = rand(1, 6);
    $jugador2[] = $dado;

    $suma2 += $dado;
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego Dadados</title>
</head>

<body>
    <h2>Jugador 1</h2>
    <div>
        <?php
        foreach ($jugador1 as $valor) {
            echo "<img src='img/$valor.jpg' width='100' style='margin:5px;'>";
        }
        ?>
    </div>
    <p>Total Puntos: <strong><?php echo $suma1; ?></strong></p>

    <h2>Jugador 2</h2>
    <div>
        <?php
        foreach ($jugador2 as $valor) {
            echo "<img src='img/$valor.jpg' width='100' style='margin:5px;'>";
        }
        ?>
    </div>
    <p>Total Puntos: <strong><?php echo $suma2; ?></strong></p>

    <h2>Resultado</h2>
    <h3>
        <?php
        if ($suma1 > $suma2) {
            echo "Ha ganado el Jugador 1 !!";
        } elseif ($suma2 > $suma1) {
            echo "Ha ganod el Jugador 2 !!";
        } else {
            echo "Ha sido un empate";
        }
        ?>
    </h3>

    <div style="text-align: left; margin-top: 50px;">

        <form action="ejercicio2.php" method="POST">
            <input type="submit" value="¡Tirar dados otra vez!"
                style="padding: 15px 30px; font-size: 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; border-radius: 5px;">
        </form>
</body>

</html>