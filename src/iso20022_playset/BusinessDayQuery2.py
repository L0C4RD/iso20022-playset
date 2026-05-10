import base_types
import BusinessDayCriteria3Choice
import QueryType2Code

class BusinessDayQuery2(base_types._BaseFieldType):

	__slots__ = ["_Crit", "_QryTp"]
	@property
	def Crit(self):
		return self._Crit

	@Crit.setter
	def Crit(self, value):
		self._Crit = value if type(value) != auto else self.make_default("Crit")

	@Crit.deleter
	def Crit(self):
		del self._Crit
		self._Crit = None

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
		base_types.FieldEntry(name='Crit', type=BusinessDayCriteria3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

