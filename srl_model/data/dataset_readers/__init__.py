"""
A :class:`~allennlp.data.dataset_readers.dataset_reader.DatasetReader`
reads a file and converts it to a
:class:`~allennlp.data.dataset.Dataset`.
The various subclasses know how to read specific filetypes
and produce datasets in the formats required by specific models.
"""

# pylint: disable=line-too-long
from srl_model.data.dataset_readers.atis import AtisDatasetReader
from srl_model.data.dataset_readers.ccgbank import CcgBankDatasetReader
from srl_model.data.dataset_readers.conll2003 import Conll2003DatasetReader
from srl_model.data.dataset_readers.ontonotes_ner import OntonotesNamedEntityRecognition
from srl_model.data.dataset_readers.coreference_resolution import ConllCorefReader, WinobiasReader
from srl_model.data.dataset_readers.dataset_reader import DatasetReader
from srl_model.data.dataset_readers.language_modeling import LanguageModelingReader
from srl_model.data.dataset_readers.nlvr import NlvrDatasetReader
from srl_model.data.dataset_readers.penn_tree_bank import PennTreeBankConstituencySpanDatasetReader
from srl_model.data.dataset_readers.reading_comprehension import SquadReader, TriviaQaReader, QuACReader
from srl_model.data.dataset_readers.semantic_role_labeling import SrlReader
from srl_model.data.dataset_readers.seq2seq import Seq2SeqDatasetReader
from srl_model.data.dataset_readers.sequence_tagging import SequenceTaggingDatasetReader
from srl_model.data.dataset_readers.snli import SnliReader
from srl_model.data.dataset_readers.universal_dependencies import UniversalDependenciesDatasetReader
from srl_model.data.dataset_readers.stanford_sentiment_tree_bank import (
        StanfordSentimentTreeBankDatasetReader)
from srl_model.data.dataset_readers.wikitables import WikiTablesDatasetReader
from srl_model.data.dataset_readers.quora_paraphrase import QuoraParaphraseDatasetReader
