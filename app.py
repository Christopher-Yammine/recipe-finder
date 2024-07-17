import streamlit as st
import requests


st.title("Recipe Finder")


ingredients = st.text_input("Enter ingredients (comma separated)")


def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey=3a0aaf1dccae480c9da6d06e1ea617d4"
    response = requests.get(url)
    return response.json()


if st.button("Search"):
    if ingredients:
        recipes = get_recipes(ingredients)
        
        if recipes:
            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'])
                
                st.write("**Missing Ingredients:**")
                for ingredient in recipe['missedIngredients']:
                    st.write(f"{ingredient['name'].capitalize()} - {ingredient['amount']} {ingredient['unit']}")
                    st.image(ingredient['image'])
        else:
            st.write("No recipes found.")
    else:
        st.write("Please enter some ingredients.")
