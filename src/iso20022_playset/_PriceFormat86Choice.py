from . import base_types
from ._AmountPrice5 import AmountPrice5
from ._PercentagePrice2 import PercentagePrice2
from ._RestrictedFINDecimalNumber import RestrictedFINDecimalNumber

class PriceFormat86Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPric", "_IndxPts", "_PctgPric"]
	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if type(value) != base_types.auto else self.make_default("AmtPric")

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = None

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if type(value) != base_types.auto else self.make_default("IndxPts")

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = None

	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if type(value) != base_types.auto else self.make_default("PctgPric")

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
	))

