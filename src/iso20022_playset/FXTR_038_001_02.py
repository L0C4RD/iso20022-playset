from . import base_types
from .ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02 import ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02

class FXTR_038_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradConfStsAdvcAck"]
		@property
		def FXTradConfStsAdvcAck(self):
			return self._FXTradConfStsAdvcAck

		@FXTradConfStsAdvcAck.setter
		def FXTradConfStsAdvcAck(self, value):
			self._FXTradConfStsAdvcAck = value if type(value) != base_types.auto else self.make_default("FXTradConfStsAdvcAck")

		@FXTradConfStsAdvcAck.deleter
		def FXTradConfStsAdvcAck(self):
			del self._FXTradConfStsAdvcAck
			self._FXTradConfStsAdvcAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfStsAdvcAck', type=ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))

