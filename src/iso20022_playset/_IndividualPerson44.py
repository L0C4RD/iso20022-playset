from . import base_types
from ._CitizenshipInformation1 import CitizenshipInformation1
from ._CommunicationAddress3 import CommunicationAddress3
from ._CountryAndResidentialStatusType1 import CountryAndResidentialStatusType1
from ._CountryCode import CountryCode
from ._Gender1Code import Gender1Code
from ._GenericIdentification44 import GenericIdentification44
from ._ISODate import ISODate
from ._IndividualPersonNameLong2 import IndividualPersonNameLong2
from ._LanguageCode import LanguageCode
from ._Max35Text import Max35Text
from ._PostalAddress27 import PostalAddress27
from ._TransferInstruction1 import TransferInstruction1

class IndividualPerson44(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_CityOfBirth", "_CtryAndResdtlSts", "_CtryOfBirth", "_CtznshInf", "_CurNm", "_Gndr", "_Lang", "_OthrDtls", "_OthrId", "_PmryComAdr", "_PrvcOfBirth", "_PrvsNm", "_PstlAdr", "_SclSctyNb", "_ScndryComAdr", "_TaxtnCtry"]
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
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if type(value) != base_types.auto else self.make_default("CityOfBirth")

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = None

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if type(value) != base_types.auto else self.make_default("CtryAndResdtlSts")

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != base_types.auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	@property
	def CtznshInf(self):
		return self._CtznshInf

	@CtznshInf.setter
	def CtznshInf(self, value):
		self._CtznshInf = value if type(value) != base_types.auto else self.make_default("CtznshInf")

	@CtznshInf.deleter
	def CtznshInf(self):
		del self._CtznshInf
		self._CtznshInf = None

	@property
	def CurNm(self):
		return self._CurNm

	@CurNm.setter
	def CurNm(self, value):
		self._CurNm = value if type(value) != base_types.auto else self.make_default("CurNm")

	@CurNm.deleter
	def CurNm(self):
		del self._CurNm
		self._CurNm = None

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
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def OthrDtls(self):
		return self._OthrDtls

	@OthrDtls.setter
	def OthrDtls(self, value):
		self._OthrDtls = value if type(value) != base_types.auto else self.make_default("OthrDtls")

	@OthrDtls.deleter
	def OthrDtls(self):
		del self._OthrDtls
		self._OthrDtls = None

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if type(value) != base_types.auto else self.make_default("OthrId")

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = None

	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if type(value) != base_types.auto else self.make_default("PmryComAdr")

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = None

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if type(value) != base_types.auto else self.make_default("PrvcOfBirth")

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = None

	@property
	def PrvsNm(self):
		return self._PrvsNm

	@PrvsNm.setter
	def PrvsNm(self, value):
		self._PrvsNm = value if type(value) != base_types.auto else self.make_default("PrvsNm")

	@PrvsNm.deleter
	def PrvsNm(self):
		del self._PrvsNm
		self._PrvsNm = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

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
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if type(value) != base_types.auto else self.make_default("ScndryComAdr")

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = None

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if type(value) != base_types.auto else self.make_default("TaxtnCtry")

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryAndResdtlSts', type=CountryAndResidentialStatusType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtznshInf', type=CitizenshipInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurNm', type=IndividualPersonNameLong2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gndr', type=Gender1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDtls', type=TransferInstruction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsNm', type=IndividualPersonNameLong2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress27, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

