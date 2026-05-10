from . import base_types
from ._RestrictedFINDecimalNumber import RestrictedFINDecimalNumber
from ._RestrictedFINImpliedCurrencyAndAmount import RestrictedFINImpliedCurrencyAndAmount

class FinancialInstrumentQuantity31Choice(base_types._BaseFieldType):

	__slots__ = ["_FaceAmt", "_Unit"]
	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if type(value) != base_types.auto else self.make_default("FaceAmt")

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FaceAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

