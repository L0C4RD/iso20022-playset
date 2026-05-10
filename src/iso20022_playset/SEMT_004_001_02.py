from . import base_types
from .CustodyStatementOfHoldingsCancellationV02 import CustodyStatementOfHoldingsCancellationV02

class SEMT_004_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtdyStmtOfHldgsCxlV02"]
		@property
		def CtdyStmtOfHldgsCxlV02(self):
			return self._CtdyStmtOfHldgsCxlV02

		@CtdyStmtOfHldgsCxlV02.setter
		def CtdyStmtOfHldgsCxlV02(self, value):
			self._CtdyStmtOfHldgsCxlV02 = value if type(value) != auto else self.make_default("CtdyStmtOfHldgsCxlV02")

		@CtdyStmtOfHldgsCxlV02.deleter
		def CtdyStmtOfHldgsCxlV02(self):
			del self._CtdyStmtOfHldgsCxlV02
			self._CtdyStmtOfHldgsCxlV02 = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtdyStmtOfHldgsCxlV02', type=CustodyStatementOfHoldingsCancellationV02, min=1, max=1, mutex_group=None, array=False),
		))

