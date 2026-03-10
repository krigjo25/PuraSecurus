#   Python Libraries
from __future__ import annotations
from typing import Optional

#   Third-party Libraries
from std_log import Logger


class AppWatcher(Logger):
    def __init__(self, name: str, dir:Optional[str] = None):
        super().__init__(dir = dir or 'logs', name=f"{self.__class__.__name__} -- {name}.log")

class NavigationWatcher(Logger):
    def __init__(self, name: str, dir:Optional[str] = None):
        super().__init__(dir = dir or 'logs', name=f"{self.__class__.__name__} -- {name}.log")