# pylint: disable=unused-import
import warnings

from srl_model.predictors.semantic_role_labeler import SemanticRoleLabelerPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated."
              " Please use allennlp.predictors.*", FutureWarning)
