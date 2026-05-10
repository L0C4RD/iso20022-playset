from . import base_types
import ForeignExchangeTradeWithdrawalNotificationV03

class FXTR_013_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradWdrwlNtfctn"]
		@property
		def FXTradWdrwlNtfctn(self):
			return self._FXTradWdrwlNtfctn

		@FXTradWdrwlNtfctn.setter
		def FXTradWdrwlNtfctn(self, value):
			self._FXTradWdrwlNtfctn = value if type(value) != auto else self.make_default("FXTradWdrwlNtfctn")

		@FXTradWdrwlNtfctn.deleter
		def FXTradWdrwlNtfctn(self):
			del self._FXTradWdrwlNtfctn
			self._FXTradWdrwlNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradWdrwlNtfctn', type=ForeignExchangeTradeWithdrawalNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

