# Standard Libraries
from typing import Dict, List

#   Third-party Libraries
import reflex as rx
from rxconfig import config

#   Internal Libraries
from components.text.elements import heading
from components.navigation.navigation import anchor_navigation

def logo() -> rx.Component: return rx.image(src="logo/logo.png", alt=f"{config.app_name} Logo", width="50px")       #type: ignore - Image is a valid component, but pylance doesn't recognize it.

def header() -> rx.Component:

    raw_menu_items: List[Dict[str, str | List[str]]] = [
        { "label": "List of Resturants","href": "/", "cls": ["btn", "router-btn"] },
        { "label": "Add Resturant", "href": "/add-resturant", "cls": ["btn", "router-btn"] },
    ]


    return rx.box(                                                                                                  #type: ignore - Box is a valid component, but pylance doesn't recognize it.
            rx.vstack(                                                                                              #type: ignore - HStack is a valid component, but pylance doesn't recognize it.
                logo(),
                heading(config.app_name, size="9")
                ),

            rx.hstack(                                                                                          #type: ignore - VStack is a valid component, but pylance doesn't recognize it.
                    anchor_navigation(raw_menu_items)
                ),
                as_="header"),