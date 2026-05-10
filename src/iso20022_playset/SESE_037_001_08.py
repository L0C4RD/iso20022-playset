from . import base_types
from .PortfolioTransferNotificationV08 import PortfolioTransferNotificationV08

class SESE_037_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfNtfctn"]
		@property
		def PrtflTrfNtfctn(self):
			return self._PrtflTrfNtfctn

		@PrtflTrfNtfctn.setter
		def PrtflTrfNtfctn(self, value):
			self._PrtflTrfNtfctn = value if type(value) != auto else self.make_default("PrtflTrfNtfctn")

		@PrtflTrfNtfctn.deleter
		def PrtflTrfNtfctn(self):
			del self._PrtflTrfNtfctn
			self._PrtflTrfNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfNtfctn', type=PortfolioTransferNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))

