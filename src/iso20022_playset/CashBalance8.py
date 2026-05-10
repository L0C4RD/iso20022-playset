from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .CashAvailability1 import CashAvailability1
from .CreditDebitCode import CreditDebitCode
from .BalanceType13 import BalanceType13
from .CreditLine3 import CreditLine3

class CashBalance8(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Dt", "_Avlbty", "_Tp", "_CdtDbtInd", "_CdtLine"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Avlbty(self):
		return self._Avlbty

	@Avlbty.setter
	def Avlbty(self, value):
		self._Avlbty = value if type(value) != auto else self.make_default("Avlbty")

	@Avlbty.deleter
	def Avlbty(self):
		del self._Avlbty
		self._Avlbty = None

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
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def CdtLine(self):
		return self._CdtLine

	@CdtLine.setter
	def CdtLine(self, value):
		self._CdtLine = value if type(value) != auto else self.make_default("CdtLine")

	@CdtLine.deleter
	def CdtLine(self):
		del self._CdtLine
		self._CdtLine = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=BalanceType13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtLine', type=CreditLine3, min=0, max=None, mutex_group=None, array=True),
	))

