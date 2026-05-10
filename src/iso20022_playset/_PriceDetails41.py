from . import base_types
from ._PriceFormat86Choice import PriceFormat86Choice
from ._PriceFormat87Choice import PriceFormat87Choice
from ._PriceFormat85Choice import PriceFormat85Choice

class PriceDetails41(base_types._BaseFieldType):

	__slots__ = ["_GncCshPricPdPerPdct", "_GncCshPricRcvdPerPdct", "_CshInLieuOfShrPric"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GncCshPricPdPerPdct', type=PriceFormat86Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GncCshPricRcvdPerPdct', type=PriceFormat87Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat85Choice, min=0, max=1, mutex_group=None, array=False),
	))

