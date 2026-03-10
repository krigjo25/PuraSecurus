#   Python Libraries
from typing import Dict, List

#   Third-party Libraries
import reflex as rx
from pydantic import ValidationError

#   Internal Libraries
from utils.logger import NavigationWatcher
from components.navigation.anchor import anchor
from components.navigation.models import AnchorModel

logger = NavigationWatcher(name='Navigation-Watcher')
logger.file_handler()

def anchor_navigation(anchors: List[Dict[str, str | List[str]]]) -> rx.Component:

    validated_anchors: List[AnchorModel] = []

    for item in anchors:
        raw_cls = item.get("cls", [])
        raw_href = item.get("href", "")
        raw_label = item.get("label", "")
        
        try:
            model: AnchorModel = AnchorModel(
                label = raw_label if isinstance(raw_label, str) else "",
                href = raw_href if isinstance(raw_href, str) else "",
                cls = raw_cls if isinstance(raw_cls, list) else [])

            validated_anchors.append(model)

        except ValidationError as e:
            logger.error(f"Pydantic {e.__class__} anchor data: {e.errors()}")


    list_of_anchors = [anchor(data) for data in validated_anchors]

    return rx.hstack( *list_of_anchors ) #type: ignore - HStack is a valid component, but pylance doesn't recognize it.
