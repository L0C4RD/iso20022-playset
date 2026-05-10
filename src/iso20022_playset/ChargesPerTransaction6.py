import base_types
import Max140Text
import ChargesPerTransactionRecord6
import Max35Text
import CashAccount40
import TotalCharges7
import BranchAndFinancialInstitutionIdentification8

class ChargesPerTransaction6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Rcrd", "_TtlChrgsPerTx", "_ChrgsAcctAgtAcct", "_ChrgsId", "_ChrgsAcctAgt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def TtlChrgsPerTx(self):
		return self._TtlChrgsPerTx

	@TtlChrgsPerTx.setter
	def TtlChrgsPerTx(self, value):
		self._TtlChrgsPerTx = value if type(value) != auto else self.make_default("TtlChrgsPerTx")

	@TtlChrgsPerTx.deleter
	def TtlChrgsPerTx(self):
		del self._TtlChrgsPerTx
		self._TtlChrgsPerTx = None

	@property
	def ChrgsAcctAgtAcct(self):
		return self._ChrgsAcctAgtAcct

	@ChrgsAcctAgtAcct.setter
	def ChrgsAcctAgtAcct(self, value):
		self._ChrgsAcctAgtAcct = value if type(value) != auto else self.make_default("ChrgsAcctAgtAcct")

	@ChrgsAcctAgtAcct.deleter
	def ChrgsAcctAgtAcct(self):
		del self._ChrgsAcctAgtAcct
		self._ChrgsAcctAgtAcct = None

	@property
	def ChrgsId(self):
		return self._ChrgsId

	@ChrgsId.setter
	def ChrgsId(self, value):
		self._ChrgsId = value if type(value) != auto else self.make_default("ChrgsId")

	@ChrgsId.deleter
	def ChrgsId(self):
		del self._ChrgsId
		self._ChrgsId = None

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if type(value) != auto else self.make_default("ChrgsAcctAgt")

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=ChargesPerTransactionRecord6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlChrgsPerTx', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

