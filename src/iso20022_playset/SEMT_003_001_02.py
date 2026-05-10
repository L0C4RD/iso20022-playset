import base_types
import AccountingStatementOfHoldingsV02

class SEMT_003_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctgStmtOfHldgsV02"]
		@property
		def AcctgStmtOfHldgsV02(self):
			return self._AcctgStmtOfHldgsV02

		@AcctgStmtOfHldgsV02.setter
		def AcctgStmtOfHldgsV02(self, value):
			self._AcctgStmtOfHldgsV02 = value if type(value) != auto else self.make_default("AcctgStmtOfHldgsV02")

		@AcctgStmtOfHldgsV02.deleter
		def AcctgStmtOfHldgsV02(self):
			del self._AcctgStmtOfHldgsV02
			self._AcctgStmtOfHldgsV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctgStmtOfHldgsV02', type=AccountingStatementOfHoldingsV02, min=1, max=1, mutex_group=None, array=False),
		))

