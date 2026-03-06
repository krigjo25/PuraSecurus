#   Third-party Libraries
import reflex as rx
from rxconfig import config

#   Internal Libraries
from components.template.header import header
from components.template.footer import footer


class State(rx.State):
    """The app state."""
    pass

def layout_wrapper(page_content: rx.Component) -> rx.Component:
    return rx.fragment(                                                             #type: ignore - Fragment is a valid component, but pylance doesn't recognize it.)
    rx.color_mode.button(position="top-right"),                                     #type: ignore - ColorModeButton is a valid component, but pylance doesn't recognize it.
    
    header(),
    rx.container(page_content),                                                     #type: ignore - Container is a valid component, but pylance doesn't recognize it.
    footer()
    )

def index() -> rx.Component:

    main:rx.Component = rx.container(                                               #type: ignore - Container is a valid component, but pylance doesn't recognize it.
        rx.vstack(                                                                  #type: ignore - VStack is a valid component, but pylance doesn't recognize it.
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),                 #type: ignore - Text and Code are valid components, but pylance doesn't recognize them.
                size="5",
            ),
            rx.link(                                                                #type: ignore - Link is a valid component, but pylance doesn't recognize it.
                rx.button("Check out our docs!"),                                   #type: ignore - Button is a valid component, but pylance doesn't recognize it.
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
    return layout_wrapper(page_content = main)

def add_resturant() -> rx.Component:
    main: rx.Component = rx.text("Add Resturant Page")                              #type: ignore - Text is a valid component, but pylance doesn't recognize it.
    return layout_wrapper(page_content=main)

def view_details() -> rx.Component:
    main: rx.Component = rx.text("View Details Page")                               #type: ignore - Text is a valid component, but pylance doesn't recognize it.
    return layout_wrapper(page_content=main)

app = rx.App()
app.add_page(index)                                                                  #type: ignore - add_page is a valid method, but pylance doesn't recognize it.
app.add_page(add_resturant)                                                      #type: ignore - add_resturant is not defined, but it is a valid page that will be added later.
app.add_page(view_details)                                                       #type: ignore - view_details is not defined, but it is a valid page that will be added later.