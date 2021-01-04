from instabot import Bot
import random
import os

os.rename(r'bee.jpg',r'bee.jpg.REMOVE_ME')
os.rename(r'bee.jpg.REMOVE_ME',r'bee.jpg')
bot = Bot()
bot.login(username = "xyztic",password = "ricky123")
bot.upload_photo("bee.jpg",caption ="HAHAHA")
