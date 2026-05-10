from . import base_types
from .ForeignExchangeTradeInstructionV06 import ForeignExchangeTradeInstructionV06

class FXTR_014_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradInstr"]
		@property
		def FXTradInstr(self):
			return self._FXTradInstr

		@FXTradInstr.setter
		def FXTradInstr(self, value):
			self._FXTradInstr = value if type(value) != base_types.auto else self.make_default("FXTradInstr")

		@FXTradInstr.deleter
		def FXTradInstr(self):
			del self._FXTradInstr
			self._FXTradInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstr', type=ForeignExchangeTradeInstructionV06, min=1, max=1, mutex_group=None, array=False),
		))

