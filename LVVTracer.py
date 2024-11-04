from types import FrameType, TracebackType
from typing import Any, Dict, List, Set, Optional, Union, Tuple, Type

class LVVTracer():
    def __init__(self, target_func: str):
        self.target_func = target_func

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_tp: Type, exc_value: BaseException,
                 exc_traceback: TracebackType) -> Optional[bool]:
        return None

    def getLVVmap(self) -> dict:
        return {}
