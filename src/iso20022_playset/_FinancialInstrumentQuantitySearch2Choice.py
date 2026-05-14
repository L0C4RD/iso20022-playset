# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ImpliedCurrencyAmountRange1Choice import ImpliedCurrencyAmountRange1Choice
from ._QuantityRange1Choice import QuantityRange1Choice

class FinancialInstrumentQuantitySearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_FaceAmt", "_Unit"]
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
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=QuantityRange1Choice, min=0, max=1, mutex_group=1, array=False),
	))