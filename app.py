from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

size = {
    'millimeter': [1, 'mm'],
    'centimeter': [10, 'cm'],
    'meter': [1000, 'm'],
    'kilometer': [1000000, 'km'],
    'inch': [25.4, 'in'],
    'foot': [304.8, 'ft'],
    'yard': [914.4, 'yd'],
    'mile': [1609344, 'mi'],
    'milligram': [1, 'mg'],
    'gram': [1000, 'g'],
    'kilogram': [1000000, 'kg'],
    'ounce': [28349.52, 'oz'],
    'pound': [453592.37, 'lb'],
    'celsius': [1, '°C'],
    'fahrenheit': [1, '°F'],
    'kelvin': [1, 'K']
}
temperatures = {
    ('celsius', 'fahrenheit'): lambda x: x * 1.8 + 32,
    ('celsius', 'kelvin'): lambda x: x + 273.15,
    ('fahrenheit', 'celsius'): lambda x: (x - 32) / 1.8,
    ('fahrenheit', 'kelvin'):lambda x: (x + 459.67) * (5 / 9),
    ('kelvin', 'celsius'): lambda  x: x - 273.15,
    ('kelvin', 'fahrenheit'): lambda x: x * 1.8 - 459.67
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.json['value'])
    converted_from = request.json['converted_from']
    converted_to = request.json['converted_to']
    unit = request.json['unit']

    if converted_from == converted_to: return jsonify(f'{str(value)}  {size[converted_to][1]}')
    if unit == 'temperature':
        calculate = temperatures.get((converted_from, converted_to))
        result = calculate(value)
        return jsonify(f'{str(round(result, 2))} {size[converted_to][1]}')
    else:
        result = value * size[converted_from][0] / size[converted_to][0]
        return jsonify(f'{str(result)} {size[converted_to][1]}')

if __name__ == '__main__':
    app.run()
