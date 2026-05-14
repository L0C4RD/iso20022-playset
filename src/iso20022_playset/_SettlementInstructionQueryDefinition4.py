from . import base_types
from ._SettlementInstructionQueryCriteria4 import SettlementInstructionQueryCriteria4
from ._SettlementQueryType1Code import SettlementQueryType1Code

class SettlementInstructionQueryDefinition4(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='QryTp', type=SettlementQueryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SettlementInstructionQueryCriteria4, min=1, max=1, mutex_group=None, array=False),
	))

