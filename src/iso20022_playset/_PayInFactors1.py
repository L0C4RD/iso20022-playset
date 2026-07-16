# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CurrencyFactors1

class PayInFactors1(base_types._BaseFieldType):

	__slots__ = ["_AggtShrtPosLmt", "_CcyFctrs"]
	@property
	def AggtShrtPosLmt(self):
		return self._AggtShrtPosLmt

	@AggtShrtPosLmt.setter
	def AggtShrtPosLmt(self, value):
		self._AggtShrtPosLmt = value if value is not None else base_types.UninitialisedField(self, 'AggtShrtPosLmt', ActiveCurrencyAndAmount, False)

	@AggtShrtPosLmt.deleter
	def AggtShrtPosLmt(self):
		del self._AggtShrtPosLmt
		self._AggtShrtPosLmt = base_types.UninitialisedField(self, 'AggtShrtPosLmt', ActiveCurrencyAndAmount, False)

	@property
	def CcyFctrs(self):
		return self._CcyFctrs

	@CcyFctrs.setter
	def CcyFctrs(self, value):
		self._CcyFctrs = value if value is not None else base_types.UninitialisedField(self, 'CcyFctrs', CurrencyFactors1, True)

	@CcyFctrs.deleter
	def CcyFctrs(self):
		del self._CcyFctrs
		self._CcyFctrs = base_types.UninitialisedField(self, 'CcyFctrs', CurrencyFactors1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtShrtPosLmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyFctrs', type=CurrencyFactors1, min=1, max=None, mutex_group=None, array=True),
	))