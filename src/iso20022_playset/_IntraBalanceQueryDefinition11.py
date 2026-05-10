from . import base_types
from .IntraBalanceQueryCriteria11 import IntraBalanceQueryCriteria11
from .MovementResponseType1Code import MovementResponseType1Code

class IntraBalanceQueryDefinition11(base_types._BaseFieldType):

	__slots__ = ["_SchCrit", "_QryTp"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchCrit', type=IntraBalanceQueryCriteria11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=MovementResponseType1Code, min=1, max=1, mutex_group=None, array=False),
	))

