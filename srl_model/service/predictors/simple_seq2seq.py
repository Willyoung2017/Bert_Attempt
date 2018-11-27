# pylint: disable=unused-import
import warnings

from srl_model.predictors.simple_seq2seq import SimpleSeq2SeqPredictor
warnings.warn("allennlp.service.predictors.* has been deprecated. "
              " Please use allennlp.predictors.*", FutureWarning)
