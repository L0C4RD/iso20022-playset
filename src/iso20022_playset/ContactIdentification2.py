from . import base_types
import Max256Text
import PhoneNumber
import Max35Text
import NamePrefix1Code

class ContactIdentification2(base_types._BaseFieldType):

	__slots__ = ["_EmailAdr", "_NmPrfx", "_GvnNm", "_FaxNb", "_PhneNb", "_Nm", "_MobNb"]
	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	@property
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if type(value) != auto else self.make_default("NmPrfx")

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

	@property
	def FaxNb(self):
		return self._FaxNb

	@FaxNb.setter
	def FaxNb(self, value):
		self._FaxNb = value if type(value) != auto else self.make_default("FaxNb")

	@FaxNb.deleter
	def FaxNb(self):
		del self._FaxNb
		self._FaxNb = None

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if type(value) != auto else self.make_default("PhneNb")

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = None

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
	def MobNb(self):
		return self._MobNb

	@MobNb.setter
	def MobNb(self, value):
		self._MobNb = value if type(value) != auto else self.make_default("MobNb")

	@MobNb.deleter
	def MobNb(self):
		del self._MobNb
		self._MobNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
	))

