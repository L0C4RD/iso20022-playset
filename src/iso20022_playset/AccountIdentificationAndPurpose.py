from . import base_types
from .SecuritiesAccountPurposeType1Code import SecuritiesAccountPurposeType1Code
from .AccountIdentification1 import AccountIdentification1

class AccountIdentificationAndPurpose(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Purp"]
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
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AccountIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=SecuritiesAccountPurposeType1Code, min=1, max=1, mutex_group=None, array=False),
	))

