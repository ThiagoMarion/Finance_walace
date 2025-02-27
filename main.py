"""
Streamlit dashboard application with custom color palette.
Displays data from an Excel file in a customized layout.
"""

from pathlib import Path
import pandas as pd
import streamlit as st

# Constants
DATA_PATH = Path('Data/Dataset.xlsx')

st.set_page_config(layout='wide')

st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF;
        }
        .stButton button {
            background-color: #1565C0;
            color: white;
        }
        * {
            font-family: sans-serif;
            color: #2E2E2E;
        }
    </style>
""", unsafe_allow_html=True)

def load_data() -> pd.DataFrame:
    """Load and return the dataset from Excel file."""
    df = pd.read_excel(DATA_PATH)

    df['recorded'] = df['recorded'].replace({'S': True, 'N': False})
    df['frequency'] = df['frequency'].replace({'S': True, 'N': False})

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype('string')
    
    df['month'] = df['cash_date'].dt.to_period('M') 
    return df

def setup_page():
    """Configure page layout and basic elements."""
    st.title("Custom Color Palette Example")
    st.write("This is a layout example using the provided color palette.")

def main():
    """Main application function."""
    setup_page()
    st.session_state['df'] = load_data()
    st.dataframe(st.session_state['df'])
    st.button("Click me!")

if __name__ == '__main__':
    main()




