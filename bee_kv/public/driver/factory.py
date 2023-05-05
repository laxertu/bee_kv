from bee_kv.public.driver.ports import KvDataManagerPort
from bee_kv.public.driver.entities import KvDataOperationRequestDto


def get_dto() -> KvDataOperationRequestDto:
    return KvDataOperationRequestDto()


def get_handler() -> KvDataManagerPort:
    from bee_kv.application.driver.implementations import DefaultImplementation
    return DefaultImplementation()
