from . import base_types
import UnitOfMeasure1Code
import Max6Text
import Max35Text
import FleetServiceType1Code
import Tax41
import TrueFalseIndicator
import DecimalNumber
import Max4Text
import ImpliedCurrencyAndAmount

class FleetLineItem5(base_types._BaseFieldType):

	__slots__ = ["_NonTaxbl", "_UnitOfMeasr", "_UnitPric", "_PdctCdAssgnr", "_PdctQty", "_DscntAmt", "_FuelBrndCd", "_SvcTp", "_Fuel", "_UnitPricTax", "_OthrUnitOfMeasr", "_Tax", "_TtlAmtExclgTax", "_TtlAmtInclgTax", "_PdctCd", "_PdctCtgy", "_PdctQlfr"]
	@property
	def NonTaxbl(self):
		return self._NonTaxbl

	@NonTaxbl.setter
	def NonTaxbl(self, value):
		self._NonTaxbl = value if type(value) != auto else self.make_default("NonTaxbl")

	@NonTaxbl.deleter
	def NonTaxbl(self):
		del self._NonTaxbl
		self._NonTaxbl = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def PdctCdAssgnr(self):
		return self._PdctCdAssgnr

	@PdctCdAssgnr.setter
	def PdctCdAssgnr(self, value):
		self._PdctCdAssgnr = value if type(value) != auto else self.make_default("PdctCdAssgnr")

	@PdctCdAssgnr.deleter
	def PdctCdAssgnr(self):
		del self._PdctCdAssgnr
		self._PdctCdAssgnr = None

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if type(value) != auto else self.make_default("PdctQty")

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = None

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if type(value) != auto else self.make_default("DscntAmt")

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = None

	@property
	def FuelBrndCd(self):
		return self._FuelBrndCd

	@FuelBrndCd.setter
	def FuelBrndCd(self, value):
		self._FuelBrndCd = value if type(value) != auto else self.make_default("FuelBrndCd")

	@FuelBrndCd.deleter
	def FuelBrndCd(self):
		del self._FuelBrndCd
		self._FuelBrndCd = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def Fuel(self):
		return self._Fuel

	@Fuel.setter
	def Fuel(self, value):
		self._Fuel = value if type(value) != auto else self.make_default("Fuel")

	@Fuel.deleter
	def Fuel(self):
		del self._Fuel
		self._Fuel = None

	@property
	def UnitPricTax(self):
		return self._UnitPricTax

	@UnitPricTax.setter
	def UnitPricTax(self, value):
		self._UnitPricTax = value if type(value) != auto else self.make_default("UnitPricTax")

	@UnitPricTax.deleter
	def UnitPricTax(self):
		del self._UnitPricTax
		self._UnitPricTax = None

	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if type(value) != auto else self.make_default("OthrUnitOfMeasr")

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TtlAmtExclgTax(self):
		return self._TtlAmtExclgTax

	@TtlAmtExclgTax.setter
	def TtlAmtExclgTax(self, value):
		self._TtlAmtExclgTax = value if type(value) != auto else self.make_default("TtlAmtExclgTax")

	@TtlAmtExclgTax.deleter
	def TtlAmtExclgTax(self):
		del self._TtlAmtExclgTax
		self._TtlAmtExclgTax = None

	@property
	def TtlAmtInclgTax(self):
		return self._TtlAmtInclgTax

	@TtlAmtInclgTax.setter
	def TtlAmtInclgTax(self, value):
		self._TtlAmtInclgTax = value if type(value) != auto else self.make_default("TtlAmtInclgTax")

	@TtlAmtInclgTax.deleter
	def TtlAmtInclgTax(self):
		del self._TtlAmtInclgTax
		self._TtlAmtInclgTax = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if type(value) != auto else self.make_default("PdctCtgy")

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = None

	@property
	def PdctQlfr(self):
		return self._PdctQlfr

	@PdctQlfr.setter
	def PdctQlfr(self, value):
		self._PdctQlfr = value if type(value) != auto else self.make_default("PdctQlfr")

	@PdctQlfr.deleter
	def PdctQlfr(self):
		del self._PdctQlfr
		self._PdctQlfr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonTaxbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelBrndCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=FleetServiceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fuel', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPricTax', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmtExclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQlfr', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
	))

