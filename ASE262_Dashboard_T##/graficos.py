
import plotly.graph_objects as go

from analisis import (
    agrupar_por_producto,
    ventas_por_vendedor,
    ventas_por_categoria
)

from conexion_sheets import obtener_datos


# COLORES PARA LOS GRÁFICOS
colores = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6"]


# 1. GRÁFICO DE BARRAS: UNIDADES POR PRODUCTO
def grafico_barras(datos):

    resumen = agrupar_por_producto(datos)

    productos = list(resumen.keys())
    cantidades = list(resumen.values())

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=productos,
        y=cantidades,
        marker_color=[
            colores[i % len(colores)]
            for i in range(len(productos))
        ],
        text=cantidades,
        textposition="auto",
        hovertemplate=(
            "Producto: %{x}<br>"
            "Unidades: %{y}<extra></extra>"
        )
    ))

    fig.update_layout(
        title="1. Unidades vendidas por producto",
        xaxis_title="Producto",
        yaxis_title="Unidades vendidas",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=50, r=30, t=70, b=50),
        showlegend=False
    )

    return fig


# 2. GRÁFICO DE DONA: DISTRIBUCIÓN POR PRODUCTO
def grafico_dona(datos):

    resumen = agrupar_por_producto(datos)

    productos = list(resumen.keys())
    cantidades = list(resumen.values())

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=productos,
        values=cantidades,
        hole=0.60,
        marker=dict(colors=colores),
        textinfo="label+percent",
        hovertemplate=(
            "Producto: %{label}<br>"
            "Unidades: %{value}<br>"
            "Porcentaje: %{percent}<extra></extra>"
        )
    ))

    fig.update_layout(
        title="2. Distribución porcentual por producto",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=30, r=30, t=70, b=30),
        showlegend=False
    )

    return fig


# 3. GRÁFICO DE BARRAS: VENTAS POR VENDEDOR
def grafico_vendedores(datos):

    resumen = ventas_por_vendedor(datos)

    vendedores = list(resumen.keys())
    ventas = list(resumen.values())

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=vendedores,
        y=ventas,
        marker_color="#10B981",
        text=[f"S/ {v:,.2f}" for v in ventas],
        textposition="auto",
        hovertemplate=(
            "Vendedor: %{x}<br>"
            "Ventas: S/ %{y:,.2f}<extra></extra>"
        )
    ))

    fig.update_layout(
        title="3. Ventas totales por vendedor",
        xaxis_title="Vendedor",
        yaxis_title="Ventas totales (S/)",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=60, r=30, t=70, b=50),
        showlegend=False
    )

    return fig


# 4. GRÁFICO DE DONA: VENTAS POR CATEGORÍA
def grafico_categorias(datos):

    resumen = ventas_por_categoria(datos)

    categorias = list(resumen.keys())
    ventas = list(resumen.values())

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=categorias,
        values=ventas,
        hole=0.60,
        marker=dict(colors=colores),
        textinfo="label+percent",
        hovertemplate=(
            "Categoría: %{label}<br>"
            "Ventas: S/ %{value:,.2f}<br>"
            "Porcentaje: %{percent}<extra></extra>"
        )
    ))

    fig.update_layout(
        title="4. Ventas totales por categoría",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=30, r=30, t=70, b=30),
        showlegend=False
    )

    return fig


# BLOQUE PARA PROBAR LOS GRÁFICOS SIN FLASK
if __name__ == "__main__":

    # Obtener registros de Google Sheets
    datos = obtener_datos()

    # Mostrar los gráficos por separado
    grafico_barras(datos).show()
    grafico_dona(datos).show()
    grafico_vendedores(datos).show()
    grafico_categorias(datos).show()
