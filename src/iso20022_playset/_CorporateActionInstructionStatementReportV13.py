# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification68
from . import Pagination1
from . import Statement72
from . import SupplementaryData1

class CorporateActionInstructionStatementReportV13(base_types._BaseFieldType):

	__slots__ = ["_AcctAndStmtDtls", "_Pgntn", "_SplmtryData", "_StmtGnlDtls"]
	@property
	def AcctAndStmtDtls(self):
		return self._AcctAndStmtDtls

	@AcctAndStmtDtls.setter
	def AcctAndStmtDtls(self, value):
		self._AcctAndStmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctAndStmtDtls', AccountIdentification68, True)

	@AcctAndStmtDtls.deleter
	def AcctAndStmtDtls(self):
		del self._AcctAndStmtDtls
		self._AcctAndStmtDtls = base_types.UninitialisedField(self, 'AcctAndStmtDtls', AccountIdentification68, True)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement72, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement72, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctAndStmtDtls', type=AccountIdentification68, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement72, min=1, max=1, mutex_group=None, array=False),
	))