# import streamlit as st

# st.title('Srilankan Taste')
# st.header('Welcome to Srilankan Taste')

# st.info('Information about Srilankan Taste')

# st.write('This is a web application that provides information about Srilankan Taste.')

# st.markdown('## Description')



# st.checkbox('I agree')

# st.button('Submit')

# st.select_slider('Select a value', options=['A', 'B', 'C'])

import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout="wide")

# Simulated Menu Data (Food Item, Price, and Image URL)
menu_data = [
    {"name": "Pizza", "price": 8.99, "image_path": "pizza.png"},
    {"name": "Biriyani", "price": 5.49, "image_path": "Biriyani.png"},
    {"name": "Pasta", "price": 7.99, "image_path": "pizza.png"},
    {"name": "Salad", "price": 4.99, "image_path": "pizza.png"},
    {"name": "Soda", "price": 1.99, "image_path": "Biriyani.png"},
    {"name": "Coffee", "price": 2.49, "image_path": "Biriyani.png"},
]

# Function to load and resize local images
def load_and_resize_image(image_path, size=(200, 200)):
    img = Image.open(image_path)
    img = img.resize(size)
    return img

st.markdown("""
    <style>
    /* CSS to increase the size of the tab labels */
    div[data-testid="stHorizontalBlock"] div[role="tab"] {
        font-size: 60px !important;
    }
    </style>
    """, unsafe_allow_html=True)
# Create tabs for navigation
tabs = st.tabs(["Home", "About", "Contact Us"])

# Home Page Tab
with tabs[0]:
    st.title("Restaurant Menu Dashboard")

    # Display the menu items in rows of three
    for i in range(0, len(menu_data), 3):
        cols = st.columns(3)  # Create three columns

        for idx, col in enumerate(cols):
            if i + idx < len(menu_data):  # To avoid out-of-range index errors
                item = menu_data[i + idx]
                resized_img = load_and_resize_image(item["image_path"])  # Resize image
                col.subheader(f"{item['name']} - ${item['price']:.2f}")
                col.image(resized_img, caption=item['name'], use_column_width=True)

# About Page Tab
with tabs[1]:
    st.title("About Us")
    st.write("""
        Welcome to our restaurant! We pride ourselves on serving the best quality food made with fresh ingredients.
        Whether you're in the mood for pizza, burgers, or something healthier like a salad, we have something for everyone.
        Visit us and experience great service and delicious food.
    """)

# Contact Us Page Tab
with tabs[2]:
    st.title("Contact Us")
    st.write("""
        We'd love to hear from you! Please reach out to us with any questions or feedback.
        \n**Phone**: +1 (234) 567-890
        \n**Email**: info@restaurant.com
        \n**Address**: 123 Food Street, Tasty Town, Flavorland
    """)