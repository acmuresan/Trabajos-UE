import os 

def guardar_inventario(inventario, nombre_archivo="inventario.txt"):
    """    
    Guarda el inventario en un archivo de texto.

    Recorre la lista de productos y escribe cada uno en una línea del archivo,
    usando el formato: nombre,precio,cantidad. Antes de los datos escribe
    una cabecera con los nombres de las columnas.

    Esta función se usa cada vez que queremos que los cambios del inventario
    (por ejemplo, al actualizar cantidades) se mantengan guardados para
    la próxima vez que se ejecute el programa.

    Parámetros:
        inventario (list[dict]):
            Lista de productos. Cada producto es un diccionario con las claves
            "nombre" (str), "precio" (float) y "cantidad" (int).
        nombre_archivo (str):
            Nombre del fichero donde se va a guardar el inventario. Por defecto
            se usa "inventario.txt".

    Retorno:
        None. Solo escribe en el archivo, no devuelve ningún valor.
        
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("nombre,precio,cantidad\n")
        
        for producto in inventario:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
        
def cargar_inventario(nombre_archivo="inventario.txt"):
    """
    Carga el inventario desde un archivo de texto o crea uno por defecto
    si el archivo todavía no existe.

    Si el fichero no existe (por ejemplo, la primera vez que se ejecuta
    el programa), se crea una lista de productos inicial, se guarda en disco
    y se devuelve. Si el fichero sí existe, se lee línea a línea para
    reconstruir la lista de diccionarios con los productos.

    Parámetros:
        nombre_archivo (str):
            Nombre del fichero desde el que se va a cargar el inventario.
            Por defecto se usa "inventario.txt".

    Retorno:
        list[dict]: Lista de productos. Cada producto es un diccionario con
        "nombre" (str), "precio" (float) y "cantidad" (int).
    
    """
    inventario = []
    
    
    if not os.path.exists(nombre_archivo):
        
        inventario = [
            {"nombre": "Portatil", "precio": 799.99, "cantidad": 10},
            {"nombre": "Telefono", "precio": 299.99, "cantidad": 5},
            {"nombre": "Tablet", "precio": 199.99, "cantidad": 0},
        ]
        
        guardar_inventario(inventario, nombre_archivo)
        return inventario
  
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        primera_linea = archivo.readline().strip()
        
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            
            partes = linea.split(",")
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])
            
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            inventario.append(producto)
            
    return inventario

def mostrar_inventario(inventario):
    """   
    Muestra por pantalla el inventario actual con un formato de tabla.

    Si el inventario está vacío, muestra un mensaje indicándolo y no intenta
    imprimir la tabla. Si hay productos, se muestra una cabecera con columnas
    para el número de producto, el nombre, el precio y la cantidad. Cada
    producto aparece numerado a partir de 1 para que sea más fácil de identificar
    por el usuario.

    Parámetros:
        inventario (list[dict]):
            Lista de productos que se quieren mostrar.
    
    """
    
    print("\n--INVENTARIO ACTUAL--")
    
    if not inventario:
        print("No hay productos en el inventario")
        return
    
    print(f"{'Nº':<4} {'Nombre':<20} {'Precio (€)':>12} {'Cantidad':>10}")
    print("-" * 50)
    
    for i, producto in enumerate(inventario, start=1):
         print(
            f"{i:<4} "
            f"{producto['nombre']:<20} "
            f"{producto['precio']:>12.2f} "
            f"{producto['cantidad']:>10}"
        )
         
    print("-" * 50)
    
def calcular_valor_total(inventario):
    """
    Calcula el valor total del inventario.

    Para cada producto, multiplica su precio por la cantidad disponible
    y va sumando todos esos valores en una variable acumuladora. Al final,
    devuelve la suma total como un número decimal (float).

    Esta función solo hace el cálculo; la responsabilidad de mostrar el
    resultado por pantalla es de la parte del programa que la llama.

    Parámetros:
        inventario (list[dict]):
            Lista de productos. Cada producto debe tener las claves
            "precio" (float) y "cantidad" (int).

    Retorno:
        float: Suma total de precio * cantidad de todos los productos.
        Si el inventario está vacío, devuelve 0.0.
    """
    total = 0.0
    
    for producto in inventario:
        total += producto["precio"] * producto["cantidad"]
        
    return total

def mostrar_productos_agotados(inventario):
    
    print("\n-- PRODUCTOS AGOTADOS --")
    
    agotados = [p for p in inventario if p["cantidad"] == 0]
    
    if not agotados:
        print("No hay productos agotados.")
        return
    
    for producto in agotados:
        print(f"- {producto['nombre']}")
        
def actualizar_cantidad_producto(inventario, nombre_archivo="inventario.txt"):
    """
    Permite modificar la cantidad de un producto del inventario elegido
    por el usuario.

    Primero se muestra el inventario completo para que el usuario pueda
    ver el número de cada producto. A continuación se le pide que introduzca
    el número del producto que quiere actualizar. La entrada se valida para
    asegurarnos de que sea un número entero y esté dentro del rango válido.

    Después se solicita la nueva cantidad. También se valida que sea un entero
    y que no sea un número negativo. Si todo es correcto, se actualiza la
    cantidad del producto dentro de la lista de inventario y se llama a
    'guardar_inventario' para que los cambios se guarden en el archivo.

    Parámetros:
        inventario (list[dict]):
            Lista de productos que se está gestionando en el programa.
        nombre_archivo (str):
            Nombre del archivo de texto donde se guardará el inventario
            actualizado. Por defecto es "inventario.txt".

    Retorno:
        None. La función modifica la lista en memoria y actualiza el archivo.
        
    """
    
    if not inventario:
        print("No hay productos para actualizar.")
        return
    
    mostrar_inventario(inventario)
    
    while True:
        try:
            opcion = int(input("Introduce el número del producto que quieres actualizar: "))
            if 1 <= opcion <= len(inventario):
                 break
            else:
                print(f"Por favor, introduce un número entre 1 y {len(inventario)}.")
        except ValueError:
            print("Entrada no válida. Debes introducir un número entero.")
            print("La cantidad no pude ser negativa")
            
    producto = inventario[opcion - 1] 
    print(f"Has seleccionado: {producto['nombre']} (Cantidad actual: {producto['cantidad']})")
    
    while True:
        try:
            nueva_cantidad = int(input("Introduce la nueva cantidad: "))
            if nueva_cantidad < 0:
                print("La cantidad no pude ser negativa")
            else:
                break
        except ValueError:
            print("Entrada no válida. Debes introducir un número entero.")
            print("La cantidad no pude ser negativa")  
            
    producto["cantidad"] = nueva_cantidad 
    guardar_inventario(inventario, nombre_archivo)
    
    print(f"Cantidad actualizada. Nueva cantidad de {producto['nombre']}: {producto['cantidad']}")
    
def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles para el usuario.

    Esta función solo se encarga de imprimir el texto del menú por pantalla.
    La lectura de la opción elegida y la lógica que se ejecuta después se
    gestionan en la función 'main'.
    
    """
    print("\n== GESTIÓN DE INVENTARIO DE TIENDA ELECTRÓNICA ==")
    print("1. Mostrar inventario")
    print("2. Calcular valor total del inventario")
    print("3. Mostrar productos agotados")
    print("4. Actualizar cantidad de un producto")
    print("5. Salir")
    
def main():
    """    
    Función principal del programa.

    - Carga el inventario desde el archivo.
    - Muestra un menú en un bucle.
    - Lee la opción del usuario.
    - Usa 'match' para decidir qué acción realizar según la opción introducida.
    
    """
    
    inventario = cargar_inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()
        
        match opcion:
            case "1":
                mostrar_inventario(inventario)
            
            case "2":
                valor_total = calcular_valor_total(inventario)
                print(f"\nValor total del inventario: {valor_total:.2f} €")
                
            case "3":
                mostrar_productos_agotados(inventario)
                
            case "4":
                actualizar_cantidad_producto(inventario)
                
            case "5":
                print("Saliendo del programa.")
                break
            
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
                
if __name__ == "__main__":
    main()
    