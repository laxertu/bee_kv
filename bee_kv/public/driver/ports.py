from abc import ABC, abstractmethod

from bee_core.public.driver.entities import PortHandler
from bee_kv.public.driver.entities import KvDataOperationResponse, KvDataOperationRequest

CMD_SAVE = "save"
CMD_GET = "get"
CMD_REMOVE = "remove"
CMD_GET_ALL = "get_all"
CMD_RESET = "reset"


class Port(PortHandler, ABC):

    @abstractmethod
    def validate(self, request: KvDataOperationRequest):
        pass


class SavePort(Port):

    @abstractmethod
    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        pass


class GetPort(Port):

    @abstractmethod
    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        pass


class GetAllPort(Port):

    @abstractmethod
    def handle(self, request: KvDataOperationRequest) -> list[KvDataOperationResponse]:
        pass


class RemovePort(Port):

    @abstractmethod
    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        pass


class ResetPort(Port):

    @abstractmethod
    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        pass
