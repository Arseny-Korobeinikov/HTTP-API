from abc import ABC]

class Handler(ABC):
    @abstractmethod
    def can_handle(self, update:dict) -> bool: ...

    @abstractmethod
    def handle(self, update: dict) -> bool:
        pass