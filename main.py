import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой
# Основной класс
class Currency:
	# Ссылка на нужную страницу
	DOLLAR_UA = 'https://www.google.com/search?q=dollar+uah&sxsrf=AOaemvLmMDYwvV2rCrNaGYIWHbzmLKd7oA%3A1631739586993&ei=wl5CYbiMPMWurgSojqTgBA&oq=dollar+uah&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEMsBMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoFCAAQgAQ6CAgAELEDEIMBOggILhCxAxCDAToLCC4QgAQQxwEQowI6EgguEIAEELEDEMcBENEDEAoQAToICAAQgAQQsQM6BAguEEM6BwgAELEDEEM6DQgAEIAEEIcCELEDEBQ6CwguEIAEEMcBEK8BOg4ILhCABBCxAxDHARCjAjoHCC4QQxCTAjoECAAQQzoLCAAQgAQQsQMQgwE6CgguEMcBEKMCEEM6BwguELEDEEM6DQguEMcBEKMCEEMQkwI6BAgAEAo6CAgAEBYQChAeSgQIQRgAUPn5I1jrjCRg144kaARwAngAgAF_iAGyCJIBAzIuOJgBAKABAcgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwi49crT74HzAhVFl4sKHSgHCUwQ4dUDCA4&uact=5'
	# Заголовки для передачи вместе с URL
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

	current_converted_price = 0
	difference = 5 # Разница после которой будет отправлено сообщение на почту

	def __init__(self):
		# Установка курса валюты при создании объекта
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# Метод для получения курса валюты
	def get_currency_price(self):
		# Парсим всю страницу
		full_page = requests.get(self.DOLLAR_UA, headers=self.headers)

		# Разбираем через BeautifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# Проверка изменения валюты
	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		if currency >= self.current_converted_price + self.difference:
			print("Курс сильно вырос, может пора что-то делать?")
			self.send_mail()
		elif currency <= self.current_converted_price - self.difference:
			print("Курс сильно упал, может пора что-то делать?")
			self.send_mail()
		print("Сейчас курс: 1 доллар = " +str(currency,)+'грн')
		time.sleep(1) # Засыпание программы на 3 секунды
		self.check_currency()

	

# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()