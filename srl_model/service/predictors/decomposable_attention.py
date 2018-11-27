# pylint: disable=unused-import
import warnings

from srl_model.predictors.decomposable_attention import DecomposableAttentionPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
