import base_types
import QueryType2Code
import MemberCriteriaDefinition2Choice

class MemberQueryDefinition4(base_types._BaseFieldType):

	__slots__ = ["_MmbCrit", "_QryTp"]
	@property
	def MmbCrit(self):
		return self._MmbCrit

	@MmbCrit.setter
	def MmbCrit(self, value):
		self._MmbCrit = value if type(value) != auto else self.make_default("MmbCrit")

	@MmbCrit.deleter
	def MmbCrit(self):
		del self._MmbCrit
		self._MmbCrit = None

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbCrit', type=MemberCriteriaDefinition2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

