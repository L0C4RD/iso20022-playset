from . import base_types
import PartyIdentification157
import Role7Choice
import Account30

class Intermediary45(base_types._BaseFieldType):

	__slots__ = ["_Role", "_Acct", "_Id"]
	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Role', type=Role7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification157, min=1, max=1, mutex_group=None, array=False),
	))

