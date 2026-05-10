from . import base_types
from ._VolumeMetrics5 import VolumeMetrics5
from ._PriceMetrics3 import PriceMetrics3

class PositionSetMetrics13(base_types._BaseFieldType):

	__slots__ = ["_PricMtrcs", "_VolMtrcs"]
	@property
	def PricMtrcs(self):
		return self._PricMtrcs

	@PricMtrcs.setter
	def PricMtrcs(self, value):
		self._PricMtrcs = value if type(value) != base_types.auto else self.make_default("PricMtrcs")

	@PricMtrcs.deleter
	def PricMtrcs(self):
		del self._PricMtrcs
		self._PricMtrcs = None

	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if type(value) != base_types.auto else self.make_default("VolMtrcs")

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricMtrcs', type=PriceMetrics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics5, min=1, max=1, mutex_group=None, array=False),
	))

