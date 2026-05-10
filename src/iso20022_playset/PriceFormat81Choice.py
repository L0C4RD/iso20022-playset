from . import base_types
import PercentagePrice3
import AmountPrice3
import PriceValueType10Code

class PriceFormat81Choice(base_types._BaseFieldType):

	__slots__ = ["_NotSpcfdPric", "_AmtPric", "_PctgPric"]
	@property
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if type(value) != auto else self.make_default("NotSpcfdPric")

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType10Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPric', type=AmountPrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice3, min=0, max=1, mutex_group=1, array=False),
	))

