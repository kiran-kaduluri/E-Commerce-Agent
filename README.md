# 🛒 E-Commerce Product Comparison

   This project is a Streamlit-based web application that compares products from Amazon and Flipkart using real-time APIs. It leverages LangChain with Groq's LLM to analyze and recommend the best product based on price, reviews, and specifications.

## 🌐 Live Deployment

Check out the live app: `https://e-commerce-kiran.streamlit.app/`

## 🚀 Features

- 📊 Compare products from Amazon and Flipkart in real-time

- 💬 AI-powered recommendations using Groq's LLM

- 🔍 Detailed product listings with price, ratings, and links
   

## 🛠️ Installation
To set up the project locally:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-comparison.git
cd ecommerce-comparison
```
2. Set up a virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set environment variables:
Create a `.env` file with the following:
```bash
GROQ_API_KEY=your_groq_api_key
RAPIDAPI_KEY=your_rapidapi_key

```
6. Run the Streamlit app:
```bash
streamlit run app.py
```

## 📋 Requirements
Add these to your `requirements.txt`:
```
streamlit
requests
langchain
langchain_groq
python-dotenv

```

## 🖥️ Deployment
To deploy on **Streamlit Cloud**:

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io) and log in with GitHub.
3. Click **"New app"** and select your repository.
4. Enter `app.py` as the entry point.
5. Click **"Deploy"** and your app will go live!


## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push the branch (`git push origin feature-branch`).
5. Submit a pull request.


