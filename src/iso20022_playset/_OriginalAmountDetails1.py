# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount

class OriginalAmountDetails1(base_types._BaseFieldType):

	__slots__ = ["_ActlAmt", "_MaxAmt", "_MinAmt"]
	@property
	def ActlAmt(self):
		return self._ActlAmt

	@ActlAmt.setter
	def ActlAmt(self, value):
		self._ActlAmt = value if value is not None else base_types.UninitialisedField(self, 'ActlAmt', ImpliedCurrencyAndAmount, False)

	@ActlAmt.deleter
	def ActlAmt(self):
		del self._ActlAmt
		self._ActlAmt = base_types.UninitialisedField(self, 'ActlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxAmt', ImpliedCurrencyAndAmount, False)

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = base_types.UninitialisedField(self, 'MaxAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MinAmt(self):
		return self._MinAmt

	@MinAmt.setter
	def MinAmt(self, value):
		self._MinAmt = value if value is not None else base_types.UninitialisedField(self, 'MinAmt', ImpliedCurrencyAndAmount, False)

	@MinAmt.deleter
	def MinAmt(self):
		del self._MinAmt
		self._MinAmt = base_types.UninitialisedField(self, 'MinAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))