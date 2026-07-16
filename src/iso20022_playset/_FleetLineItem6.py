# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import FleetServiceType1Code
from . import ImpliedCurrencyAndAmount
from . import Max15Text
from . import Max35Text
from . import TrueFalseIndicator
from . import UnitOfMeasure1Code

class FleetLineItem6(base_types._BaseFieldType):

	__slots__ = ["_AllwdItm", "_Fuel", "_PdctCd", "_PdctCtgy", "_PdctQty", "_SvcTp", "_TtlAmtExclgTax", "_TtlAmtInclgTax", "_UnitOfMeasr"]
	@property
	def AllwdItm(self):
		return self._AllwdItm

	@AllwdItm.setter
	def AllwdItm(self, value):
		self._AllwdItm = value if value is not None else base_types.UninitialisedField(self, 'AllwdItm', TrueFalseIndicator, False)

	@AllwdItm.deleter
	def AllwdItm(self):
		del self._AllwdItm
		self._AllwdItm = base_types.UninitialisedField(self, 'AllwdItm', TrueFalseIndicator, False)

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
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max15Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max15Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllwdItm', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fuel', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=FleetServiceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtExclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInclgTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
	))