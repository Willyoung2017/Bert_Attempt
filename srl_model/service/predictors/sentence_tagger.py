# pylint: disable=unused-import
import warnings

from srl_model.predictors.sentence_tagger import SentenceTaggerPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
