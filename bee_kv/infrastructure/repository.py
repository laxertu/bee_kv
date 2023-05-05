import pathlib
import shelve

from bee_kv.application.driven.ports import KvRepository, ItemNotfoundException
from bee_kv.application.model.entities import KvDataItem


class DictToFileRepository(KvRepository):

    def __init__(self, file_path: str):
        self._file_path = pathlib.Path(file_path)

    def save(self, kv_data_item: KvDataItem):
        with shelve.open(str(self._file_path), "c") as fp:
            fp[kv_data_item.key] = kv_data_item.value

    def get(self, key: str) -> KvDataItem:
        return KvDataItem(key=key, value=self._get_object(key))

    def get_all(self) -> dict:
        with shelve.open(str(self._file_path)) as fp:
            return {key: KvDataItem(key=key, value=fp.get(key)) for key in fp.keys()}

    def reset(self) -> None:
        with shelve.open(str(self._file_path), "c") as fp:
            fp.clear()

    def remove(self, key: str) -> None:
        with shelve.open(str(self._file_path), "c") as fp:
            try:
                fp.pop(key)
            except Exception:
                raise ItemNotfoundException(f"Error while removing {key} or unexistent key")

    def _get_object(self, key: str):
        with shelve.open(str(self._file_path)) as fp:
            result = fp.get(key)
            if result is None:
                raise ItemNotfoundException(f"Key not found {key}")
            return result
