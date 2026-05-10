import base_types
import QueryType2Code
import StandingOrderCriteria5Choice

class StandingOrderQuery5(base_types._BaseFieldType):

	__slots__ = ["_StgOrdrCrit", "_QryTp"]
	@property
	def StgOrdrCrit(self):
		return self._StgOrdrCrit

	@StgOrdrCrit.setter
	def StgOrdrCrit(self, value):
		self._StgOrdrCrit = value if type(value) != auto else self.make_default("StgOrdrCrit")

	@StgOrdrCrit.deleter
	def StgOrdrCrit(self):
		del self._StgOrdrCrit
		self._StgOrdrCrit = None

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
		base_types.FieldEntry(name='StgOrdrCrit', type=StandingOrderCriteria5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

