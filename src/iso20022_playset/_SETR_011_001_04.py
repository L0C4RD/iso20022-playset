from . import base_types
from ._SubscriptionOrderCancellationRequestV04 import SubscriptionOrderCancellationRequestV04

class SETR_011_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptOrdrCxlReq"]
		@property
		def SbcptOrdrCxlReq(self):
			return self._SbcptOrdrCxlReq

		@SbcptOrdrCxlReq.setter
		def SbcptOrdrCxlReq(self, value):
			self._SbcptOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("SbcptOrdrCxlReq")

		@SbcptOrdrCxlReq.deleter
		def SbcptOrdrCxlReq(self):
			del self._SbcptOrdrCxlReq
			self._SbcptOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrCxlReq', type=SubscriptionOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

