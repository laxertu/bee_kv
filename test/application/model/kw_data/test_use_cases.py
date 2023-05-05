from unittest import TestCase
from unittest.mock import Mock, MagicMock

import pytest

import bee_kv.infrastructure.repository
from bee_kv.application.model.entities import KvDataItem
from bee_kv.application.driven.ports import KvRepository
from bee_kv.application.model.use_cases import KwDataUseCase


class KvTestCase(TestCase):
    def setUp(self) -> None:
        self._repository = MagicMock(KvRepository)
        self._sut = KwDataUseCase(self._repository)

    def test_save(self):
        self._sut.save(KvDataItem(key="conf", value={}))
        self._repository.save.assert_called_once()

    def test_get_all(self):
        self._sut.get_all()
        self._repository.get_all.assert_called_once()

    def test_get_exists(self):
        self._repository.get = Mock(return_value=KvDataItem(key="1", value={"a": "b"}))

        obtained = self._sut.get(key="1")
        self.assertEqual(obtained.value, {"a": "b"})

    def test_get_not_exists(self):
        self._repository.get = Mock(side_effect=bee_kv.application.driven.ports.ItemNotfoundException())
        with pytest.raises(bee_kv.application.driven.ports.ItemNotfoundException):
            _ = self._sut.get(key="2")

    def test_remove_not_exists(self):
        self._repository.remove = Mock(side_effect=bee_kv.application.driven.ports.ItemNotfoundException)

        with pytest.raises(bee_kv.application.driven.ports.ItemNotfoundException):
            self._sut.remove(key="2")

    def test_remove_exists(self):
        self._repository.remove = Mock()
        self._sut.remove(key="test")
        self._repository.remove.assert_called_once()

    def test_reset(self):
        self._repository.reset = Mock()
        self._sut.reset()
        self._repository.reset.assert_called_once()
