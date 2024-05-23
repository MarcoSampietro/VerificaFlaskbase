from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

dati_clienti = pd.read_csv('/workspace/VerificaFlaskbase/data/dati_clienti.csv')

@app.route('/')
def homepage():
    risultato = sorted(list(set(dati_clienti['Country'])))
    return render_template('index.html', lista=risultato)

@app.route('/elencocitta/<nazione>', methods=['GET'])
def citta(nazione):
    info = dati_clienti[dati_clienti['Country'] == nazione]
    city_counts = info['City'].value_counts().sort_values(ascending=False)
    return render_template('radiobutton.html', tabella=city_counts)

@app.route('/elencoclienti', methods=['GET'])
def clienti():
    citta = request.args.get('citta')
    info = dati_clienti[dati_clienti['City'] == citta]
    return render_template('clienti.html', tabella=info.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=32457, debug=True)