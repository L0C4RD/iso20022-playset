# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndicativeOrMarketPrice13Choice
from . import PriceFormat77Choice
from . import PriceFormat78Choice

class CorporateActionPrice88(base_types._BaseFieldType):

	__slots__ = ["_GncCshPricPdPerPdct", "_GncCshPricRcvdPerPdct", "_IndctvOrMktPric", "_IssePric"]
	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat77Choice, False)

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat77Choice, False)

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat78Choice, False)

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat78Choice, False)

	@property
	def IndctvOrMktPric(self):
		return self._IndctvOrMktPric

	@IndctvOrMktPric.setter
	def IndctvOrMktPric(self, value):
		self._IndctvOrMktPric = value if value is not None else base_types.UninitialisedField(self, 'IndctvOrMktPric', IndicativeOrMarketPrice13Choice, False)

	@IndctvOrMktPric.deleter
	def IndctvOrMktPric(self):
		del self._IndctvOrMktPric
		self._IndctvOrMktPric = base_types.UninitialisedField(self, 'IndctvOrMktPric', IndicativeOrMarketPrice13Choice, False)

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if value is not None else base_types.UninitialisedField(self, 'IssePric', PriceFormat77Choice, False)

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = base_types.UninitialisedField(self, 'IssePric', PriceFormat77Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat77Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat78Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndctvOrMktPric', type=IndicativeOrMarketPrice13Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceFormat77Choice, min=0, max=1, mutex_group=None, array=False),
	))