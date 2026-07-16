# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import BalanceType13
from . import CashAvailability1
from . import CreditDebitCode
from . import CreditLine3
from . import DateAndDateTime2Choice

class CashBalance8(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Avlbty", "_CdtDbtInd", "_CdtLine", "_Dt", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

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
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def CdtLine(self):
		return self._CdtLine

	@CdtLine.setter
	def CdtLine(self, value):
		self._CdtLine = value if value is not None else base_types.UninitialisedField(self, 'CdtLine', CreditLine3, True)

	@CdtLine.deleter
	def CdtLine(self):
		del self._CdtLine
		self._CdtLine = base_types.UninitialisedField(self, 'CdtLine', CreditLine3, True)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BalanceType13, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BalanceType13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtLine', type=CreditLine3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType13, min=1, max=1, mutex_group=None, array=False),
	))