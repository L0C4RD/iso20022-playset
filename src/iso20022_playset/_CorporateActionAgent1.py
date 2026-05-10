from . import base_types
from ._AgentRole1FormatChoice import AgentRole1FormatChoice
from ._NameAndAddress5 import NameAndAddress5
from ._PartyIdentification2Choice import PartyIdentification2Choice

class CorporateActionAgent1(base_types._BaseFieldType):

	__slots__ = ["_AgtRole", "_AgtId", "_CtctPrsn"]
	@property
	def AgtRole(self):
		return self._AgtRole

	@AgtRole.setter
	def AgtRole(self, value):
		self._AgtRole = value if type(value) != base_types.auto else self.make_default("AgtRole")

	@AgtRole.deleter
	def AgtRole(self):
		del self._AgtRole
		self._AgtRole = None

	@property
	def AgtId(self):
		return self._AgtId

	@AgtId.setter
	def AgtId(self, value):
		self._AgtId = value if type(value) != base_types.auto else self.make_default("AgtId")

	@AgtId.deleter
	def AgtId(self):
		del self._AgtId
		self._AgtId = None

	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != base_types.auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtRole', type=AgentRole1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsn', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
	))

