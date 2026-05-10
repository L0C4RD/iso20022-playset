from . import base_types
from ._CustodyStatementOfHoldingsV02 import CustodyStatementOfHoldingsV02

class SEMT_002_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtdyStmtOfHldgsV02"]
		@property
		def CtdyStmtOfHldgsV02(self):
			return self._CtdyStmtOfHldgsV02

		@CtdyStmtOfHldgsV02.setter
		def CtdyStmtOfHldgsV02(self, value):
			self._CtdyStmtOfHldgsV02 = value if type(value) != base_types.auto else self.make_default("CtdyStmtOfHldgsV02")

		@CtdyStmtOfHldgsV02.deleter
		def CtdyStmtOfHldgsV02(self):
			del self._CtdyStmtOfHldgsV02
			self._CtdyStmtOfHldgsV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtdyStmtOfHldgsV02', type=CustodyStatementOfHoldingsV02, min=1, max=1, mutex_group=None, array=False),
		))

