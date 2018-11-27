"""
A :class:`~allennlp.server.predictors.predictor.Predictor` is
a wrapper for an AllenNLP ``Model``
that makes JSON predictions using JSON inputs. If you
want to serve up a model through the web service
(or using ``allennlp.commands.predict``), you'll need
a ``Predictor`` that wraps it.
"""
import warnings

from srl_model.predictors.predictor import Predictor
from srl_model.predictors.bidaf import BidafPredictor
from srl_model.predictors.constituency_parser import ConstituencyParserPredictor
from srl_model.predictors.coref import CorefPredictor
from srl_model.predictors.decomposable_attention import DecomposableAttentionPredictor
from srl_model.predictors.semantic_role_labeler import SemanticRoleLabelerPredictor
from srl_model.predictors.sentence_tagger import SentenceTaggerPredictor
from srl_model.predictors.simple_seq2seq import SimpleSeq2SeqPredictor
from srl_model.predictors.wikitables_parser import WikiTablesParserPredictor
from srl_model.predictors.nlvr_parser import NlvrParserPredictor

warnings.warn("allennlp.service.predictors.* has been depreciated. "
              "Please use allennlp.predictors.*", FutureWarning)
