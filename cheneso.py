import csv
from telegram import ForceReply, Update, Chat
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ApplicationBuilder
from math import radians, sin, cos, asin, sqrt


with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è", TOKEN)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    text = update.message.text
    id = update.message.chat.id

    if update.message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        # location = message.location

        # una volta trovata una LOCATION dovete usare una funzione per scorrere i vostri dataset/database

        #array_posizione_minima = []
        #array_posizione_minima = scorri_csv(lat, lon)
        scorri_csv(lat, lon)
        #print (array_posizione_minima)

        # cercate l'oggetto più vicino alla vostra posizione (con il codice che trovate sul gruppo Telegram)
        # restituite in output nel prossimo await update.message.reply_venue con la lat e lon dell'oggetto, Nome e Via

        # qui prendete i valori di NomeOggetto e NomeVia dal vostro DB
        
        await update.message.reply_venue(array_posizione_minima[0], array_posizione_minima[1], 'cestino', 'via cestino')

        #await update.message.reply_text(lat)
        #await update.message.reply_text(lon)
        #handle_location(id, message.location)

    else:
        await update.message.reply_text('Mandami una posizione')

    await update.message.reply_text(id)


def scorri_csv(lat, lon):
    distanzaMinima = 0
    lat_minimo = 0
    lon_minimo = 0
    
    with open("data/datiCestino.csv", 'r', encoding = 'latin-1') as csvfile:
        prima_riga = True
        reader = csv.reader(csvfile, delimiter=',')

        for riga in reader:
            if prima_riga:
                prima_riga= False
                continue
            print(riga)
            lat2 = riga[1]
            lon2 = riga[2]
            print(lon2)
            distanza_cestino = distanza(lat, lon, lat2, lon2)
            if (distanza_cestino < distanzaMinima):
                distanzaMinima = distanza_cestino
                lat_minimo = lat2
                lon_minimo = lon2
    #return lat_minimo, lon_minimo
    print(lat_minimo, lon_minimo, distanzaMinima)


            
def distanza(lat1,lon1, lat2, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return((c * r)*1000)





def main():
    # Crare l'applicazione (il vostro bot)
    app = ApplicationBuilder().token(TOKEN).build()

    # Controlla tutti i messaggi inviati, se il messaggio inviato è una LOCATION, fai partire la funzione handle_message
    app.add_handler(MessageHandler(filters.LOCATION, handle_message))

    # Run the bot until the user presses Ctrl-C
    app.run_polling()

if __name__ == "__main__":
    main()