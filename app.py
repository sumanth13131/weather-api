import requests
from flask import Flask,jsonify


app=Flask(__name__)


@app.route('/<city>',methods=['GET','POST'])
def index(city):
	url=f'https://api.waqi.info/search/?token=e4c9bb358133d176ec63970412650e83e32a61a2&keyword={city}'
	#print(url)
	response=requests.post(url=url)
	result=response.json()
	try:
		if result['status'] == 'ok':
			loc=result['data'][0]['station']['name']
			url=f'https://api.waqi.info/feed/{loc}/?token=e4c9bb358133d176ec63970412650e83e32a61a2'
			response=requests.post(url=url)
			result=response.json()
			o3=result['data']['forecast']['daily']['o3'][3]['avg']
			pm10=result['data']['forecast']['daily']['pm10'][3]['avg']
			pm25=result['data']['forecast']['daily']['pm25'][3]['avg']
			uvi=result['data']['forecast']['daily']['uvi'][3]['avg']
			data={'o3':o3,'pm10':pm10,'pm25':pm25,'uvi':uvi}
		else:
			data={'o3':0,'pm10':0,'pm25':0,'uvi':0}
	except :
		data={'o3':0,'pm10':0,'pm25':0,'uvi':0}
	return jsonify(data)



if '__main__' == __name__:
	app.run(debug=True)