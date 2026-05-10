from . import base_types
from .ShortLong1Code import ShortLong1Code
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class OriginalAndCurrentQuantities6(base_types._BaseFieldType):

	__slots__ = ["_ShrtLngPos", "_AmtsdVal", "_FaceAmt"]
	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if type(value) != base_types.auto else self.make_default("ShrtLngPos")

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

