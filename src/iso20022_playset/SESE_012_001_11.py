from . import base_types
from .PortfolioTransferInstructionV11 import PortfolioTransferInstructionV11

class SESE_012_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfInstr"]
		@property
		def PrtflTrfInstr(self):
			return self._PrtflTrfInstr

		@PrtflTrfInstr.setter
		def PrtflTrfInstr(self, value):
			self._PrtflTrfInstr = value if type(value) != auto else self.make_default("PrtflTrfInstr")

		@PrtflTrfInstr.deleter
		def PrtflTrfInstr(self):
			del self._PrtflTrfInstr
			self._PrtflTrfInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfInstr', type=PortfolioTransferInstructionV11, min=1, max=1, mutex_group=None, array=False),
		))

