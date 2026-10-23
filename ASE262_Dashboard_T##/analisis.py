
from conexion_sheets import obtener_datos


# FUNCIÓN 1: CONTAR REGISTROS
def contar_registros(registros):
    return len(registros)


# FUNCIÓN 2: AGRUPAR POR PRODUCTO
def agrupar_por_producto(registros):
    resumen = {}

    for registro in registros:
        producto = registro["Producto"]
        cantidad = int(registro["Cantidad"])

        if producto not in resumen:
            resumen[producto] = 0

        resumen[producto] += cantidad

    return resumen


# FUNCIÓN 3: CALCULAR VENTAS
def calcular_ventas(registros):
    total = 0

    for registro in registros:
        cantidad = int(registro["Cantidad"])
        precio = float(registro["Precio"])

        subtotal = cantidad * precio
        total += subtotal

    return total


# FUNCIÓN 4: VENTAS POR VENDEDOR
def ventas_por_vendedor(registros):
    resumen = {}

    for registro in registros:
        vendedor = registro["Vendedor"]
        cantidad = int(registro["Cantidad"])
        precio = float(registro["Precio"])

        venta = cantidad * precio

        if vendedor not in resumen:
            resumen[vendedor] = 0

        resumen[vendedor] += venta

    return resumen


# FUNCIÓN 5: VENTAS POR CATEGORÍA
def ventas_por_categoria(registros):
    resumen = {}

    for registro in registros:
        categoria = registro["Categoria"]
        cantidad = int(registro["Cantidad"])
        precio = float(registro["Precio"])

        venta = cantidad * precio

        if categoria not in resumen:
            resumen[categoria] = 0

        resumen[categoria] += venta

    return resumen


# BLOQUE PARA PROBAR LAS FUNCIONES
if __name__ == "__main__":

    datos = obtener_datos()

    total_registros = contar_registros(datos)
    resumen = agrupar_por_producto(datos)
    ventas_totales = calcular_ventas(datos)
    vendedores = ventas_por_vendedor(datos)
    categorias = ventas_por_categoria(datos)

    print("Registros:", total_registros)
    print("Unidades:", resumen)
    print("Ventas S/:", ventas_totales)
    print("Ventas por vendedor:", vendedores)
    print("Ventas por categoría:", categorias)
