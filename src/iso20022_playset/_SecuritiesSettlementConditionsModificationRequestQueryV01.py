# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesModificationQueryDefinition1
from . import SupplementaryData1

class SecuritiesSettlementConditionsModificationRequestQueryV01(base_types._BaseFieldType):

	__slots__ = ["_QryDef", "_SplmtryData"]
	@property
	def QryDef(self):
		return self._QryDef

	@QryDef.setter
	def QryDef(self, value):
		self._QryDef = value if value is not None else base_types.UninitialisedField(self, 'QryDef', SecuritiesModificationQueryDefinition1, False)

	@QryDef.deleter
	def QryDef(self):
		del self._QryDef
		self._QryDef = base_types.UninitialisedField(self, 'QryDef', SecuritiesModificationQueryDefinition1, False)

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
		base_types.FieldEntry(name='QryDef', type=SecuritiesModificationQueryDefinition1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))