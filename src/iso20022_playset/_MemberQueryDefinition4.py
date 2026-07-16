# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MemberCriteriaDefinition2Choice
from . import QueryType2Code

class MemberQueryDefinition4(base_types._BaseFieldType):

	__slots__ = ["_MmbCrit", "_QryTp"]
	@property
	def MmbCrit(self):
		return self._MmbCrit

	@MmbCrit.setter
	def MmbCrit(self, value):
		self._MmbCrit = value if value is not None else base_types.UninitialisedField(self, 'MmbCrit', MemberCriteriaDefinition2Choice, False)

	@MmbCrit.deleter
	def MmbCrit(self):
		del self._MmbCrit
		self._MmbCrit = base_types.UninitialisedField(self, 'MmbCrit', MemberCriteriaDefinition2Choice, False)

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
		base_types.FieldEntry(name='MmbCrit', type=MemberCriteriaDefinition2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))