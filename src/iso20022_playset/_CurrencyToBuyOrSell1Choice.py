# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode

class CurrencyToBuyOrSell1Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyToBuy", "_CcyToSell"]
	@property
	def CcyToBuy(self):
		return self._CcyToBuy

	@CcyToBuy.setter
	def CcyToBuy(self, value):
		self._CcyToBuy = value if value is not None else base_types.UninitialisedField(self, 'CcyToBuy', ActiveCurrencyCode, False)

	@CcyToBuy.deleter
	def CcyToBuy(self):
		del self._CcyToBuy
		self._CcyToBuy = base_types.UninitialisedField(self, 'CcyToBuy', ActiveCurrencyCode, False)

	@property
	def CcyToSell(self):
		return self._CcyToSell

	@CcyToSell.setter
	def CcyToSell(self, value):
		self._CcyToSell = value if value is not None else base_types.UninitialisedField(self, 'CcyToSell', ActiveCurrencyCode, False)

	@CcyToSell.deleter
	def CcyToSell(self):
		del self._CcyToSell
		self._CcyToSell = base_types.UninitialisedField(self, 'CcyToSell', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyToBuy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CcyToSell', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
	))