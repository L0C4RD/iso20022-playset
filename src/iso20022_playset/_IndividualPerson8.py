from . import base_types
from ._GenderCode import GenderCode
from ._NamePrefix1Code import NamePrefix1Code
from ._Max35Text import Max35Text
from ._PostalAddress1 import PostalAddress1
from ._ISODate import ISODate

class IndividualPerson8(base_types._BaseFieldType):

	__slots__ = ["_SclSctyNb", "_NmSfx", "_Nm", "_Gndr", "_GvnNm", "_BirthDt", "_NmPrfx", "_IndvInvstrAdr"]
	@property
	def SclSctyNb(self):
		return self._SclSctyNb

	@SclSctyNb.setter
	def SclSctyNb(self, value):
		self._SclSctyNb = value if type(value) != base_types.auto else self.make_default("SclSctyNb")

	@SclSctyNb.deleter
	def SclSctyNb(self):
		del self._SclSctyNb
		self._SclSctyNb = None

	@property
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if type(value) != base_types.auto else self.make_default("NmSfx")

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = None

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
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if type(value) != base_types.auto else self.make_default("Gndr")

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = None

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
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != base_types.auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

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
	def IndvInvstrAdr(self):
		return self._IndvInvstrAdr

	@IndvInvstrAdr.setter
	def IndvInvstrAdr(self, value):
		self._IndvInvstrAdr = value if type(value) != base_types.auto else self.make_default("IndvInvstrAdr")

	@IndvInvstrAdr.deleter
	def IndvInvstrAdr(self):
		del self._IndvInvstrAdr
		self._IndvInvstrAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gndr', type=GenderCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvInvstrAdr', type=PostalAddress1, min=1, max=1, mutex_group=None, array=False),
	))

