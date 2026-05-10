from . import base_types
from .ForeignExchangeTradeBulkStatusNotificationV06 import ForeignExchangeTradeBulkStatusNotificationV06

class FXTR_030_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradBlkStsNtfctn"]
		@property
		def FXTradBlkStsNtfctn(self):
			return self._FXTradBlkStsNtfctn

		@FXTradBlkStsNtfctn.setter
		def FXTradBlkStsNtfctn(self, value):
			self._FXTradBlkStsNtfctn = value if type(value) != auto else self.make_default("FXTradBlkStsNtfctn")

		@FXTradBlkStsNtfctn.deleter
		def FXTradBlkStsNtfctn(self):
			del self._FXTradBlkStsNtfctn
			self._FXTradBlkStsNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradBlkStsNtfctn', type=ForeignExchangeTradeBulkStatusNotificationV06, min=1, max=1, mutex_group=None, array=False),
		))

