import base_types
import PortfolioTransferCancellationRequestV09

class SESE_014_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfCxlReq"]
		@property
		def PrtflTrfCxlReq(self):
			return self._PrtflTrfCxlReq

		@PrtflTrfCxlReq.setter
		def PrtflTrfCxlReq(self, value):
			self._PrtflTrfCxlReq = value if type(value) != auto else self.make_default("PrtflTrfCxlReq")

		@PrtflTrfCxlReq.deleter
		def PrtflTrfCxlReq(self):
			del self._PrtflTrfCxlReq
			self._PrtflTrfCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfCxlReq', type=PortfolioTransferCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))

