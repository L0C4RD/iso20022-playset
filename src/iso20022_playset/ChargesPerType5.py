from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .ChargeType3Choice import ChargeType3Choice
from .ChargesPerTypeRecord5 import ChargesPerTypeRecord5
from .CashAccount40 import CashAccount40
from .TotalCharges7 import TotalCharges7
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class ChargesPerType5(base_types._BaseFieldType):

	__slots__ = ["_ChrgsAcctOwnr", "_TtlChrgsPerChrgTp", "_AddtlInf", "_ChrgsAcct", "_Tp", "_ChrgsId", "_Rcrd"]
	@property
	def ChrgsAcctOwnr(self):
		return self._ChrgsAcctOwnr

	@ChrgsAcctOwnr.setter
	def ChrgsAcctOwnr(self, value):
		self._ChrgsAcctOwnr = value if type(value) != auto else self.make_default("ChrgsAcctOwnr")

	@ChrgsAcctOwnr.deleter
	def ChrgsAcctOwnr(self):
		del self._ChrgsAcctOwnr
		self._ChrgsAcctOwnr = None

	@property
	def TtlChrgsPerChrgTp(self):
		return self._TtlChrgsPerChrgTp

	@TtlChrgsPerChrgTp.setter
	def TtlChrgsPerChrgTp(self, value):
		self._TtlChrgsPerChrgTp = value if type(value) != auto else self.make_default("TtlChrgsPerChrgTp")

	@TtlChrgsPerChrgTp.deleter
	def TtlChrgsPerChrgTp(self):
		del self._TtlChrgsPerChrgTp
		self._TtlChrgsPerChrgTp = None

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
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if type(value) != auto else self.make_default("ChrgsAcct")

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsAcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsPerChrgTp', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=ChargesPerTypeRecord5, min=1, max=None, mutex_group=None, array=True),
	))

