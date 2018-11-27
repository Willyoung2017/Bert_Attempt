# pylint: disable=no-self-use,invalid-name
from collections import defaultdict

from srl_model.common.testing import AllenNlpTestCase
from srl_model.data import Token
from srl_model.data.token_indexers import SingleIdTokenIndexer


class TestSingleIdTokenIndexer(AllenNlpTestCase):
    def test_count_vocab_items_respects_casing(self):
        indexer = SingleIdTokenIndexer("words")
        counter = defaultdict(lambda: defaultdict(int))
        indexer.count_vocab_items(Token("Hello"), counter)
        indexer.count_vocab_items(Token("hello"), counter)
        assert counter["words"] == {"hello": 1, "Hello": 1}

        indexer = SingleIdTokenIndexer("words", lowercase_tokens=True)
        counter = defaultdict(lambda: defaultdict(int))
        indexer.count_vocab_items(Token("Hello"), counter)
        indexer.count_vocab_items(Token("hello"), counter)
        assert counter["words"] == {"hello": 2}

    def test_as_array_produces_token_sequence(self):
        indexer = SingleIdTokenIndexer("words")
        padded_tokens = indexer.pad_token_sequence({'key': [1, 2, 3, 4, 5]}, {'key': 10}, {})
        assert padded_tokens == {'key': [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]}