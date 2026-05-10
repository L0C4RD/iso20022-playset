from . import base_types
from .Max35Text import Max35Text
from .Max256Text import Max256Text
from .PhoneNumber import PhoneNumber
from .BICIdentifier import BICIdentifier
from .NamePrefix1Code import NamePrefix1Code

class ContactIdentification3(base_types._BaseFieldType):

	__slots__ = ["_PhneNb", "_FaxNb", "_EmailAdr", "_BIC", "_GvnNm", "_Nm", "_Role", "_NmPrfx"]
	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if type(value) != base_types.auto else self.make_default("PhneNb")

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = None

	@property
	def FaxNb(self):
		return self._FaxNb

	@FaxNb.setter
	def FaxNb(self, value):
		self._FaxNb = value if type(value) != base_types.auto else self.make_default("FaxNb")

	@FaxNb.deleter
	def FaxNb(self):
		del self._FaxNb
		self._FaxNb = None

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != base_types.auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != base_types.auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

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
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if type(value) != base_types.auto else self.make_default("NmPrfx")

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Code, min=0, max=1, mutex_group=None, array=False),
	))

