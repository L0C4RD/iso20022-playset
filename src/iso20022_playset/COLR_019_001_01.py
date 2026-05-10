from . import base_types
from .TripartyCollateralTransactionInstructionV01 import TripartyCollateralTransactionInstructionV01

class COLR_019_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrptyCollTxInstr"]
		@property
		def TrptyCollTxInstr(self):
			return self._TrptyCollTxInstr

		@TrptyCollTxInstr.setter
		def TrptyCollTxInstr(self, value):
			self._TrptyCollTxInstr = value if type(value) != base_types.auto else self.make_default("TrptyCollTxInstr")

		@TrptyCollTxInstr.deleter
		def TrptyCollTxInstr(self):
			del self._TrptyCollTxInstr
			self._TrptyCollTxInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstr', type=TripartyCollateralTransactionInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))

