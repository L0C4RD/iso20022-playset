from . import base_types
from .SingleQualifiedPartyIdentification1 import SingleQualifiedPartyIdentification1
from .PartyIdentification2Choice import PartyIdentification2Choice
from .GenericIdentification1 import GenericIdentification1
from .xs:ID import xs:ID
from .Max256Text import Max256Text

class QualifiedPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Id", "_RoleDesc", "_Role", "_ShrtId"]
	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

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

	@property
	def RoleDesc(self):
		return self._RoleDesc

	@RoleDesc.setter
	def RoleDesc(self, value):
		self._RoleDesc = value if type(value) != base_types.auto else self.make_default("RoleDesc")

	@RoleDesc.deleter
	def RoleDesc(self):
		del self._RoleDesc
		self._RoleDesc = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != base_types.auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	@property
	def ShrtId(self):
		return self._ShrtId

	@ShrtId.setter
	def ShrtId(self, value):
		self._ShrtId = value if type(value) != base_types.auto else self.make_default("ShrtId")

	@ShrtId.deleter
	def ShrtId(self):
		del self._ShrtId
		self._ShrtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=SingleQualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoleDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

