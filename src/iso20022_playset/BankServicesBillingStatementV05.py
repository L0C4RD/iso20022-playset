from . import base_types
import StatementGroup5
import ReportHeader6

class BankServicesBillingStatementV05(base_types._BaseFieldType):

	__slots__ = ["_BllgStmtGrp", "_RptHdr"]
	@property
	def BllgStmtGrp(self):
		return self._BllgStmtGrp

	@BllgStmtGrp.setter
	def BllgStmtGrp(self, value):
		self._BllgStmtGrp = value if type(value) != auto else self.make_default("BllgStmtGrp")

	@BllgStmtGrp.deleter
	def BllgStmtGrp(self):
		del self._BllgStmtGrp
		self._BllgStmtGrp = None

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgStmtGrp', type=StatementGroup5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=ReportHeader6, min=1, max=1, mutex_group=None, array=False),
	))

