import bee_kv.public.driver.ports
from bee_kv.application.model.entities import model_from_dto, KvDataItem, KvDto
from bee_kv.public.driver.factory import get_request


def test_dto_to_model():
    dto = KvDto(key='a', value=1)

    model = model_from_dto(dto)
    assert model.key == dto.key
    assert model.value == dto.value


def test_model_to_dto():
    model = KvDataItem(key="a", value=1)
    dto = model.dto

    assert model.key == dto.key
    assert model.value == dto.value
