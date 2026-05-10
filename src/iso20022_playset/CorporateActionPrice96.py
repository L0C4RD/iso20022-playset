import base_types
import PriceFormat91Choice

class CorporateActionPrice96(base_types._BaseFieldType):

	__slots__ = ["_MaxPric", "_FrstBidIncrmtPric", "_LastBidIncrmtPric", "_MinPric"]
	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if type(value) != auto else self.make_default("MaxPric")

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = None

	@property
	def FrstBidIncrmtPric(self):
		return self._FrstBidIncrmtPric

	@FrstBidIncrmtPric.setter
	def FrstBidIncrmtPric(self, value):
		self._FrstBidIncrmtPric = value if type(value) != auto else self.make_default("FrstBidIncrmtPric")

	@FrstBidIncrmtPric.deleter
	def FrstBidIncrmtPric(self):
		del self._FrstBidIncrmtPric
		self._FrstBidIncrmtPric = None

	@property
	def LastBidIncrmtPric(self):
		return self._LastBidIncrmtPric

	@LastBidIncrmtPric.setter
	def LastBidIncrmtPric(self, value):
		self._LastBidIncrmtPric = value if type(value) != auto else self.make_default("LastBidIncrmtPric")

	@LastBidIncrmtPric.deleter
	def LastBidIncrmtPric(self):
		del self._LastBidIncrmtPric
		self._LastBidIncrmtPric = None

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if type(value) != auto else self.make_default("MinPric")

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstBidIncrmtPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastBidIncrmtPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat91Choice, min=0, max=1, mutex_group=None, array=False),
	))

