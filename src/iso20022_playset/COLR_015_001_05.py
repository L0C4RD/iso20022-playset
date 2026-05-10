from . import base_types
import InterestPaymentStatementV05

class COLR_015_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntrstPmtStmt"]
		@property
		def IntrstPmtStmt(self):
			return self._IntrstPmtStmt

		@IntrstPmtStmt.setter
		def IntrstPmtStmt(self, value):
			self._IntrstPmtStmt = value if type(value) != auto else self.make_default("IntrstPmtStmt")

		@IntrstPmtStmt.deleter
		def IntrstPmtStmt(self):
			del self._IntrstPmtStmt
			self._IntrstPmtStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtStmt', type=InterestPaymentStatementV05, min=1, max=1, mutex_group=None, array=False),
		))

