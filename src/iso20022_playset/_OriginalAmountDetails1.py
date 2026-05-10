from . import base_types
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class OriginalAmountDetails1(base_types._BaseFieldType):

	__slots__ = ["_MaxAmt", "_ActlAmt", "_MinAmt"]
	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if type(value) != base_types.auto else self.make_default("MaxAmt")

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = None

	@property
	def ActlAmt(self):
		return self._ActlAmt

	@ActlAmt.setter
	def ActlAmt(self, value):
		self._ActlAmt = value if type(value) != base_types.auto else self.make_default("ActlAmt")

	@ActlAmt.deleter
	def ActlAmt(self):
		del self._ActlAmt
		self._ActlAmt = None

	@property
	def MinAmt(self):
		return self._MinAmt

	@MinAmt.setter
	def MinAmt(self, value):
		self._MinAmt = value if type(value) != base_types.auto else self.make_default("MinAmt")

	@MinAmt.deleter
	def MinAmt(self):
		del self._MinAmt
		self._MinAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

