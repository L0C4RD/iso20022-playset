# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat88Choice
from . import PriceFormat89Choice
from . import PriceFormat90Choice

class PriceDetails42(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_GncCshPricPdPerPdct", "_GncCshPricRcvdPerPdct"]
	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat88Choice, False)

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat88Choice, False)

	@property
	def GncCshPricPdPerPdct(self):
		return self._GncCshPricPdPerPdct

	@GncCshPricPdPerPdct.setter
	def GncCshPricPdPerPdct(self, value):
		self._GncCshPricPdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat89Choice, False)

	@GncCshPricPdPerPdct.deleter
	def GncCshPricPdPerPdct(self):
		del self._GncCshPricPdPerPdct
		self._GncCshPricPdPerPdct = base_types.UninitialisedField(self, 'GncCshPricPdPerPdct', PriceFormat89Choice, False)

	@property
	def GncCshPricRcvdPerPdct(self):
		return self._GncCshPricRcvdPerPdct

	@GncCshPricRcvdPerPdct.setter
	def GncCshPricRcvdPerPdct(self, value):
		self._GncCshPricRcvdPerPdct = value if value is not None else base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat90Choice, False)

	@GncCshPricRcvdPerPdct.deleter
	def GncCshPricRcvdPerPdct(self):
		del self._GncCshPricRcvdPerPdct
		self._GncCshPricRcvdPerPdct = base_types.UninitialisedField(self, 'GncCshPricRcvdPerPdct', PriceFormat90Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat88Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat89Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat90Choice, min=0, max=1, mutex_group=None, array=False),
	))