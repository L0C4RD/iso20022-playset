from . import base_types
from ._PartyIdentification136 import PartyIdentification136
from ._Account29 import Account29
from ._Role6Choice import Role6Choice

class Intermediary44(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Role", "_Acct"]
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
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=Role6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account29, min=0, max=1, mutex_group=None, array=False),
	))

