from . import base_types
from .DatePeriod5 import DatePeriod5
from .CashAccount40 import CashAccount40
from .BranchAndFinancialInstitutionIdentification6 import BranchAndFinancialInstitutionIdentification6
from .PercentageRate import PercentageRate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Max140Text import Max140Text

class AdjustmentCompensation1(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_CompstnAgt", "_IntrstRate", "_InitlAmt", "_CompstnAcct", "_Rsn", "_AmtDue", "_DueChrgs"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def CompstnAgt(self):
		return self._CompstnAgt

	@CompstnAgt.setter
	def CompstnAgt(self, value):
		self._CompstnAgt = value if type(value) != base_types.auto else self.make_default("CompstnAgt")

	@CompstnAgt.deleter
	def CompstnAgt(self):
		del self._CompstnAgt
		self._CompstnAgt = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if type(value) != base_types.auto else self.make_default("InitlAmt")

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = None

	@property
	def CompstnAcct(self):
		return self._CompstnAcct

	@CompstnAcct.setter
	def CompstnAcct(self, value):
		self._CompstnAcct = value if type(value) != base_types.auto else self.make_default("CompstnAcct")

	@CompstnAcct.deleter
	def CompstnAcct(self):
		del self._CompstnAcct
		self._CompstnAcct = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def AmtDue(self):
		return self._AmtDue

	@AmtDue.setter
	def AmtDue(self, value):
		self._AmtDue = value if type(value) != base_types.auto else self.make_default("AmtDue")

	@AmtDue.deleter
	def AmtDue(self):
		del self._AmtDue
		self._AmtDue = None

	@property
	def DueChrgs(self):
		return self._DueChrgs

	@DueChrgs.setter
	def DueChrgs(self, value):
		self._DueChrgs = value if type(value) != base_types.auto else self.make_default("DueChrgs")

	@DueChrgs.deleter
	def DueChrgs(self):
		del self._DueChrgs
		self._DueChrgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=DatePeriod5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDue', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueChrgs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

