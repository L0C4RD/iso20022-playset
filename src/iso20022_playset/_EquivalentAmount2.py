from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class EquivalentAmount2(base_types._BaseFieldType):

	__slots__ = ["_CcyOfTrf", "_Amt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CcyOfTrf(self):
		return self._CcyOfTrf

	@CcyOfTrf.setter
	def CcyOfTrf(self, value):
		self._CcyOfTrf = value if type(value) != base_types.auto else self.make_default("CcyOfTrf")

	@CcyOfTrf.deleter
	def CcyOfTrf(self):
		del self._CcyOfTrf
		self._CcyOfTrf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOfTrf', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

