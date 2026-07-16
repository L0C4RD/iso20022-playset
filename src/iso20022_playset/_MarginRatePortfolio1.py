# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import Max2000Text

class MarginRatePortfolio1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_LngMrgnRate", "_ShrtMrgnRate"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@property
	def LngMrgnRate(self):
		return self._LngMrgnRate

	@LngMrgnRate.setter
	def LngMrgnRate(self, value):
		self._LngMrgnRate = value if value is not None else base_types.UninitialisedField(self, 'LngMrgnRate', ActiveCurrencyAnd24Amount, False)

	@LngMrgnRate.deleter
	def LngMrgnRate(self):
		del self._LngMrgnRate
		self._LngMrgnRate = base_types.UninitialisedField(self, 'LngMrgnRate', ActiveCurrencyAnd24Amount, False)

	@property
	def ShrtMrgnRate(self):
		return self._ShrtMrgnRate

	@ShrtMrgnRate.setter
	def ShrtMrgnRate(self, value):
		self._ShrtMrgnRate = value if value is not None else base_types.UninitialisedField(self, 'ShrtMrgnRate', ActiveCurrencyAnd24Amount, False)

	@ShrtMrgnRate.deleter
	def ShrtMrgnRate(self):
		del self._ShrtMrgnRate
		self._ShrtMrgnRate = base_types.UninitialisedField(self, 'ShrtMrgnRate', ActiveCurrencyAnd24Amount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngMrgnRate', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMrgnRate', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))