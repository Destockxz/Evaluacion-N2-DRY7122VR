import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "uE15X8syGYuyrOxeWJBgEsJb7ZIl2kC0"

while True:
	print("Bienvenido el dia es ")
	import datetime

	hora_actual = datetime.datetime.now()

	print(hora_actual)
	orig = input("lugar de origen: ")
	if orig == "exit" or orig == "exit":
		break

	dest = input("Destino: ")
	if dest == "exit" or dest == "exit":
		break

	url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
	print("URL: " + (url))
	json_data = requests.get(url).json()
	json_status = json_data["info"]["statuscode"]

	if json_status == 0:
		print("API Status:" + str(json_status) + "= Una llamada de ruta exitosa.\ n")
		print("=============================================")
		print("De" + (orig) + " to " + (dest))
		print("Tiempo de duracion:   " + (json_data["route"]["formattedTime"]))
		print("Kilometros:      " + str((json_data["route"]["distance"])*1.61))
		#print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
		for each in json_data["route"]["legs"][0]["maneuvers"]:
                        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                        print("=============================================\n")

