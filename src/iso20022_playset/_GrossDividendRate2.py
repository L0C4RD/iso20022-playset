# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GrossDividendRateType1FormatChoice

class GrossDividendRate2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateTp"]
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
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', GrossDividendRateType1FormatChoice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', GrossDividendRateType1FormatChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=GrossDividendRateType1FormatChoice, min=1, max=1, mutex_group=None, array=False),
	))