# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice3
from . import DecimalNumber
from . import PercentagePrice3
from . import PriceValueType10Code

class PriceFormat80Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPric", "_IndxPts", "_NotSpcfdPric", "_PctgPric"]
	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if value is not None else base_types.UninitialisedField(self, 'AmtPric', AmountPrice3, False)

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = base_types.UninitialisedField(self, 'AmtPric', AmountPrice3, False)

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if value is not None else base_types.UninitialisedField(self, 'IndxPts', DecimalNumber, False)

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = base_types.UninitialisedField(self, 'IndxPts', DecimalNumber, False)

	@property
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType10Code, False)

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType10Code, False)

	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if value is not None else base_types.UninitialisedField(self, 'PctgPric', PercentagePrice3, False)

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = base_types.UninitialisedField(self, 'PctgPric', PercentagePrice3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType10Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice3, min=0, max=1, mutex_group=1, array=False),
	))