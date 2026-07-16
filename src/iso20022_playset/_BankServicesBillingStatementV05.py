# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportHeader6
from . import StatementGroup5

class BankServicesBillingStatementV05(base_types._BaseFieldType):

	__slots__ = ["_BllgStmtGrp", "_RptHdr"]
	@property
	def BllgStmtGrp(self):
		return self._BllgStmtGrp

	@BllgStmtGrp.setter
	def BllgStmtGrp(self, value):
		self._BllgStmtGrp = value if value is not None else base_types.UninitialisedField(self, 'BllgStmtGrp', StatementGroup5, True)

	@BllgStmtGrp.deleter
	def BllgStmtGrp(self):
		del self._BllgStmtGrp
		self._BllgStmtGrp = base_types.UninitialisedField(self, 'BllgStmtGrp', StatementGroup5, True)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', ReportHeader6, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', ReportHeader6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgStmtGrp', type=StatementGroup5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=ReportHeader6, min=1, max=1, mutex_group=None, array=False),
	))