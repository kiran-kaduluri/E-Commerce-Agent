🛒 E-Commerce Product Comparison

This project is a Streamlit-based web application that compares products from Amazon and Flipkart using real-time APIs. It leverages LangChain with Groq's LLM to analyze and recommend the best product based on price, reviews, and specifications.

🚀 Features

Compare Products: Fetch real-time product data from Amazon and Flipkart.

AI Recommendation: Get the best product suggestion using Groq's AI model.

Product Listings: Display product details including title, price, rating, and purchase links.

🧰 Tech Stack

Python 3.10+

Streamlit (for the UI)

LangChain (for AI integration)

Groq API (for LLM-powered insights)

RapidAPI (for real-time Amazon and Flipkart data)

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/ecommerce-comparison.git

cd ecommerce-comparison

Set up a virtual environment (optional):

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set environment variables:

Create a .env file with the following:

GROQ_API_KEY=your_groq_api_key

RAPIDAPI_KEY=your_rapidapi_key

▶️ Usage

Run the application:

streamlit run app.py

Enter a product name in the input box and click "Compare Products".

📊 Output

AI Recommendation: Best product based on a detailed comparison.

Product Listings: Display individual product details from both platforms.

🔒 API Configuration

Ensure you have valid API keys:

Groq API: Get your Groq API key

RapidAPI: Get Amazon and Flipkart API keys

📝 License

This project is licensed under the MIT License.

📧 Contact

For any issues or suggestions, feel free to reach out:

GitHub: yourusername

Email: your@email.com

