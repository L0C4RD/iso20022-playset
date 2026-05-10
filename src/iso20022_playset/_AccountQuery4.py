from . import base_types
from ._QueryType2Code import QueryType2Code
from ._AccountCriteria4Choice import AccountCriteria4Choice

class AccountQuery4(base_types._BaseFieldType):

	__slots__ = ["_AcctCrit", "_QryTp"]
	@property
	def AcctCrit(self):
		return self._AcctCrit

	@AcctCrit.setter
	def AcctCrit(self, value):
		self._AcctCrit = value if type(value) != base_types.auto else self.make_default("AcctCrit")

	@AcctCrit.deleter
	def AcctCrit(self):
		del self._AcctCrit
		self._AcctCrit = None

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
		base_types.FieldEntry(name='AcctCrit', type=AccountCriteria4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

