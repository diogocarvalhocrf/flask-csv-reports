from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    dados = [
        request.form.get("escola"),
        request.form.get("data"),
        request.form.get("presenca")
    ]
    # Apenas exemplo simplificado: grava em CSV
    with open("relatorio.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(dados)
    return "Dados recebidos com sucesso!"
