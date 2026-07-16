# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat72Choice
from . import PriceFormat73Choice
from . import PriceFormat74Choice

class PriceDetails39(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_GncCshPricPdPerPdct", "_GncCshPricRcvdPerPdct", "_RedPric"]
	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat74Choice, False)

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat74Choice, False)

	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat73Choice, False)

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat73Choice, False)

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat72Choice, False)

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat72Choice, False)

	@property
	def RedPric(self):
		return self._RedPric

	@RedPric.setter
	def RedPric(self, value):
		self._RedPric = value if value is not None else base_types.UninitialisedField(self, 'RedPric', PriceFormat74Choice, False)

	@RedPric.deleter
	def RedPric(self):
		del self._RedPric
		self._RedPric = base_types.UninitialisedField(self, 'RedPric', PriceFormat74Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat73Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat72Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
	))