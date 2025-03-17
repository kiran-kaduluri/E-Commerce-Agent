import os
import requests
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import urllib3

# Disable SSL Warnings (For RapidAPI SSL Issues)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Amazon Search Tool using RapidAPI
def search_amazon(query):
    url = "https://real-time-amazon-data.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "ace595d123msh1d744c1f92d8fc5p1f43ddjsn05e0934740e9",
        "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
    }
    params = {"query": query, "country": "IN"}

    response = requests.get(url, headers=headers, params=params, verify=False)
    if response.status_code != 200:
        st.error(f"Error fetching Amazon search data: {response.status_code} - {response.json()}")
        return []

    data = response.json().get('data', {}).get('products', [])

    return [
        {
            'title': item.get('product_title', 'N/A'),
            'price': item.get('product_price', 'N/A'),
            'link': item.get('product_url', 'N/A'),
            'rating': item.get('product_star_rating', 'N/A'),
            'reviews': item.get('product_num_ratings', 'N/A'),
            'seller': item.get('product_byline', 'N/A')
        }
        for item in data[:5]
    ]

# Flipkart Search Tool using new RapidAPI
def search_flipkart(query):
    url = "https://real-time-flipkart-data2.p.rapidapi.com/product-details"
    headers = {
        "X-RapidAPI-Key": "ace595d123msh1d744c1f92d8fc5p1f43ddjsn05e0934740e9 ",
        "X-RapidAPI-Host": "real-time-flipkart-data2.p.rapidapi.com"
    }

    product_ids = ["MOBH4DQFSY9ETDUU"]  # Placeholder PID, dynamically fetch based on query

    products = []
    for pid in product_ids:
        params = {"pincode": "400001", "pid": pid}

        response = requests.get(url, headers=headers, params=params, verify=False)
        if response.status_code != 200:
            st.error(f"Error fetching Flipkart data: {response.status_code} - {response.json()}")
            continue

        item = response.json().get('productDetails', {})

        products.append({
            'title': item.get('title', 'N/A'),
            'price': item.get('price', 'N/A'),
            'link': f"https://www.flipkart.com/item/{pid}",
            'rating': item.get('rating', 'N/A'),
            'reviews': item.get('reviewsCount', 'N/A')
        })

    return products

# E-Commerce Agent Class
class ECommerceAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model_name="mixtral-8x7b-32768",
            api_key="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 "
        )
        self.prompt = PromptTemplate(
            template="Compare these products: {products}. Recommend the best product based on price, reviews, and specs. Include links for each product.",
            input_variables=["products"]
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_comparison(self, query):
        amazon_data = search_amazon(query)
        flipkart_data = search_flipkart(query)
        combined_data = amazon_data + flipkart_data

        if not combined_data:
            return "No product data found. Please try a different query.", []

        comparison = self.chain.run(products=combined_data)
        return comparison, combined_data

# Streamlit App Interface
st.title("🛒 E-Commerce Product Comparison")
st.subheader("Compare products from Amazon and Flipkart")

# Set up agent
agent = ECommerceAgent()

# User input
product_query = st.text_input("Enter the product name to compare:")

if st.button("Compare Products"):
    with st.spinner("Fetching product details..."):
        comparison_result, product_data = agent.generate_comparison(product_query)

        # Display AI-based comparison
        st.subheader("📊 AI Recommendation:")
        st.write(comparison_result)

        # Display individual product details
        st.subheader("🔍 Product Listings:")

        for product in product_data:
            st.markdown(f"**{product['title']}**")
            st.write(f"💰 Price: {product['price']}")
            st.write(f"⭐ Rating: {product['rating']} (Reviews: {product['reviews']})")
            st.markdown(f"[🔗 View Product]({product['link']})")
            st.markdown("---")