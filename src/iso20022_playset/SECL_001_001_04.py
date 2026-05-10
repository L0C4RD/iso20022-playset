from . import base_types
from .TradeLegNotificationV04 import TradeLegNotificationV04

class SECL_001_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TradLegNtfctn"]
		@property
		def TradLegNtfctn(self):
			return self._TradLegNtfctn

		@TradLegNtfctn.setter
		def TradLegNtfctn(self, value):
			self._TradLegNtfctn = value if type(value) != auto else self.make_default("TradLegNtfctn")

		@TradLegNtfctn.deleter
		def TradLegNtfctn(self):
			del self._TradLegNtfctn
			self._TradLegNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegNtfctn', type=TradeLegNotificationV04, min=1, max=1, mutex_group=None, array=False),
		))

