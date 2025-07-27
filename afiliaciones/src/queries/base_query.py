from abc import ABC, abstractmethod

class BaseQuery(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):  # pragma: no cover
        raise NotImplementedError("Please implement in subclass")

