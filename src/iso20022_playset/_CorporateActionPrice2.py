# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat3Choice

class CorporateActionPrice2(base_types._BaseFieldType):

	__slots__ = ["_MaxPric", "_MinPric"]
	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if value is not None else base_types.UninitialisedField(self, 'MaxPric', PriceFormat3Choice, False)

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = base_types.UninitialisedField(self, 'MaxPric', PriceFormat3Choice, False)

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if value is not None else base_types.UninitialisedField(self, 'MinPric', PriceFormat3Choice, False)

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = base_types.UninitialisedField(self, 'MinPric', PriceFormat3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxPric', type=PriceFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat3Choice, min=0, max=1, mutex_group=None, array=False),
	))