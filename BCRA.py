import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

def base_request(date_from: str, date_to: str, serie: str, detalle: str) -> str:
	payload = {
		"fecha_desde": date_from,
		"fecha_hasta": date_to,
		"B1": "Enviar",
		"primeravez": 1,
		"serie": serie,
		"detalle": detalle
	}
	req = requests.post('http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp', data=payload)
	return req.text

def build_timeframe(frame: str) -> list:
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

def base_parsing(timeframe: str, series_id: str, detalle: str):
	tf = build_timeframe(timeframe)
	data_request = base_request(tf[0], tf[1], series_id, detalle)
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

def monetary_base(timeframe: str) -> list:
	return base_parsing(timeframe, '7930', 'Base Monetaria - Promedio acumulado del mes  (MM de $)')

def fx_reserves(timeframe: str) -> list:
	return base_parsing(timeframe, '246', 'Reservas Internacionales del BCRA (en millones de dólares - cifras provisorias sujetas a cambio de valuación)')

def monthly_inflation(timeframe: str) -> list:
	return base_parsing(timeframe, '7931', 'Base Monetaria - Promedio acumulado del mes  (MM de $)')

