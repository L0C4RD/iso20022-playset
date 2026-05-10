import base_types
import TransferInInstructionV09

class SESE_005_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfInInstr"]
		@property
		def TrfInInstr(self):
			return self._TrfInInstr

		@TrfInInstr.setter
		def TrfInInstr(self, value):
			self._TrfInInstr = value if type(value) != auto else self.make_default("TrfInInstr")

		@TrfInInstr.deleter
		def TrfInInstr(self):
			del self._TrfInInstr
			self._TrfInInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInInstr', type=TransferInInstructionV09, min=1, max=1, mutex_group=None, array=False),
		))

