# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice3
from . import DecimalNumber
from . import PercentagePrice2

class PriceFormat75Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPric", "_IndxPts", "_PctgPric"]
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
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if value is not None else base_types.UninitialisedField(self, 'PctgPric', PercentagePrice2, False)

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = base_types.UninitialisedField(self, 'PctgPric', PercentagePrice2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
	))