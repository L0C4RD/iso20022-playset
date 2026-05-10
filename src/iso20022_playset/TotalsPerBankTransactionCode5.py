from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .DecimalNumber import DecimalNumber
from .BankTransactionCodeStructure4 import BankTransactionCodeStructure4
from .NumberAndSumOfTransactions1 import NumberAndSumOfTransactions1
from .Max15NumericText import Max15NumericText
from .AmountAndDirection35 import AmountAndDirection35
from .CashAvailability1 import CashAvailability1
from .TrueFalseIndicator import TrueFalseIndicator

class TotalsPerBankTransactionCode5(base_types._BaseFieldType):

	__slots__ = ["_CdtNtries", "_FcstInd", "_BkTxCd", "_TtlNetNtry", "_Sum", "_Avlbty", "_Dt", "_DbtNtries", "_NbOfNtries"]
	@property
	def CdtNtries(self):
		return self._CdtNtries

	@CdtNtries.setter
	def CdtNtries(self, value):
		self._CdtNtries = value if type(value) != auto else self.make_default("CdtNtries")

	@CdtNtries.deleter
	def CdtNtries(self):
		del self._CdtNtries
		self._CdtNtries = None

	@property
	def FcstInd(self):
		return self._FcstInd

	@FcstInd.setter
	def FcstInd(self, value):
		self._FcstInd = value if type(value) != auto else self.make_default("FcstInd")

	@FcstInd.deleter
	def FcstInd(self):
		del self._FcstInd
		self._FcstInd = None

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if type(value) != auto else self.make_default("BkTxCd")

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = None

	@property
	def TtlNetNtry(self):
		return self._TtlNetNtry

	@TtlNetNtry.setter
	def TtlNetNtry(self, value):
		self._TtlNetNtry = value if type(value) != auto else self.make_default("TtlNetNtry")

	@TtlNetNtry.deleter
	def TtlNetNtry(self):
		del self._TtlNetNtry
		self._TtlNetNtry = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

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
	def DbtNtries(self):
		return self._DbtNtries

	@DbtNtries.setter
	def DbtNtries(self, value):
		self._DbtNtries = value if type(value) != auto else self.make_default("DbtNtries")

	@DbtNtries.deleter
	def DbtNtries(self):
		del self._DbtNtries
		self._DbtNtries = None

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FcstInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtry', type=AmountAndDirection35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

