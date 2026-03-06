#   Third-party Libraries
from typing import Dict, List

import reflex as rx

#   Internal Libraries
from components.text.elements import heading
from components.navigation.navigation import anchor_navigation

def logo() -> rx.Component: return rx.image(src="logo/logo.png", alt="PuraSecurus Logo", width="50px")                  #type: ignore - Image is a valid component, but pylance doesn't recognize it.

def header() -> rx.Component:

    raw_menu_items: List[Dict[str, str | List[str]]] = [
        { "label": "List of Resturants","href": "/", "cls": ["btn", "router-btn"] },
        { "label": "Add Resturant", "href": "/add-resturant", "cls": ["btn", "router-btn"] },
        { "label": "View Details", "href": "/view-details", "cls": ["btn", "router-btn"] },
    ]
    return rx.hstack(                                                                                                   #type: ignore - HStack is a valid component, but pylance doesn't recognize it.                               
        logo(),
        heading("PuraSecurus", size="9"),
        anchor_navigation(raw_menu_items),
        )