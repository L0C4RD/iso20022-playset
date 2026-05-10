import base_types
import PriceFormat2Choice

class CorporateActionPrice4(base_types._BaseFieldType):

	__slots__ = ["_IndctvPric", "_MktPric"]
	@property
	def IndctvPric(self):
		return self._IndctvPric

	@IndctvPric.setter
	def IndctvPric(self, value):
		self._IndctvPric = value if type(value) != auto else self.make_default("IndctvPric")

	@IndctvPric.deleter
	def IndctvPric(self):
		del self._IndctvPric
		self._IndctvPric = None

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if type(value) != auto else self.make_default("MktPric")

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvPric', type=PriceFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPric', type=PriceFormat2Choice, min=0, max=1, mutex_group=None, array=False),
	))

