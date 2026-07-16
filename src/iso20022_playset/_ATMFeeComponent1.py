# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max70Text

class ATMFeeComponent1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_FeeLabl"]
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
	def FeeLabl(self):
		return self._FeeLabl

	@FeeLabl.setter
	def FeeLabl(self, value):
		self._FeeLabl = value if value is not None else base_types.UninitialisedField(self, 'FeeLabl', Max70Text, False)

	@FeeLabl.deleter
	def FeeLabl(self):
		del self._FeeLabl
		self._FeeLabl = base_types.UninitialisedField(self, 'FeeLabl', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FeeLabl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))