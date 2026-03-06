import reflex as rx

def heading(heading: str, size: str = "7") -> rx.Component: return rx.heading(heading, size=size)                                                 #type: ignore - Heading is a valid component, but pylance doesn't recognize it.