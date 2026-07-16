# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import FleetServiceType1Code
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max4Text
from . import Max6Text
from . import Tax41
from . import TrueFalseIndicator
from . import UnitOfMeasure1Code

class FleetLineItem5(base_types._BaseFieldType):

	__slots__ = ["_DscntAmt", "_Fuel", "_FuelBrndCd", "_NonTaxbl", "_OthrUnitOfMeasr", "_PdctCd", "_PdctCdAssgnr", "_PdctCtgy", "_PdctQlfr", "_PdctQty", "_SvcTp", "_Tax", "_TtlAmtExclgTax", "_TtlAmtInclgTax", "_UnitOfMeasr", "_UnitPric", "_UnitPricTax"]
	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntAmt', ImpliedCurrencyAndAmount, False)

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = base_types.UninitialisedField(self, 'DscntAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Fuel(self):
		return self._Fuel

	@Fuel.setter
	def Fuel(self, value):
		self._Fuel = value if value is not None else base_types.UninitialisedField(self, 'Fuel', TrueFalseIndicator, False)

	@Fuel.deleter
	def Fuel(self):
		del self._Fuel
		self._Fuel = base_types.UninitialisedField(self, 'Fuel', TrueFalseIndicator, False)

	@property
	def FuelBrndCd(self):
		return self._FuelBrndCd

	@FuelBrndCd.setter
	def FuelBrndCd(self, value):
		self._FuelBrndCd = value if value is not None else base_types.UninitialisedField(self, 'FuelBrndCd', Max4Text, False)

	@FuelBrndCd.deleter
	def FuelBrndCd(self):
		del self._FuelBrndCd
		self._FuelBrndCd = base_types.UninitialisedField(self, 'FuelBrndCd', Max4Text, False)

	@property
	def NonTaxbl(self):
		return self._NonTaxbl

	@NonTaxbl.setter
	def NonTaxbl(self, value):
		self._NonTaxbl = value if value is not None else base_types.UninitialisedField(self, 'NonTaxbl', TrueFalseIndicator, False)

	@NonTaxbl.deleter
	def NonTaxbl(self):
		del self._NonTaxbl
		self._NonTaxbl = base_types.UninitialisedField(self, 'NonTaxbl', TrueFalseIndicator, False)

	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max4Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max4Text, False)

	@property
	def PdctCdAssgnr(self):
		return self._PdctCdAssgnr

	@PdctCdAssgnr.setter
	def PdctCdAssgnr(self, value):
		self._PdctCdAssgnr = value if value is not None else base_types.UninitialisedField(self, 'PdctCdAssgnr', Max35Text, False)

	@PdctCdAssgnr.deleter
	def PdctCdAssgnr(self):
		del self._PdctCdAssgnr
		self._PdctCdAssgnr = base_types.UninitialisedField(self, 'PdctCdAssgnr', Max35Text, False)

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'PdctCtgy', Max35Text, False)

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = base_types.UninitialisedField(self, 'PdctCtgy', Max35Text, False)

	@property
	def PdctQlfr(self):
		return self._PdctQlfr

	@PdctQlfr.setter
	def PdctQlfr(self, value):
		self._PdctQlfr = value if value is not None else base_types.UninitialisedField(self, 'PdctQlfr', Max6Text, False)

	@PdctQlfr.deleter
	def PdctQlfr(self):
		del self._PdctQlfr
		self._PdctQlfr = base_types.UninitialisedField(self, 'PdctQlfr', Max6Text, False)

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if value is not None else base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', FleetServiceType1Code, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', FleetServiceType1Code, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@property
	def TtlAmtExclgTax(self):
		return self._TtlAmtExclgTax

	@TtlAmtExclgTax.setter
	def TtlAmtExclgTax(self, value):
		self._TtlAmtExclgTax = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtExclgTax', ImpliedCurrencyAndAmount, False)

	@TtlAmtExclgTax.deleter
	def TtlAmtExclgTax(self):
		del self._TtlAmtExclgTax
		self._TtlAmtExclgTax = base_types.UninitialisedField(self, 'TtlAmtExclgTax', ImpliedCurrencyAndAmount, False)

	@property
	def TtlAmtInclgTax(self):
		return self._TtlAmtInclgTax

	@TtlAmtInclgTax.setter
	def TtlAmtInclgTax(self, value):
		self._TtlAmtInclgTax = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtInclgTax', ImpliedCurrencyAndAmount, False)

	@TtlAmtInclgTax.deleter
	def TtlAmtInclgTax(self):
		del self._TtlAmtInclgTax
		self._TtlAmtInclgTax = base_types.UninitialisedField(self, 'TtlAmtInclgTax', ImpliedCurrencyAndAmount, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@property
	def UnitPricTax(self):
		return self._UnitPricTax

	@UnitPricTax.setter
	def UnitPricTax(self, value):
		self._UnitPricTax = value if value is not None else base_types.UninitialisedField(self, 'UnitPricTax', TrueFalseIndicator, False)

	@UnitPricTax.deleter
	def UnitPricTax(self):
		del self._UnitPricTax
		self._UnitPricTax = base_types.UninitialisedField(self, 'UnitPricTax', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fuel', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelBrndCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonTaxbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQlfr', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=FleetServiceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmtExclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPricTax', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))