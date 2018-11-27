# pylint: disable=unused-import
import warnings

from srl_model.predictors.coref import CorefPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated. "
              " Please use allennlp.predictors.*", FutureWarning)
