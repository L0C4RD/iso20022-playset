from . import base_types
from .Max35Text import Max35Text
from .PhoneNumber import PhoneNumber
from .Max70Text import Max70Text
from .Max140Text import Max140Text
from .NamePrefix1Code import NamePrefix1Code
from .Max2048Text import Max2048Text

class Contacts3(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Dept", "_PhneNb", "_JobTitl", "_FaxNb", "_Rspnsblty", "_Nm", "_NmPrfx", "_EmailAdr", "_MobNb"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if type(value) != base_types.auto else self.make_default("Dept")

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = None

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
	def JobTitl(self):
		return self._JobTitl

	@JobTitl.setter
	def JobTitl(self, value):
		self._JobTitl = value if type(value) != base_types.auto else self.make_default("JobTitl")

	@JobTitl.deleter
	def JobTitl(self):
		del self._JobTitl
		self._JobTitl = None

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
	def Rspnsblty(self):
		return self._Rspnsblty

	@Rspnsblty.setter
	def Rspnsblty(self, value):
		self._Rspnsblty = value if type(value) != base_types.auto else self.make_default("Rspnsblty")

	@Rspnsblty.deleter
	def Rspnsblty(self):
		del self._Rspnsblty
		self._Rspnsblty = None

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
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if type(value) != base_types.auto else self.make_default("NmPrfx")

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = None

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
	def MobNb(self):
		return self._MobNb

	@MobNb.setter
	def MobNb(self, value):
		self._MobNb = value if type(value) != base_types.auto else self.make_default("MobNb")

	@MobNb.deleter
	def MobNb(self):
		del self._MobNb
		self._MobNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobTitl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspnsblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
	))

