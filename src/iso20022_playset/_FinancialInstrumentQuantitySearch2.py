# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAmountRange1Choice

class FinancialInstrumentQuantitySearch2(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_FaceAmt"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAmountRange1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAmountRange1Choice, min=1, max=1, mutex_group=None, array=False),
	))