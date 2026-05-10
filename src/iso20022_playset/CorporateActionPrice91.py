from . import base_types
from .PriceFormat84Choice import PriceFormat84Choice
from .IndicativeOrMarketPrice15Choice import IndicativeOrMarketPrice15Choice
from .PriceFormat83Choice import PriceFormat83Choice

class CorporateActionPrice91(base_types._BaseFieldType):

	__slots__ = ["_GncCshPricRcvdPerPdct", "_IssePric", "_GncCshPricPdPerPdct", "_IndctvOrMktPric"]
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
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if type(value) != auto else self.make_default("IssePric")

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = None

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
	def IndctvOrMktPric(self):
		return self._IndctvOrMktPric

	@IndctvOrMktPric.setter
	def IndctvOrMktPric(self, value):
		self._IndctvOrMktPric = value if type(value) != auto else self.make_default("IndctvOrMktPric")

	@IndctvOrMktPric.deleter
	def IndctvOrMktPric(self):
		del self._IndctvOrMktPric
		self._IndctvOrMktPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat84Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceFormat83Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat83Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndctvOrMktPric', type=IndicativeOrMarketPrice15Choice, min=0, max=1, mutex_group=None, array=False),
	))

