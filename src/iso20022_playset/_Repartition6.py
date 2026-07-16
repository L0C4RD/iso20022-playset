# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import FinancialInstrument87
from . import UnitsOrAmountOrPercentage1Choice

class Repartition6(base_types._BaseFieldType):

	__slots__ = ["_CcyOfPlan", "_FinInstrm", "_Qty"]
	@property
	def CcyOfPlan(self):
		return self._CcyOfPlan

	@CcyOfPlan.setter
	def CcyOfPlan(self, value):
		self._CcyOfPlan = value if value is not None else base_types.UninitialisedField(self, 'CcyOfPlan', ActiveOrHistoricCurrencyCode, False)

	@CcyOfPlan.deleter
	def CcyOfPlan(self):
		del self._CcyOfPlan
		self._CcyOfPlan = base_types.UninitialisedField(self, 'CcyOfPlan', ActiveOrHistoricCurrencyCode, False)

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrument87, False)

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrument87, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', UnitsOrAmountOrPercentage1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', UnitsOrAmountOrPercentage1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyOfPlan', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrument87, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitsOrAmountOrPercentage1Choice, min=1, max=1, mutex_group=None, array=False),
	))