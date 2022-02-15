#!/usr/bin/env python3

import telebot
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

f = open("key.txt","r")
API_KEY = f.read().rstrip("\n")

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["oi"])
def greet(message):
	bot.send_message(message.chat.id, "Ola, escolha o formato a ser pesquisado:\n/1.Standard\n/2.Modern\n/3.Pioneer\n/4.Historic\n/5.Pauper\n/6.Legacy\n/7.Vintage\n/8.Penny Dreadful\n/9.Commander 1v1\n/10.Commander\n/11.Historic Brawl\n/12.Brawl")
	
@bot.message_handler(commands=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
def choice(message):

	if(message.text == "/1"):
		bot.send_message(message.chat.id, "Voce escolheu: Standard.")
		formato = "standard"
	elif(message.text == "/2"):
		bot.send_message(message.chat.id, "Voce escolheu: Modern.")
		formato = "modern"
	elif(message.text == "/3"):
		bot.send_message(message.chat.id, "Voce escolheu: Pioneer.")
		formato = "pioneer"
	elif(message.text == "/4"):
		bot.send_message(message.chat.id, "Voce escolheu: Historic.")
		formato = "historic"
	elif(message.text == "/5"):
		bot.send_message(message.chat.id, "Voce escolheu: Pauper.")
		formato = "pauper"
	elif(message.text == "/6"):
		bot.send_message(message.chat.id, "Voce escolheu: Legacy.")
		formato = "legacy"
	elif(message.text == "/7"):
		bot.send_message(message.chat.id, "Voce escolheu: Vintage.")
		formato = "vintage"
	elif(message.text == "/8"):
		bot.send_message(message.chat.id, "Voce escolheu: Penny Dreadful.")
		formato = "penny_dreadful"
	elif(message.text == "/9"):
		bot.send_message(message.chat.id, "Voce escolheu: Commander 1v1.")
		formato = "commander_1v1"
	elif(message.text == "/10"):
		bot.send_message(message.chat.id, "Voce escolheu: Commander.")
		formato = "commander"
	elif(message.text == "/11"):
		bot.send_message(message.chat.id, "Voce escolheu: Historic Brawl.")
		formato = "historic_brawl"
	elif(message.text == "/12"):
		bot.send_message(message.chat.id, "Voce escolheu: Brawl.")
		formato = "brawl"
		
	LINK = "https://www.mtggoldfish.com/metagame/" + formato + "#paper"
	bot.send_message(message.chat.id, LINK)

	
	print("link: " + LINK)


	driver = webdriver.Chrome(ChromeDriverManager().install())
	
	driver.get(LINK)
	
	for i in range(5):
		deck_path = "//div[@class='archetype-tile-container']/div[" + str(i+1) + "]"
		
		name = driver.find_element(By.XPATH, deck_path + "/div[2]/div/div/span[2]/a").text
		print("Deck: " + name + ".")
		
		try:
			colors = driver.find_element(By.XPATH, deck_path + "/div[2]/div/div[2]/span").get_attribute("aria-label").strip("colors: ")
		except:
			colors = "colorless"
		print("Cores: " + colors + ".")
		
		card1 = driver.find_element(By.XPATH, deck_path + "/div[2]/div/ul/li[1]").text
		card2 = driver.find_element(By.XPATH, deck_path + "/div[2]/div/ul/li[2]").text
		card3 = driver.find_element(By.XPATH, deck_path + "/div[2]/div/ul/li[3]").text
		print("Cartas: " + card1 + ", " + card2 + ", " + card3 + ".")
		
		percent = driver.find_element(By.XPATH, deck_path + "/div[2]/div[2]/div[1]/div/div[2]").text
		print("Meta: " + percent + ".") 
		
		price = driver.find_element(By.XPATH, deck_path + "/div[2]/div[2]/div[2]/div[1]/div[2]").text.strip("$&nbsp;  ")
		print("Preco: " + price + " USD.")
		
		print("")
		
		bot.send_message(message.chat.id, "Deck: " + name + ".\nCores: " + colors + ".\nCartas: " + card1 + ", " + card2 + ", " + card3 + ".\nMeta: " + percent + ".\nPreco: " + price + " USD.")
        	

  	
  	

bot.polling()
