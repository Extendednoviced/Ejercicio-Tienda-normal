import os,time
os.system("cls")
bandera = True
pedido = False

while bandera:
    os.system("cls")
    print("1. Agregar pedido")
    print("2. Ver resumen")
    print("3. Descargar boleta")
    print("4. Salir")
    try:
        #1
        opcion = int(input("Ingrese opcion: \n"))
        if opcion == 1:
            nombre = ""
            rut = ""
            opc_producto = 0
            cantidad = 0
            print("Agregar pedido")
            os.system("cls")
            while len(nombre) <= 3 or len(nombre) >= 20:
                nombre = input("Ingrese su nombre: \n")
            while len(rut) < 8:
                rut = (input("Ingrese su rut: \n"))
            
            print("1. Hamburguesa $5000")
            print("2. Pizza $8000")
            print("3. Ensalada $4000")
            while opc_producto <= 0 or opc_producto > 3:
                opc_producto = int(input("Ingrese una opcion del menu: \n"))
            while cantidad <= 0:
                cantidad = int(input("Ingrese la cantidad de productos que va a llevar: \n"))
            if opc_producto == 1:
                producto = "Hamburguesa"
                monto_producto = 5000
            elif opc_producto == 2:
                producto = "Pizza"
                monto_producto = 8000
            else:
                producto = "Ensalada"
                monto_producto = 4000
                
            total = monto_producto * cantidad
            pedido = True
            
        #2
        elif opcion == 2:
            print("Ver resumen")
            os.system("cls")
            if pedido:
                print("\tResumen")
                print(f"Cliente: {nombre}")
                print(f"Rut: {rut}")
                print(f"Producto: {producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: ${total}")
            
            else:
                print("No existen pedidos para visualizar")
            time.sleep(4)
            
        #3
        elif opcion == 3:
            print("Descargar boleta")
            os.system("cls")
            if pedido:
                with open("bolsa.txt", "w") as archivo:
                    archivo.write("\tBoleta\n")
                    archivo.write(f"Cliente: {nombre}\n")
                    archivo.write(f"Rut: {rut}\n")
                    archivo.write(f"Producto: {producto}\n")
                    archivo.write(f"Cantidad: {cantidad}\n")
                    archivo.write(f"Total a pagar: ${total}\n")
                    
                print("Gracias por su compra")
            else:
                print("No existen datos para visualizar")
        #4
        elif opcion == 4:
            print("Salir")
            os.system("cls")
            bandera = False
        else:
                print("Datos ingresados no existen, intente nuevamente")
    except:
        ("Error, el valor ingresado debe ser un numero entero")