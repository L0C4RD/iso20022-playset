from . import base_types
import ContactPersonal1
import Max2NumericText
import CompanyAssigner2Code
import Max35Text
import ISOMax3ACountryCode
import DepartureOrArrival1
import AuthorisedAmount2
import TrueFalseIndicator
import AdditionalData1
import Tax41
import LoyaltyProgramme4
import ImpliedCurrencyAndAmount
import Address2
import LodgingActivity1Code
import LodgingRoom2
import DepartureOrArrival2
import PartyIdentification285
import ContactBusiness1
import Max4NumericText
import LodgingLineItem3
import Credentials3
import Location6
import Max70Text

class Lodging4(base_types._BaseFieldType):

	__slots__ = ["_PrprtyId", "_SummryCmmdtyId", "_Dprture", "_AuthrsdAmt", "_PrprtyCtry", "_CstmrAdr", "_Room", "_AddtlData", "_InsrncAmt", "_PrprtyCtct", "_CstmrId", "_NoShow", "_PrprtyAssgnr", "_TtlAmt", "_PrprtyTp", "_CstmrNm", "_LineItm", "_CstmrFileRefNb", "_PrprtyNm", "_FolioNb", "_TtlTax", "_LltyPrgrmm", "_CstmrAge", "_NbOfRooms", "_Drtn", "_PrprtyOthrTp", "_Arrvl", "_Insrnc", "_PrprtyFireSftyAct", "_PrstgsPrprty", "_PrprtyLctn", "_CstmrCtct"]
	@property
	def PrprtyId(self):
		return self._PrprtyId

	@PrprtyId.setter
	def PrprtyId(self, value):
		self._PrprtyId = value if type(value) != auto else self.make_default("PrprtyId")

	@PrprtyId.deleter
	def PrprtyId(self):
		del self._PrprtyId
		self._PrprtyId = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if type(value) != auto else self.make_default("Dprture")

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = None

	@property
	def AuthrsdAmt(self):
		return self._AuthrsdAmt

	@AuthrsdAmt.setter
	def AuthrsdAmt(self, value):
		self._AuthrsdAmt = value if type(value) != auto else self.make_default("AuthrsdAmt")

	@AuthrsdAmt.deleter
	def AuthrsdAmt(self):
		del self._AuthrsdAmt
		self._AuthrsdAmt = None

	@property
	def PrprtyCtry(self):
		return self._PrprtyCtry

	@PrprtyCtry.setter
	def PrprtyCtry(self, value):
		self._PrprtyCtry = value if type(value) != auto else self.make_default("PrprtyCtry")

	@PrprtyCtry.deleter
	def PrprtyCtry(self):
		del self._PrprtyCtry
		self._PrprtyCtry = None

	@property
	def CstmrAdr(self):
		return self._CstmrAdr

	@CstmrAdr.setter
	def CstmrAdr(self, value):
		self._CstmrAdr = value if type(value) != auto else self.make_default("CstmrAdr")

	@CstmrAdr.deleter
	def CstmrAdr(self):
		del self._CstmrAdr
		self._CstmrAdr = None

	@property
	def Room(self):
		return self._Room

	@Room.setter
	def Room(self, value):
		self._Room = value if type(value) != auto else self.make_default("Room")

	@Room.deleter
	def Room(self):
		del self._Room
		self._Room = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def PrprtyCtct(self):
		return self._PrprtyCtct

	@PrprtyCtct.setter
	def PrprtyCtct(self, value):
		self._PrprtyCtct = value if type(value) != auto else self.make_default("PrprtyCtct")

	@PrprtyCtct.deleter
	def PrprtyCtct(self):
		del self._PrprtyCtct
		self._PrprtyCtct = None

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def PrprtyAssgnr(self):
		return self._PrprtyAssgnr

	@PrprtyAssgnr.setter
	def PrprtyAssgnr(self, value):
		self._PrprtyAssgnr = value if type(value) != auto else self.make_default("PrprtyAssgnr")

	@PrprtyAssgnr.deleter
	def PrprtyAssgnr(self):
		del self._PrprtyAssgnr
		self._PrprtyAssgnr = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if type(value) != auto else self.make_default("PrprtyTp")

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = None

	@property
	def CstmrNm(self):
		return self._CstmrNm

	@CstmrNm.setter
	def CstmrNm(self, value):
		self._CstmrNm = value if type(value) != auto else self.make_default("CstmrNm")

	@CstmrNm.deleter
	def CstmrNm(self):
		del self._CstmrNm
		self._CstmrNm = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def CstmrFileRefNb(self):
		return self._CstmrFileRefNb

	@CstmrFileRefNb.setter
	def CstmrFileRefNb(self, value):
		self._CstmrFileRefNb = value if type(value) != auto else self.make_default("CstmrFileRefNb")

	@CstmrFileRefNb.deleter
	def CstmrFileRefNb(self):
		del self._CstmrFileRefNb
		self._CstmrFileRefNb = None

	@property
	def PrprtyNm(self):
		return self._PrprtyNm

	@PrprtyNm.setter
	def PrprtyNm(self, value):
		self._PrprtyNm = value if type(value) != auto else self.make_default("PrprtyNm")

	@PrprtyNm.deleter
	def PrprtyNm(self):
		del self._PrprtyNm
		self._PrprtyNm = None

	@property
	def FolioNb(self):
		return self._FolioNb

	@FolioNb.setter
	def FolioNb(self, value):
		self._FolioNb = value if type(value) != auto else self.make_default("FolioNb")

	@FolioNb.deleter
	def FolioNb(self):
		del self._FolioNb
		self._FolioNb = None

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if type(value) != auto else self.make_default("TtlTax")

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def CstmrAge(self):
		return self._CstmrAge

	@CstmrAge.setter
	def CstmrAge(self, value):
		self._CstmrAge = value if type(value) != auto else self.make_default("CstmrAge")

	@CstmrAge.deleter
	def CstmrAge(self):
		del self._CstmrAge
		self._CstmrAge = None

	@property
	def NbOfRooms(self):
		return self._NbOfRooms

	@NbOfRooms.setter
	def NbOfRooms(self, value):
		self._NbOfRooms = value if type(value) != auto else self.make_default("NbOfRooms")

	@NbOfRooms.deleter
	def NbOfRooms(self):
		del self._NbOfRooms
		self._NbOfRooms = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def PrprtyOthrTp(self):
		return self._PrprtyOthrTp

	@PrprtyOthrTp.setter
	def PrprtyOthrTp(self, value):
		self._PrprtyOthrTp = value if type(value) != auto else self.make_default("PrprtyOthrTp")

	@PrprtyOthrTp.deleter
	def PrprtyOthrTp(self):
		del self._PrprtyOthrTp
		self._PrprtyOthrTp = None

	@property
	def Arrvl(self):
		return self._Arrvl

	@Arrvl.setter
	def Arrvl(self, value):
		self._Arrvl = value if type(value) != auto else self.make_default("Arrvl")

	@Arrvl.deleter
	def Arrvl(self):
		del self._Arrvl
		self._Arrvl = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def PrprtyFireSftyAct(self):
		return self._PrprtyFireSftyAct

	@PrprtyFireSftyAct.setter
	def PrprtyFireSftyAct(self, value):
		self._PrprtyFireSftyAct = value if type(value) != auto else self.make_default("PrprtyFireSftyAct")

	@PrprtyFireSftyAct.deleter
	def PrprtyFireSftyAct(self):
		del self._PrprtyFireSftyAct
		self._PrprtyFireSftyAct = None

	@property
	def PrstgsPrprty(self):
		return self._PrstgsPrprty

	@PrstgsPrprty.setter
	def PrstgsPrprty(self, value):
		self._PrstgsPrprty = value if type(value) != auto else self.make_default("PrstgsPrprty")

	@PrstgsPrprty.deleter
	def PrstgsPrprty(self):
		del self._PrstgsPrprty
		self._PrstgsPrprty = None

	@property
	def PrprtyLctn(self):
		return self._PrprtyLctn

	@PrprtyLctn.setter
	def PrprtyLctn(self, value):
		self._PrprtyLctn = value if type(value) != auto else self.make_default("PrprtyLctn")

	@PrprtyLctn.deleter
	def PrprtyLctn(self):
		del self._PrprtyLctn
		self._PrprtyLctn = None

	@property
	def CstmrCtct(self):
		return self._CstmrCtct

	@CstmrCtct.setter
	def CstmrCtct(self, value):
		self._CstmrCtct = value if type(value) != auto else self.make_default("CstmrCtct")

	@CstmrCtct.deleter
	def CstmrCtct(self):
		del self._CstmrCtct
		self._CstmrCtct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrprtyId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdAmt', type=AuthorisedAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrprtyCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Room', type=LodgingRoom2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrId', type=Credentials3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyAssgnr', type=CompanyAssigner2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyTp', type=LodgingActivity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=LodgingLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrFileRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FolioNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrAge', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfRooms', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Arrvl', type=DepartureOrArrival2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyFireSftyAct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrstgsPrprty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLctn', type=Location6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCtct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
	))

