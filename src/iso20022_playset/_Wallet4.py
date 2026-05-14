from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._CardDataReading12Code import CardDataReading12Code
from ._Frequency12Code import Frequency12Code
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._LocalData20 import LocalData20
from ._Max10PositiveNumber import Max10PositiveNumber
from ._Max35Text import Max35Text
from ._Max5PositiveNumber import Max5PositiveNumber
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._RiskAssessment1Code import RiskAssessment1Code

class Wallet4(base_types._BaseFieldType):

	__slots__ = ["_AcctAge", "_AcctCtry", "_AcctEmailAge", "_Actvty", "_ActvtyIntrvl", "_CardDataNtryMd", "_DaysSncLastActvty", "_LastWlltChng", "_NtlData", "_PANAge", "_PrvdrAcctScore", "_PrvdrAdr", "_PrvdrBizNm", "_PrvdrDvcScore", "_PrvdrId", "_PrvdrLclData", "_PrvdrLglCorpNm", "_PrvdrNm", "_PrvdrPhneScore", "_PrvdrRskAssmnt", "_PrvdrRskAssmntMdlVrsn", "_PrvdrRsnCd", "_PrvtData", "_SspdCrds", "_UsrAcctAge"]
	@property
	def AcctAge(self):
		return self._AcctAge

	@AcctAge.setter
	def AcctAge(self, value):
		self._AcctAge = value if type(value) != base_types.auto else self.make_default("AcctAge")

	@AcctAge.deleter
	def AcctAge(self):
		del self._AcctAge
		self._AcctAge = None

	@property
	def AcctCtry(self):
		return self._AcctCtry

	@AcctCtry.setter
	def AcctCtry(self, value):
		self._AcctCtry = value if type(value) != base_types.auto else self.make_default("AcctCtry")

	@AcctCtry.deleter
	def AcctCtry(self):
		del self._AcctCtry
		self._AcctCtry = None

	@property
	def AcctEmailAge(self):
		return self._AcctEmailAge

	@AcctEmailAge.setter
	def AcctEmailAge(self, value):
		self._AcctEmailAge = value if type(value) != base_types.auto else self.make_default("AcctEmailAge")

	@AcctEmailAge.deleter
	def AcctEmailAge(self):
		del self._AcctEmailAge
		self._AcctEmailAge = None

	@property
	def Actvty(self):
		return self._Actvty

	@Actvty.setter
	def Actvty(self, value):
		self._Actvty = value if type(value) != base_types.auto else self.make_default("Actvty")

	@Actvty.deleter
	def Actvty(self):
		del self._Actvty
		self._Actvty = None

	@property
	def ActvtyIntrvl(self):
		return self._ActvtyIntrvl

	@ActvtyIntrvl.setter
	def ActvtyIntrvl(self, value):
		self._ActvtyIntrvl = value if type(value) != base_types.auto else self.make_default("ActvtyIntrvl")

	@ActvtyIntrvl.deleter
	def ActvtyIntrvl(self):
		del self._ActvtyIntrvl
		self._ActvtyIntrvl = None

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if type(value) != base_types.auto else self.make_default("CardDataNtryMd")

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = None

	@property
	def DaysSncLastActvty(self):
		return self._DaysSncLastActvty

	@DaysSncLastActvty.setter
	def DaysSncLastActvty(self, value):
		self._DaysSncLastActvty = value if type(value) != base_types.auto else self.make_default("DaysSncLastActvty")

	@DaysSncLastActvty.deleter
	def DaysSncLastActvty(self):
		del self._DaysSncLastActvty
		self._DaysSncLastActvty = None

	@property
	def LastWlltChng(self):
		return self._LastWlltChng

	@LastWlltChng.setter
	def LastWlltChng(self, value):
		self._LastWlltChng = value if type(value) != base_types.auto else self.make_default("LastWlltChng")

	@LastWlltChng.deleter
	def LastWlltChng(self):
		del self._LastWlltChng
		self._LastWlltChng = None

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
	def PANAge(self):
		return self._PANAge

	@PANAge.setter
	def PANAge(self, value):
		self._PANAge = value if type(value) != base_types.auto else self.make_default("PANAge")

	@PANAge.deleter
	def PANAge(self):
		del self._PANAge
		self._PANAge = None

	@property
	def PrvdrAcctScore(self):
		return self._PrvdrAcctScore

	@PrvdrAcctScore.setter
	def PrvdrAcctScore(self, value):
		self._PrvdrAcctScore = value if type(value) != base_types.auto else self.make_default("PrvdrAcctScore")

	@PrvdrAcctScore.deleter
	def PrvdrAcctScore(self):
		del self._PrvdrAcctScore
		self._PrvdrAcctScore = None

	@property
	def PrvdrAdr(self):
		return self._PrvdrAdr

	@PrvdrAdr.setter
	def PrvdrAdr(self, value):
		self._PrvdrAdr = value if type(value) != base_types.auto else self.make_default("PrvdrAdr")

	@PrvdrAdr.deleter
	def PrvdrAdr(self):
		del self._PrvdrAdr
		self._PrvdrAdr = None

	@property
	def PrvdrBizNm(self):
		return self._PrvdrBizNm

	@PrvdrBizNm.setter
	def PrvdrBizNm(self, value):
		self._PrvdrBizNm = value if type(value) != base_types.auto else self.make_default("PrvdrBizNm")

	@PrvdrBizNm.deleter
	def PrvdrBizNm(self):
		del self._PrvdrBizNm
		self._PrvdrBizNm = None

	@property
	def PrvdrDvcScore(self):
		return self._PrvdrDvcScore

	@PrvdrDvcScore.setter
	def PrvdrDvcScore(self, value):
		self._PrvdrDvcScore = value if type(value) != base_types.auto else self.make_default("PrvdrDvcScore")

	@PrvdrDvcScore.deleter
	def PrvdrDvcScore(self):
		del self._PrvdrDvcScore
		self._PrvdrDvcScore = None

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if type(value) != base_types.auto else self.make_default("PrvdrId")

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = None

	@property
	def PrvdrLclData(self):
		return self._PrvdrLclData

	@PrvdrLclData.setter
	def PrvdrLclData(self, value):
		self._PrvdrLclData = value if type(value) != base_types.auto else self.make_default("PrvdrLclData")

	@PrvdrLclData.deleter
	def PrvdrLclData(self):
		del self._PrvdrLclData
		self._PrvdrLclData = None

	@property
	def PrvdrLglCorpNm(self):
		return self._PrvdrLglCorpNm

	@PrvdrLglCorpNm.setter
	def PrvdrLglCorpNm(self, value):
		self._PrvdrLglCorpNm = value if type(value) != base_types.auto else self.make_default("PrvdrLglCorpNm")

	@PrvdrLglCorpNm.deleter
	def PrvdrLglCorpNm(self):
		del self._PrvdrLglCorpNm
		self._PrvdrLglCorpNm = None

	@property
	def PrvdrNm(self):
		return self._PrvdrNm

	@PrvdrNm.setter
	def PrvdrNm(self, value):
		self._PrvdrNm = value if type(value) != base_types.auto else self.make_default("PrvdrNm")

	@PrvdrNm.deleter
	def PrvdrNm(self):
		del self._PrvdrNm
		self._PrvdrNm = None

	@property
	def PrvdrPhneScore(self):
		return self._PrvdrPhneScore

	@PrvdrPhneScore.setter
	def PrvdrPhneScore(self, value):
		self._PrvdrPhneScore = value if type(value) != base_types.auto else self.make_default("PrvdrPhneScore")

	@PrvdrPhneScore.deleter
	def PrvdrPhneScore(self):
		del self._PrvdrPhneScore
		self._PrvdrPhneScore = None

	@property
	def PrvdrRskAssmnt(self):
		return self._PrvdrRskAssmnt

	@PrvdrRskAssmnt.setter
	def PrvdrRskAssmnt(self, value):
		self._PrvdrRskAssmnt = value if type(value) != base_types.auto else self.make_default("PrvdrRskAssmnt")

	@PrvdrRskAssmnt.deleter
	def PrvdrRskAssmnt(self):
		del self._PrvdrRskAssmnt
		self._PrvdrRskAssmnt = None

	@property
	def PrvdrRskAssmntMdlVrsn(self):
		return self._PrvdrRskAssmntMdlVrsn

	@PrvdrRskAssmntMdlVrsn.setter
	def PrvdrRskAssmntMdlVrsn(self, value):
		self._PrvdrRskAssmntMdlVrsn = value if type(value) != base_types.auto else self.make_default("PrvdrRskAssmntMdlVrsn")

	@PrvdrRskAssmntMdlVrsn.deleter
	def PrvdrRskAssmntMdlVrsn(self):
		del self._PrvdrRskAssmntMdlVrsn
		self._PrvdrRskAssmntMdlVrsn = None

	@property
	def PrvdrRsnCd(self):
		return self._PrvdrRsnCd

	@PrvdrRsnCd.setter
	def PrvdrRsnCd(self, value):
		self._PrvdrRsnCd = value if type(value) != base_types.auto else self.make_default("PrvdrRsnCd")

	@PrvdrRsnCd.deleter
	def PrvdrRsnCd(self):
		del self._PrvdrRsnCd
		self._PrvdrRsnCd = None

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
	def SspdCrds(self):
		return self._SspdCrds

	@SspdCrds.setter
	def SspdCrds(self, value):
		self._SspdCrds = value if type(value) != base_types.auto else self.make_default("SspdCrds")

	@SspdCrds.deleter
	def SspdCrds(self):
		del self._SspdCrds
		self._SspdCrds = None

	@property
	def UsrAcctAge(self):
		return self._UsrAcctAge

	@UsrAcctAge.setter
	def UsrAcctAge(self, value):
		self._UsrAcctAge = value if type(value) != base_types.auto else self.make_default("UsrAcctAge")

	@UsrAcctAge.deleter
	def UsrAcctAge(self):
		del self._UsrAcctAge
		self._UsrAcctAge = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctEmailAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actvty', type=Max10PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyIntrvl', type=Frequency12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysSncLastActvty', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastWlltChng', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PANAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrAcctScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrDvcScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvdrLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrPhneScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrRskAssmnt', type=RiskAssessment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrRskAssmntMdlVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SspdCrds', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrAcctAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

