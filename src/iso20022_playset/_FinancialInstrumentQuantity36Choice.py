from . import base_types
from ._Max30DecimalNumber import Max30DecimalNumber
from ._RestrictedFINDecimalNumber import RestrictedFINDecimalNumber
from ._RestrictedFINImpliedCurrencyAndAmount import RestrictedFINImpliedCurrencyAndAmount

class FinancialInstrumentQuantity36Choice(base_types._BaseFieldType):

	__slots__ = ["_FaceAmt", "_Unit", "_DgtlTknUnit", "_AmtsdVal"]
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

	@property
	def DgtlTknUnit(self):
		return self._DgtlTknUnit

	@DgtlTknUnit.setter
	def DgtlTknUnit(self, value):
		self._DgtlTknUnit = value if type(value) != base_types.auto else self.make_default("DgtlTknUnit")

	@DgtlTknUnit.deleter
	def DgtlTknUnit(self):
		del self._DgtlTknUnit
		self._DgtlTknUnit = None

	@property
	def AmtsdVal(self):
		return self._AmtsdVal

	@AmtsdVal.setter
	def AmtsdVal(self, value):
		self._AmtsdVal = value if type(value) != base_types.auto else self.make_default("AmtsdVal")

	@AmtsdVal.deleter
	def AmtsdVal(self):
		del self._AmtsdVal
		self._AmtsdVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FaceAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlTknUnit', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtsdVal', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

