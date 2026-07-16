# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceMetrics3
from . import VolumeMetrics5

class PositionSetMetrics13(base_types._BaseFieldType):

	__slots__ = ["_PricMtrcs", "_VolMtrcs"]
	@property
	def PricMtrcs(self):
		return self._PricMtrcs

	@PricMtrcs.setter
	def PricMtrcs(self, value):
		self._PricMtrcs = value if value is not None else base_types.UninitialisedField(self, 'PricMtrcs', PriceMetrics3, False)

	@PricMtrcs.deleter
	def PricMtrcs(self):
		del self._PricMtrcs
		self._PricMtrcs = base_types.UninitialisedField(self, 'PricMtrcs', PriceMetrics3, False)

	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if value is not None else base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics5, False)

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricMtrcs', type=PriceMetrics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics5, min=1, max=1, mutex_group=None, array=False),
	))