import base_types
import PriceValueType10Code
import RestrictedFINDecimalNumber
import AmountPrice5
import PercentagePrice3

class PriceFormat93Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgPric", "_NotSpcfdPric", "_AmtPric", "_IndxPts"]
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
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if type(value) != auto else self.make_default("IndxPts")

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType10Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPric', type=AmountPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

