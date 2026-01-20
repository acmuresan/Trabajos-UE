<?php
$alto = rand(5, 15);
$ancho = rand(5, 15);

echo "<h3>Alto: $alto <br> Ancho: $ancho</h3>";

echo "<pre>";

for ($i = 0; $i < $alto; $i++) {
    for ($j = 0; $j < $ancho; $j++) {
        echo "* ";
    }
    echo "<br>";
}

echo "</pre>";
?>