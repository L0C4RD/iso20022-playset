# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max30DecimalNumber
from . import Quantity5Code
from . import RestrictedFINDecimalNumber
from . import RestrictedFINImpliedCurrencyAndAmount

class FinancialInstrumentQuantity43Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_Cd", "_DgtlTknUnit", "_FaceAmt", "_Unit"]
	@property
	def AmtsdVal(self):
		return self._AmtsdVal

	@AmtsdVal.setter
	def AmtsdVal(self, value):
		self._AmtsdVal = value if value is not None else base_types.UninitialisedField(self, 'AmtsdVal', RestrictedFINImpliedCurrencyAndAmount, False)

	@AmtsdVal.deleter
	def AmtsdVal(self):
		del self._AmtsdVal
		self._AmtsdVal = base_types.UninitialisedField(self, 'AmtsdVal', RestrictedFINImpliedCurrencyAndAmount, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Quantity5Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Quantity5Code, False)

	@property
	def DgtlTknUnit(self):
		return self._DgtlTknUnit

	@DgtlTknUnit.setter
	def DgtlTknUnit(self, value):
		self._DgtlTknUnit = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknUnit', Max30DecimalNumber, False)

	@DgtlTknUnit.deleter
	def DgtlTknUnit(self):
		del self._DgtlTknUnit
		self._DgtlTknUnit = base_types.UninitialisedField(self, 'DgtlTknUnit', Max30DecimalNumber, False)

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if value is not None else base_types.UninitialisedField(self, 'FaceAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = base_types.UninitialisedField(self, 'FaceAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', RestrictedFINDecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', RestrictedFINDecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtsdVal', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=Quantity5Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlTknUnit', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaceAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))