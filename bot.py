# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
import urllib, json

TOKEN = '228961500:AAEypJQbLytI33_LiNxPQXpLsTUbsaldaV4' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['tokenpls'])
def command_getTokenPrice(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.cid
    
    url = "https://wowtoken.info/wowtoken.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    
    tokenNAprice = data['update']['NA']['formatted']['buy']
    
    bot.send_message( cid, tokenNAprice) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    
@bot.message_handler(commands=['jorge_di_lo_tuyo'])
def command_getjorge1pls(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.cid
    #bot.send_message( cid, "") # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    sti = open('./stickers/jorgesticker1.webp', 'rb')
    bot.send_sticker(cid, sti)

@bot.message_handler(commands=['que_hacemos_ahora'])
def command_getedo1pls(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.cid
    #bot.send_message( cid, "") # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    sti = open('./stickers/edosticker1.webp', 'rb')
    bot.send_sticker(cid, sti)

#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.