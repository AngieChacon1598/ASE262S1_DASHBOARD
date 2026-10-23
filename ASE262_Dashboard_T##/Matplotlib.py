
import matplotlib.pyplot as plt

from analisis import (
    agrupar_por_producto,
    calcular_ventas,
    contar_registros,
    ventas_por_vendedor,
    ventas_por_categoria
)

from conexion_sheets import obtener_datos


# OBTENER DATOS DE GOOGLE SHEETS
datos = obtener_datos()

resumen = agrupar_por_producto(datos)
total_reg = contar_registros(datos)
total_ven = calcular_ventas(datos)

# NUEVOS INDICADORES
resumen_vendedores = ventas_por_vendedor(datos)
resumen_categorias = ventas_por_categoria(datos)

productos = list(resumen.keys())
cantidades = list(resumen.values())

colores = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6"]


# 1. PRIMER GRÁFICO: BARRAS POR PRODUCTO
plt.figure(figsize=(7, 4))

plt.bar(
    productos,
    cantidades,
    color=[colores[i % len(colores)] for i in range(len(productos))],
    edgecolor="black"
)

plt.title(
    "1. Unidades Vendidas por Producto",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Producto")
plt.ylabel("Unidades Vendidas")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


# 2. SEGUNDO GRÁFICO: DONA POR PRODUCTO
plt.figure(figsize=(6, 6))

plt.pie(
    cantidades,
    labels=productos,
    autopct="%1.1f%%",
    startangle=140,
    colors=[colores[i % len(colores)] for i in range(len(productos))]
)

circulo_centro = plt.Circle((0, 0), 0.60, fc="white")

fig = plt.gcf()
fig.gca().add_artist(circulo_centro)

plt.title(
    "2. Distribución Porcentual (%)",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.show()


# 3. TERCER GRÁFICO: TARJETA DE MÉTRICAS (KPIs)
plt.figure(figsize=(5, 4))
plt.axis("off")

texto_kpi = (
    "MÉTRICAS CLAVE\n\n"
    f"• Total Registros: {total_reg}\n\n"
    f"• Total Unidades: {sum(cantidades)}\n\n"
    f"• Ventas Totales: S/ {total_ven:,.2f}"
)

plt.text(
    0.1,
    0.5,
    texto_kpi,
    fontsize=13,
    verticalalignment="center",
    bbox=dict(
        boxstyle="round,pad=1.2",
        facecolor="#EBF3F9",
        edgecolor="#3B82F6"
    )
)

plt.title(
    "3. Resumen General",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.show()


# 4. CUARTO GRÁFICO: VENTAS POR VENDEDOR

vendedores = list(resumen_vendedores.keys())
ventas_vendedores = list(resumen_vendedores.values())

plt.figure(figsize=(8, 5))

plt.bar(
    vendedores,
    ventas_vendedores,
    color="#10B981",
    edgecolor="black"
)

plt.title(
    "4. Ventas Totales por Vendedor",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Vendedor")
plt.ylabel("Ventas Totales (S/)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


# 5. QUINTO GRÁFICO: VENTAS POR CATEGORÍA

categorias = list(resumen_categorias.keys())
ventas_categorias = list(resumen_categorias.values())

plt.figure(figsize=(6, 6))

plt.pie(
    ventas_categorias,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=140,
    colors=[colores[i % len(colores)] for i in range(len(categorias))]
)

circulo_centro = plt.Circle((0, 0), 0.60, fc="white")

fig = plt.gcf()
fig.gca().add_artist(circulo_centro)

plt.title(
    "5. Ventas Totales por Categoría",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.show()
