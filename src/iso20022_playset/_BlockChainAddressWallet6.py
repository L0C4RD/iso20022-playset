from . import base_types
from ._RestrictedFINXMax70Text import RestrictedFINXMax70Text
from ._RestrictedFINXMax140Text import RestrictedFINXMax140Text
from ._PurposeCode7Choice import PurposeCode7Choice

class BlockChainAddressWallet6(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Tp", "_Nm"]
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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PurposeCode7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=RestrictedFINXMax70Text, min=0, max=1, mutex_group=None, array=False),
	))

