from . import base_types
from .PortfolioTransferNotification002V07 import PortfolioTransferNotification002V07

class SESE_037_002_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfNtfctn"]
		@property
		def PrtflTrfNtfctn(self):
			return self._PrtflTrfNtfctn

		@PrtflTrfNtfctn.setter
		def PrtflTrfNtfctn(self, value):
			self._PrtflTrfNtfctn = value if type(value) != base_types.auto else self.make_default("PrtflTrfNtfctn")

		@PrtflTrfNtfctn.deleter
		def PrtflTrfNtfctn(self):
			del self._PrtflTrfNtfctn
			self._PrtflTrfNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfNtfctn', type=PortfolioTransferNotification002V07, min=1, max=1, mutex_group=None, array=False),
		))

