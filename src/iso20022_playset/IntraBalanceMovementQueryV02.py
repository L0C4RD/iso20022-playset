import base_types
import SupplementaryData1
import IntraBalanceQueryDefinition11
import DocumentIdentification51

class IntraBalanceMovementQueryV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_QryDef", "_Id"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def QryDef(self):
		return self._QryDef

	@QryDef.setter
	def QryDef(self, value):
		self._QryDef = value if type(value) != auto else self.make_default("QryDef")

	@QryDef.deleter
	def QryDef(self):
		del self._QryDef
		self._QryDef = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QryDef', type=IntraBalanceQueryDefinition11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification51, min=0, max=1, mutex_group=None, array=False),
	))

