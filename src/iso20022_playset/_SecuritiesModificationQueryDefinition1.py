from . import base_types
from ._MovementResponseType1Code import MovementResponseType1Code
from ._SecuritiesModificationQueryCriteria1 import SecuritiesModificationQueryCriteria1

class SecuritiesModificationQueryDefinition1(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_SchCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != base_types.auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != base_types.auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=MovementResponseType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SecuritiesModificationQueryCriteria1, min=1, max=1, mutex_group=None, array=False),
	))

