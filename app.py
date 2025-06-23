from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

placas = [
    "200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","216","218",
    "300","301","302","303","304","305","306","307","308","309","310","311","312","313","314","315","316","317","318",
    "400","401","402","403","404","405","406","407","408","409","410","411","412","413",
    "500","505","506","507","508","509","510","511","512","513",
    "F01","F02","F03","F04","F05","F06","F07","F08","F09","F10",
    "POZUELO","SIGMA","COMAPAN","MAFAM","MEGASUPER","AUTOMERCADO",
    "DEMASA","INOLASA","EXPORTACION UNIMAR","HILLTOP","SAM","CARTAINESA","AUTODELI","WALMART","PRICSMART"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        placa = request.form.get('placa')
        hora_inicio = request.form.get('horaInicio')
        hora_fin = request.form.get('horaFin')
        # Aquí podrías procesar los datos como guardarlos en base de datos
        return f'Datos recibidos: {fecha}, {placa}, {hora_inicio}, {hora_fin}'

    return render_template('formulario.html', placas=placas, fecha_hoy=date.today().isoformat())

if __name__ == '__main__':
    app.run(debug=True)