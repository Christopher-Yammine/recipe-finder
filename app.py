"""
A Streamlit app to find recipes based on ingredients.
"""

import streamlit as st
import requests


st.title("Recipe Finder")

# Input field for ingredients
ingredients_input = st.text_input("Enter ingredients (comma separated)")

def get_recipes(ingredients):
    """
    Fetch recipes based on ingredients from the Spoonacular API.
    
    Args:
    ingredients (str): Comma-separated list of ingredients.
    
    Returns:
    list: A list of recipes.
    """
    api_key = "3a0aaf1dccae480c9da6d06e1ea617d4"
    url = (
        f"https://api.spoonacular.com/recipes/findByIngredients?"
        f"ingredients={ingredients}&number=5&apiKey={api_key}"
    )
    response = requests.get(url, timeout=10)  # Added timeout for the request
    return response.json()

if st.button("Search"):
    if ingredients_input:
        recipes = get_recipes(ingredients_input)

        if recipes:
            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'])

                st.write("**Missing Ingredients:**")
                for ingredient in recipe['missedIngredients']:
                    st.write(f"{ingredient['name'].capitalize()} - "
                             f"{ingredient['amount']} {ingredient['unit']}")
                    st.image(ingredient['image'])
        else:
            st.write("No recipes found.")
    else:
        st.write("Please enter some ingredients.")
