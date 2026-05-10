from . import base_types
from .PurposeCode8Choice import PurposeCode8Choice
from .RestrictedFINXMax35Text import RestrictedFINXMax35Text
from .RestrictedFINXMax140Text import RestrictedFINXMax140Text
from .RestrictedFINXMax70Text import RestrictedFINXMax70Text

class BlockChainAddressWallet10(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Id", "_Tp", "_Dsgnt"]
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
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != base_types.auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=RestrictedFINXMax70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PurposeCode8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
	))

