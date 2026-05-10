from . import base_types
import Statement75
import AccountIdentification74
import SupplementaryData1
import Pagination1

class CorporateActionInstructionStatementReport002V13(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StmtGnlDtls", "_Pgntn", "_AcctAndStmtDtls"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def AcctAndStmtDtls(self):
		return self._AcctAndStmtDtls

	@AcctAndStmtDtls.setter
	def AcctAndStmtDtls(self, value):
		self._AcctAndStmtDtls = value if type(value) != auto else self.make_default("AcctAndStmtDtls")

	@AcctAndStmtDtls.deleter
	def AcctAndStmtDtls(self):
		del self._AcctAndStmtDtls
		self._AcctAndStmtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement75, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctAndStmtDtls', type=AccountIdentification74, min=1, max=None, mutex_group=None, array=True),
	))

