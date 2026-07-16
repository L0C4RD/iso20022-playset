# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max70Text
from . import TrueFalseIndicator

class DetailedAmount18(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_ChrgAcctTo", "_Labl"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def ChrgAcctTo(self):
		return self._ChrgAcctTo

	@ChrgAcctTo.setter
	def ChrgAcctTo(self, value):
		self._ChrgAcctTo = value if value is not None else base_types.UninitialisedField(self, 'ChrgAcctTo', TrueFalseIndicator, False)

	@ChrgAcctTo.deleter
	def ChrgAcctTo(self):
		del self._ChrgAcctTo
		self._ChrgAcctTo = base_types.UninitialisedField(self, 'ChrgAcctTo', TrueFalseIndicator, False)

	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if value is not None else base_types.UninitialisedField(self, 'Labl', Max70Text, False)

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = base_types.UninitialisedField(self, 'Labl', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgAcctTo', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Labl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))