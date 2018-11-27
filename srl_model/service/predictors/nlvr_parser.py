# pylint: disable=unused-import
import warnings

from srl_model.predictors.nlvr_parser import NlvrParserPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
