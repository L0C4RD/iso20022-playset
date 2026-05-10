from . import base_types
from .PartyIdentification285 import PartyIdentification285
from .Max10PositiveNumber import Max10PositiveNumber
from .Max5PositiveNumber import Max5PositiveNumber
from .Max35Text import Max35Text
from .CardDataReading9Code import CardDataReading9Code
from .Frequency12Code import Frequency12Code
from .RiskAssessment1Code import RiskAssessment1Code
from .AdditionalData1 import AdditionalData1
from .ISOMax3ACountryCode import ISOMax3ACountryCode

class Wallet3(base_types._BaseFieldType):

	__slots__ = ["_LastWlltChng", "_PrvdrRskAssmntMdlVrsn", "_AcctAge", "_Actvty", "_PrvdrRskAssmnt", "_CardDataNtryMd", "_ActvtyIntrvl", "_AcctEmailAge", "_AcctCtry", "_PrvdrPhneScore", "_OthrCardDataNtryMd", "_AddtlData", "_UsrAcctAge", "_PANAge", "_PrvdrAcctScore", "_SspdCrds", "_DaysSncLastActvty", "_PrvdrDvcScore", "_Prvdr"]
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
	def OthrCardDataNtryMd(self):
		return self._OthrCardDataNtryMd

	@OthrCardDataNtryMd.setter
	def OthrCardDataNtryMd(self, value):
		self._OthrCardDataNtryMd = value if type(value) != base_types.auto else self.make_default("OthrCardDataNtryMd")

	@OthrCardDataNtryMd.deleter
	def OthrCardDataNtryMd(self):
		del self._OthrCardDataNtryMd
		self._OthrCardDataNtryMd = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

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
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != base_types.auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastWlltChng', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrRskAssmntMdlVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actvty', type=Max10PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrRskAssmnt', type=RiskAssessment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyIntrvl', type=Frequency12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctEmailAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrPhneScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCardDataNtryMd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UsrAcctAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANAge', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrAcctScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspdCrds', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysSncLastActvty', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrDvcScore', type=Max5PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
	))

