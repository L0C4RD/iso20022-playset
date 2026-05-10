from . import base_types
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class OriginalAndCurrentQuantities1(base_types._BaseFieldType):

	__slots__ = ["_FaceAmt", "_AmtsdVal"]
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
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

