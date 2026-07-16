# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BillingFeeRecord1
from . import Max40Text
from . import PercentageRate
from . import TaxExemption1

class BillingTaxRecord2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgsAndFees", "_Desc", "_Rate", "_TaxXmptn", "_TaxblAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def ChrgsAndFees(self):
		return self._ChrgsAndFees

	@ChrgsAndFees.setter
	def ChrgsAndFees(self, value):
		self._ChrgsAndFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAndFees', BillingFeeRecord1, True)

	@ChrgsAndFees.deleter
	def ChrgsAndFees(self):
		del self._ChrgsAndFees
		self._ChrgsAndFees = base_types.UninitialisedField(self, 'ChrgsAndFees', BillingFeeRecord1, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max40Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max40Text, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if value is not None else base_types.UninitialisedField(self, 'TaxXmptn', TaxExemption1, True)

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = base_types.UninitialisedField(self, 'TaxXmptn', TaxExemption1, True)

	@property
	def TaxblAmt(self):
		return self._TaxblAmt

	@TaxblAmt.setter
	def TaxblAmt(self, value):
		self._TaxblAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxblAmt', ActiveCurrencyAndAmount, False)

	@TaxblAmt.deleter
	def TaxblAmt(self):
		del self._TaxblAmt
		self._TaxblAmt = base_types.UninitialisedField(self, 'TaxblAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAndFees', type=BillingFeeRecord1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))