from . import base_types
import RiskAssessment3
import RiskInputData2

class RiskContext3(base_types._BaseFieldType):

	__slots__ = ["_Assmnt", "_InptData"]
	@property
	def Assmnt(self):
		return self._Assmnt

	@Assmnt.setter
	def Assmnt(self, value):
		self._Assmnt = value if type(value) != auto else self.make_default("Assmnt")

	@Assmnt.deleter
	def Assmnt(self):
		del self._Assmnt
		self._Assmnt = None

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if type(value) != auto else self.make_default("InptData")

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assmnt', type=RiskAssessment3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InptData', type=RiskInputData2, min=0, max=None, mutex_group=None, array=True),
	))

