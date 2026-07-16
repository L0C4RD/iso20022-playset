# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndicativeOrMarketPrice14Choice
from . import PriceFormat46Choice
from . import PriceFormat79Choice
from . import PriceFormat80Choice
from . import PriceFormat81Choice

class CorporateActionPrice89(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_CshValForTax", "_GncCshPricPdPerPdct", "_GncCshPricRcvdPerPdct", "_IndctvOrMktPric"]
	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat81Choice, False)

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat81Choice, False)

	@property
	def CshValForTax(self):
		return self._CshValForTax

	@CshValForTax.setter
	def CshValForTax(self, value):
		self._CshValForTax = value if value is not None else base_types.UninitialisedField(self, 'CshValForTax', PriceFormat46Choice, False)

	@CshValForTax.deleter
	def CshValForTax(self):
		del self._CshValForTax
		self._CshValForTax = base_types.UninitialisedField(self, 'CshValForTax', PriceFormat46Choice, False)

	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat80Choice, False)

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat80Choice, False)

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat79Choice, False)

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat79Choice, False)

	@property
	def IndctvOrMktPric(self):
		return self._IndctvOrMktPric

	@IndctvOrMktPric.setter
	def IndctvOrMktPric(self, value):
		self._IndctvOrMktPric = value if value is not None else base_types.UninitialisedField(self, 'IndctvOrMktPric', IndicativeOrMarketPrice14Choice, False)

	@IndctvOrMktPric.deleter
	def IndctvOrMktPric(self):
		del self._IndctvOrMktPric
		self._IndctvOrMktPric = base_types.UninitialisedField(self, 'IndctvOrMktPric', IndicativeOrMarketPrice14Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat81Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshValForTax', type=PriceFormat46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat79Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndctvOrMktPric', type=IndicativeOrMarketPrice14Choice, min=0, max=1, mutex_group=None, array=False),
	))