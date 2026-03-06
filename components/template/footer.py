#   Third-party Libraries
import reflex as rx

def copyright() -> rx.Component: return rx.text("© 2026 PuraSecurus. All rights reserved.", size="1", color="gray.500")    #type: ignore - Text is a valid component, but pylance doesn't recognize it.
def footer() -> rx.Component:
    return rx.hstack( copyright())                                                                                          #type: ignore - HStack is a valid component, but pylance doesn't recognize it.