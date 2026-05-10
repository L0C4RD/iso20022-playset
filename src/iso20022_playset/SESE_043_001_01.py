from . import base_types
import PortfolioTransferCompletionV01

class SESE_043_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfCmpltn"]
		@property
		def PrtflTrfCmpltn(self):
			return self._PrtflTrfCmpltn

		@PrtflTrfCmpltn.setter
		def PrtflTrfCmpltn(self, value):
			self._PrtflTrfCmpltn = value if type(value) != auto else self.make_default("PrtflTrfCmpltn")

		@PrtflTrfCmpltn.deleter
		def PrtflTrfCmpltn(self):
			del self._PrtflTrfCmpltn
			self._PrtflTrfCmpltn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfCmpltn', type=PortfolioTransferCompletionV01, min=1, max=1, mutex_group=None, array=False),
		))

