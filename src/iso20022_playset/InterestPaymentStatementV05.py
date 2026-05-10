import base_types
import Max35Text
import Obligation9
import Agreement4
import Statement85
import InterestStatement5
import Pagination1
import SupplementaryData1

class InterestPaymentStatementV05(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_SplmtryData", "_Agrmt", "_Pgntn", "_Oblgtn", "_StmtParams", "_IntrstStmt"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

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
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if type(value) != auto else self.make_default("Agrmt")

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = None

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
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if type(value) != auto else self.make_default("Oblgtn")

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = None

	@property
	def StmtParams(self):
		return self._StmtParams

	@StmtParams.setter
	def StmtParams(self, value):
		self._StmtParams = value if type(value) != auto else self.make_default("StmtParams")

	@StmtParams.deleter
	def StmtParams(self):
		del self._StmtParams
		self._StmtParams = None

	@property
	def IntrstStmt(self):
		return self._IntrstStmt

	@IntrstStmt.setter
	def IntrstStmt(self, value):
		self._IntrstStmt = value if type(value) != auto else self.make_default("IntrstStmt")

	@IntrstStmt.deleter
	def IntrstStmt(self):
		del self._IntrstStmt
		self._IntrstStmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtParams', type=Statement85, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstStmt', type=InterestStatement5, min=1, max=1, mutex_group=None, array=False),
	))

