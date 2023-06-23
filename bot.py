import pandas as pd
from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from telegram import ForceReply, Chat
from telegram.ext import Application, MessageHandler, filters
from math import radians, sin, cos, asin, sqrt, atan2


with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è", TOKEN)

"""
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
    datiCestini.to_csv('data/datiCestino.csv', index = False)
    datiCestini = datiCestini[datiCestini['recycling:plastic'] == 'yes']
    datiCestini.to_csv('data/cestiniPlastic.csv')
    datiCestini = datiCestini[datiCestini['recycling:glass'] == 'yes']
    datiCestini.to_csv('data/cestiniGlass.csv')
    datiCestini = datiCestini[datiCestini['recycling:paper'] == 'yes']
    datiCestini.to_csv('data/cestiniPaper.csv')
"""


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("""Comandi disponibili:

    CONDIVIDI LA POSIZIONE per trovare il cestino più vicino a te
    /setlocation: metti il paese da dove vuoi cercare
    /mapbins: porta alla mappa di tutti i cestini
    /maptype: metti il tipo del cestino da cercare
    """)


async def setlocation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("bussolengo", url='http://umap.openstreetmap.fr/it/map/bussolengo_931583?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("castelnuovo", url='http://umap.openstreetmap.fr/it/map/castelnuovo_931665?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("lazise", url='http://umap.openstreetmap.fr/it/map/lazise_931666?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("mozzecane", url='http://umap.openstreetmap.fr/it/map/mozzecane_931667?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("pastrengo", url='http://umap.openstreetmap.fr/it/map/pastrengo_931668?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("pescantina", url='http://umap.openstreetmap.fr/it/map/pescantina_931670?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("sommacampagna", url='http://umap.openstreetmap.fr/it/map/sommacampagna_931671?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("sona", url='http://umap.openstreetmap.fr/it/map/sona_931672?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("valeggio", url='http://umap.openstreetmap.fr/it/map/valeggio_931673?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("vigasio", url='http://umap.openstreetmap.fr/it/map/vigasio_931677?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("villafranca", url='http://umap.openstreetmap.fr/it/map/villafranca_931678?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true') ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Seleziona un paese:', reply_markup=reply_markup)


async def mapbins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("mappa", url='http://umap.openstreetmap.fr/it/map/mappa_cestini_931800?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Schiaccia il bottone:', reply_markup=reply_markup)


async def maptype(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("plastic", url='http://umap.openstreetmap.fr/it/map/mappa_plastic_931806?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("glass", url='http://umap.openstreetmap.fr/it/map/mappa_glass_931802?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')],
                [InlineKeyboardButton("paper", url='http://umap.openstreetmap.fr/it/map/mappa_paper_931804?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Schiaccia il bottone:', reply_markup=reply_markup)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    text = update.message.text
    id = update.message.chat.id

    if update.message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        risultato = scorri_csv(lat, lon)

        await update.message.reply_venue(risultato[1], risultato[0], 'NomeOggetto', 'NomeVia?')

    else:
        await update.message.reply_text('Mandami una posizione')


def scorri_csv(lat,lon):
    percorso = r"C:\Users\PC\OneDrive\Documenti\GitHub\12Cestini\data\datiCestino.csv"
    percorso = percorso.replace("\\", "/")

    cestini = pd.read_csv(percorso)

    lista_lat_lon = cestini.iloc[:][['lon','lat']]
    distanzaMinima = 10**10

    for row in range(len(lista_lat_lon)):
        lat_cestino = lista_lat_lon.iloc[row]['lon']
        lon_cestino = lista_lat_lon.iloc[row]['lat']

        distanza_cestino = distanza(lat, lon, lat_cestino, lon_cestino)

        if (distanza_cestino < distanzaMinima):
            distanzaMinima = distanza_cestino
            lat_minimo = lat_cestino
            lon_minimo = lon_cestino

    return(lat_minimo, lon_minimo, distanzaMinima)


def distanza(lat1,lon1, lat2, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    # c = 2 * m.asin(m.sqrt(a))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371
    return((c * r)) #*1000


def main():
    #ordina_csv()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("setlocation", setlocation))
    app.add_handler(CommandHandler("mapbins", mapbins))
    app.add_handler(CommandHandler("maptype", maptype))
    app.add_handler(MessageHandler(filters.LOCATION, handle_message))
    app.run_polling()


if __name__ == '__main__':
    main()
