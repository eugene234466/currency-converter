from flask import Flask, render_template, request, jsonify  
import requests
from datetime import datetime, timedelta   
import os

app = Flask(__name__)                      

BASE_API_URL = "https://open.er-api.com/v6/latest/{currency}"

rate_cache = {}
CACHE_TTL_MINUTES = 60                    


def get_rates(base_currency):
    if base_currency in rate_cache:
        age = datetime.now() - rate_cache[base_currency]["fetched_at"]   
        if age < timedelta(minutes=CACHE_TTL_MINUTES):                   
            return rate_cache[base_currency]["rates"]

    try:
        response = requests.get(BASE_API_URL.format(currency=base_currency))  
        response.raise_for_status()                                            
        rates = response.json()["rates"]                                   
    except Exception as e:                                                     
        return None                                                          

    rate_cache[base_currency] = {"rates": rates, "fetched_at": datetime.now()} 
    return rates                                                               


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])                    
def convert():
    data       = request.get_json()                        
    amount     = data.get('amount')
    from_cur   = data.get('from_cur')
    to_cur     = data.get('to_cur')

    if not amount or not from_cur or not to_cur:            
        return jsonify({'error': 'Missing fields'}), 400

    try:
        amount = float(amount)                              
    except ValueError:
        return jsonify({'error': 'Amount must be a number'}), 400

    rates = get_rates(from_cur)

    if rates is None:                                       
        return jsonify({'error': 'API unavailable'}), 503

    if to_cur not in rates:                                 
        return jsonify({'error': f'Unknown currency: {to_cur}'}), 400

    rate   = rates[to_cur]
    result = round(amount * rate, 4)

    return jsonify({                                       
        'result':      result,
        'rate':        rate,
        'from':        from_cur,
        'to':          to_cur,
        'amount':      amount,
        'last_updated': rate_cache[from_cur]['fetched_at'].strftime('%Y-%m-%d %H:%M UTC')
    })
    
    
@app.route('/currencies')
def currencies():
    rates = get_rates('USD')
    if rates is None:
        return jsonify({'error': 'Could not fetch currencies'}), 503
    return jsonify(sorted(rates.keys()))
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  
    