# pylint: disable=unused-import
import warnings

from srl_model.predictors.predictor import Predictor, DEFAULT_PREDICTORS
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
