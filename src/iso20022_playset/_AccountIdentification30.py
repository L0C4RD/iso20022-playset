from . import base_types
from .AccountInformationType1Code import AccountInformationType1Code
from .AccountIdentification26 import AccountIdentification26

class AccountIdentification30(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_Id"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

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
		base_types.FieldEntry(name='AcctTp', type=AccountInformationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentification26, min=1, max=1, mutex_group=None, array=False),
	))

