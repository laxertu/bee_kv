import bee_kv.public.driver.ports as ports
from bee_kv.public.driver.factory import get_request, get_handler
from bee_kv.public.driver.entities import KvDataOperationResponse, KvDataOperationRequest
from bee_kv.public.driver import DEFAULT_CONTEXT_ID


class Facade:

    def __init__(self, context_id: str = DEFAULT_CONTEXT_ID):
        self.context_id = context_id

    def save(self, key: str, value=object) -> KvDataOperationResponse:
        request: KvDataOperationRequest = get_request(ports.CMD_SAVE)
        request.payload.key = key
        request.payload.value = value
        request.payload.context_id = self.context_id

        handler = get_handler(ports.CMD_SAVE)
        return handler.handle(request)

    def get(self, key: str) -> KvDataOperationResponse:
        request: KvDataOperationRequest = get_request(ports.CMD_GET)
        request.payload.key = key
        request.payload.context_id = self.context_id

        handler = get_handler(ports.CMD_GET)
        return handler.handle(request)

    def get_all(self) -> dict[str: KvDataOperationResponse]:
        request: KvDataOperationRequest = get_request(ports.CMD_GET_ALL)
        request.payload.context_id = self.context_id

        handler = get_handler(ports.CMD_GET_ALL)
        return {c.payload.key: c.payload for c in handler.handle(request)}

    def reset(self) -> None:
        request: KvDataOperationRequest = get_request(ports.CMD_RESET)
        request.payload.context_id = self.context_id

        handler = get_handler(ports.CMD_RESET)
        handler.handle(request)

    def remove(self, key: str) -> None:
        request: KvDataOperationRequest = get_request(ports.CMD_REMOVE)
        request.payload.context_id = self.context_id
        request.payload.key = key

        handler = get_handler(ports.CMD_REMOVE)
        handler.handle(request)

