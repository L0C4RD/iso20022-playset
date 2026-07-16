# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import AuthorisedAmount2
from . import ContactBusiness1
from . import Customer10
from . import DepartureOrArrival1
from . import DepartureOrArrival2
from . import ISO3NumericCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import LocalData20
from . import LodgingActivity2Code
from . import LodgingLineItem4
from . import LodgingRoom2
from . import LoyaltyProgramme4
from . import Max35Text
from . import Max4NumericText
from . import Max70Text
from . import Max99Text
from . import Tax44
from . import TrueFalseIndicator

class Lodging5(base_types._BaseFieldType):

	__slots__ = ["_Arrvl", "_AuthrsdAmt", "_Cstmr", "_Dprture", "_Drtn", "_FolioNb", "_Insrnc", "_InsrncAmt", "_LineItm", "_LltyPrgrmm", "_NbOfRooms", "_NoShow", "_NtlData", "_PrprtyAdr", "_PrprtyBizNm", "_PrprtyCtct", "_PrprtyFireSftyAct", "_PrprtyId", "_PrprtyLclCcy", "_PrprtyLclData", "_PrprtyLclTmZone", "_PrprtyLctnCd", "_PrprtyLglCorpNm", "_PrprtyNm", "_PrprtyTp", "_PrstgsPrprty", "_PrvtData", "_Room", "_SummryCmmdtyId", "_TtlAmt", "_TtlTax"]
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
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if value is not None else base_types.UninitialisedField(self, 'Cstmr', Customer10, True)

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = base_types.UninitialisedField(self, 'Cstmr', Customer10, True)

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
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', LodgingLineItem4, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', LodgingLineItem4, True)

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrprtyAdr(self):
		return self._PrprtyAdr

	@PrprtyAdr.setter
	def PrprtyAdr(self, value):
		self._PrprtyAdr = value if value is not None else base_types.UninitialisedField(self, 'PrprtyAdr', Address4, False)

	@PrprtyAdr.deleter
	def PrprtyAdr(self):
		del self._PrprtyAdr
		self._PrprtyAdr = base_types.UninitialisedField(self, 'PrprtyAdr', Address4, False)

	@property
	def PrprtyBizNm(self):
		return self._PrprtyBizNm

	@PrprtyBizNm.setter
	def PrprtyBizNm(self, value):
		self._PrprtyBizNm = value if value is not None else base_types.UninitialisedField(self, 'PrprtyBizNm', Max35Text, False)

	@PrprtyBizNm.deleter
	def PrprtyBizNm(self):
		del self._PrprtyBizNm
		self._PrprtyBizNm = base_types.UninitialisedField(self, 'PrprtyBizNm', Max35Text, False)

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
		self._PrprtyId = value if value is not None else base_types.UninitialisedField(self, 'PrprtyId', Max35Text, False)

	@PrprtyId.deleter
	def PrprtyId(self):
		del self._PrprtyId
		self._PrprtyId = base_types.UninitialisedField(self, 'PrprtyId', Max35Text, False)

	@property
	def PrprtyLclCcy(self):
		return self._PrprtyLclCcy

	@PrprtyLclCcy.setter
	def PrprtyLclCcy(self, value):
		self._PrprtyLclCcy = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLclCcy', ISO3NumericCurrencyCode, False)

	@PrprtyLclCcy.deleter
	def PrprtyLclCcy(self):
		del self._PrprtyLclCcy
		self._PrprtyLclCcy = base_types.UninitialisedField(self, 'PrprtyLclCcy', ISO3NumericCurrencyCode, False)

	@property
	def PrprtyLclData(self):
		return self._PrprtyLclData

	@PrprtyLclData.setter
	def PrprtyLclData(self, value):
		self._PrprtyLclData = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLclData', LocalData20, True)

	@PrprtyLclData.deleter
	def PrprtyLclData(self):
		del self._PrprtyLclData
		self._PrprtyLclData = base_types.UninitialisedField(self, 'PrprtyLclData', LocalData20, True)

	@property
	def PrprtyLclTmZone(self):
		return self._PrprtyLclTmZone

	@PrprtyLclTmZone.setter
	def PrprtyLclTmZone(self, value):
		self._PrprtyLclTmZone = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLclTmZone', Max70Text, False)

	@PrprtyLclTmZone.deleter
	def PrprtyLclTmZone(self):
		del self._PrprtyLclTmZone
		self._PrprtyLclTmZone = base_types.UninitialisedField(self, 'PrprtyLclTmZone', Max70Text, False)

	@property
	def PrprtyLctnCd(self):
		return self._PrprtyLctnCd

	@PrprtyLctnCd.setter
	def PrprtyLctnCd(self, value):
		self._PrprtyLctnCd = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLctnCd', Max35Text, False)

	@PrprtyLctnCd.deleter
	def PrprtyLctnCd(self):
		del self._PrprtyLctnCd
		self._PrprtyLctnCd = base_types.UninitialisedField(self, 'PrprtyLctnCd', Max35Text, False)

	@property
	def PrprtyLglCorpNm(self):
		return self._PrprtyLglCorpNm

	@PrprtyLglCorpNm.setter
	def PrprtyLglCorpNm(self, value):
		self._PrprtyLglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'PrprtyLglCorpNm', Max99Text, False)

	@PrprtyLglCorpNm.deleter
	def PrprtyLglCorpNm(self):
		del self._PrprtyLglCorpNm
		self._PrprtyLglCorpNm = base_types.UninitialisedField(self, 'PrprtyLglCorpNm', Max99Text, False)

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
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if value is not None else base_types.UninitialisedField(self, 'PrprtyTp', LodgingActivity2Code, False)

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = base_types.UninitialisedField(self, 'PrprtyTp', LodgingActivity2Code, False)

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
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

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
		self._TtlTax = value if value is not None else base_types.UninitialisedField(self, 'TtlTax', Tax44, True)

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = base_types.UninitialisedField(self, 'TtlTax', Tax44, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Arrvl', type=DepartureOrArrival2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdAmt', type=AuthorisedAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cstmr', type=Customer10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FolioNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=LodgingLineItem4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfRooms', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrprtyAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyFireSftyAct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLclCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrprtyLclTmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLctnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyTp', type=LodgingActivity2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrstgsPrprty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Room', type=LodgingRoom2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
	))