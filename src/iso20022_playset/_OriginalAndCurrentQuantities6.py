# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import ShortLong1Code

class OriginalAndCurrentQuantities6(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_FaceAmt", "_ShrtLngPos"]
	@property
	def AmtsdVal(self):
		return self._AmtsdVal

	@AmtsdVal.setter
	def AmtsdVal(self, value):
		self._AmtsdVal = value if value is not None else base_types.UninitialisedField(self, 'AmtsdVal', ImpliedCurrencyAndAmount, False)

	@AmtsdVal.deleter
	def AmtsdVal(self):
		del self._AmtsdVal
		self._AmtsdVal = base_types.UninitialisedField(self, 'AmtsdVal', ImpliedCurrencyAndAmount, False)

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
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if value is not None else base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))