
# IMPORTAR FLASK
from flask import Flask, render_template

# IMPORTAR LA CONEXIÓN CON GOOGLE SHEETS
from conexion_sheets import obtener_datos

# IMPORTAR LAS FUNCIONES DE ANÁLISIS
from analisis import (
    contar_registros,
    agrupar_por_producto,
    calcular_ventas
)

# IMPORTAR LAS FUNCIONES DE GRÁFICOS
from graficos import (
    grafico_barras,
    grafico_dona,
    grafico_vendedores,
    grafico_categorias
)


# 1. CREAR LA APLICACIÓN FLASK
app = Flask(__name__)


# 2. DEFINIR LA RUTA PRINCIPAL
@app.route("/")
def dashboard():

    # 3. OBTENER LOS DATOS DESDE GOOGLE SHEETS
    datos = obtener_datos()

    # 4. CALCULAR LOS INDICADORES KPI
    total_registros = contar_registros(datos)

    resumen = agrupar_por_producto(datos)
    total_unidades = sum(resumen.values())

    ventas_totales = calcular_ventas(datos)

    # 5. GENERAR LOS GRÁFICOS INTERACTIVOS
    fig1 = grafico_barras(datos)
    fig2 = grafico_dona(datos)
    fig3 = grafico_vendedores(datos)
    fig4 = grafico_categorias(datos)

    # 6. CONVERTIR LOS GRÁFICOS A HTML
    grafico1 = fig1.to_html(
        full_html=False,
        include_plotlyjs=False
    )

    grafico2 = fig2.to_html(
        full_html=False,
        include_plotlyjs=False
    )

    grafico3 = fig3.to_html(
        full_html=False,
        include_plotlyjs=False
    )

    grafico4 = fig4.to_html(
        full_html=False,
        include_plotlyjs=False
    )

    # 7. ENVIAR LOS RESULTADOS A dashboard.html
    return render_template(
        "dashboard.html",
        total_registros=total_registros,
        total_unidades=total_unidades,
        ventas_totales=ventas_totales,
        grafico1=grafico1,
        grafico2=grafico2,
        grafico3=grafico3,
        grafico4=grafico4
    )


# 8. EJECUTAR LA APLICACIÓN
if __name__ == "__main__":
    app.run(debug=True)
