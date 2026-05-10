import base_types
import SecuritiesFinancingInstructionV12

class SESE_033_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgInstr"]
		@property
		def SctiesFincgInstr(self):
			return self._SctiesFincgInstr

		@SctiesFincgInstr.setter
		def SctiesFincgInstr(self, value):
			self._SctiesFincgInstr = value if type(value) != auto else self.make_default("SctiesFincgInstr")

		@SctiesFincgInstr.deleter
		def SctiesFincgInstr(self):
			del self._SctiesFincgInstr
			self._SctiesFincgInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgInstr', type=SecuritiesFinancingInstructionV12, min=1, max=1, mutex_group=None, array=False),
		))

