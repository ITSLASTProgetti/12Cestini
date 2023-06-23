import pandas as pd


def ordina_csv():
    csv_1 = pd.read_csv('data/cestini_bussolengo.csv', usecols=['id', 'lon', 'lat'])
    csv_2 = pd.read_csv('data/cestini_castelnuovo.csv', usecols=['id', 'lon', 'lat', 'recycling:plastic', 'recycling:glass'])
    csv_3 = pd.read_csv('data/cestini_lazise.csv', usecols=['id', 'lon', 'lat', 'recycling:plastic', 'recycling:glass', 'recycling:paper'])
    csv_4 = pd.read_csv('data/cestini_mozzecane.csv', usecols=['id', 'lon', 'lat', 'recycling:plastic', 'recycling:glass', 'recycling:paper'])
    csv_5 = pd.read_csv('data/cestini_pastrengo.csv', usecols=['id', 'lon', 'lat'])
    csv_6 = pd.read_csv('data/cestini_pescantina.csv', usecols=['id', 'lon', 'lat', 'recycling:glass'])
    csv_7 = pd.read_csv('data/cestini_sommacampagna.csv', usecols=['id', 'lon', 'lat', ])
    csv_8 = pd.read_csv('data/cestini_sona.csv', usecols=['id', 'lon', 'lat'])
    csv_9 = pd.read_csv('data/cestini_valeggio.csv', usecols=['id', 'lon', 'lat'])
    csv_10 = pd.read_csv('data/cestini_vigasio.csv', usecols=['id', 'lon', 'lat'])
    csv_11 = pd.read_csv('data/cestini_villafranca.csv', usecols=['id', 'lon', 'lat', 'recycling:plastic', 'recycling:glass', 'recycling:paper'])

    datiCestini = pd.concat([csv_1, csv_2, csv_3, csv_4, csv_5, csv_6, csv_7, csv_8, csv_9, csv_10, csv_11, ])
    datiCestini[['lon','lat']] = datiCestini[['lon','lat']].apply(pd.to_numeric)

    datiCestini.to_csv('data/datiCestino.csv', index = False)
    datiCestini = datiCestini[datiCestini['recycling:plastic'] == 'yes']
    datiCestini.to_csv('data/cestiniPlastic.csv')
    datiCestini = datiCestini[datiCestini['recycling:glass'] == 'yes']
    datiCestini.to_csv('data/cestiniGlass.csv')
    datiCestini = datiCestini[datiCestini['recycling:paper'] == 'yes']
    datiCestini.to_csv('data/cestiniPaper.csv')


ordina_csv()