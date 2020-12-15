import json
from typing import Any


class AttributeDict:
    def __init__(self, value={}, **kwargs):
        if isinstance(value, list):
            self.value = [
                self.__make(item) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            self.value = dict(value, **kwargs)

    def __len__(self) -> int:
        return len(self.value)

    def __str__(self) -> str:
        return json.dumps(self.value, default=lambda x: x.__dict__())

    def __repr__(self) -> str:
        return self.value.__repr__()

    def __dict__(self) -> dict:
        return self.value

    def __bool__(self) -> bool:
        return bool(self.value)

    def __getattr__(self, name: str) -> Any:
        if isinstance(self.value, list):
            return self.value[name]

        return self.__get(name)

    def __getitem__(self, key: str) -> Any:
        return self.__getattr__(key)

    def __contains__(self, element: Any) -> bool:
        return element in self.value

    def __get(self, name: str) -> Any:
        value = self.value.get(name)

        if name in self.value:
            if isinstance(value, dict):
                value = self.__make(value)
            elif isinstance(value, list):
                value = [
                    item if not isinstance(item, dict) else self.__make(item)
                    for item in value
                ]
            elif isinstance(value, tuple):
                value = (item
                         if not isinstance(item, dict) else self.__make(item)
                         for item in value)
            elif isinstance(value, set):
                value = {
                    item if not isinstance(item, dict) else self.__make(item)
                    for item in value
                }
        else:
            if hasattr(name, self.value):
                value = getattr(name, self.value)

        return value

    @classmethod
    def __make(cls, *args, **kwargs):
        return cls(*args, **kwargs)
