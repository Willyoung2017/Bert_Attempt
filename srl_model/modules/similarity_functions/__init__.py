"""
A ``SimilarityFunction`` takes a pair of tensors with the same shape, and computes a similarity
function on the vectors in the last dimension.
"""
from srl_model.modules.similarity_functions.bilinear import BilinearSimilarity
from srl_model.modules.similarity_functions.cosine import CosineSimilarity
from srl_model.modules.similarity_functions.dot_product import DotProductSimilarity
from srl_model.modules.similarity_functions.linear import LinearSimilarity
from srl_model.modules.similarity_functions.multiheaded import MultiHeadedSimilarity
from srl_model.modules.similarity_functions.similarity_function import SimilarityFunction
