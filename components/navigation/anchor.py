#   Third-party Libraries
import reflex as rx

#   Internal Libraries
from components.navigation.models import AnchorModel


def anchor(data: AnchorModel) -> rx.Component:

    return rx.link(                                                                            #type: ignore - Link is a valid component, but pylance doesn't recognize it.
        data.label,
        href = data.href,
        is_external =  data.is_external,
        class_name = " ".join([i for i in data.cls if i]))