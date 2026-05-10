import base_types
import RestrictedFINXMax140Text
import RestrictedFINXMax70Text
import RestrictedFINXMax35Text
import PurposeCode8Choice

class BlockChainAddressWallet10(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Tp", "_Dsgnt", "_Id"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

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
		base_types.FieldEntry(name='Nm', type=RestrictedFINXMax70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PurposeCode8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax140Text, min=1, max=1, mutex_group=None, array=False),
	))

