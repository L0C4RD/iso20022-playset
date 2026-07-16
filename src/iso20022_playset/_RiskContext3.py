# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RiskAssessment3
from . import RiskInputData2

class RiskContext3(base_types._BaseFieldType):

	__slots__ = ["_Assmnt", "_InptData"]
	@property
	def Assmnt(self):
		return self._Assmnt

	@Assmnt.setter
	def Assmnt(self, value):
		self._Assmnt = value if value is not None else base_types.UninitialisedField(self, 'Assmnt', RiskAssessment3, True)

	@Assmnt.deleter
	def Assmnt(self):
		del self._Assmnt
		self._Assmnt = base_types.UninitialisedField(self, 'Assmnt', RiskAssessment3, True)

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if value is not None else base_types.UninitialisedField(self, 'InptData', RiskInputData2, True)

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = base_types.UninitialisedField(self, 'InptData', RiskInputData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assmnt', type=RiskAssessment3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InptData', type=RiskInputData2, min=0, max=None, mutex_group=None, array=True),
	))