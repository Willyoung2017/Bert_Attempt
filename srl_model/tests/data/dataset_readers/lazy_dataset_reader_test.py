# pylint: disable=no-self-use,invalid-name,abstract-method
from typing import Iterable, List

from srl_model.data.fields import TextField
from srl_model.data.instance import Instance
from srl_model.data.dataset_readers import DatasetReader
from srl_model.data.token_indexers import SingleIdTokenIndexer
from srl_model.data.tokenizers import Token
from srl_model.common.testing import AllenNlpTestCase
from srl_model.common.util import ensure_list


class LazyDatasetReader(DatasetReader):
    def __init__(self, instances: List[Instance], lazy: bool) -> None:
        super().__init__()
        self.lazy = lazy
        self._instances = instances
        self.num_reads = 0

    def _read(self, _: str) -> Iterable[Instance]:
        self.num_reads += 1
        return (instance for instance in self._instances)


class TestLazyDatasetReader(AllenNlpTestCase):
    def setUp(self):
        super().setUp()
        token_indexer = {"tokens": SingleIdTokenIndexer()}

        field1 = TextField([Token(t) for t in ["this", "is", "a", "sentence", "."]],
                           token_indexer)
        field2 = TextField([Token(t) for t in ["this", "is", "a", "different", "sentence", "."]],
                           token_indexer)
        field3 = TextField([Token(t) for t in ["here", "is", "a", "sentence", "."]],
                           token_indexer)
        field4 = TextField([Token(t) for t in ["this", "is", "short"]],
                           token_indexer)
        self.instances = [Instance({"text1": field1, "text2": field2}),
                          Instance({"text1": field3, "text2": field4})]

    def test_lazy(self):
        reader = LazyDatasetReader(self.instances, lazy=True)
        assert reader.num_reads == 0

        instances = reader.read('path/to/file')

        for _ in range(10):
            _instances = (i for i in instances)
            assert ensure_list(_instances) == self.instances

        assert reader.num_reads == 10

    def test_non_lazy(self):
        reader = LazyDatasetReader(self.instances, lazy=False)
        assert reader.num_reads == 0

        instances = reader.read('path/to/file')

        for _ in range(10):
            _instances = (i for i in instances)
            assert ensure_list(_instances) == self.instances

        assert reader.num_reads == 1
