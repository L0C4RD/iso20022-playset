from . import base_types
from ._PriceFormat74Choice import PriceFormat74Choice
from ._PriceFormat46Choice import PriceFormat46Choice
from ._IndicativeOrMarketPrice12Choice import IndicativeOrMarketPrice12Choice
from ._PriceFormat73Choice import PriceFormat73Choice
from ._PriceFormat72Choice import PriceFormat72Choice

class CorporateActionPrice82(base_types._BaseFieldType):

	__slots__ = ["_IndctvOrMktPric", "_CshValForTax", "_GncCshPricRcvdPerPdct", "_CshInLieuOfShrPric", "_GncCshPricPdPerPdct"]
	@property
	def IndctvOrMktPric(self):
		return self._IndctvOrMktPric

	@IndctvOrMktPric.setter
	def IndctvOrMktPric(self, value):
		self._IndctvOrMktPric = value if type(value) != base_types.auto else self.make_default("IndctvOrMktPric")

	@IndctvOrMktPric.deleter
	def IndctvOrMktPric(self):
		del self._IndctvOrMktPric
		self._IndctvOrMktPric = None

	@property
	def CshValForTax(self):
		return self._CshValForTax

	@CshValForTax.setter
	def CshValForTax(self, value):
		self._CshValForTax = value if type(value) != base_types.auto else self.make_default("CshValForTax")

	@CshValForTax.deleter
	def CshValForTax(self):
		del self._CshValForTax
		self._CshValForTax = None

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if type(value) != base_types.auto else self.make_default("GncCshPricRcvdPerPdct")

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = None

	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if type(value) != base_types.auto else self.make_default("CshInLieuOfShrPric")

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = None

	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if type(value) != base_types.auto else self.make_default("GncCshPricPdPerPdct")

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvOrMktPric', type=IndicativeOrMarketPrice12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshValForTax', type=PriceFormat46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat72Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat73Choice, min=0, max=1, mutex_group=None, array=False),
	))

