from . import base_types
import ForeignExchangeTradeConfirmationStatusAdviceV02

class FXTR_037_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradConfStsAdvc"]
		@property
		def FXTradConfStsAdvc(self):
			return self._FXTradConfStsAdvc

		@FXTradConfStsAdvc.setter
		def FXTradConfStsAdvc(self, value):
			self._FXTradConfStsAdvc = value if type(value) != auto else self.make_default("FXTradConfStsAdvc")

		@FXTradConfStsAdvc.deleter
		def FXTradConfStsAdvc(self):
			del self._FXTradConfStsAdvc
			self._FXTradConfStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfStsAdvc', type=ForeignExchangeTradeConfirmationStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

