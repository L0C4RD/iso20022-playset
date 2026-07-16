# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification51
from . import IntraBalanceQueryDefinition10
from . import SupplementaryData1

class IntraBalanceMovementCancellationQueryV02(base_types._BaseFieldType):

	__slots__ = ["_Id", "_QryDef", "_SplmtryData"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification51, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification51, False)

	@property
	def QryDef(self):
		return self._QryDef

	@QryDef.setter
	def QryDef(self, value):
		self._QryDef = value if value is not None else base_types.UninitialisedField(self, 'QryDef', IntraBalanceQueryDefinition10, False)

	@QryDef.deleter
	def QryDef(self):
		del self._QryDef
		self._QryDef = base_types.UninitialisedField(self, 'QryDef', IntraBalanceQueryDefinition10, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryDef', type=IntraBalanceQueryDefinition10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))