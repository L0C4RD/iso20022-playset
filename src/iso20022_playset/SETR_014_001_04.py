from . import base_types
from .SwitchOrderCancellationRequestV04 import SwitchOrderCancellationRequestV04

class SETR_014_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SwtchOrdrCxlReq"]
		@property
		def SwtchOrdrCxlReq(self):
			return self._SwtchOrdrCxlReq

		@SwtchOrdrCxlReq.setter
		def SwtchOrdrCxlReq(self, value):
			self._SwtchOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("SwtchOrdrCxlReq")

		@SwtchOrdrCxlReq.deleter
		def SwtchOrdrCxlReq(self):
			del self._SwtchOrdrCxlReq
			self._SwtchOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrCxlReq', type=SwitchOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

