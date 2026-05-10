from . import base_types
from .SecuritiesFinancingModificationInstruction002V08 import SecuritiesFinancingModificationInstruction002V08

class SESE_036_002_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgModInstr"]
		@property
		def SctiesFincgModInstr(self):
			return self._SctiesFincgModInstr

		@SctiesFincgModInstr.setter
		def SctiesFincgModInstr(self, value):
			self._SctiesFincgModInstr = value if type(value) != auto else self.make_default("SctiesFincgModInstr")

		@SctiesFincgModInstr.deleter
		def SctiesFincgModInstr(self):
			del self._SctiesFincgModInstr
			self._SctiesFincgModInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgModInstr', type=SecuritiesFinancingModificationInstruction002V08, min=1, max=1, mutex_group=None, array=False),
		))

