# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISINOct2015Identifier

class CollateralValuation6(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_NmnlAmt"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@property
	def NmnlAmt(self):
		return self._NmnlAmt

	@NmnlAmt.setter
	def NmnlAmt(self, value):
		self._NmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'NmnlAmt', ActiveCurrencyAndAmount, False)

	@NmnlAmt.deleter
	def NmnlAmt(self):
		del self._NmnlAmt
		self._NmnlAmt = base_types.UninitialisedField(self, 'NmnlAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))