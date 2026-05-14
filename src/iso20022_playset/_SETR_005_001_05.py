from . import base_types
from ._RedemptionOrderCancellationRequestV05 import RedemptionOrderCancellationRequestV05

class SETR_005_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedOrdrCxlReq"]
		@property
		def RedOrdrCxlReq(self):
			return self._RedOrdrCxlReq

		@RedOrdrCxlReq.setter
		def RedOrdrCxlReq(self, value):
			self._RedOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("RedOrdrCxlReq")

		@RedOrdrCxlReq.deleter
		def RedOrdrCxlReq(self):
			del self._RedOrdrCxlReq
			self._RedOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrCxlReq', type=RedemptionOrderCancellationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

