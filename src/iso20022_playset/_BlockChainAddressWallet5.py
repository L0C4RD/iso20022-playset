from . import base_types
from ._Max140Text import Max140Text
from ._CollateralAccountIdentificationType3Choice import CollateralAccountIdentificationType3Choice
from ._Max70Text import Max70Text

class BlockChainAddressWallet5(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Tp", "_Id"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CollateralAccountIdentificationType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

