# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1000Text
from . import NonEquitySubClassSegmentationCriteria1Code

class NonEquitySubClassSegmentationCriterion1(base_types._BaseFieldType):

	__slots__ = ["_CritNm", "_CritVal"]
	@property
	def CritNm(self):
		return self._CritNm

	@CritNm.setter
	def CritNm(self, value):
		self._CritNm = value if value is not None else base_types.UninitialisedField(self, 'CritNm', NonEquitySubClassSegmentationCriteria1Code, False)

	@CritNm.deleter
	def CritNm(self):
		del self._CritNm
		self._CritNm = base_types.UninitialisedField(self, 'CritNm', NonEquitySubClassSegmentationCriteria1Code, False)

	@property
	def CritVal(self):
		return self._CritVal

	@CritVal.setter
	def CritVal(self, value):
		self._CritVal = value if value is not None else base_types.UninitialisedField(self, 'CritVal', Max1000Text, False)

	@CritVal.deleter
	def CritVal(self):
		del self._CritVal
		self._CritVal = base_types.UninitialisedField(self, 'CritVal', Max1000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CritNm', type=NonEquitySubClassSegmentationCriteria1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CritVal', type=Max1000Text, min=1, max=1, mutex_group=None, array=False),
	))