from . import base_types
from ._Address4 import Address4
from ._ContactPersonal2 import ContactPersonal2
from ._Credentials3 import Credentials3
from ._Max105Text import Max105Text
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text

class Customer10(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Age", "_CstmrFileRefNb", "_Ctct", "_GvnNm", "_Id", "_LastNm", "_MddlNm", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Age(self):
		return self._Age

	@Age.setter
	def Age(self, value):
		self._Age = value if type(value) != base_types.auto else self.make_default("Age")

	@Age.deleter
	def Age(self):
		del self._Age
		self._Age = None

	@property
	def CstmrFileRefNb(self):
		return self._CstmrFileRefNb

	@CstmrFileRefNb.setter
	def CstmrFileRefNb(self, value):
		self._CstmrFileRefNb = value if type(value) != base_types.auto else self.make_default("CstmrFileRefNb")

	@CstmrFileRefNb.deleter
	def CstmrFileRefNb(self):
		del self._CstmrFileRefNb
		self._CstmrFileRefNb = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != base_types.auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

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
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if type(value) != base_types.auto else self.make_default("LastNm")

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = None

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if type(value) != base_types.auto else self.make_default("MddlNm")

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = None

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
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Age', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrFileRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
	))

