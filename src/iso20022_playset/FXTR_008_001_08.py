from . import base_types
import ForeignExchangeTradeStatusNotificationV08

class FXTR_008_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradStsNtfctn"]
		@property
		def FXTradStsNtfctn(self):
			return self._FXTradStsNtfctn

		@FXTradStsNtfctn.setter
		def FXTradStsNtfctn(self, value):
			self._FXTradStsNtfctn = value if type(value) != auto else self.make_default("FXTradStsNtfctn")

		@FXTradStsNtfctn.deleter
		def FXTradStsNtfctn(self):
			del self._FXTradStsNtfctn
			self._FXTradStsNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradStsNtfctn', type=ForeignExchangeTradeStatusNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))

