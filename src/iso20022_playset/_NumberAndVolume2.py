# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DecimalNumberFraction5

class NumberAndVolume2(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_Vol"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', DecimalNumberFraction5, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', DecimalNumberFraction5, False)

	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if value is not None else base_types.UninitialisedField(self, 'Vol', ActiveOrHistoricCurrencyAndAmount, False)

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = base_types.UninitialisedField(self, 'Vol', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=DecimalNumberFraction5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))