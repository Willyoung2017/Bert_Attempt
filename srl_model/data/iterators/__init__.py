"""
The various :class:`~allennlp.data.iterators.data_iterator.DataIterator` subclasses
can be used to iterate over datasets with different batching and padding schemes.
"""

from srl_model.data.iterators.data_iterator import DataIterator
from srl_model.data.iterators.basic_iterator import BasicIterator
from srl_model.data.iterators.bucket_iterator import BucketIterator
from srl_model.data.iterators.epoch_tracking_bucket_iterator import EpochTrackingBucketIterator
