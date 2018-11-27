"""
A :class:`~allennlp.data.fields.field.Field` is some piece of data instance
that ends up as an array in a model.
"""

from srl_model.data.fields.field import Field
from srl_model.data.fields.array_field import ArrayField
from srl_model.data.fields.index_field import IndexField
from srl_model.data.fields.knowledge_graph_field import KnowledgeGraphField
from srl_model.data.fields.label_field import LabelField
from srl_model.data.fields.multilabel_field import MultiLabelField
from srl_model.data.fields.list_field import ListField
from srl_model.data.fields.metadata_field import MetadataField
from srl_model.data.fields.production_rule_field import ProductionRuleField
from srl_model.data.fields.sequence_field import SequenceField
from srl_model.data.fields.sequence_label_field import SequenceLabelField
from srl_model.data.fields.span_field import SpanField
from srl_model.data.fields.text_field import TextField
