from . import base_types
from ._TotalCharges7 import TotalCharges7
from ._Max35Text import Max35Text
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ChargeType3Choice import ChargeType3Choice
from ._ChargesPerTypeRecord6 import ChargesPerTypeRecord6
from ._Max140Text import Max140Text
from ._CashAccount40 import CashAccount40

class ChargesPerType6(base_types._BaseFieldType):

	__slots__ = ["_ChrgsId", "_ChrgsAcctAgt", "_AddtlInf", "_ChrgsAcctAgtAcct", "_TtlChrgsPerChrgTp", "_Rcrd", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if type(value) != base_types.auto else self.make_default("ChrgsAcctAgt")

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = None

	@property
	def ChrgsAcctAgtAcct(self):
		return self._ChrgsAcctAgtAcct

	@ChrgsAcctAgtAcct.setter
	def ChrgsAcctAgtAcct(self, value):
		self._ChrgsAcctAgtAcct = value if type(value) != base_types.auto else self.make_default("ChrgsAcctAgtAcct")

	@ChrgsAcctAgtAcct.deleter
	def ChrgsAcctAgtAcct(self):
		del self._ChrgsAcctAgtAcct
		self._ChrgsAcctAgtAcct = None

	@property
	def ChrgsId(self):
		return self._ChrgsId

	@ChrgsId.setter
	def ChrgsId(self, value):
		self._ChrgsId = value if type(value) != base_types.auto else self.make_default("ChrgsId")

	@ChrgsId.deleter
	def ChrgsId(self):
		del self._ChrgsId
		self._ChrgsId = None

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != base_types.auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TtlChrgsPerChrgTp(self):
		return self._TtlChrgsPerChrgTp

	@TtlChrgsPerChrgTp.setter
	def TtlChrgsPerChrgTp(self, value):
		self._TtlChrgsPerChrgTp = value if type(value) != base_types.auto else self.make_default("TtlChrgsPerChrgTp")

	@TtlChrgsPerChrgTp.deleter
	def TtlChrgsPerChrgTp(self):
		del self._TtlChrgsPerChrgTp
		self._TtlChrgsPerChrgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=ChargesPerTypeRecord6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsPerChrgTp', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
	))

