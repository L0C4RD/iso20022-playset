# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Address2
from . import AuthorisedAmount2
from . import CompanyAssigner2Code
from . import ContactBusiness1
from . import ContactPersonal1
from . import Credentials3
from . import DepartureOrArrival1
from . import DepartureOrArrival2
from . import ISOMax3ACountryCode
from . import ImpliedCurrencyAndAmount
from . import Location6
from . import LodgingActivity1Code
from . import LodgingLineItem3
from . import LodgingRoom2
from . import LoyaltyProgramme4
from . import Max2NumericText
from . import Max35Text
from . import Max4NumericText
from . import Max70Text
from . import PartyIdentification285
from . import Tax41
from . import TrueFalseIndicator

class Lodging4(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Arrvl", "_AuthrsdAmt", "_CstmrAdr", "_CstmrAge", "_CstmrCtct", "_CstmrFileRefNb", "_CstmrId", "_CstmrNm", "_Dprture", "_Drtn", "_FolioNb", "_Insrnc", "_InsrncAmt", "_LineItm", "_LltyPrgrmm", "_NbOfRooms", "_NoShow", "_PrprtyAssgnr", "_PrprtyCtct", "_PrprtyCtry", "_PrprtyFireSftyAct", "_PrprtyId", "_PrprtyLctn", "_PrprtyNm", "_PrprtyOthrTp", "_PrprtyTp", "_PrstgsPrprty", "_Room", "_SummryCmmdtyId", "_TtlAmt", "_TtlTax"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def Arrvl(self):
		return self._Arrvl

	@Arrvl.setter
	def Arrvl(self, value):
		self._Arrvl = value if value is not None else base_types.UninitialisedField(self, 'Arrvl', DepartureOrArrival2, False)

	@Arrvl.deleter
	def Arrvl(self):
		del self._Arrvl
		self._Arrvl = base_types.UninitialisedField(self, 'Arrvl', DepartureOrArrival2, False)

	@property
	def AuthrsdAmt(self):
		return self._AuthrsdAmt

	@AuthrsdAmt.setter
	def AuthrsdAmt(self, value):
		self._AuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdAmt', AuthorisedAmount2, True)

	@AuthrsdAmt.deleter
	def AuthrsdAmt(self):
		del self._AuthrsdAmt
		self._AuthrsdAmt = base_types.UninitialisedField(self, 'AuthrsdAmt', AuthorisedAmount2, True)

	@property
	def CstmrAdr(self):
		return self._CstmrAdr

	@CstmrAdr.setter
	def CstmrAdr(self, value):
		self._CstmrAdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrAdr', Address2, False)

	@CstmrAdr.deleter
	def CstmrAdr(self):
		del self._CstmrAdr
		self._CstmrAdr = base_types.UninitialisedField(self, 'CstmrAdr', Address2, False)

	@property
	def CstmrAge(self):
		return self._CstmrAge

	@CstmrAge.setter
	def CstmrAge(self, value):
		self._CstmrAge = value if value is not None else base_types.UninitialisedField(self, 'CstmrAge', Max2NumericText, False)

	@CstmrAge.deleter
	def CstmrAge(self):
		del self._CstmrAge
		self._CstmrAge = base_types.UninitialisedField(self, 'CstmrAge', Max2NumericText, False)

	@property
	def CstmrCtct(self):
		return self._CstmrCtct

	@CstmrCtct.setter
	def CstmrCtct(self, value):
		self._CstmrCtct = value if value is not None else base_types.UninitialisedField(self, 'CstmrCtct', ContactPersonal1, False)

	@CstmrCtct.deleter
	def CstmrCtct(self):
		del self._CstmrCtct
		self._CstmrCtct = base_types.UninitialisedField(self, 'CstmrCtct', ContactPersonal1, False)

	@property
	def CstmrFileRefNb(self):
		return self._CstmrFileRefNb

	@CstmrFileRefNb.setter
	def CstmrFileRefNb(self, value):
		self._CstmrFileRefNb = value if value is not None else base_types.UninitialisedField(self, 'CstmrFileRefNb', Max70Text, False)

	@CstmrFileRefNb.deleter
	def CstmrFileRefNb(self):
		del self._CstmrFileRefNb
		self._CstmrFileRefNb = base_types.UninitialisedField(self, 'CstmrFileRefNb', Max70Text, False)

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if value is not None else base_types.UninitialisedField(self, 'CstmrId', Credentials3, False)

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = base_types.UninitialisedField(self, 'CstmrId', Credentials3, False)

	@property
	def CstmrNm(self):
		return self._CstmrNm

	@CstmrNm.setter
	def CstmrNm(self, value):
		self._CstmrNm = value if value is not None else base_types.UninitialisedField(self, 'CstmrNm', Max70Text, False)

	@CstmrNm.deleter
	def CstmrNm(self):
		del self._CstmrNm
		self._CstmrNm = base_types.UninitialisedField(self, 'CstmrNm', Max70Text, False)

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if value is not None else base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def FolioNb(self):
		return self._FolioNb

	@FolioNb.setter
	def FolioNb(self, value):
		self._FolioNb = value if value is not None else base_types.UninitialisedField(self, 'FolioNb', Max35Text, False)

	@FolioNb.deleter
	def FolioNb(self):
		del self._FolioNb
		self._FolioNb = base_types.UninitialisedField(self, 'FolioNb', Max35Text, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', LodgingLineItem3, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', LodgingLineItem3, True)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, True)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, True)

	@property
	def NbOfRooms(self):
		return self._NbOfRooms

	@NbOfRooms.setter
	def NbOfRooms(self, value):
		self._NbOfRooms = value if value is not None else base_types.UninitialisedField(self, 'NbOfRooms', Max4NumericText, False)

	@NbOfRooms.deleter
	def NbOfRooms(self):
		del self._NbOfRooms
		self._NbOfRooms = base_types.UninitialisedField(self, 'NbOfRooms', Max4NumericText, False)

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if value is not None else base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@property
	def PrprtyAssgnr(self):
		return self._PrprtyAssgnr

	@PrprtyAssgnr.setter
	def PrprtyAssgnr(self, value):
		self._PrprtyAssgnr = value if value is not None else base_types.UninitialisedField(self, 'PrprtyAssgnr', CompanyAssigner2Code, False)

	@PrprtyAssgnr.deleter
	def PrprtyAssgnr(self):
		del self._PrprtyAssgnr
		self._PrprtyAssgnr = base_types.UninitialisedField(self, 'PrprtyAssgnr', CompanyAssigner2Code, False)

	@property
	def PrprtyCtct(self):
		return self._PrprtyCtct

	@PrprtyCtct.setter
	def PrprtyCtct(self, value):
		self._PrprtyCtct = value if value is not None else base_types.UninitialisedField(self, 'PrprtyCtct', ContactBusiness1, False)

	@PrprtyCtct.deleter
	def PrprtyCtct(self):
		del self._PrprtyCtct
		self._PrprtyCtct = base_types.UninitialisedField(self, 'PrprtyCtct', ContactBusiness1, False)

	@property
	def PrprtyCtry(self):
		return self._PrprtyCtry

	@PrprtyCtry.setter
	def PrprtyCtry(self, value):
		self._PrprtyCtry = value if value is not None else base_types.UninitialisedField(self, 'PrprtyCtry', ISOMax3ACountryCode, False)

	@PrprtyCtry.deleter
	def PrprtyCtry(self):
		del self._PrprtyCtry
		self._PrprtyCtry = base_types.UninitialisedField(self, 'PrprtyCtry', ISOMax3ACountryCode, False)

	@property
	def PrprtyFireSftyAct(self):
		return self._PrprtyFireSftyAct

	@PrprtyFireSftyAct.setter
	def PrprtyFireSftyAct(self, value):
		self._PrprtyFireSftyAct = value if value is not None else base_types.UninitialisedField(self, 'PrprtyFireSftyAct', TrueFalseIndicator, False)

	@PrprtyFireSftyAct.deleter
	def PrprtyFireSftyAct(self):
		del self._PrprtyFireSftyAct
		self._PrprtyFireSftyAct = base_types.UninitialisedField(self, 'PrprtyFireSftyAct', TrueFalseIndicator, False)

	@property
	def PrprtyId(self):
		return self._PrprtyId

	@PrprtyId.setter
	def PrprtyId(self, value):
		self._PrprtyId = value if value is not None else base_types.UninitialisedField(self, 'PrprtyId', PartyIdentification285, False)

	@PrprtyId.deleter
	def PrprtyId(self):
		del self._PrprtyId
		self._PrprtyId = base_types.UninitialisedField(self, 'PrprtyId', PartyIdentification285, False)

	@property
	def PrprtyLctn(self):
		return self._PrprtyLctn

	@PrprtyLctn.setter
	def PrprtyLctn(self, value):
		self._PrprtyLctn = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLctn', Location6, False)

	@PrprtyLctn.deleter
	def PrprtyLctn(self):
		del self._PrprtyLctn
		self._PrprtyLctn = base_types.UninitialisedField(self, 'PrprtyLctn', Location6, False)

	@property
	def PrprtyNm(self):
		return self._PrprtyNm

	@PrprtyNm.setter
	def PrprtyNm(self, value):
		self._PrprtyNm = value if value is not None else base_types.UninitialisedField(self, 'PrprtyNm', Max35Text, False)

	@PrprtyNm.deleter
	def PrprtyNm(self):
		del self._PrprtyNm
		self._PrprtyNm = base_types.UninitialisedField(self, 'PrprtyNm', Max35Text, False)

	@property
	def PrprtyOthrTp(self):
		return self._PrprtyOthrTp

	@PrprtyOthrTp.setter
	def PrprtyOthrTp(self, value):
		self._PrprtyOthrTp = value if value is not None else base_types.UninitialisedField(self, 'PrprtyOthrTp', Max35Text, False)

	@PrprtyOthrTp.deleter
	def PrprtyOthrTp(self):
		del self._PrprtyOthrTp
		self._PrprtyOthrTp = base_types.UninitialisedField(self, 'PrprtyOthrTp', Max35Text, False)

	@property
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if value is not None else base_types.UninitialisedField(self, 'PrprtyTp', LodgingActivity1Code, False)

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = base_types.UninitialisedField(self, 'PrprtyTp', LodgingActivity1Code, False)

	@property
	def PrstgsPrprty(self):
		return self._PrstgsPrprty

	@PrstgsPrprty.setter
	def PrstgsPrprty(self, value):
		self._PrstgsPrprty = value if value is not None else base_types.UninitialisedField(self, 'PrstgsPrprty', Max35Text, False)

	@PrstgsPrprty.deleter
	def PrstgsPrprty(self):
		del self._PrstgsPrprty
		self._PrstgsPrprty = base_types.UninitialisedField(self, 'PrstgsPrprty', Max35Text, False)

	@property
	def Room(self):
		return self._Room

	@Room.setter
	def Room(self, value):
		self._Room = value if value is not None else base_types.UninitialisedField(self, 'Room', LodgingRoom2, True)

	@Room.deleter
	def Room(self):
		del self._Room
		self._Room = base_types.UninitialisedField(self, 'Room', LodgingRoom2, True)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if value is not None else base_types.UninitialisedField(self, 'TtlTax', Tax41, True)

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = base_types.UninitialisedField(self, 'TtlTax', Tax41, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Arrvl', type=DepartureOrArrival2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdAmt', type=AuthorisedAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrAge', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCtct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrFileRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrId', type=Credentials3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FolioNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=LodgingLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfRooms', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyAssgnr', type=CompanyAssigner2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyFireSftyAct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLctn', type=Location6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyTp', type=LodgingActivity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrstgsPrprty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Room', type=LodgingRoom2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
	))