# pylint: disable=no-self-use,invalid-name
from srl_model.common.testing import AllenNlpTestCase
from srl_model.models.archival import load_archive
from srl_model.predictors import Predictor


class TestSimpleSeq2SeqPredictor(AllenNlpTestCase):
    def test_uses_named_inputs(self):
        inputs = {
                "source": "What kind of test succeeded on its first attempt?",
        }

        archive = load_archive(self.FIXTURES_ROOT / 'encoder_decoder' / 'simple_seq2seq' /
                               'serialization' / 'model.tar.gz')
        predictor = Predictor.from_archive(archive, 'simple_seq2seq')

        result = predictor.predict_json(inputs)

        predicted_tokens = result.get("predicted_tokens")
        assert predicted_tokens is not None
        assert isinstance(predicted_tokens, list)
        assert all(isinstance(x, str) for x in predicted_tokens)
