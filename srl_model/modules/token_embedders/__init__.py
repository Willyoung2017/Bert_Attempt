"""
A :class:`~allennlp.modules.token_embedders.token_embedder.TokenEmbedder` is a ``Module`` that
embeds one-hot-encoded tokens as vectors.
"""

from srl_model.modules.token_embedders.token_embedder import TokenEmbedder
from srl_model.modules.token_embedders.embedding import Embedding
from srl_model.modules.token_embedders.token_characters_encoder import TokenCharactersEncoder
from srl_model.modules.token_embedders.elmo_token_embedder import ElmoTokenEmbedder
from srl_model.modules.token_embedders.openai_transformer_embedder import OpenaiTransformerEmbedder
