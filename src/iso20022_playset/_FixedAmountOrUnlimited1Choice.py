# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Unlimited9Text

class FixedAmountOrUnlimited1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_NotLtd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def NotLtd(self):
		return self._NotLtd

	@NotLtd.setter
	def NotLtd(self, value):
		self._NotLtd = value if value is not None else base_types.UninitialisedField(self, 'NotLtd', Unlimited9Text, False)

	@NotLtd.deleter
	def NotLtd(self):
		del self._NotLtd
		self._NotLtd = base_types.UninitialisedField(self, 'NotLtd', Unlimited9Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotLtd', type=Unlimited9Text, min=0, max=1, mutex_group=1, array=False),
	))