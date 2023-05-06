from typing import List

from bee_core.public.driver.entities import PortRequest, PortResponse
import bee_kv.public.driver.ports as ports
from bee_kv.public.driver.entities import KvDataOperationResponse, KvDataOperationRequest
from bee_kv.application.model.use_cases import KwDataUseCase
from bee_kv.application.model.entities import model_from_dto
from bee_kv.infrastructure.factory import create_repository


class BaseHandler(ports.Port):

    def __init__(self):
        self.implementation = DefaultImplementation()

    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse | list[KvDataOperationResponse]:
        pass

    def validate(self, request: KvDataOperationRequest):
        pass


class Save(BaseHandler):

    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        return self.implementation.handle_save(request)


class Get(BaseHandler):

    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        return self.implementation.handle_get(request)


class GetAll(BaseHandler):

    def handle(self, request: KvDataOperationRequest) -> list[KvDataOperationResponse]:
        return self.implementation.handle_get_all(request)


class Remove(BaseHandler):

    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        return self.implementation.handle_remove(request)


class Reset(BaseHandler):

    def handle(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        return self.implementation.handle_reset(request)


class DefaultImplementation(ports.KvDataManagerPort):

    def handle(self, request: PortRequest) -> PortResponse:
        pass

    def validate(self, request: PortRequest):
        pass

    def handle_save(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        item = model_from_dto(request.payload)
        KwDataUseCase(repository=create_repository(request.context_id)).save(item)
        return KvDataOperationResponse()

    def handle_get(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        key = request.payload.key
        result = KwDataUseCase(repository=create_repository(request.context_id)).get(key)
        return KvDataOperationResponse(payload=result.dto)

    def handle_get_all(self, request: KvDataOperationRequest) -> list[KvDataOperationResponse]:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        return [KvDataOperationResponse(payload=kv.dto) for kv in use_case.get_all().values()]

    def handle_reset(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        use_case.reset()
        return KvDataOperationResponse()

    def handle_remove(self, request: KvDataOperationRequest) -> KvDataOperationResponse:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        use_case.remove(request.payload.key)
        return KvDataOperationResponse()
