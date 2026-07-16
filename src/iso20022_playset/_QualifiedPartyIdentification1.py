# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import Max256Text
from . import PartyIdentification2Choice
from . import SingleQualifiedPartyIdentification1
from . import xs:ID

class QualifiedPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Pty", "_Role", "_RoleDesc", "_ShrtId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', xs:ID, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', xs:ID, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', SingleQualifiedPartyIdentification1, True)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', SingleQualifiedPartyIdentification1, True)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', GenericIdentification1, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', GenericIdentification1, False)

	@property
	def RoleDesc(self):
		return self._RoleDesc

	@RoleDesc.setter
	def RoleDesc(self, value):
		self._RoleDesc = value if value is not None else base_types.UninitialisedField(self, 'RoleDesc', Max256Text, False)

	@RoleDesc.deleter
	def RoleDesc(self):
		del self._RoleDesc
		self._RoleDesc = base_types.UninitialisedField(self, 'RoleDesc', Max256Text, False)

	@property
	def ShrtId(self):
		return self._ShrtId

	@ShrtId.setter
	def ShrtId(self, value):
		self._ShrtId = value if value is not None else base_types.UninitialisedField(self, 'ShrtId', PartyIdentification2Choice, False)

	@ShrtId.deleter
	def ShrtId(self):
		del self._ShrtId
		self._ShrtId = base_types.UninitialisedField(self, 'ShrtId', PartyIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=SingleQualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Role', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoleDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))