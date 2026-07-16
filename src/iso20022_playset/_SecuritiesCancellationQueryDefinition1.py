# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MovementResponseType1Code
from . import SecuritiesCancellationQueryCriteria1

class SecuritiesCancellationQueryDefinition1(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_SchCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', MovementResponseType1Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', MovementResponseType1Code, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', SecuritiesCancellationQueryCriteria1, False)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', SecuritiesCancellationQueryCriteria1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=MovementResponseType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SecuritiesCancellationQueryCriteria1, min=1, max=1, mutex_group=None, array=False),
	))