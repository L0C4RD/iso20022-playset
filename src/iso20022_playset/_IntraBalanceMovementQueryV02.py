from . import base_types
from ._DocumentIdentification51 import DocumentIdentification51
from ._IntraBalanceQueryDefinition11 import IntraBalanceQueryDefinition11
from ._SupplementaryData1 import SupplementaryData1

class IntraBalanceMovementQueryV02(base_types._BaseFieldType):

	__slots__ = ["_Id", "_QryDef", "_SplmtryData"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
		base_types.FieldEntry(name='Id', type=DocumentIdentification51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryDef', type=IntraBalanceQueryDefinition11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

