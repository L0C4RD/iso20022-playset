from . import base_types
from ._SubscriptionBulkOrderCancellationRequestV04 import SubscriptionBulkOrderCancellationRequestV04

class SETR_008_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptBlkOrdrCxlReq"]
		@property
		def SbcptBlkOrdrCxlReq(self):
			return self._SbcptBlkOrdrCxlReq

		@SbcptBlkOrdrCxlReq.setter
		def SbcptBlkOrdrCxlReq(self, value):
			self._SbcptBlkOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("SbcptBlkOrdrCxlReq")

		@SbcptBlkOrdrCxlReq.deleter
		def SbcptBlkOrdrCxlReq(self):
			del self._SbcptBlkOrdrCxlReq
			self._SbcptBlkOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrCxlReq', type=SubscriptionBulkOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

