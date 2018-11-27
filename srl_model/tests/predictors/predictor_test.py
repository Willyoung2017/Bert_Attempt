# pylint: disable=no-self-use,invalid-name
from srl_model.common.testing import AllenNlpTestCase
from srl_model.models.archival import load_archive
from srl_model.predictors import Predictor

class TestPredictor(AllenNlpTestCase):
    def test_from_archive_does_not_consume_params(self):
        archive = load_archive(self.FIXTURES_ROOT / 'bidaf' / 'serialization' / 'model.tar.gz')
        Predictor.from_archive(archive, 'machine-comprehension')

        # If it consumes the params, this will raise an exception
        Predictor.from_archive(archive, 'machine-comprehension')
