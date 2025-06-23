from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")  # ✅ Indica que los archivos HTML están en 'templates'
CORS(app)  # ✅ Permitir conexiones desde otros dispositivos

EXCEL_PATH = r"C:\Users\HP\OneDrive - Instituto Nacional de Aprendizaje\Desktop\Versión 3.04\SIT Certificados.xlsx"
SHEET_NAME = "Registros"

# ✅ Ruta principal para cargar el formulario
@app.route('/')
def home():
    return render_template("index.html")  # 📄 Carga correctamente la página

# ✅ Ruta para guardar registros en Excel
@app.route('/guardar_registro', methods=['POST'])
def guardar_registro():
    data = request.json
    try:
        if not os.path.exists(EXCEL_PATH):
            df = pd.DataFrame(columns=["Fecha", "Orden", "Placa", "Código", "Descripción", "Cantidad", "Lote", "Vencimiento"])
        else:
            df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

        nuevo_registro = pd.DataFrame([[data["fecha"], data.get("orden", ""), data.get("placa", ""),
                                        data["codigo"], data["descripcion"], data["cantidad"], data["lote"], data["vencimiento"]]],
                                      columns=df.columns)

        df = pd.concat([df, nuevo_registro], ignore_index=True)

        with pd.ExcelWriter(EXCEL_PATH, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

        print("✅ Registro guardado correctamente en Excel:", nuevo_registro)
        return jsonify({"mensaje": "Registro guardado correctamente"})

    except Exception as e:
        print("⚠️ Error al guardar en Excel:", str(e))
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ✅ Flask ahora acepta conexiones externas