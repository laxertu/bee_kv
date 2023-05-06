from dataclasses import dataclass

from bee_core.public.driver.entities import Dto, PortRequest, PortResponse
from bee_kv.public.driver import DEFAULT_CONTEXT_ID


@dataclass
class KvDto(Dto):
    key: str = None
    value: object = None


@dataclass
class KvDataOperationRequest(PortRequest):
    payload: KvDto
    context_id: str = DEFAULT_CONTEXT_ID


@dataclass
class KvDataOperationResponse(PortResponse):
    error: str = None
    payload: KvDto | dict[str, KvDto] = None

