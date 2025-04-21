# PriceX - Price Comparison Website

A modern, futuristic price comparison web application that compares product prices between Amazon and Flipkart. Built with Python Flask and modern web technologies.

## Team Members

- **Jeswin Thomas** - Student ID: 20222054
- **Deva Nandan S** - Student ID: 20222037
- **Devinanda D** - Student ID: 20222039
- **Evin John** - Student ID: 20222043

## Features

- Real-time price comparison between Amazon and Flipkart
- Clean, responsive and futuristic user interface
- Interactive animations and particle effects
- Direct links to product pages
- Sample data for popular categories (phones, laptops, headphones, watches)

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Animations**: GSAP (GreenSock Animation Platform)
- **Visual Effects**: Particles.js
- **Demo Data**: Sample product database with simulated price variations

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/price-x.git
cd price-x
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter a product name in the search box and click "Compare Prices" to see price comparisons.

## Project Structure

```
price-x/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── static/               # Static assets
│   └── images/           # Image assets
└── templates/            # HTML templates
    └── index.html        # Main application template
```

## Academic Note

This project was developed as an academic demonstration of e-commerce technology and web development principles.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Important Notes

- The application scrapes data from Amazon.in and Flipkart.com
- Results may vary based on your location and the websites' availability
- Please use responsibly and respect the websites' terms of service
- This tool is for educational purposes only

## Technical Details

- Backend: Python Flask
- Frontend: HTML, TailwindCSS, JavaScript
- Web Scraping: BeautifulSoup4, Requests
- Concurrent scraping using ThreadPoolExecutor

## Limitations

- Only shows the first matching product from each website
- Prices may not include shipping costs or special offers
- Accuracy depends on the product listing format on the websites

## Contributing

Feel free to submit issues and enhancement requests! 