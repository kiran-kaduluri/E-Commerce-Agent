---

##🛒 E-Commerce Product Comparison

This project is a Streamlit web application that compares products from Amazon and Flipkart using real-time data from RapidAPI. The app leverages LangChain and Groq API to provide AI-generated insights and recommendations based on product price, ratings, and reviews.


---

##📌 Features

🔍 Product Search: Search for any product and fetch live data from Amazon and Flipkart.

📊 AI-Powered Comparison: Uses LangChain and Groq's Mixtral-8x7B model to analyze and compare products.

📈 Detailed Insights: Displays product details, including price, rating, reviews, and direct links.

⚡ Real-Time Data: Fetches the latest product data using RapidAPI endpoints.



---

##🏗️ Project Structure

📂 e-commerce-comparison/
├── 📄 main.py         # Main Streamlit app
└── 📄 README.md      # Project documentation


---

##🧰 Tech Stack

Python (≥3.10)

Streamlit (UI Framework)

LangChain (AI Agent Framework)

Groq API (AI Model: Mixtral-8x7B)

RapidAPI (Amazon & Flipkart Data APIs)



---

##🚀 Getting Started

1. Clone the Repository

git clone https://github.com/your-username/e-commerce-comparison.git
cd e-commerce-comparison

2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

##requirements.txt content (if needed):

streamlit
requests
langchain
langchain-groq
urllib3

4. Set Up Environment Variables

Create a .env file to securely store API keys:

# .env file
GROQ_API_KEY=your-groq-api-key
RAPIDAPI_KEY=your-rapidapi-key

Or, update the API keys in the main.py script directly.

5. Run the Application

streamlit run main.py


---

##📊 Usage

1. Enter the product name (e.g., "iPhone 15") in the search bar.


2. Click "Compare Products" to fetch and compare data from Amazon and Flipkart.


3. View AI-generated recommendations and detailed product listings with direct purchase links.




---

##🔐 API Configuration

Ensure you have valid API keys:

Groq API Key: Sign up at Groq

RapidAPI Key: Subscribe to the following APIs:

Amazon Real-Time Data

Flipkart Real-Time Data



Replace placeholder values in the script:

"X-RapidAPI-Key": "your-rapidapi-key"
api_key="your-groq-api-key"


---

##📌 Customization

1. Modify the product search logic to dynamically fetch Flipkart product IDs.


2. Customize the AI comparison prompt in the ECommerceAgent class:



template="Compare these products: {products}. Recommend the best product based on price, reviews, and specs."


---

📄 License

This project is licensed under the MIT License.


---

##🖥️ Deployment
To deploy on Streamlit Cloud:

Push your code to a GitHub repository.
Go to Streamlit Cloud and log in with GitHub.
Click "New app" and select your repository.
Enter app.py as the entry point.
Click "Deploy" and your app will go live!
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push the branch (git push origin feature-branch).
Submit a pull request.


---

##📧 Contact

For questions or support, reach out via GitHub Issues.

Happy Coding! 🚀


---
