import bee_kv.public.driver.ports as ports
from bee_kv.public.driver.factory import get_request, get_handler, get_cmd_handler
from bee_kv.public.driver.entities import KvDataOperationResponse, KvDataOperationRequest
from bee_kv.public.driver import DEFAULT_CONTEXT_ID
from bee_kv.application.driver.implementations import BaseHandler

class Facade:

    def __init__(self, context_id: str = DEFAULT_CONTEXT_ID):
        self.context_id = context_id

    def save(self, key: str, value=object) -> KvDataOperationResponse:
        request: KvDataOperationRequest = get_request(ports.CMD_SAVE)
        request.payload.key = key
        request.payload.value = value
        request.payload.context_id = self.context_id

        handler = get_cmd_handler(ports.CMD_SAVE)
        return handler.handle(request)

    def get(self, key: str) -> KvDataOperationResponse:
        request: KvDataOperationRequest = get_request(ports.CMD_GET)
        request.payload.key = key
        request.payload.context_id = self.context_id

        handler = get_cmd_handler(ports.CMD_GET)
        return handler.handle(request)

    def get_all(self) -> dict[str: KvDataOperationResponse]:
        handler = get_cmd_handler(ports.CMD_GET_ALL)
        dto: KvDataOperationRequest = get_request(ports.CMD_GET_ALL)
        dto.context_id = self.context_id
        return {c.key: c.payload for c in handler.handle(dto)}

    def reset(self) -> None:
        handler = get_cmd_handler(ports.CMD_RESET)
        dto: KvDataOperationRequest = get_request(ports.CMD_RESET)
        dto.context_id = self.context_id
        handler.handle(dto)

    def remove(self, key: str) -> None:
        handler = get_cmd_handler(ports.CMD_REMOVE)
        dto: KvDataOperationRequest = get_request(ports.CMD_REMOVE)
        dto.context_id = self.context_id
        dto.key = key
        handler.handle(dto)

