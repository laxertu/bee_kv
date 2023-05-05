from dataclasses import dataclass

from bee_kv.public.driver import DEFAULT_CONTEXT_ID


@dataclass
class KvDataOperationResponseDto:
    error: str = None
    key: str = None
    value: object = None


@dataclass
class KvDataOperationRequestDto:
    context_id: str = DEFAULT_CONTEXT_ID
    key: str = None
    value: object = None
