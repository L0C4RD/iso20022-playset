from . import base_types
from ._NonEquitySubClassSegmentationCriteria1Code import NonEquitySubClassSegmentationCriteria1Code
from ._Max1000Text import Max1000Text

class NonEquitySubClassSegmentationCriterion1(base_types._BaseFieldType):

	__slots__ = ["_CritNm", "_CritVal"]
	@property
	def CritNm(self):
		return self._CritNm

	@CritNm.setter
	def CritNm(self, value):
		self._CritNm = value if type(value) != base_types.auto else self.make_default("CritNm")

	@CritNm.deleter
	def CritNm(self):
		del self._CritNm
		self._CritNm = None

	@property
	def CritVal(self):
		return self._CritVal

	@CritVal.setter
	def CritVal(self, value):
		self._CritVal = value if type(value) != base_types.auto else self.make_default("CritVal")

	@CritVal.deleter
	def CritVal(self):
		del self._CritVal
		self._CritVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CritNm', type=NonEquitySubClassSegmentationCriteria1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CritVal', type=Max1000Text, min=1, max=1, mutex_group=None, array=False),
	))

