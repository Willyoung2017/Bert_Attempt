"""
Custom PyTorch
`Module <http://pytorch.org/docs/master/nn.html#torch.nn.Module>`_ s
that are used as components in AllenNLP
:class:`~allennlp.models.model.Model` s.
"""

from srl_model.modules.conditional_random_field import ConditionalRandomField
from srl_model.modules.elmo import Elmo
from srl_model.modules.feedforward import FeedForward
from srl_model.modules.highway import Highway
from srl_model.modules.layer_norm import LayerNorm
from srl_model.modules.maxout import Maxout
from srl_model.modules.scalar_mix import ScalarMix
from srl_model.modules.seq2seq_encoders import Seq2SeqEncoder
from srl_model.modules.seq2vec_encoders import Seq2VecEncoder
from srl_model.modules.similarity_functions import SimilarityFunction
from srl_model.modules.span_pruner import SpanPruner
from srl_model.modules.text_field_embedders import TextFieldEmbedder
from srl_model.modules.time_distributed import TimeDistributed
from srl_model.modules.token_embedders import TokenEmbedder, Embedding
from srl_model.modules.matrix_attention import MatrixAttention
from srl_model.modules.attention import Attention
from srl_model.modules.input_variational_dropout import InputVariationalDropout
from srl_model.modules.bimpm_matching import BiMpmMatching
