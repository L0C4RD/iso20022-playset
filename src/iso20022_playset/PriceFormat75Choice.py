from . import base_types
import DecimalNumber
import PercentagePrice2
import AmountPrice3

class PriceFormat75Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgPric", "_AmtPric", "_IndxPts"]
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
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPric', type=AmountPrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

