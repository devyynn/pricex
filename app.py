from flask import Flask, render_template, request, jsonify
import random
import time
import logging

# Initialize Flask application with new name
app = Flask(__name__, static_folder="static")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PriceX")  # Changed from PriceSync to PriceX

# Sample product database
SAMPLE_PRODUCTS = {
    'iphone': [
        {
            'title': 'Apple iPhone 15 (128GB) - Blue',
            'price': 74999,
            'url': 'https://www.amazon.in/Apple-iPhone-15-128GB-Blue/dp/B0CHX2F5QT',
            'source': 'Amazon'
        },
        {
            'title': 'APPLE iPhone 15 (Blue, 128 GB)',
            'price': 73990,
            'url': 'https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itm6ac6439c2b91e',
            'source': 'Flipkart'
        }
    ],
    'samsung': [
        {
            'title': 'Samsung Galaxy S24 5G (256GB) - Phantom Black',
            'price': 79999,
            'url': 'https://www.amazon.in/Samsung-Galaxy-S24-256GB-Phantom/dp/B0CQPZ9Z8Y',
            'source': 'Amazon'
        },
        {
            'title': 'SAMSUNG Galaxy S24 5G (Phantom Black, 256 GB)',
            'price': 78490,
            'url': 'https://www.flipkart.com/samsung-galaxy-s24-phantom-black-256-gb/p/itm6ac6439c2b91e',
            'source': 'Flipkart'
        }
    ],
    'laptop': [
        {
            'title': 'HP Pavilion 14 12th Gen Intel Core i5 16GB/512GB SSD 14 inch(35.6 cm) Laptop',
            'price': 62990,
            'url': 'https://www.amazon.in/HP-Pavilion-i5-1235U-Graphics-14-dv2014TU/dp/B0B4N6JQBS',
            'source': 'Amazon'
        },
        {
            'title': 'HP Pavilion Intel Core i5 12th Gen 1235U - (16 GB/512 GB SSD/Windows 11 Home) 14-dv2014TU Thin and Light Laptop',
            'price': 61490,
            'url': 'https://www.flipkart.com/hp-pavilion-intel-core-i5-12th-gen-1235u-16-gb-512-gb-ssd-windows-11-home-14-dv2014tu-thin-light-laptop/p/itm6e22c9e00217c',
            'source': 'Flipkart'
        }
    ],
    'headphones': [
        {
            'title': 'Sony WH-1000XM4 Wireless Noise Cancelling Headphones',
            'price': 24990,
            'url': 'https://www.amazon.in/Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863TXGM3',
            'source': 'Amazon'
        },
        {
            'title': 'SONY WH-1000XM4 Bluetooth Headset',
            'price': 24499,
            'url': 'https://www.flipkart.com/sony-wh-1000xm4-bluetooth-headset/p/itm0c7bd5f5462df',
            'source': 'Flipkart'
        }
    ],
    'watch': [
        {
            'title': 'Apple Watch Series 9 GPS 45mm Midnight Aluminium Case',
            'price': 48900,
            'url': 'https://www.amazon.in/Apple-Watch-Series-9-GPS/dp/B0CHX9VJCH',
            'source': 'Amazon'
        },
        {
            'title': 'APPLE Watch Series 9 GPS 45mm Midnight Aluminium Case',
            'price': 47990,
            'url': 'https://www.flipkart.com/apple-watch-series-9-gps-45mm-midnight-aluminium-case/p/itm6e22c9e00217c',
            'source': 'Flipkart'
        }
    ]
}

def find_matching_products(query):
    """Find products that match the search query"""
    query = query.lower()
    results = []
    
    # Search through our sample database
    for key, products in SAMPLE_PRODUCTS.items():
        if query in key or any(query in product['title'].lower() for product in products):
            results.extend(products)
    
    # If no exact matches, try partial matches
    if not results:
        for key, products in SAMPLE_PRODUCTS.items():
            for word in query.split():
                if word in key or any(word in product['title'].lower() for product in products):
                    results.extend(products)
                    break
    
    # Add small random price variations to simulate real-time changes
    for product in results:
        variation = random.uniform(-500, 500)  # ±500 rupees variation
        product['price'] = round(product['price'] + variation)
    
    return list({product['source']: product for product in results}.values())  # Remove duplicates

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_prices():
    product_name = request.form.get('product_name')
    if not product_name:
        return jsonify({'error': 'Product name is required'})

    logger.info(f"Comparing prices for: {product_name}")
    
    # Simulate network delay
    time.sleep(random.uniform(0.5, 1.5))
    
    # Get matching products
    results = find_matching_products(product_name)
    
    logger.info(f"Found {len(results)} results")
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True) 