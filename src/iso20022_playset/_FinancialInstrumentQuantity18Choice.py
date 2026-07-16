# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount

class FinancialInstrumentQuantity18Choice(base_types._BaseFieldType):

	__slots__ = ["_FaceAmt", "_Unit"]
	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if value is not None else base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAndAmount, False)

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))