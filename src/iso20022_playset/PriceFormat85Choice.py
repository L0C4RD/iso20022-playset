import base_types
import AmountPrice5
import PercentagePrice2

class PriceFormat85Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgPric", "_AmtPric"]
	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if type(value) != auto else self.make_default("PctgPric")

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = None

	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if type(value) != auto else self.make_default("AmtPric")

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPric', type=AmountPrice5, min=0, max=1, mutex_group=1, array=False),
	))

