from . import base_types
from ._IntraPositionQueryDefinition8 import IntraPositionQueryDefinition8
from ._SupplementaryData1 import SupplementaryData1

class IntraPositionMovementQueryV01(base_types._BaseFieldType):

	__slots__ = ["_QryDef", "_SplmtryData"]
	@property
	def QryDef(self):
		return self._QryDef

	@QryDef.setter
	def QryDef(self, value):
		self._QryDef = value if type(value) != base_types.auto else self.make_default("QryDef")

	@QryDef.deleter
	def QryDef(self):
		del self._QryDef
		self._QryDef = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryDef', type=IntraPositionQueryDefinition8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

