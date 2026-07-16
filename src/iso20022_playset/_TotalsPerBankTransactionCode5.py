# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection35
from . import BankTransactionCodeStructure4
from . import CashAvailability1
from . import DateAndDateTime2Choice
from . import DecimalNumber
from . import Max15NumericText
from . import NumberAndSumOfTransactions1
from . import TrueFalseIndicator

class TotalsPerBankTransactionCode5(base_types._BaseFieldType):

	__slots__ = ["_Avlbty", "_BkTxCd", "_CdtNtries", "_DbtNtries", "_Dt", "_FcstInd", "_NbOfNtries", "_Sum", "_TtlNetNtry"]
	@property
	def Avlbty(self):
		return self._Avlbty

	@Avlbty.setter
	def Avlbty(self, value):
		self._Avlbty = value if value is not None else base_types.UninitialisedField(self, 'Avlbty', CashAvailability1, True)

	@Avlbty.deleter
	def Avlbty(self):
		del self._Avlbty
		self._Avlbty = base_types.UninitialisedField(self, 'Avlbty', CashAvailability1, True)

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if value is not None else base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@property
	def CdtNtries(self):
		return self._CdtNtries

	@CdtNtries.setter
	def CdtNtries(self, value):
		self._CdtNtries = value if value is not None else base_types.UninitialisedField(self, 'CdtNtries', NumberAndSumOfTransactions1, False)

	@CdtNtries.deleter
	def CdtNtries(self):
		del self._CdtNtries
		self._CdtNtries = base_types.UninitialisedField(self, 'CdtNtries', NumberAndSumOfTransactions1, False)

	@property
	def DbtNtries(self):
		return self._DbtNtries

	@DbtNtries.setter
	def DbtNtries(self, value):
		self._DbtNtries = value if value is not None else base_types.UninitialisedField(self, 'DbtNtries', NumberAndSumOfTransactions1, False)

	@DbtNtries.deleter
	def DbtNtries(self):
		del self._DbtNtries
		self._DbtNtries = base_types.UninitialisedField(self, 'DbtNtries', NumberAndSumOfTransactions1, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@property
	def FcstInd(self):
		return self._FcstInd

	@FcstInd.setter
	def FcstInd(self, value):
		self._FcstInd = value if value is not None else base_types.UninitialisedField(self, 'FcstInd', TrueFalseIndicator, False)

	@FcstInd.deleter
	def FcstInd(self):
		del self._FcstInd
		self._FcstInd = base_types.UninitialisedField(self, 'FcstInd', TrueFalseIndicator, False)

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if value is not None else base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if value is not None else base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	@property
	def TtlNetNtry(self):
		return self._TtlNetNtry

	@TtlNetNtry.setter
	def TtlNetNtry(self, value):
		self._TtlNetNtry = value if value is not None else base_types.UninitialisedField(self, 'TtlNetNtry', AmountAndDirection35, False)

	@TtlNetNtry.deleter
	def TtlNetNtry(self):
		del self._TtlNetNtry
		self._TtlNetNtry = base_types.UninitialisedField(self, 'TtlNetNtry', AmountAndDirection35, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FcstInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtry', type=AmountAndDirection35, min=0, max=1, mutex_group=None, array=False),
	))