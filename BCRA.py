import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

class BCRA:
	def __init__(self):
		super(BCRA, self).__init__()
		self.base_url  = 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp'

	def base_request(self, date_from: str, date_to: str, serie: str, detalle: str) -> str:
		payload = {
			"fecha_desde": date_from,
			"fecha_hasta": date_to,
			"B1": "Enviar",
			"primeravez": 1,
			"serie": serie,
			"detalle": detalle
		}
		req = requests.post(self.base_url, data=payload)
		return req.text

	def build_timeframe(self, frame: str) -> list:
		# Data from BCRA has a 5-6 days delay
		tf_dict = {
			'Y': 370,
			'W': 12,
			'M': 35
		}
		tf = frame.split(' ')
		tf_from = date.today() - timedelta(days=tf_dict[tf[1]])
		tf_to = date.today() - timedelta(days=5)
		return [tf_from, tf_to]

	def base_parsing(self, timeframe: str, series_id: str, detalle: str):
		tf = self.build_timeframe(timeframe)
		data_request = self.base_request(tf[0], tf[1], series_id, detalle)
		parse_data = BeautifulSoup(data_request, features='lxml')
		table_body = parse_data.find_all('tbody')
		data_series = []
		for t_body in table_body:
			find_tr = t_body.find('tr')
			find_td = find_tr.find_all('td')
			date = datetime.strptime(find_td[0].text.strip(), '%d/%m/%Y').strftime('%d-%m-%Y')
			value = find_td[1].text.strip().replace('.','')
			data_series.append([date, value])
		return data_series

	def monetary_base(self, timeframe: str) -> list:
		return self.base_parsing(timeframe, '7930', 'Base Monetaria - Promedio acumulado del mes  (MM de $)')

	def fx_reserves(self):
		pass

	def monthly_inflation(self):
		pass