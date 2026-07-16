# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChargesType1Choice
from . import CurrencyAndAmount

class ChargesDetails4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgsTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@property
	def ChrgsTp(self):
		return self._ChrgsTp

	@ChrgsTp.setter
	def ChrgsTp(self, value):
		self._ChrgsTp = value if value is not None else base_types.UninitialisedField(self, 'ChrgsTp', ChargesType1Choice, False)

	@ChrgsTp.deleter
	def ChrgsTp(self):
		del self._ChrgsTp
		self._ChrgsTp = base_types.UninitialisedField(self, 'ChrgsTp', ChargesType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsTp', type=ChargesType1Choice, min=1, max=1, mutex_group=None, array=False),
	))