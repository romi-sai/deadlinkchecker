import streamlit as st
import requests
try:
    from bs4 import BeautifulSoup
except:
    from BeautifulSoup import BeautifulSoup
from urllib.parse import urljoin

def check_links(url, max_depth):
    visited_links = set()
    broken_links = []
    links_to_visit = [(url, 1)]

    while links_to_visit:
        current_url, depth = links_to_visit.pop(0)

        if depth > max_depth or current_url in visited_links:
            continue

        visited_links.add(current_url)

        try:
            response = requests.get(current_url)
            if response.status_code == 404:
                broken_links.append(f"{current_url}: {response.status_code}")

            if 'text/html' in response.headers.get('Content-Type', ''):
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links:
                    next_url = urljoin(current_url, link['href'])
                    links_to_visit.append((next_url, depth + 1))

        except Exception as e:
            # st.warning(f"Error checking link {current_url}: {e}")
            pass

    return visited_links, broken_links

def main(url, max_depth):
    st.text(f"Checking links till depth: {max_depth}")
    visited_links, broken_links = check_links(url, max_depth)

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
