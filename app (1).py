# L9 - Your first Streamlit page: Lee's Sugar Rush Bakery
# CIS 211 | Week 6 teaching module
# This bakery, its menu, and its opening hours are fictional class examples.
# Read this file alongside the Week 6 handout. It is a Python script, not a notebook.

# 1. Import the Streamlit library. The short name "st" refers to that library.
#    requirements.txt tells the hosting service to install Streamlit.
import streamlit as st

# 2. Reuse Python data structures from L6 and L7.
#    A list holds several items. A dictionary connects each key to a value.
highlights = [
    "Small batches throughout the day",
    "A menu with clearly displayed prices",
    "A convenient stop for an afternoon treat",
]

menu = {
    "cupcake": 3.75,
    "cookie": 2.00,
    "muffin": 2.75,
    "scone": 3.25,
    "brownie": 3.00,
}

shop_info = {
    "hours": "Monday-Friday, 9:00 a.m.-4:00 p.m. (fictional example)",
    "featured_item": "cupcake",
}

# 3. A function can RETURN text to the code that calls it (L5).
#    The f-string shows exactly two digits after the decimal point (L2).
def format_price(amount):
    return f"${amount:.2f}"


# 4. These calls DISPLAY content on the page, from top to bottom.
#    The title is the page's main heading. A caption adds a short supporting note.
st.title("Bright Bakery")
st.caption("A fictional bakery information page created for CIS 211.")

st.header("About our bakery")
st.write("Welcome to Bright Bakery, a small neighborhood bakery in our class example.")

# 5. Markdown goes INSIDE a Python string when passed to st.markdown().
#    Triple quotes allow the string to span several lines. Blank lines separate blocks.
#    The ** marks make text bold; the * marks make text italic.
st.markdown("""
We believe in **simple choices** and *a welcoming atmosphere*.

This page shares our example menu and opening hours.
""")

st.subheader("What you can expect")

# 6. The loop visits each value in the LIST. Each call displays one bullet.
#    st.write() understands Markdown when it receives a string.
for highlight in highlights:
    st.write(f"- {highlight}")

st.header("Menu")
st.caption("All prices below are fictional examples in U.S. dollars.")

# 7. .items() supplies each key and value from the DICTIONARY (L7).
#    format_price() returns text; st.write() displays that text on the page.
for item, price in menu.items():
    st.write(f"{item}: {format_price(price)}")

st.subheader("Featured item")

# 8. Square brackets look up a DICTIONARY value by its key (L7).
featured_item = shop_info["featured_item"]
featured_price = menu[featured_item]
st.write(f"Today's featured item is the {featured_item}: {format_price(featured_price)}.")

st.header("Opening hours")
st.write(shop_info["hours"])

st.header("About this class example")

# 9. Markdown links use [readable label](complete URL).
#    This real link goes to the official documentation for the library used here.
st.markdown("[Read the official Streamlit documentation](https://docs.streamlit.io/)")
st.caption("An information page: read the source, then personalize a copy for practice.")

# PRACTICE EDITS (ungraded rehearsal):
# - Change the bakery title and the introductory sentence.
# - Add one highlight to the list, remembering quotes and commas.
# - Change the cookie price and check that its displayed amount updates.
# - Add another Markdown paragraph, with a blank line between paragraphs.
# Lab 4 asks you to make a DIFFERENT fictional campus club or service page.
