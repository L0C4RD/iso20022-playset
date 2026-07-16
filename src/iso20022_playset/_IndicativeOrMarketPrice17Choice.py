# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat88Choice

class IndicativeOrMarketPrice17Choice(base_types._BaseFieldType):

	__slots__ = ["_IndctvPric", "_MktPric"]
	@property
	def IndctvPric(self):
		return self._IndctvPric

	@IndctvPric.setter
	def IndctvPric(self, value):
		self._IndctvPric = value if value is not None else base_types.UninitialisedField(self, 'IndctvPric', PriceFormat88Choice, False)

	@IndctvPric.deleter
	def IndctvPric(self):
		del self._IndctvPric
		self._IndctvPric = base_types.UninitialisedField(self, 'IndctvPric', PriceFormat88Choice, False)

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if value is not None else base_types.UninitialisedField(self, 'MktPric', PriceFormat88Choice, False)

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = base_types.UninitialisedField(self, 'MktPric', PriceFormat88Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvPric', type=PriceFormat88Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktPric', type=PriceFormat88Choice, min=0, max=1, mutex_group=1, array=False),
	))