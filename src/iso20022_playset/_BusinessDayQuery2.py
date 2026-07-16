# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDayCriteria3Choice
from . import QueryType2Code

class BusinessDayQuery2(base_types._BaseFieldType):

	__slots__ = ["_Crit", "_QryTp"]
	@property
	def Crit(self):
		return self._Crit

	@Crit.setter
	def Crit(self, value):
		self._Crit = value if value is not None else base_types.UninitialisedField(self, 'Crit', BusinessDayCriteria3Choice, False)

	@Crit.deleter
	def Crit(self):
		del self._Crit
		self._Crit = base_types.UninitialisedField(self, 'Crit', BusinessDayCriteria3Choice, False)

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
		base_types.FieldEntry(name='Crit', type=BusinessDayCriteria3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))