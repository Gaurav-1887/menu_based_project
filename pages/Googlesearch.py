import streamlit as st
from googlesearch import search
import requests
from bs4 import BeautifulSoup

def get_top_5_google_results(query):
    search_results = search(query, num_results=5)
    results = []
    for url in search_results:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'No title'
            results.append({'url': url, 'title': title})
        except Exception as e:
            pass
    return results

st.title("Google Search Top 5 Results")
query = st.text_input("Enter the search query:")
if st.button("Search"):
    if query:
        results = get_top_5_google_results(query)
        if results:
            for result in results:
                st.write(f"**Title:** {result['title']}\n**URL:** {result['url']}\n")
        else:
            st.write("No results found.")
    else:
        st.error("Please enter a search query.")
