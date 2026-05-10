from . import base_types
import NameAndAddress5
import AgentRole1FormatChoice
import PartyIdentification2Choice

class CorporateActionAgent1(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_AgtId", "_AgtRole"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	@property
	def AgtId(self):
		return self._AgtId

	@AgtId.setter
	def AgtId(self, value):
		self._AgtId = value if type(value) != auto else self.make_default("AgtId")

	@AgtId.deleter
	def AgtId(self):
		del self._AgtId
		self._AgtId = None

	@property
	def AgtRole(self):
		return self._AgtRole

	@AgtRole.setter
	def AgtRole(self, value):
		self._AgtRole = value if type(value) != auto else self.make_default("AgtRole")

	@AgtRole.deleter
	def AgtRole(self):
		del self._AgtRole
		self._AgtRole = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtRole', type=AgentRole1FormatChoice, min=1, max=1, mutex_group=None, array=False),
	))

