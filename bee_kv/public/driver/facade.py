from bee_kv.public.driver.factory import get_dto, get_handler
from bee_kv.public.driver.entities import KvDataOperationResponseDto, KvDataOperationRequestDto
from bee_kv.public.driver import DEFAULT_CONTEXT_ID


class Facade:

    def __init__(self, context_id: str = DEFAULT_CONTEXT_ID):
        self.context_id = context_id

    def save(self, key: str, value=object) -> KvDataOperationResponseDto:
        dto: KvDataOperationRequestDto = get_dto()
        dto.key = key
        dto.value = value
        dto.context_id = self.context_id

        handler = get_handler()
        return handler.handle_save(dto)

    def get(self, key: str) -> KvDataOperationResponseDto:
        dto: KvDataOperationRequestDto = get_dto()
        dto.key = key
        dto.context_id = self.context_id

        handler = get_handler()
        return handler.handle_get(dto)

    def get_all(self) -> dict[str: KvDataOperationResponseDto]:
        handler = get_handler()
        dto: KvDataOperationRequestDto = get_dto()
        dto.context_id = self.context_id
        return {c.key: c for c in handler.handle_get_all(dto)}

    def reset(self) -> None:
        handler = get_handler()
        dto: KvDataOperationRequestDto = get_dto()
        dto.context_id = self.context_id
        handler.handle_reset(dto)

    def remove(self, key: str) -> None:
        handler = get_handler()
        dto: KvDataOperationRequestDto = get_dto()
        dto.context_id = self.context_id
        dto.key = key
        handler.handle_remove(dto)

