"""
These submodules contain the classes for AllenNLP models,
all of which are subclasses of :class:`~allennlp.models.model.Model`.
"""

from srl_model.models.model import Model
from srl_model.models.archival import archive_model, load_archive, Archive
from srl_model.models.biattentive_classification_network import BiattentiveClassificationNetwork
from srl_model.models.constituency_parser import SpanConstituencyParser
from srl_model.models.biaffine_dependency_parser import BiaffineDependencyParser
from srl_model.models.coreference_resolution.coref import CoreferenceResolver
from srl_model.models.crf_tagger import CrfTagger
from srl_model.models.decomposable_attention import DecomposableAttention
from srl_model.models.encoder_decoders.simple_seq2seq import SimpleSeq2Seq
from srl_model.models.reading_comprehension.bidaf import BidirectionalAttentionFlow
from srl_model.models.semantic_parsing.nlvr.nlvr_coverage_semantic_parser import NlvrCoverageSemanticParser
from srl_model.models.semantic_parsing.nlvr.nlvr_direct_semantic_parser import NlvrDirectSemanticParser
from srl_model.models.semantic_parsing.wikitables.wikitables_mml_semantic_parser import WikiTablesMmlSemanticParser
from srl_model.models.semantic_parsing.wikitables.wikitables_erm_semantic_parser import WikiTablesErmSemanticParser
from srl_model.models.semantic_role_labeler import SemanticRoleLabeler
from srl_model.models.simple_tagger import SimpleTagger
from srl_model.models.esim import ESIM
from srl_model.models.bimpm import BiMpm
