import requests
import json
import streamlit as st


# set the apikey and limit
api_key = st.secrets["api_key"]
st.write(st.secrets['test'])
lmt = 8

# our test search
search_term = st.text_input('Search GIF', 'TGIF')

# get the top 8 GIFs for the search term
r = requests.get(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, api_key, lmt))

if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    top_8gifs = json.loads(r.content)
    st.image(top_8gifs['results'][0]["media"][0]["gif"]["url"])

else:
    top_8gifs = None

