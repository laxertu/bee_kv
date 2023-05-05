from abc import ABC, abstractmethod

from bee_kv.public.driver.entities import KvDataOperationResponseDto, KvDataOperationRequestDto


class KvDataManagerPort(ABC):

    @abstractmethod
    def handle_save(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        ...

    @abstractmethod
    def handle_get(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        ...

    @abstractmethod
    def handle_get_all(self, request: KvDataOperationRequestDto) -> list[KvDataOperationResponseDto]:
        ...

    @abstractmethod
    def handle_reset(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        ...

    @abstractmethod
    def handle_remove(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        ...
