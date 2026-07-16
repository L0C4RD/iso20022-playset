# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentRole1FormatChoice
from . import NameAndAddress5
from . import PartyIdentification2Choice

class CorporateActionAgent1(base_types._BaseFieldType):

	__slots__ = ["_AgtId", "_AgtRole", "_CtctPrsn"]
	@property
	def AgtId(self):
		return self._AgtId

	@AgtId.setter
	def AgtId(self, value):
		self._AgtId = value if value is not None else base_types.UninitialisedField(self, 'AgtId', PartyIdentification2Choice, False)

	@AgtId.deleter
	def AgtId(self):
		del self._AgtId
		self._AgtId = base_types.UninitialisedField(self, 'AgtId', PartyIdentification2Choice, False)

	@property
	def AgtRole(self):
		return self._AgtRole

	@AgtRole.setter
	def AgtRole(self, value):
		self._AgtRole = value if value is not None else base_types.UninitialisedField(self, 'AgtRole', AgentRole1FormatChoice, False)

	@AgtRole.deleter
	def AgtRole(self):
		del self._AgtRole
		self._AgtRole = base_types.UninitialisedField(self, 'AgtRole', AgentRole1FormatChoice, False)

	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsn', NameAndAddress5, False)

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = base_types.UninitialisedField(self, 'CtctPrsn', NameAndAddress5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtRole', type=AgentRole1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsn', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
	))