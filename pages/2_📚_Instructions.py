import streamlit as st

st.set_page_config(page_title="Instructions", page_icon="📖")

st.title('Instructions!')

st.subheader('How to use this website?')
st.write('Step 1: Click the Checker option from the navigation sidebar')
st.write('Step 2: Enter the url/website you would like to check the dead links for.')

st.write('Step 3: Choose the level of depth you would like to check for.')
st.error('If you are choosing depth of anything above 3, and you hit check, and the link checking begins, YOU HAVE TO WAIT. Streamlit and many other libraries like streamlit do not support concurrent threads to run, so this website will be requesting one website after another, and waiting to check its status and outputting any links that are broken. This process is very time consuming. Thank you for your patience.')
st.write('Step 4: Now, you wait for the links with their status codes.')

#st.success('NOTE: You should be seeing a blue box that says that link checking is in process. This ofcourse, means that link checking is underway and you just wait now. The deadlinks will be printing along with their status code which should be 404. Once the link checking is completed, you should see a message saying link checking was complete! If no deadlinks were found, you should see "Link checking completed. No broken links found!". If any deadlinks were found, you should see "Link checking completed. Found ___ broken link(s)."')
st.markdown("""
    <div style="background-color: #87CEEB; padding: 10px; border-radius: 10px;">
        <strong>NOTE:</strong>
        <ul>
            <li>You should be seeing a blue box that says that link checking is in process. This, of course, means that link checking is underway, and you just need to wait now.</li>
            <li>The deadlinks will be printing along with their status code, which should be 404. Once the link checking is completed, you should see a message saying 'link checking was complete!' along with the total number of links checked and a count of how many were non faulty and how many were dead links.</li>
            <li>If no deadlinks were found, you should see 'Link checking completed! No broken links found!'. If any deadlinks were found, you should see 'Link checking completed. Broken links: ' and the list of all broken links will be displayed here..</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

