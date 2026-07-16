# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebit3Code
from . import DecimalNumber
from . import FleetServiceType1Code
from . import ISOTime
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max4Text
from . import Max6Text
from . import PercentageRate
from . import Tax44
from . import TrueFalseIndicator
from . import UnitOfMeasure14Code

class FleetLineItem7(base_types._BaseFieldType):

	__slots__ = ["_ChrggCmpltnTm", "_ChrggStartTm", "_CostPlusUnitDscnt", "_CostPlusUnitDscntSgn", "_CostPlusUnitPric", "_DscntAmt", "_FlatDscntRate", "_Fuel", "_FuelBrndCd", "_NetAmt", "_NonTaxbl", "_PctgDscntRate", "_PdctCd", "_PdctCdAssgnr", "_PdctCtgy", "_PdctQlfr", "_PdctQty", "_PerUnitDscntRate", "_SvcTp", "_Tax", "_TtlAmtExclgTax", "_TtlAmtInclgTax", "_TtlTmChrgg", "_TtlTmPlugdIn", "_UnitOfMeasr", "_UnitPric", "_UnitPricTax"]
	@property
	def ChrggCmpltnTm(self):
		return self._ChrggCmpltnTm

	@ChrggCmpltnTm.setter
	def ChrggCmpltnTm(self, value):
		self._ChrggCmpltnTm = value if value is not None else base_types.UninitialisedField(self, 'ChrggCmpltnTm', ISOTime, False)

	@ChrggCmpltnTm.deleter
	def ChrggCmpltnTm(self):
		del self._ChrggCmpltnTm
		self._ChrggCmpltnTm = base_types.UninitialisedField(self, 'ChrggCmpltnTm', ISOTime, False)

	@property
	def ChrggStartTm(self):
		return self._ChrggStartTm

	@ChrggStartTm.setter
	def ChrggStartTm(self, value):
		self._ChrggStartTm = value if value is not None else base_types.UninitialisedField(self, 'ChrggStartTm', ISOTime, False)

	@ChrggStartTm.deleter
	def ChrggStartTm(self):
		del self._ChrggStartTm
		self._ChrggStartTm = base_types.UninitialisedField(self, 'ChrggStartTm', ISOTime, False)

	@property
	def CostPlusUnitDscnt(self):
		return self._CostPlusUnitDscnt

	@CostPlusUnitDscnt.setter
	def CostPlusUnitDscnt(self, value):
		self._CostPlusUnitDscnt = value if value is not None else base_types.UninitialisedField(self, 'CostPlusUnitDscnt', ImpliedCurrencyAndAmount, False)

	@CostPlusUnitDscnt.deleter
	def CostPlusUnitDscnt(self):
		del self._CostPlusUnitDscnt
		self._CostPlusUnitDscnt = base_types.UninitialisedField(self, 'CostPlusUnitDscnt', ImpliedCurrencyAndAmount, False)

	@property
	def CostPlusUnitDscntSgn(self):
		return self._CostPlusUnitDscntSgn

	@CostPlusUnitDscntSgn.setter
	def CostPlusUnitDscntSgn(self, value):
		self._CostPlusUnitDscntSgn = value if value is not None else base_types.UninitialisedField(self, 'CostPlusUnitDscntSgn', CreditDebit3Code, False)

	@CostPlusUnitDscntSgn.deleter
	def CostPlusUnitDscntSgn(self):
		del self._CostPlusUnitDscntSgn
		self._CostPlusUnitDscntSgn = base_types.UninitialisedField(self, 'CostPlusUnitDscntSgn', CreditDebit3Code, False)

	@property
	def CostPlusUnitPric(self):
		return self._CostPlusUnitPric

	@CostPlusUnitPric.setter
	def CostPlusUnitPric(self, value):
		self._CostPlusUnitPric = value if value is not None else base_types.UninitialisedField(self, 'CostPlusUnitPric', ImpliedCurrencyAndAmount, False)

	@CostPlusUnitPric.deleter
	def CostPlusUnitPric(self):
		del self._CostPlusUnitPric
		self._CostPlusUnitPric = base_types.UninitialisedField(self, 'CostPlusUnitPric', ImpliedCurrencyAndAmount, False)

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
	def FlatDscntRate(self):
		return self._FlatDscntRate

	@FlatDscntRate.setter
	def FlatDscntRate(self, value):
		self._FlatDscntRate = value if value is not None else base_types.UninitialisedField(self, 'FlatDscntRate', ImpliedCurrencyAndAmount, False)

	@FlatDscntRate.deleter
	def FlatDscntRate(self):
		del self._FlatDscntRate
		self._FlatDscntRate = base_types.UninitialisedField(self, 'FlatDscntRate', ImpliedCurrencyAndAmount, False)

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
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

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
	def PctgDscntRate(self):
		return self._PctgDscntRate

	@PctgDscntRate.setter
	def PctgDscntRate(self, value):
		self._PctgDscntRate = value if value is not None else base_types.UninitialisedField(self, 'PctgDscntRate', PercentageRate, False)

	@PctgDscntRate.deleter
	def PctgDscntRate(self):
		del self._PctgDscntRate
		self._PctgDscntRate = base_types.UninitialisedField(self, 'PctgDscntRate', PercentageRate, False)

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
	def PerUnitDscntRate(self):
		return self._PerUnitDscntRate

	@PerUnitDscntRate.setter
	def PerUnitDscntRate(self, value):
		self._PerUnitDscntRate = value if value is not None else base_types.UninitialisedField(self, 'PerUnitDscntRate', ImpliedCurrencyAndAmount, False)

	@PerUnitDscntRate.deleter
	def PerUnitDscntRate(self):
		del self._PerUnitDscntRate
		self._PerUnitDscntRate = base_types.UninitialisedField(self, 'PerUnitDscntRate', ImpliedCurrencyAndAmount, False)

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
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax44, True)

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
	def TtlTmChrgg(self):
		return self._TtlTmChrgg

	@TtlTmChrgg.setter
	def TtlTmChrgg(self, value):
		self._TtlTmChrgg = value if value is not None else base_types.UninitialisedField(self, 'TtlTmChrgg', ISOTime, False)

	@TtlTmChrgg.deleter
	def TtlTmChrgg(self):
		del self._TtlTmChrgg
		self._TtlTmChrgg = base_types.UninitialisedField(self, 'TtlTmChrgg', ISOTime, False)

	@property
	def TtlTmPlugdIn(self):
		return self._TtlTmPlugdIn

	@TtlTmPlugdIn.setter
	def TtlTmPlugdIn(self, value):
		self._TtlTmPlugdIn = value if value is not None else base_types.UninitialisedField(self, 'TtlTmPlugdIn', ISOTime, False)

	@TtlTmPlugdIn.deleter
	def TtlTmPlugdIn(self):
		del self._TtlTmPlugdIn
		self._TtlTmPlugdIn = base_types.UninitialisedField(self, 'TtlTmPlugdIn', ISOTime, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure14Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure14Code, False)

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
		base_types.FieldEntry(name='ChrggCmpltnTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrggStartTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostPlusUnitDscnt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostPlusUnitDscntSgn', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostPlusUnitPric', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlatDscntRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fuel', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelBrndCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonTaxbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgDscntRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQlfr', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PerUnitDscntRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=FleetServiceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmtExclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTmChrgg', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTmPlugdIn', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure14Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPricTax', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))