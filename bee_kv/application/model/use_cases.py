from bee_kv.application.model.entities import KvDataItem
from bee_kv.application.driven.ports import KvRepository


class KwDataUseCase:
    def __init__(self, repository: KvRepository):
        self._repository: KvRepository = repository

    def save(self, cnf: KvDataItem) -> None:
        self._repository.save(cnf)

    def get(self, key: str) -> KvDataItem:
        return self._repository.get(key)

    def get_all(self) -> dict[str, KvDataItem]:
        return self._repository.get_all()

    def remove(self, key: str) -> None:
        self._repository.remove(key)

    def reset(self) -> None:
        self._repository.reset()
