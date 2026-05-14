from . import base_types
from ._RiskAssessment4 import RiskAssessment4
from ._RiskInputData3 import RiskInputData3

class RiskContext4(base_types._BaseFieldType):

	__slots__ = ["_Assmnt", "_InptData"]
	@property
	def Assmnt(self):
		return self._Assmnt

	@Assmnt.setter
	def Assmnt(self, value):
		self._Assmnt = value if type(value) != base_types.auto else self.make_default("Assmnt")

	@Assmnt.deleter
	def Assmnt(self):
		del self._Assmnt
		self._Assmnt = None

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if type(value) != base_types.auto else self.make_default("InptData")

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assmnt', type=RiskAssessment4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InptData', type=RiskInputData3, min=0, max=None, mutex_group=None, array=True),
	))

