# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPMemberType1Code import CCPMemberType1Code
from ._PartyIdentification178Choice import PartyIdentification178Choice

class PartyIdentification242(base_types._BaseFieldType):

	__slots__ = ["_CCPMmbTp", "_Id"]
	@property
	def CCPMmbTp(self):
		return self._CCPMmbTp

	@CCPMmbTp.setter
	def CCPMmbTp(self, value):
		self._CCPMmbTp = value if type(value) != base_types.auto else self.make_default("CCPMmbTp")

	@CCPMmbTp.deleter
	def CCPMmbTp(self):
		del self._CCPMmbTp
		self._CCPMmbTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCPMmbTp', type=CCPMemberType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
	))