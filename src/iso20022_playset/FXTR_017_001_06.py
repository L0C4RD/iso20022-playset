from . import base_types
import ForeignExchangeTradeStatusAndDetailsNotificationV06

class FXTR_017_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradStsAndDtlsNtfctn"]
		@property
		def FXTradStsAndDtlsNtfctn(self):
			return self._FXTradStsAndDtlsNtfctn

		@FXTradStsAndDtlsNtfctn.setter
		def FXTradStsAndDtlsNtfctn(self, value):
			self._FXTradStsAndDtlsNtfctn = value if type(value) != auto else self.make_default("FXTradStsAndDtlsNtfctn")

		@FXTradStsAndDtlsNtfctn.deleter
		def FXTradStsAndDtlsNtfctn(self):
			del self._FXTradStsAndDtlsNtfctn
			self._FXTradStsAndDtlsNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradStsAndDtlsNtfctn', type=ForeignExchangeTradeStatusAndDetailsNotificationV06, min=1, max=1, mutex_group=None, array=False),
		))

