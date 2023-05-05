from bee_kv.application.driven.ports import KvRepository
from bee_kv.infrastructure.repository import DictToFileRepository


def create_repository(context_id: str) -> KvRepository:
    return DictToFileRepository(f"/tmp/{context_id}")
