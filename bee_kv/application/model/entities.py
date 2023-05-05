from dataclasses import dataclass

from bee_kv.public.driver.entities import KvDataOperationResponseDto, KvDataOperationRequestDto


@dataclass()
class KvDataItem:
    key: str = None
    value: object = None

    @property
    def dto(self) -> KvDataOperationResponseDto:
        return KvDataOperationResponseDto(key=self.key, value=self.value)


def model_from_dto(dto: KvDataOperationRequestDto) -> KvDataItem:
    return KvDataItem(key=dto.key, value=dto.value)

