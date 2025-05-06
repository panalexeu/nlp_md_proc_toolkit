import pandas as pd
import streamlit as st

# global configuration
st.set_page_config(layout='wide')

# session state
if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame()

if 'text' not in st.session_state:
    st.session_state['text'] = ''

# content
st.title('CSV-Markdown editor')
st.markdown('This simple editor allows you to manually check the markdown formatting of text in a CSV file and render '
            'it. To do so, copy the text value from the data editor to the text area in the `Input` section, press '
            '`CTRL+Enter`, and evaluate the formatting in the right column labeled `Markdown`. Edit the text in '
            '`Input` once it is properly formatted, then copy and paste it back into the CSV editor.')


# file uploading
if file_upload := st.file_uploader(label='Choose a .csv file', accept_multiple_files=False):
    st.session_state['df'] = pd.read_csv(file_upload)

# layout
col1, col2, col3 = st.columns([1, 1, 1], gap='small', border=True, vertical_alignment='top')

# editor
with col1:
    st.write('Dataframe')
    st.data_editor(st.session_state['df'])

# text input
with col2:
    st.write('Input')
    if text := st.text_area('Text'):
        st.session_state['text'] = text

# markdown render of text input
with col3:
    st.write('Markdown')

    with st.container(height=512):
        st.markdown(st.session_state['text'])
