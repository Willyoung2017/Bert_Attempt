# pylint: disable=unused-import
import warnings

from srl_model.predictors.wikitables_parser import WikiTablesParserPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
