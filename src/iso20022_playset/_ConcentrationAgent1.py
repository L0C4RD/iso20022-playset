from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._ConcentrationAccount1 import ConcentrationAccount1

class ConcentrationAgent1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Acct"]
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
		base_types.FieldEntry(name='Id', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=ConcentrationAccount1, min=1, max=None, mutex_group=None, array=True),
	))

