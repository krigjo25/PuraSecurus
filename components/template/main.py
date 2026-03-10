import reflex as rx

def main(page_content: rx.Component) -> rx.Component:
    return rx.container(page_content)                   #type: ignore - Container is a valid component, but pylance doesn't recognize it.