import requests #allow you to send HTTP/1.1 requests using Python

def by_city():
    city = input('Enter your city : ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=156f44ec04034538dcc726300a3c12b3&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

def by_location():

    latitude = input('Enter your latitude : ')
    longitude = input('Enter your longitude : ')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=156f44ec04034538dcc726300a3c12b3&units=metric'.format(latitude, longitude)
    res = requests.get(url)
    data = res.json()
    show_data(data)

def show_data(data):
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    print()
    
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))


def main():
    print('1. Get data By city')
    print('2. Get data By location')
    choice = input('Enter your choice : ')

    if choice == '1':
        by_city()

    else:
        by_location()    

if __name__ == '__main__':
    main()