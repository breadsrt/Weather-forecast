import requests
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
app.setStyleSheet("""
        QWidget
        {
            background: 4f4e4e;
        }
        QPushButton
        {
            background-color: #03a198;
            border-width: 1px;
            border-color: red;
            border-radius: 1px;
            margin: 5px;
            color: white;
            
        }
        QLineEdit
        {
        font-family: cursive;
        }
    """)

get_weather = QPushButton("Отримати прогнноз")
city_val = QLineEdit()
city_val.setPlaceholderText("Введіть місто")
result_input = QLineEdit()
result_input.setPlaceholderText("Температура")
presure_input = QLineEdit()
presure_input.setPlaceholderText("Тиск")
visibility_input = QLineEdit()
visibility_input.setPlaceholderText("Видимість")
windspeed_input = QLineEdit()
windspeed_input.setPlaceholderText("Швидкісь вітру")
sea_level = QLineEdit()
sea_level.setPlaceholderText("Рівень моря")
timezone = QLineEdit()
timezone.setPlaceholderText("Часовий пояс")

def weather():
    city_name = city_val.text()
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=f81703c1f3b81ad93e6644153c4a426e")
    data = response.json()
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    visibility = data['visibility']
    wind = data['wind']['speed']
    city = data['name']
    sea_lvl = data['main']['sea_level']
    timezone_dat = data['timezone']
    result_input.setText("Температура: " + str(round(temp-273.15, 1)))
    presure_input.setText("Тиск: " + str(pressure))
    visibility_input.setText("Видимість: " + str(visibility))
    windspeed_input.setText("Швидкість вітру: " + str(wind))
    sea_level.setText("Рівень моря: " + str(sea_lvl))
    if timezone_dat == 7200:
        timezone.setText("Часовий пояс: Київ")



main_line = QVBoxLayout()
main_line.addWidget(city_val)
main_line.addWidget(result_input)
main_line.addWidget(presure_input)
main_line.addWidget(visibility_input)
main_line.addWidget(windspeed_input)
main_line.addWidget(sea_level)
main_line.addWidget(timezone)
main_line.addWidget(get_weather)




get_weather.clicked.connect(weather)


window.setLayout(main_line)
window.show()
app.exec()