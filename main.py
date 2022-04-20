import requests # 𝐌𝐨𝐝𝐮𝐥𝐞 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐔𝐑𝐋.
from bs4 import BeautifulSoup # 𝐌𝐨𝐝𝐮𝐥𝐞 𝐭𝐨 𝐰𝐨𝐫𝐤 𝐰𝐢𝐭𝐡 𝐇𝐓𝐌𝐋. 
import time # 𝐌𝐨𝐝𝐮𝐥𝐞 𝐭𝐨 𝐬𝐭𝐨𝐩 𝐭𝐡𝐞 𝐩𝐫𝐨𝐠𝐫𝐚𝐦.
# 𝐌𝐚𝐢𝐧 𝐜𝐥𝐚𝐬𝐬 
class Currency:
	# 𝐘𝐨𝐮𝐫 𝐩𝐚𝐫𝐬𝐞 𝐩𝐚𝐠𝐞 𝐥𝐢𝐧𝐤. 
	DOLLAR_UAH = 'https://www.google.com/search?q=dollar+UAH&client=opera-gx&hs=bdo&sxsrf=APq-WBvBFS8B7wgFwq2XULI-lPVeXLylKg%3A1649886063378&ei=b0NXYqLbFseX8gL49LngBQ&ved=0ahUKEwjizujFgJL3AhXHi1wKHXh6DlwQ4dUDCA0&uact=5&oq=dollar+UAH&gs_lcp=Cgdnd3Mtd2l6EAMyDAgAEAoQywEQRhCCAjIFCAAQgAQyBwgAEAoQywEyBwgAEAoQywEyBwgAEAoQywEyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6BQgAEMsBOgQIABAeOgkIABDJAxAKEB46BwgjELACECc6BAgAEA06BAgjECc6CQgAEAoQywEQKjoECAAQCkoECEEYAEoECEYYAFC3EFixIWDVImgEcAF4AIABYIgBigWSAQE4mAEAoAEByAEKwAEB&sclient=gws-wiz'
	# 𝐇𝐞𝐚𝐝𝐞𝐫 𝐭𝐨 𝐟𝐥𝐚𝐬𝐡 𝐰𝐢𝐭𝐡 𝐔𝐑𝐋. 𝐘𝐨𝐮𝐫 𝐮𝐬𝐞𝐫 𝐚𝐠𝐞𝐧𝐭, 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐟𝐢𝐧𝐝 𝐢𝐭 𝐟𝐨𝐥𝐥𝐨𝐰 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐤 𝐡𝐭𝐭𝐩://𝐦𝐲-𝐮𝐬𝐞𝐫-𝐚𝐠𝐞𝐧𝐭.𝐜𝐨𝐦. 
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}

	current_converted_price = 0

	def __init__(self):
		#
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# 𝐌𝐞𝐭𝐡𝐨𝐝 𝐭𝐨 𝐩𝐚𝐫𝐬𝐞 𝐩𝐚𝐠𝐞.
	def get_currency_price(self):
		# 𝐏𝐚𝐫𝐬𝐞 𝐰𝐡𝐨𝐥𝐞 𝐩𝐚𝐠𝐞. 
		full_page = requests.get(self.DOLLAR_UAH, headers=self.headers)

		# 𝐁𝐞𝐚𝐮𝐭𝐢𝐟𝐮𝐥𝐒𝐨𝐮𝐩 𝐚𝐧𝐚𝐥𝐲𝐬𝐢𝐬.
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐝𝐚𝐭𝐚 𝐚𝐧𝐝 𝐩𝐮𝐭 𝐢𝐭 𝐛𝐚𝐜𝐤  𝐭𝐨 𝐭𝐞𝐱𝐭. 
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐜𝐮𝐫𝐫𝐞𝐧𝐜𝐲 𝐜𝐡𝐚𝐧𝐠𝐞𝐬.
	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		print("1 Dollar  = " +str(currency,) + ' UAH')
		time.sleep(10) # 𝐏𝐫𝐨𝐠𝐫𝐚𝐦 𝐬𝐥𝐞𝐞𝐩 𝟏𝟎 𝐬𝐞𝐜𝐨𝐧𝐝𝐬. 
		self.check_currency()

	

# 𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐨𝐛𝐣𝐞𝐜𝐭 𝐚𝐧𝐝 𝐜𝐚𝐥𝐥 𝐢𝐭. 
currency = Currency()
currency.check_currency()
