import tkinter as tk
import requests
import time

#function
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f&units=metric"
    
    json_data = requests.get(api).json()

    if json_data['cod'] == '404':
        info_small.config(text='The city was not found. Try again.')
        info_big.config(text='')
    else:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'])
        min_temp = int(json_data['main']['temp_min'])
        max_temp = int(json_data['main']['temp_max'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
        
        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        info_big.config(text = final_info)
        info_small.config(text = final_data)

#creating canvas
canvas = tk.Tk()
canvas.geometry("500x400")
canvas.title("Weather App")

#fonts
font_small = ("Helvetica", 15, "bold")
font_big = ("Helvetica", 35, "bold")

#entry box
textField = tk.Entry(canvas, justify='center', width=20, font=font_big)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

#instructions
instructions= tk.Label(text='Enter city name to check the current weather.', font=font_small, pady=10)
instructions.pack()

#displaying info
info_big = tk.Label(canvas, font=font_big)
info_big.pack()
info_small = tk.Label(canvas, font=font_small)
info_small.pack()

canvas.mainloop()