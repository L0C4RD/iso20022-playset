# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CitizenshipInformation1
from . import CommunicationAddress3
from . import CountryAndResidentialStatusType1
from . import CountryCode
from . import Gender1Code
from . import GenericIdentification44
from . import ISODate
from . import IndividualPersonNameLong2
from . import LanguageCode
from . import Max35Text
from . import PostalAddress27
from . import TransferInstruction1

class IndividualPerson44(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_CityOfBirth", "_CtryAndResdtlSts", "_CtryOfBirth", "_CtznshInf", "_CurNm", "_Gndr", "_Lang", "_OthrDtls", "_OthrId", "_PmryComAdr", "_PrvcOfBirth", "_PrvsNm", "_PstlAdr", "_SclSctyNb", "_ScndryComAdr", "_TaxtnCtry"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if value is not None else base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType1, False)

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType1, False)

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@property
	def CtznshInf(self):
		return self._CtznshInf

	@CtznshInf.setter
	def CtznshInf(self, value):
		self._CtznshInf = value if value is not None else base_types.UninitialisedField(self, 'CtznshInf', CitizenshipInformation1, True)

	@CtznshInf.deleter
	def CtznshInf(self):
		del self._CtznshInf
		self._CtznshInf = base_types.UninitialisedField(self, 'CtznshInf', CitizenshipInformation1, True)

	@property
	def CurNm(self):
		return self._CurNm

	@CurNm.setter
	def CurNm(self, value):
		self._CurNm = value if value is not None else base_types.UninitialisedField(self, 'CurNm', IndividualPersonNameLong2, False)

	@CurNm.deleter
	def CurNm(self):
		del self._CurNm
		self._CurNm = base_types.UninitialisedField(self, 'CurNm', IndividualPersonNameLong2, False)

	@property
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if value is not None else base_types.UninitialisedField(self, 'Gndr', Gender1Code, False)

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = base_types.UninitialisedField(self, 'Gndr', Gender1Code, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@property
	def OthrDtls(self):
		return self._OthrDtls

	@OthrDtls.setter
	def OthrDtls(self, value):
		self._OthrDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrDtls', TransferInstruction1, True)

	@OthrDtls.deleter
	def OthrDtls(self):
		del self._OthrDtls
		self._OthrDtls = base_types.UninitialisedField(self, 'OthrDtls', TransferInstruction1, True)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', GenericIdentification44, True)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', GenericIdentification44, True)

	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if value is not None else base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress3, False)

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress3, False)

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	@property
	def PrvsNm(self):
		return self._PrvsNm

	@PrvsNm.setter
	def PrvsNm(self, value):
		self._PrvsNm = value if value is not None else base_types.UninitialisedField(self, 'PrvsNm', IndividualPersonNameLong2, True)

	@PrvsNm.deleter
	def PrvsNm(self):
		del self._PrvsNm
		self._PrvsNm = base_types.UninitialisedField(self, 'PrvsNm', IndividualPersonNameLong2, True)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress27, True)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress27, True)

	@property
	def SclSctyNb(self):
		return self._SclSctyNb

	@SclSctyNb.setter
	def SclSctyNb(self, value):
		self._SclSctyNb = value if value is not None else base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	@SclSctyNb.deleter
	def SclSctyNb(self):
		del self._SclSctyNb
		self._SclSctyNb = base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	@property
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if value is not None else base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress3, False)

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress3, False)

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if value is not None else base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

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