# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification6
from . import CashAccount40
from . import DatePeriod5
from . import Max140Text
from . import PercentageRate

class AdjustmentCompensation1(base_types._BaseFieldType):

	__slots__ = ["_AmtDue", "_CompstnAcct", "_CompstnAgt", "_DueChrgs", "_InitlAmt", "_IntrstRate", "_Prd", "_Rsn"]
	@property
	def AmtDue(self):
		return self._AmtDue

	@AmtDue.setter
	def AmtDue(self, value):
		self._AmtDue = value if value is not None else base_types.UninitialisedField(self, 'AmtDue', ActiveCurrencyAndAmount, False)

	@AmtDue.deleter
	def AmtDue(self):
		del self._AmtDue
		self._AmtDue = base_types.UninitialisedField(self, 'AmtDue', ActiveCurrencyAndAmount, False)

	@property
	def CompstnAcct(self):
		return self._CompstnAcct

	@CompstnAcct.setter
	def CompstnAcct(self, value):
		self._CompstnAcct = value if value is not None else base_types.UninitialisedField(self, 'CompstnAcct', CashAccount40, False)

	@CompstnAcct.deleter
	def CompstnAcct(self):
		del self._CompstnAcct
		self._CompstnAcct = base_types.UninitialisedField(self, 'CompstnAcct', CashAccount40, False)

	@property
	def CompstnAgt(self):
		return self._CompstnAgt

	@CompstnAgt.setter
	def CompstnAgt(self, value):
		self._CompstnAgt = value if value is not None else base_types.UninitialisedField(self, 'CompstnAgt', BranchAndFinancialInstitutionIdentification6, False)

	@CompstnAgt.deleter
	def CompstnAgt(self):
		del self._CompstnAgt
		self._CompstnAgt = base_types.UninitialisedField(self, 'CompstnAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def DueChrgs(self):
		return self._DueChrgs

	@DueChrgs.setter
	def DueChrgs(self, value):
		self._DueChrgs = value if value is not None else base_types.UninitialisedField(self, 'DueChrgs', ActiveCurrencyAndAmount, False)

	@DueChrgs.deleter
	def DueChrgs(self):
		del self._DueChrgs
		self._DueChrgs = base_types.UninitialisedField(self, 'DueChrgs', ActiveCurrencyAndAmount, False)

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if value is not None else base_types.UninitialisedField(self, 'InitlAmt', ActiveCurrencyAndAmount, False)

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = base_types.UninitialisedField(self, 'InitlAmt', ActiveCurrencyAndAmount, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DatePeriod5, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DatePeriod5, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDue', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueChrgs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DatePeriod5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))