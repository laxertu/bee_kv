import abc
from abc import ABC
from bee_kv.application.model.entities import KvDataItem


class ItemNotfoundException(Exception):
    ...


class KvRepository(ABC):
    @abc.abstractmethod
    def save(self, kw_data_item: KvDataItem):
        ...

    @abc.abstractmethod
    def get(self, key: str) -> KvDataItem:
        ...

    @abc.abstractmethod
    def get_all(self) -> dict:
        ...

    @abc.abstractmethod
    def reset(self) -> None:
        ...

    @abc.abstractmethod
    def remove(self, key: str) -> None:
        ...
