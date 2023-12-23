import streamlit as st
import requests
try:
    from bs4 import BeautifulSoup
except:
    from BeautifulSoup import BeautifulSoup
from urllib.parse import urljoin

def check_single_link(url, depth, max_depth, visited_links, broken_links):
    if depth > max_depth or url in visited_links:
        return

    visited_links.add(url)

    try:
        response = requests.get(url)
        if response.status_code == 404:
            broken_links.append(str(url) + ': ' + str(response.status_code))

        if 'text/html' in response.headers.get('Content-Type', ''):
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            for link in links:
                next_url = urljoin(url, link['href'])
                check_single_link(next_url, depth + 1, max_depth, visited_links, broken_links)

    except Exception as e:
        # st.warning(f"Error checking link {url}: {e}")
        pass

def main(url, depth):
    visited_links = set()
    broken_links = []

    st.text(f"Checking links till depth: {depth}")
    check_single_link(url, 1, depth, visited_links, broken_links)

    st.text(f"Total links checked: {len(visited_links)}")
    st.text(f"Passed links: {len(visited_links) - len(broken_links)}")
    st.error(f"Dead links: {len(broken_links)}")

    if broken_links:
        st.error("Link checking completed. Broken links:")
        for link in broken_links:
            st.warning(link)
    else:
        st.success("Link checking completed! No broken links found!")

# Streamlit UI
st.set_page_config(page_title="Deadlink Checker", page_icon="🔗", layout="wide")
st.title('Deadlink Checker!')

url = st.text_input("Enter URL to check for dead links:")
given = st.selectbox("Please select the depth you'd like to check", ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

if st.button("Check"):
    if url:
        with st.spinner("Checking links..."):
            main(url, int(given))
    else:
        st.warning("Please enter a valid URL.")
