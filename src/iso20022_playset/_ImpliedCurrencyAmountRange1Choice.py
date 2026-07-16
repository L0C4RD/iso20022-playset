# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountRangeBoundary1
from . import FromToAmountRange1
from . import ImpliedCurrencyAndAmount

class ImpliedCurrencyAmountRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQAmt", "_FrAmt", "_FrToAmt", "_NEQAmt", "_ToAmt"]
	@property
	def EQAmt(self):
		return self._EQAmt

	@EQAmt.setter
	def EQAmt(self, value):
		self._EQAmt = value if value is not None else base_types.UninitialisedField(self, 'EQAmt', ImpliedCurrencyAndAmount, False)

	@EQAmt.deleter
	def EQAmt(self):
		del self._EQAmt
		self._EQAmt = base_types.UninitialisedField(self, 'EQAmt', ImpliedCurrencyAndAmount, False)

	@property
	def FrAmt(self):
		return self._FrAmt

	@FrAmt.setter
	def FrAmt(self, value):
		self._FrAmt = value if value is not None else base_types.UninitialisedField(self, 'FrAmt', AmountRangeBoundary1, False)

	@FrAmt.deleter
	def FrAmt(self):
		del self._FrAmt
		self._FrAmt = base_types.UninitialisedField(self, 'FrAmt', AmountRangeBoundary1, False)

	@property
	def FrToAmt(self):
		return self._FrToAmt

	@FrToAmt.setter
	def FrToAmt(self, value):
		self._FrToAmt = value if value is not None else base_types.UninitialisedField(self, 'FrToAmt', FromToAmountRange1, False)

	@FrToAmt.deleter
	def FrToAmt(self):
		del self._FrToAmt
		self._FrToAmt = base_types.UninitialisedField(self, 'FrToAmt', FromToAmountRange1, False)

	@property
	def NEQAmt(self):
		return self._NEQAmt

	@NEQAmt.setter
	def NEQAmt(self, value):
		self._NEQAmt = value if value is not None else base_types.UninitialisedField(self, 'NEQAmt', ImpliedCurrencyAndAmount, False)

	@NEQAmt.deleter
	def NEQAmt(self):
		del self._NEQAmt
		self._NEQAmt = base_types.UninitialisedField(self, 'NEQAmt', ImpliedCurrencyAndAmount, False)

	@property
	def ToAmt(self):
		return self._ToAmt

	@ToAmt.setter
	def ToAmt(self, value):
		self._ToAmt = value if value is not None else base_types.UninitialisedField(self, 'ToAmt', AmountRangeBoundary1, False)

	@ToAmt.deleter
	def ToAmt(self):
		del self._ToAmt
		self._ToAmt = base_types.UninitialisedField(self, 'ToAmt', AmountRangeBoundary1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EQAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrAmt', type=AmountRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToAmt', type=FromToAmountRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToAmt', type=AmountRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
	))