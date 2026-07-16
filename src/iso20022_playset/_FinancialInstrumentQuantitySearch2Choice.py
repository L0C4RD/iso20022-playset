# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAmountRange1Choice
from . import QuantityRange1Choice

class FinancialInstrumentQuantitySearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_FaceAmt", "_Unit"]
	@property
	def AmtsdVal(self):
		return self._AmtsdVal

	@AmtsdVal.setter
	def AmtsdVal(self, value):
		self._AmtsdVal = value if value is not None else base_types.UninitialisedField(self, 'AmtsdVal', ImpliedCurrencyAmountRange1Choice, False)

	@AmtsdVal.deleter
	def AmtsdVal(self):
		del self._AmtsdVal
		self._AmtsdVal = base_types.UninitialisedField(self, 'AmtsdVal', ImpliedCurrencyAmountRange1Choice, False)

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if value is not None else base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAmountRange1Choice, False)

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAmountRange1Choice, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', QuantityRange1Choice, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', QuantityRange1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=QuantityRange1Choice, min=0, max=1, mutex_group=1, array=False),
	))