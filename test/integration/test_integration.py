from unittest import TestCase
import pytest

from bee_kv.application.model.entities import KvDataItem
from bee_kv.application.driven.ports import ItemNotfoundException

def create_kv(key: str, value: object):
    return KvDataItem(key=key, value=value)


FIXTURES: list[KvDataItem] = [
    create_kv(key="a", value={6: 7}),
    create_kv(key="b", value={"x": "y"})
]


class KvRepositoryDefaultImplementationTestCase(TestCase):

    def setUp(self) -> None:
        from bee_kv.application.driven.ports import KvRepository
        from bee_kv.infrastructure.factory import create_repository

        self._context = "test_integration"
        self.sut: KvRepository = create_repository(self._context)
        self.sut.reset()

    def _refill_scenario(self):
        self.sut.reset()
        for kv in FIXTURES:
            self.sut.save(kv)

    def test_empty(self):
        self.assertEqual(self.sut.get_all(), {})

    def test_save(self):
        self._refill_scenario()
        self.assertEqual(len(self.sut.get_all()), len(FIXTURES))

    def test_objects(self):
        self._refill_scenario()
        for i in range(0, len(FIXTURES)):
            kv = FIXTURES[i]
            with self.subTest(i=i, msg=f"Testing key {kv.key}"):
                get_result = self.sut.get(kv.key)
                self.assertEqual(kv.key, get_result.key)
                self.assertEqual(kv.value, get_result.value)

    def test_remove(self):
        self.sut.save(FIXTURES[0])
        self.sut.save(FIXTURES[1])
        self.assertEqual(len(self.sut.get_all()), 2)
        self.sut.remove(FIXTURES[0].key)
        self.assertEqual(len(self.sut.get_all()), 1)

        with pytest.raises(ItemNotfoundException):
            self.sut.remove("unexistent")

    def test_get_unexistent(self):
        with pytest.raises(ItemNotfoundException):
            self.sut.get("unexistent")


class TestFacade(TestCase):

    def setUp(self) -> None:
        from bee_kv.public.driver.facade import Facade
        self.sut = Facade("default")
        self.sut.reset()

    def test_empty(self):
        self.assertEqual(self.sut.get_all(), {})

    def test_fixtures(self):

        for kv in FIXTURES:
            self.sut.save(kv.key, kv.value)

        for kv in FIXTURES:
            get_result = self.sut.get(kv.key)
            self.assertEqual(kv.key, get_result.key)
            self.assertEqual(kv.value, get_result.value)

        self.assertEqual(len(self.sut.get_all()), len(FIXTURES))
        self.sut.reset()
        self.assertEqual(self.sut.get_all(), {})

        for kv in FIXTURES:
            self.sut.save(kv.key, kv.value)

        self.sut.remove(FIXTURES[0].key)
        self.assertEqual(len(self.sut.get_all()), len(FIXTURES) - 1)

    def test_unexistent_key(self):

        with pytest.raises(ItemNotfoundException):
            self.sut.get("unexistent")

        with pytest.raises(ItemNotfoundException):
            self.sut.remove("unexistent")
