<?php
if (isset($_POST['num1']) && isset($_POST['num2']) && isset($_POST['operacion'])) {
     
    $n1 = $_POST['num1'];
    $n2 = $_POST['num2'];
    $op = $_POST['operacion'];

} else {
    echo "<h2>Error: Acceso no permitido.</h2>";
    echo "<p>Por favor, usa el formulario para enviar datos.</p>";
    echo "<a href='operaciones.php'>Volver al formulario</a>";
    exit(); 
}


if (!is_numeric($n1) || !is_numeric($n2)) {
    echo "<h2>Error de Datos</h2>";
    echo "<p>Por favor, introduce solo valores numéricos válidos.</p>";
    echo "<a href='operaciones.php'>Volver a intentar</a>";
    exit();
}

$resultado = 0; 

switch ($op) {
    case "Suma":
        $resultado = $n1 + $n2;
        break; 
    
    case "Resta":
        $resultado = $n1 - $n2;
        break;

    case "Producto":
        $resultado = $n1 * $n2;
        break;

    case "Cociente":
       
        if ($n2 == 0) {
            echo "<h2>Error Matemático</h2>";
            echo "<p>No se puede dividir por cero.</p>";
            echo "<a href='operaciones.php'>Volver a intentar</a>";
            exit();
        }
        $resultado = $n1 / $n2;
        break;

    default:
        echo "Error: Operación no reconocida.";
        exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultado</title>
    <style>
        body { font-family: sans-serif; padding: 20px; text-align: center; }
        .resultado-box { 
            border: 2px solid #4CAF50; 
            padding: 20px; 
            display: inline-block; 
            border-radius: 10px;
            background-color: #e8f5e9;
        }
        .btn-volver {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="resultado-box">
        <h2>Resultado de la Operación</h2>
        <p>
            El resultado de realizar <strong><?php echo $op; ?></strong> 
            de los números <strong><?php echo $n1; ?></strong> 
            y <strong><?php echo $n2; ?></strong> es:
        </p>
        
        <h1 style="color: #2E7D32;"><?php echo $resultado; ?></h1>
    </div>

    <br>

    <a href="operaciones.php" class="btn-volver">Calcular otra vez</a>

</body>
</html>