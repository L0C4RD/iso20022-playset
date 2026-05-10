from . import base_types
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .UnitsOrAmountOrPercentage1Choice import UnitsOrAmountOrPercentage1Choice
from .FinancialInstrument87 import FinancialInstrument87

class Repartition6(base_types._BaseFieldType):

	__slots__ = ["_CcyOfPlan", "_Qty", "_FinInstrm"]
	@property
	def CcyOfPlan(self):
		return self._CcyOfPlan

	@CcyOfPlan.setter
	def CcyOfPlan(self, value):
		self._CcyOfPlan = value if type(value) != auto else self.make_default("CcyOfPlan")

	@CcyOfPlan.deleter
	def CcyOfPlan(self):
		del self._CcyOfPlan
		self._CcyOfPlan = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyOfPlan', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitsOrAmountOrPercentage1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrument87, min=1, max=1, mutex_group=None, array=False),
	))

