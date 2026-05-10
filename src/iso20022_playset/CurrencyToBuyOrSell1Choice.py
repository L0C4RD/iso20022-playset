from . import base_types
from .ActiveCurrencyCode import ActiveCurrencyCode

class CurrencyToBuyOrSell1Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyToSell", "_CcyToBuy"]
	@property
	def CcyToSell(self):
		return self._CcyToSell

	@CcyToSell.setter
	def CcyToSell(self, value):
		self._CcyToSell = value if type(value) != auto else self.make_default("CcyToSell")

	@CcyToSell.deleter
	def CcyToSell(self):
		del self._CcyToSell
		self._CcyToSell = None

	@property
	def CcyToBuy(self):
		return self._CcyToBuy

	@CcyToBuy.setter
	def CcyToBuy(self, value):
		self._CcyToBuy = value if type(value) != auto else self.make_default("CcyToBuy")

	@CcyToBuy.deleter
	def CcyToBuy(self):
		del self._CcyToBuy
		self._CcyToBuy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyToSell', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CcyToBuy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
	))

