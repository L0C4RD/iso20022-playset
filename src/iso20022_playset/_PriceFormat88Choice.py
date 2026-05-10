from . import base_types
from ._PriceValueType10Code import PriceValueType10Code
from ._PercentagePrice2 import PercentagePrice2
from ._AmountPrice5 import AmountPrice5

class PriceFormat88Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgPric", "_AmtPric", "_NotSpcfdPric"]
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
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if type(value) != base_types.auto else self.make_default("NotSpcfdPric")

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = None

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
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType10Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
	))

