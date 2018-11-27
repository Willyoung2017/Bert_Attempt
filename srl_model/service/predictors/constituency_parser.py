# pylint: disable=unused-import
import warnings

from srl_model.predictors.constituency_parser import ConstituencyParserPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated. "
              "Please use allennlp.predictors.*", FutureWarning)
