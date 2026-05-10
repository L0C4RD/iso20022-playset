from . import base_types
from .Balance29 import Balance29
from .ISO8583AccountTypeCode import ISO8583AccountTypeCode

class AccountBalance3(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_AcctTp"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=Balance29, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctTp', type=ISO8583AccountTypeCode, min=1, max=1, mutex_group=None, array=False),
	))

