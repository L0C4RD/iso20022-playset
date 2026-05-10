from . import base_types
from .AccountingStatementOfHoldingsCancellationV02 import AccountingStatementOfHoldingsCancellationV02

class SEMT_005_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctgStmtOfHldgsCxlV02"]
		@property
		def AcctgStmtOfHldgsCxlV02(self):
			return self._AcctgStmtOfHldgsCxlV02

		@AcctgStmtOfHldgsCxlV02.setter
		def AcctgStmtOfHldgsCxlV02(self, value):
			self._AcctgStmtOfHldgsCxlV02 = value if type(value) != base_types.auto else self.make_default("AcctgStmtOfHldgsCxlV02")

		@AcctgStmtOfHldgsCxlV02.deleter
		def AcctgStmtOfHldgsCxlV02(self):
			del self._AcctgStmtOfHldgsCxlV02
			self._AcctgStmtOfHldgsCxlV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctgStmtOfHldgsCxlV02', type=AccountingStatementOfHoldingsCancellationV02, min=1, max=1, mutex_group=None, array=False),
		))

