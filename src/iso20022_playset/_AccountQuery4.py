# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountCriteria4Choice
from . import QueryType2Code

class AccountQuery4(base_types._BaseFieldType):

	__slots__ = ["_AcctCrit", "_QryTp"]
	@property
	def AcctCrit(self):
		return self._AcctCrit

	@AcctCrit.setter
	def AcctCrit(self, value):
		self._AcctCrit = value if value is not None else base_types.UninitialisedField(self, 'AcctCrit', AccountCriteria4Choice, False)

	@AcctCrit.deleter
	def AcctCrit(self):
		del self._AcctCrit
		self._AcctCrit = base_types.UninitialisedField(self, 'AcctCrit', AccountCriteria4Choice, False)

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctCrit', type=AccountCriteria4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))