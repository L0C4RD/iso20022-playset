from . import base_types
from .ForeignExchangeTradeInstructionCancellationV06 import ForeignExchangeTradeInstructionCancellationV06

class FXTR_016_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradInstrCxl"]
		@property
		def FXTradInstrCxl(self):
			return self._FXTradInstrCxl

		@FXTradInstrCxl.setter
		def FXTradInstrCxl(self, value):
			self._FXTradInstrCxl = value if type(value) != base_types.auto else self.make_default("FXTradInstrCxl")

		@FXTradInstrCxl.deleter
		def FXTradInstrCxl(self):
			del self._FXTradInstrCxl
			self._FXTradInstrCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstrCxl', type=ForeignExchangeTradeInstructionCancellationV06, min=1, max=1, mutex_group=None, array=False),
		))

