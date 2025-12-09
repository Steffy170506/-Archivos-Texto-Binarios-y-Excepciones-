def crear_catalogo():
    """Crea la matriz para el catálogo de personajes"""
    try:
        print("\n" + "="*50)
        print("       ALIEN STAGE - CATÁLOGO DE PERSONAJES")
        print("="*50)
        
        filas = int(input("Número de categorías (filas): "))
        columnas = int(input("Número de personajes por categoría: "))
        
        if filas <= 0 or columnas <= 0:
            print("Las filas y columnas deben ser mayores a 0. Se usarán valores por defecto (4x4).")
            filas, columnas = 4, 4
        
        catalogo = [["VACIO" for _ in range(columnas)] for _ in range(filas)]
        
        personajes_alien_stage = [
            "IVAN", "TILL", "SUA", "MIZU", "HYUNA", "LYNNE", 
            "MOMO", "ISOL", "RAIN", "NOVA", "LUCY", "KYLE",
            "ALICE", "FELIX", "LUNA", "ZERO", "KAI", "REN"
        ]
        
        import random
        num_personajes = min(len(personajes_alien_stage), filas * columnas // 2)
        
        posiciones_ocupadas = []
        for _ in range(num_personajes):
            while True:
                f = random.randint(0, filas-1)
                c = random.randint(0, columnas-1)
                if (f, c) not in posiciones_ocupadas and catalogo[f][c] == "VACIO":
                    personaje = random.choice(personajes_alien_stage)
                    catalogo[f][c] = personaje
                    posiciones_ocupadas.append((f, c))
                    break
        
        print(f"\nCatálogo creado con {filas} categorías y {columnas} personajes por categoría.")
        print(f"Se han agregado {num_personajes} personajes de Alien Stage al catálogo.")
        return catalogo
        
    except ValueError:
        print("Entrada inválida. Se creará un catálogo de 4x4.")
        return [["VACIO", "IVAN", "VACIO", "TILL"],
                ["SUA", "VACIO", "MIZU", "VACIO"],
                ["VACIO", "HYUNA", "VACIO", "LYNNE"],
                ["MOMO", "VACIO", "ISOL", "VACIO"]]

def mostrar_catalogo(catalogo):
    """Muestra el catálogo de personajes con formato"""
    if not catalogo:
        print("El catálogo no ha sido creado.")
        return
    
    filas = len(catalogo)
    columnas = len(catalogo[0])
    
    print(f"\n{' CATÁLOGO ALIEN STAGE ':*^60}")
    print(f"Categorías: {filas}, Personajes por categoría: {columnas}")
    print("*" * 60)
    
    # Encabezado de columnas
    print("        ", end="")
    for col in range(columnas):
        print(f" Personaje {col+1:2}  ", end="")
    print()
    
    categorias = ["VOCALISTAS", "GUITARRISTAS", "BAJISTAS", "BATERISTAS", 
                  "TECLADISTAS", "VIOLINISTAS", "COROS", "PRODUCTORES"]
    
    for i in range(filas):
        categoria = categorias[i] if i < len(categorias) else f"Categoría {i+1}"
        print(f"{categoria:12} ", end="")
        
        for j in range(columnas):
            personaje = catalogo[i][j]
            if personaje == "VACIO":
                print("[ VACÍO ] ", end="")
            else:
                print(f"[{personaje:^7}] ", end="")
        print()
    
    print("*" * 60)
    print("Leyenda: [Nombre] = Personaje registrado, [ VACÍO ] = Espacio disponible")

def agregar_personaje(catalogo):
    """Agrega un personaje al catálogo"""
    if not catalogo:
        print("El catálogo no ha sido creado.")
        return catalogo
    
    mostrar_catalogo(catalogo)
    
    try:
        fila = int(input("\nNúmero de categoría (fila): ")) - 1
        columna = int(input("Número de posición en la categoría: ")) - 1
        
        if fila < 0 or fila >= len(catalogo) or columna < 0 or columna >= len(catalogo[0]):
            print("Error: La posición seleccionada no existe.")
            return catalogo
        
        # Verificar si la posición está vacía
        if catalogo[fila][columna] == "VACIO":
            nombre = input("Nombre del personaje: ").strip().upper()
            if nombre and nombre != "VACIO":
                catalogo[fila][columna] = nombre
                print(f"¡Personaje '{nombre}' agregado exitosamente!")
                print(f"Posición: Categoría {fila+1}, Personaje {columna+1}")
            else:
                print("Error: Nombre no válido.")
        else:
            print(f"Error: Esta posición ya está ocupada por '{catalogo[fila][columna]}'.")
            
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    
    return catalogo

def eliminar_personaje(catalogo):
    """Elimina un personaje del catálogo"""
    if not catalogo:
        print("El catálogo no ha sido creado.")
        return catalogo
    
    mostrar_catalogo(catalogo)
    
    try:
        fila = int(input("\nNúmero de categoría (fila): ")) - 1
        columna = int(input("Número de posición en la categoría: ")) - 1
        
        if fila < 0 or fila >= len(catalogo) or columna < 0 or columna >= len(catalogo[0]):
            print("Error: La posición seleccionada no existe.")
            return catalogo
        
        if catalogo[fila][columna] != "VACIO":
            personaje = catalogo[fila][columna]
            catalogo[fila][columna] = "VACIO"
            print(f"¡Personaje '{personaje}' eliminado exitosamente!")
            print(f"Posición liberada: Categoría {fila+1}, Personaje {columna+1}")
        else:
            print("Error: Esta posición ya está vacía.")
            
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    
    return catalogo

def buscar_personaje(catalogo):
    """Busca un personaje en el catálogo"""
    if not catalogo:
        print("El catálogo no ha sido creado.")
        return
    
    nombre = input("Nombre del personaje a buscar: ").strip().upper()
    if not nombre:
        print("Error: Nombre no válido.")
        return
    
    encontrados = []
    
    for i in range(len(catalogo)):
        for j in range(len(catalogo[0])):
            if catalogo[i][j] == nombre:
                encontrados.append((i, j))
    
    if encontrados:
        print(f"\nPersonaje '{nombre}' encontrado en {len(encontrados)} posición(es):")
        
        categorias = ["VOCALISTAS", "GUITARRISTAS", "BAJISTAS", "BATERISTAS", 
                      "TECLADISTAS", "VIOLINISTAS", "COROS", "PRODUCTORES"]
        
        for f, c in encontrados:
            categoria = categorias[f] if f < len(categorias) else f"Categoría {f+1}"
            print(f"  - {categoria}, Personaje {c+1}")
    else:
        print(f"\nPersonaje '{nombre}' no encontrado en el catálogo.")

def estadisticas_catalogo(catalogo):
    """Muestra estadísticas del catálogo"""
    if not catalogo:
        print("El catálogo no ha sido creado.")
        return
    
    filas = len(catalogo)
    columnas = len(catalogo[0])
    total_posiciones = filas * columnas
    
    vacias = 0
    ocupadas = 0
    personajes_unicos = set()
    
    for fila in catalogo:
        for personaje in fila:
            if personaje == "VACIO":
                vacias += 1
            else:
                ocupadas += 1
                personajes_unicos.add(personaje)
    
    print("\n" + "="*50)
    print("       ESTADÍSTICAS DEL CATÁLOGO")
    print("="*50)
    print(f"Total de posiciones: {total_posiciones}")
    print(f"Posiciones ocupadas: {ocupadas}")
    print(f"Posiciones vacías: {vacias}")
    print(f"Personajes únicos registrados: {len(personajes_unicos)}")
    print(f"Porcentaje de ocupación: {(ocupadas/total_posiciones)*100:.1f}%")
    
    if personajes_unicos:
        print("\nPersonajes registrados:")
        personajes_lista = sorted(list(personajes_unicos))
        for i in range(0, len(personajes_lista), 4):
            print("  " + ", ".join(personajes_lista[i:i+4]))
    print("="*50)

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("       SISTEMA DE CATÁLOGO - ALIEN STAGE")
    print("="*50)
    print("1. Mostrar catálogo")
    print("2. Agregar personaje")
    print("3. Eliminar personaje")
    print("4. Buscar personaje")
    print("5. Ver estadísticas")
    print("6. Salir")
    print("="*50)

def main():
    """Función principal del programa"""
    print("\n" + "☆"*50)
    print("       BIENVENIDO AL CATÁLOGO DE ALIEN STAGE")
    print("       Sistema de Gestión de Personajes")
    print("☆"*50)
    print("\nPersonajes principales: IVAN, TILL, SUA, MIZU, HYUNA, LYNNE")
    print("Otros personajes: MOMO, ISOL, RAIN, NOVA, LUCY, KYLE")

    catalogo = crear_catalogo()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                mostrar_catalogo(catalogo)
            elif opcion == 2:
                catalogo = agregar_personaje(catalogo)
            elif opcion == 3:
                catalogo = eliminar_personaje(catalogo)
            elif opcion == 4:
                buscar_personaje(catalogo)
            elif opcion == 5:
                estadisticas_catalogo(catalogo)
            elif opcion == 6:
                print("\n" + "☆"*50)
                print("       ¡Gracias por usar el Catálogo Alien Stage!")
                print("       ¡Hasta la próxima etapa musical!")
                print("☆"*50)
                break
            else:
                print("Error: Opción no válida. Por favor seleccione 1-6.")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()