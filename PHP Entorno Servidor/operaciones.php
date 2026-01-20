<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora PHP</title>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        form { background-color: #f9f9f9; padding: 20px; border: 1px solid #ccc; max-width: 400px; }
        label { display: block; margin-top: 10px; font-weight: bold; }
        input[type="text"] { width: 100%; padding: 5px; box-sizing: border-box; }
        input[type="submit"] { margin-top: 20px; padding: 10px 20px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
        input[type="submit"]:hover { background-color: #0056b3; }
    </style>
</head>
<body>

    <h2>Ejercicio 3: Calculadora</h2>

    <form action="datos_operaciones.php" method="POST">

        <label>Introduzca el primer número:</label>
        <input type="text" name="num1" required placeholder="Ej: 10">

        <label>Introduzca el segundo número:</label>
        <input type="text" name="num2" required placeholder="Ej: 5">

        <label>Seleccione la operación:</label>
        <div style="margin-top: 10px;">
            <input type="radio" name="operacion" value="Suma"> Suma <br>
            <input type="radio" name="operacion" value="Resta"> Resta <br>
            <input type="radio" name="operacion" value="Producto"> Producto <br>
            <input type="radio" name="operacion" value="Cociente" checked> Cociente
        </div>

        <input type="submit" value="Enviar datos">

    </form>

</body>
</html>