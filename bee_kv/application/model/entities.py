from dataclasses import dataclass

from bee_kv.public.driver.entities import KvDataOperationRequestDto, KvDataOperationResponseDto, KvDto


@dataclass()
class KvDataItem:
    key: str = None
    value: object = None

    @property
    def dto(self) -> KvDto:
        return KvDto(key=self.key, value=self.value)


def model_from_dto(dto: KvDto) -> KvDataItem:
    return KvDataItem(key=dto.key, value=dto.value)

