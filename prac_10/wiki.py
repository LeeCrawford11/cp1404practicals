"""
CP1404/CP5632 Practical
wiki demo
"""
import wikipedia

try:
    search_choice = input("Title of page or search phrase: ")
    page = wikipedia.page(search_choice, auto_suggest=False)
except wikipedia.exceptions.DisambiguationError as e:
    page = wikipedia.page(e.options[0])
print(page.title)
print(page.summary)
print(page.url)


