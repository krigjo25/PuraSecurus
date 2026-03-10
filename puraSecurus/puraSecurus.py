#   Third-party Libraries
import json
import reflex as rx


#   Internal Libraries
from utils.logger import AppWatcher
from components.template.main import main
from components.template.header import header
from components.template.footer import footer



logger = AppWatcher(name="PuraSecurus")
logger.file_handler()

class State(rx.State):
    """The app state."""
    pass

def layout_wrapper(page_content: rx.Component) -> rx.Component:
    return rx.container(                                                             #type: ignore - Fragment is a valid component, but pylance doesn't recognize it.)
    rx.color_mode.button(position="top-right"),                                     #type: ignore - ColorModeButton is a valid component, but pylance doesn't recognize it.
    
    header(),
    main(page_content),                                                     #type: ignore - Container is a valid component, but pylance doesn't recognize it.
    footer()
    )
def section (heading:str, size:int, text:str) -> rx.Component:
    return rx.section(                                                                              #type: ignore - Section is a valid component, but pylance doesn't recognize it.
        rx.heading(heading, size=f"{size}"),                                                        #type: ignore - Heading is a valid component, but pylance doesn't recognize it.
        rx.text(text)                                                                               #type: ignore - Text is a valid component, but pylance doesn't recognize it.
    )
def index() -> rx.Component:

    list_of_resturants = json.load(open("puraSecurus/data/resturants.json", "r"))["resturants"]     #type: ignore - load is a valid method, but pylance doesn't recognize it.

    logger.debug(f"Loaded {list_of_resturants} resturants from JSON file.")
    main:rx.Component = rx.container(                                                               #type: ignore - Container is a valid component, but pylance doesn't recognize it.
        *[section(heading=i["name"], size=5, text=i["description"]) for i in list_of_resturants]
        )
    return layout_wrapper(page_content = main)

def add_resturant() -> rx.Component:
    main: rx.Component = rx.text("Add Resturant Page")                                              #type: ignore - Text is a valid component, but pylance doesn't recognize it.
    return layout_wrapper(page_content=main)


app = rx.App()
app.add_page(index)                                                                                 #type: ignore - add_page is a valid method, but pylance doesn't recognize it.
app.add_page(add_resturant)                                                                         #type: ignore - add_page is a valid method, but pylance doesn't recognize it.
