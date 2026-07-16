# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat91Choice

class CorporateActionPrice96(base_types._BaseFieldType):

	__slots__ = ["_FrstBidIncrmtPric", "_LastBidIncrmtPric", "_MaxPric", "_MinPric"]
	@property
	def FrstBidIncrmtPric(self):
		return self._FrstBidIncrmtPric

	@FrstBidIncrmtPric.setter
	def FrstBidIncrmtPric(self, value):
		self._FrstBidIncrmtPric = value if value is not None else base_types.UninitialisedField(self, 'FrstBidIncrmtPric', PriceFormat91Choice, False)

	@FrstBidIncrmtPric.deleter
	def FrstBidIncrmtPric(self):
		del self._FrstBidIncrmtPric
		self._FrstBidIncrmtPric = base_types.UninitialisedField(self, 'FrstBidIncrmtPric', PriceFormat91Choice, False)

	@property
	def LastBidIncrmtPric(self):
		return self._LastBidIncrmtPric

	@LastBidIncrmtPric.setter
	def LastBidIncrmtPric(self, value):
		self._LastBidIncrmtPric = value if value is not None else base_types.UninitialisedField(self, 'LastBidIncrmtPric', PriceFormat91Choice, False)

	@LastBidIncrmtPric.deleter
	def LastBidIncrmtPric(self):
		del self._LastBidIncrmtPric
		self._LastBidIncrmtPric = base_types.UninitialisedField(self, 'LastBidIncrmtPric', PriceFormat91Choice, False)

	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if value is not None else base_types.UninitialisedField(self, 'MaxPric', PriceFormat91Choice, False)

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = base_types.UninitialisedField(self, 'MaxPric', PriceFormat91Choice, False)

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if value is not None else base_types.UninitialisedField(self, 'MinPric', PriceFormat91Choice, False)

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = base_types.UninitialisedField(self, 'MinPric', PriceFormat91Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstBidIncrmtPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastBidIncrmtPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
	))