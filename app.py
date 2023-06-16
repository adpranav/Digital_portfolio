import streamlit as st

def main():
    st.set_page_config(page_title='Resume', layout='wide')

    # Load the resume HTML file
    with open('resume.html', 'r') as file:
        resume_html = file.read()

    # Display the resume in Streamlit
    st.write(resume_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
