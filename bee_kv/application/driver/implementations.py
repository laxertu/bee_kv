from bee_kv.public.driver.ports import \
    KvDataManagerPort
from bee_kv.public.driver.entities import KvDataOperationResponseDto, KvDataOperationRequestDto
from bee_kv.application.model.use_cases import KwDataUseCase
from bee_kv.application.model.entities import model_from_dto
from bee_kv.infrastructure.factory import create_repository


class DefaultImplementation(KvDataManagerPort):

    def handle_save(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        item = model_from_dto(request)
        KwDataUseCase(repository=create_repository(request.context_id)).save(item)
        return item.dto

    def handle_get(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        return KwDataUseCase(repository=create_repository(request.context_id)).get(request.key).dto

    def handle_get_all(self, request: KvDataOperationRequestDto) -> list[KvDataOperationResponseDto]:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        return [cnf.dto for cnf in use_case.get_all().values()]

    def handle_reset(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        use_case.reset()
        return KvDataOperationResponseDto()

    def handle_remove(self, request: KvDataOperationRequestDto) -> KvDataOperationResponseDto:
        use_case = KwDataUseCase(repository=create_repository(request.context_id))
        use_case.remove(request.key)
        return KvDataOperationResponseDto()
