# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._AuthorisedAmount2 import AuthorisedAmount2
from ._ContactBusiness1 import ContactBusiness1
from ._Customer10 import Customer10
from ._DepartureOrArrival1 import DepartureOrArrival1
from ._DepartureOrArrival2 import DepartureOrArrival2
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LocalData20 import LocalData20
from ._LodgingActivity2Code import LodgingActivity2Code
from ._LodgingLineItem4 import LodgingLineItem4
from ._LodgingRoom2 import LodgingRoom2
from ._LoyaltyProgramme4 import LoyaltyProgramme4
from ._Max35Text import Max35Text
from ._Max4NumericText import Max4NumericText
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._Tax44 import Tax44
from ._TrueFalseIndicator import TrueFalseIndicator

class Lodging5(base_types._BaseFieldType):

	__slots__ = ["_Arrvl", "_AuthrsdAmt", "_Cstmr", "_Dprture", "_Drtn", "_FolioNb", "_Insrnc", "_InsrncAmt", "_LineItm", "_LltyPrgrmm", "_NbOfRooms", "_NoShow", "_NtlData", "_PrprtyAdr", "_PrprtyBizNm", "_PrprtyCtct", "_PrprtyFireSftyAct", "_PrprtyId", "_PrprtyLclCcy", "_PrprtyLclData", "_PrprtyLclTmZone", "_PrprtyLctnCd", "_PrprtyLglCorpNm", "_PrprtyNm", "_PrprtyTp", "_PrstgsPrprty", "_PrvtData", "_Room", "_SummryCmmdtyId", "_TtlAmt", "_TtlTax"]
	@property
	def Arrvl(self):
		return self._Arrvl

	@Arrvl.setter
	def Arrvl(self, value):
		self._Arrvl = value if type(value) != base_types.auto else self.make_default("Arrvl")

	@Arrvl.deleter
	def Arrvl(self):
		del self._Arrvl
		self._Arrvl = None

	@property
	def AuthrsdAmt(self):
		return self._AuthrsdAmt

	@AuthrsdAmt.setter
	def AuthrsdAmt(self, value):
		self._AuthrsdAmt = value if type(value) != base_types.auto else self.make_default("AuthrsdAmt")

	@AuthrsdAmt.deleter
	def AuthrsdAmt(self):
		del self._AuthrsdAmt
		self._AuthrsdAmt = None

	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if type(value) != base_types.auto else self.make_default("Cstmr")

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = None

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if type(value) != base_types.auto else self.make_default("Dprture")

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def FolioNb(self):
		return self._FolioNb

	@FolioNb.setter
	def FolioNb(self, value):
		self._FolioNb = value if type(value) != base_types.auto else self.make_default("FolioNb")

	@FolioNb.deleter
	def FolioNb(self):
		del self._FolioNb
		self._FolioNb = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != base_types.auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != base_types.auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != base_types.auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def NbOfRooms(self):
		return self._NbOfRooms

	@NbOfRooms.setter
	def NbOfRooms(self, value):
		self._NbOfRooms = value if type(value) != base_types.auto else self.make_default("NbOfRooms")

	@NbOfRooms.deleter
	def NbOfRooms(self):
		del self._NbOfRooms
		self._NbOfRooms = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != base_types.auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrprtyAdr(self):
		return self._PrprtyAdr

	@PrprtyAdr.setter
	def PrprtyAdr(self, value):
		self._PrprtyAdr = value if type(value) != base_types.auto else self.make_default("PrprtyAdr")

	@PrprtyAdr.deleter
	def PrprtyAdr(self):
		del self._PrprtyAdr
		self._PrprtyAdr = None

	@property
	def PrprtyBizNm(self):
		return self._PrprtyBizNm

	@PrprtyBizNm.setter
	def PrprtyBizNm(self, value):
		self._PrprtyBizNm = value if type(value) != base_types.auto else self.make_default("PrprtyBizNm")

	@PrprtyBizNm.deleter
	def PrprtyBizNm(self):
		del self._PrprtyBizNm
		self._PrprtyBizNm = None

	@property
	def PrprtyCtct(self):
		return self._PrprtyCtct

	@PrprtyCtct.setter
	def PrprtyCtct(self, value):
		self._PrprtyCtct = value if type(value) != base_types.auto else self.make_default("PrprtyCtct")

	@PrprtyCtct.deleter
	def PrprtyCtct(self):
		del self._PrprtyCtct
		self._PrprtyCtct = None

	@property
	def PrprtyFireSftyAct(self):
		return self._PrprtyFireSftyAct

	@PrprtyFireSftyAct.setter
	def PrprtyFireSftyAct(self, value):
		self._PrprtyFireSftyAct = value if type(value) != base_types.auto else self.make_default("PrprtyFireSftyAct")

	@PrprtyFireSftyAct.deleter
	def PrprtyFireSftyAct(self):
		del self._PrprtyFireSftyAct
		self._PrprtyFireSftyAct = None

	@property
	def PrprtyId(self):
		return self._PrprtyId

	@PrprtyId.setter
	def PrprtyId(self, value):
		self._PrprtyId = value if type(value) != base_types.auto else self.make_default("PrprtyId")

	@PrprtyId.deleter
	def PrprtyId(self):
		del self._PrprtyId
		self._PrprtyId = None

	@property
	def PrprtyLclCcy(self):
		return self._PrprtyLclCcy

	@PrprtyLclCcy.setter
	def PrprtyLclCcy(self, value):
		self._PrprtyLclCcy = value if type(value) != base_types.auto else self.make_default("PrprtyLclCcy")

	@PrprtyLclCcy.deleter
	def PrprtyLclCcy(self):
		del self._PrprtyLclCcy
		self._PrprtyLclCcy = None

	@property
	def PrprtyLclData(self):
		return self._PrprtyLclData

	@PrprtyLclData.setter
	def PrprtyLclData(self, value):
		self._PrprtyLclData = value if type(value) != base_types.auto else self.make_default("PrprtyLclData")

	@PrprtyLclData.deleter
	def PrprtyLclData(self):
		del self._PrprtyLclData
		self._PrprtyLclData = None

	@property
	def PrprtyLclTmZone(self):
		return self._PrprtyLclTmZone

	@PrprtyLclTmZone.setter
	def PrprtyLclTmZone(self, value):
		self._PrprtyLclTmZone = value if type(value) != base_types.auto else self.make_default("PrprtyLclTmZone")

	@PrprtyLclTmZone.deleter
	def PrprtyLclTmZone(self):
		del self._PrprtyLclTmZone
		self._PrprtyLclTmZone = None

	@property
	def PrprtyLctnCd(self):
		return self._PrprtyLctnCd

	@PrprtyLctnCd.setter
	def PrprtyLctnCd(self, value):
		self._PrprtyLctnCd = value if type(value) != base_types.auto else self.make_default("PrprtyLctnCd")

	@PrprtyLctnCd.deleter
	def PrprtyLctnCd(self):
		del self._PrprtyLctnCd
		self._PrprtyLctnCd = None

	@property
	def PrprtyLglCorpNm(self):
		return self._PrprtyLglCorpNm

	@PrprtyLglCorpNm.setter
	def PrprtyLglCorpNm(self, value):
		self._PrprtyLglCorpNm = value if type(value) != base_types.auto else self.make_default("PrprtyLglCorpNm")

	@PrprtyLglCorpNm.deleter
	def PrprtyLglCorpNm(self):
		del self._PrprtyLglCorpNm
		self._PrprtyLglCorpNm = None

	@property
	def PrprtyNm(self):
		return self._PrprtyNm

	@PrprtyNm.setter
	def PrprtyNm(self, value):
		self._PrprtyNm = value if type(value) != base_types.auto else self.make_default("PrprtyNm")

	@PrprtyNm.deleter
	def PrprtyNm(self):
		del self._PrprtyNm
		self._PrprtyNm = None

	@property
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if type(value) != base_types.auto else self.make_default("PrprtyTp")

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = None

	@property
	def PrstgsPrprty(self):
		return self._PrstgsPrprty

	@PrstgsPrprty.setter
	def PrstgsPrprty(self, value):
		self._PrstgsPrprty = value if type(value) != base_types.auto else self.make_default("PrstgsPrprty")

	@PrstgsPrprty.deleter
	def PrstgsPrprty(self):
		del self._PrstgsPrprty
		self._PrstgsPrprty = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def Room(self):
		return self._Room

	@Room.setter
	def Room(self, value):
		self._Room = value if type(value) != base_types.auto else self.make_default("Room")

	@Room.deleter
	def Room(self):
		del self._Room
		self._Room = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if type(value) != base_types.auto else self.make_default("TtlTax")

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = None

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