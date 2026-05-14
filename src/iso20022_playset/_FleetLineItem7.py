# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditDebit3Code import CreditDebit3Code
from ._DecimalNumber import DecimalNumber
from ._FleetServiceType1Code import FleetServiceType1Code
from ._ISOTime import ISOTime
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Max4Text import Max4Text
from ._Max6Text import Max6Text
from ._PercentageRate import PercentageRate
from ._Tax44 import Tax44
from ._TrueFalseIndicator import TrueFalseIndicator
from ._UnitOfMeasure14Code import UnitOfMeasure14Code

class FleetLineItem7(base_types._BaseFieldType):

	__slots__ = ["_ChrggCmpltnTm", "_ChrggStartTm", "_CostPlusUnitDscnt", "_CostPlusUnitDscntSgn", "_CostPlusUnitPric", "_DscntAmt", "_FlatDscntRate", "_Fuel", "_FuelBrndCd", "_NetAmt", "_NonTaxbl", "_PctgDscntRate", "_PdctCd", "_PdctCdAssgnr", "_PdctCtgy", "_PdctQlfr", "_PdctQty", "_PerUnitDscntRate", "_SvcTp", "_Tax", "_TtlAmtExclgTax", "_TtlAmtInclgTax", "_TtlTmChrgg", "_TtlTmPlugdIn", "_UnitOfMeasr", "_UnitPric", "_UnitPricTax"]
	@property
	def ChrggCmpltnTm(self):
		return self._ChrggCmpltnTm

	@ChrggCmpltnTm.setter
	def ChrggCmpltnTm(self, value):
		self._ChrggCmpltnTm = value if type(value) != base_types.auto else self.make_default("ChrggCmpltnTm")

	@ChrggCmpltnTm.deleter
	def ChrggCmpltnTm(self):
		del self._ChrggCmpltnTm
		self._ChrggCmpltnTm = None

	@property
	def ChrggStartTm(self):
		return self._ChrggStartTm

	@ChrggStartTm.setter
	def ChrggStartTm(self, value):
		self._ChrggStartTm = value if type(value) != base_types.auto else self.make_default("ChrggStartTm")

	@ChrggStartTm.deleter
	def ChrggStartTm(self):
		del self._ChrggStartTm
		self._ChrggStartTm = None

	@property
	def CostPlusUnitDscnt(self):
		return self._CostPlusUnitDscnt

	@CostPlusUnitDscnt.setter
	def CostPlusUnitDscnt(self, value):
		self._CostPlusUnitDscnt = value if type(value) != base_types.auto else self.make_default("CostPlusUnitDscnt")

	@CostPlusUnitDscnt.deleter
	def CostPlusUnitDscnt(self):
		del self._CostPlusUnitDscnt
		self._CostPlusUnitDscnt = None

	@property
	def CostPlusUnitDscntSgn(self):
		return self._CostPlusUnitDscntSgn

	@CostPlusUnitDscntSgn.setter
	def CostPlusUnitDscntSgn(self, value):
		self._CostPlusUnitDscntSgn = value if type(value) != base_types.auto else self.make_default("CostPlusUnitDscntSgn")

	@CostPlusUnitDscntSgn.deleter
	def CostPlusUnitDscntSgn(self):
		del self._CostPlusUnitDscntSgn
		self._CostPlusUnitDscntSgn = None

	@property
	def CostPlusUnitPric(self):
		return self._CostPlusUnitPric

	@CostPlusUnitPric.setter
	def CostPlusUnitPric(self, value):
		self._CostPlusUnitPric = value if type(value) != base_types.auto else self.make_default("CostPlusUnitPric")

	@CostPlusUnitPric.deleter
	def CostPlusUnitPric(self):
		del self._CostPlusUnitPric
		self._CostPlusUnitPric = None

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if type(value) != base_types.auto else self.make_default("DscntAmt")

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = None

	@property
	def FlatDscntRate(self):
		return self._FlatDscntRate

	@FlatDscntRate.setter
	def FlatDscntRate(self, value):
		self._FlatDscntRate = value if type(value) != base_types.auto else self.make_default("FlatDscntRate")

	@FlatDscntRate.deleter
	def FlatDscntRate(self):
		del self._FlatDscntRate
		self._FlatDscntRate = None

	@property
	def Fuel(self):
		return self._Fuel

	@Fuel.setter
	def Fuel(self, value):
		self._Fuel = value if type(value) != base_types.auto else self.make_default("Fuel")

	@Fuel.deleter
	def Fuel(self):
		del self._Fuel
		self._Fuel = None

	@property
	def FuelBrndCd(self):
		return self._FuelBrndCd

	@FuelBrndCd.setter
	def FuelBrndCd(self, value):
		self._FuelBrndCd = value if type(value) != base_types.auto else self.make_default("FuelBrndCd")

	@FuelBrndCd.deleter
	def FuelBrndCd(self):
		del self._FuelBrndCd
		self._FuelBrndCd = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def NonTaxbl(self):
		return self._NonTaxbl

	@NonTaxbl.setter
	def NonTaxbl(self, value):
		self._NonTaxbl = value if type(value) != base_types.auto else self.make_default("NonTaxbl")

	@NonTaxbl.deleter
	def NonTaxbl(self):
		del self._NonTaxbl
		self._NonTaxbl = None

	@property
	def PctgDscntRate(self):
		return self._PctgDscntRate

	@PctgDscntRate.setter
	def PctgDscntRate(self, value):
		self._PctgDscntRate = value if type(value) != base_types.auto else self.make_default("PctgDscntRate")

	@PctgDscntRate.deleter
	def PctgDscntRate(self):
		del self._PctgDscntRate
		self._PctgDscntRate = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != base_types.auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def PdctCdAssgnr(self):
		return self._PdctCdAssgnr

	@PdctCdAssgnr.setter
	def PdctCdAssgnr(self, value):
		self._PdctCdAssgnr = value if type(value) != base_types.auto else self.make_default("PdctCdAssgnr")

	@PdctCdAssgnr.deleter
	def PdctCdAssgnr(self):
		del self._PdctCdAssgnr
		self._PdctCdAssgnr = None

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if type(value) != base_types.auto else self.make_default("PdctCtgy")

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = None

	@property
	def PdctQlfr(self):
		return self._PdctQlfr

	@PdctQlfr.setter
	def PdctQlfr(self, value):
		self._PdctQlfr = value if type(value) != base_types.auto else self.make_default("PdctQlfr")

	@PdctQlfr.deleter
	def PdctQlfr(self):
		del self._PdctQlfr
		self._PdctQlfr = None

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if type(value) != base_types.auto else self.make_default("PdctQty")

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = None

	@property
	def PerUnitDscntRate(self):
		return self._PerUnitDscntRate

	@PerUnitDscntRate.setter
	def PerUnitDscntRate(self, value):
		self._PerUnitDscntRate = value if type(value) != base_types.auto else self.make_default("PerUnitDscntRate")

	@PerUnitDscntRate.deleter
	def PerUnitDscntRate(self):
		del self._PerUnitDscntRate
		self._PerUnitDscntRate = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != base_types.auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TtlAmtExclgTax(self):
		return self._TtlAmtExclgTax

	@TtlAmtExclgTax.setter
	def TtlAmtExclgTax(self, value):
		self._TtlAmtExclgTax = value if type(value) != base_types.auto else self.make_default("TtlAmtExclgTax")

	@TtlAmtExclgTax.deleter
	def TtlAmtExclgTax(self):
		del self._TtlAmtExclgTax
		self._TtlAmtExclgTax = None

	@property
	def TtlAmtInclgTax(self):
		return self._TtlAmtInclgTax

	@TtlAmtInclgTax.setter
	def TtlAmtInclgTax(self, value):
		self._TtlAmtInclgTax = value if type(value) != base_types.auto else self.make_default("TtlAmtInclgTax")

	@TtlAmtInclgTax.deleter
	def TtlAmtInclgTax(self):
		del self._TtlAmtInclgTax
		self._TtlAmtInclgTax = None

	@property
	def TtlTmChrgg(self):
		return self._TtlTmChrgg

	@TtlTmChrgg.setter
	def TtlTmChrgg(self, value):
		self._TtlTmChrgg = value if type(value) != base_types.auto else self.make_default("TtlTmChrgg")

	@TtlTmChrgg.deleter
	def TtlTmChrgg(self):
		del self._TtlTmChrgg
		self._TtlTmChrgg = None

	@property
	def TtlTmPlugdIn(self):
		return self._TtlTmPlugdIn

	@TtlTmPlugdIn.setter
	def TtlTmPlugdIn(self, value):
		self._TtlTmPlugdIn = value if type(value) != base_types.auto else self.make_default("TtlTmPlugdIn")

	@TtlTmPlugdIn.deleter
	def TtlTmPlugdIn(self):
		del self._TtlTmPlugdIn
		self._TtlTmPlugdIn = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def UnitPricTax(self):
		return self._UnitPricTax

	@UnitPricTax.setter
	def UnitPricTax(self, value):
		self._UnitPricTax = value if type(value) != base_types.auto else self.make_default("UnitPricTax")

	@UnitPricTax.deleter
	def UnitPricTax(self):
		del self._UnitPricTax
		self._UnitPricTax = None

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