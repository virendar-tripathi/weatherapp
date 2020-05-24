import tkinter as tk 
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

#bf14f509c80474bfad835d1e0dbec89f
#api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemprature (*F): %s' % (name, desc, temp)

	except:
		final_str = 'There was a problem in retriving the weather'

	return final_str	



def get_weather(city):
	Weather_key = 'bf14f509c80474bfad835d1e0dbec89f'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': Weather_key, 'q': city, 'units':'Metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)


def test_function(entry):
	print("This is the Entry:", entry)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))

button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()
