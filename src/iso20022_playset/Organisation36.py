from . import base_types
from .CountryCode import CountryCode
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .ISODate import ISODate
from .PostalAddress1 import PostalAddress1
from .PartyIdentification140 import PartyIdentification140

class Organisation36(base_types._BaseFieldType):

	__slots__ = ["_RegnDt", "_NtlRegnNb", "_CorpInvstrAdr", "_RegnCtry", "_Nm", "_TaxIdNb", "_TaxtnCtry", "_Id", "_Purp"]
	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if type(value) != auto else self.make_default("RegnDt")

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = None

	@property
	def NtlRegnNb(self):
		return self._NtlRegnNb

	@NtlRegnNb.setter
	def NtlRegnNb(self, value):
		self._NtlRegnNb = value if type(value) != auto else self.make_default("NtlRegnNb")

	@NtlRegnNb.deleter
	def NtlRegnNb(self):
		del self._NtlRegnNb
		self._NtlRegnNb = None

	@property
	def CorpInvstrAdr(self):
		return self._CorpInvstrAdr

	@CorpInvstrAdr.setter
	def CorpInvstrAdr(self, value):
		self._CorpInvstrAdr = value if type(value) != auto else self.make_default("CorpInvstrAdr")

	@CorpInvstrAdr.deleter
	def CorpInvstrAdr(self):
		del self._CorpInvstrAdr
		self._CorpInvstrAdr = None

	@property
	def RegnCtry(self):
		return self._RegnCtry

	@RegnCtry.setter
	def RegnCtry(self, value):
		self._RegnCtry = value if type(value) != auto else self.make_default("RegnCtry")

	@RegnCtry.deleter
	def RegnCtry(self):
		del self._RegnCtry
		self._RegnCtry = None

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
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if type(value) != auto else self.make_default("TaxIdNb")

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = None

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if type(value) != auto else self.make_default("TaxtnCtry")

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = None

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

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpInvstrAdr', type=PostalAddress1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification140, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

