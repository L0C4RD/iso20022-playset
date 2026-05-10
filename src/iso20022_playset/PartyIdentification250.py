from . import base_types
import CountryCode
import Max256Text
import DateAndPlaceOfBirth2
import NaturalPersonIdentification1
import PersonName3
import Max35Text

class PartyIdentification250(base_types._BaseFieldType):

	__slots__ = ["_CpnyRegrShrhldrId", "_EmailAdr", "_DtAndPlcOfBirth", "_Id", "_NmAndAdr", "_Ntlty"]
	@property
	def CpnyRegrShrhldrId(self):
		return self._CpnyRegrShrhldrId

	@CpnyRegrShrhldrId.setter
	def CpnyRegrShrhldrId(self, value):
		self._CpnyRegrShrhldrId = value if type(value) != auto else self.make_default("CpnyRegrShrhldrId")

	@CpnyRegrShrhldrId.deleter
	def CpnyRegrShrhldrId(self):
		del self._CpnyRegrShrhldrId
		self._CpnyRegrShrhldrId = None

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
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if type(value) != auto else self.make_default("DtAndPlcOfBirth")

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = None

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
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpnyRegrShrhldrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=NaturalPersonIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

