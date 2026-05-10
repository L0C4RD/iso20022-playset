from . import base_types
import TransferInCancellationRequestV09

class SESE_006_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfInCxlReq"]
		@property
		def TrfInCxlReq(self):
			return self._TrfInCxlReq

		@TrfInCxlReq.setter
		def TrfInCxlReq(self, value):
			self._TrfInCxlReq = value if type(value) != auto else self.make_default("TrfInCxlReq")

		@TrfInCxlReq.deleter
		def TrfInCxlReq(self):
			del self._TrfInCxlReq
			self._TrfInCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInCxlReq', type=TransferInCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))

