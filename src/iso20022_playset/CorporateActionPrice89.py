import base_types
import PriceFormat46Choice
import PriceFormat80Choice
import PriceFormat81Choice
import PriceFormat79Choice
import IndicativeOrMarketPrice14Choice

class CorporateActionPrice89(base_types._BaseFieldType):

	__slots__ = ["_IndctvOrMktPric", "_GncCshPricRcvdPerPdct", "_CshInLieuOfShrPric", "_GncCshPricPdPerPdct", "_CshValForTax"]
	@property
	def IndctvOrMktPric(self):
		return self._IndctvOrMktPric

	@IndctvOrMktPric.setter
	def IndctvOrMktPric(self, value):
		self._IndctvOrMktPric = value if type(value) != auto else self.make_default("IndctvOrMktPric")

	@IndctvOrMktPric.deleter
	def IndctvOrMktPric(self):
		del self._IndctvOrMktPric
		self._IndctvOrMktPric = None

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if type(value) != auto else self.make_default("GncCshPricRcvdPerPdct")

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = None

	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if type(value) != auto else self.make_default("CshInLieuOfShrPric")

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = None

	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if type(value) != auto else self.make_default("GncCshPricPdPerPdct")

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = None

	@property
	def CshValForTax(self):
		return self._CshValForTax

	@CshValForTax.setter
	def CshValForTax(self, value):
		self._CshValForTax = value if type(value) != auto else self.make_default("CshValForTax")

	@CshValForTax.deleter
	def CshValForTax(self):
		del self._CshValForTax
		self._CshValForTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvOrMktPric', type=IndicativeOrMarketPrice14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat79Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat81Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshValForTax', type=PriceFormat46Choice, min=0, max=1, mutex_group=None, array=False),
	))

