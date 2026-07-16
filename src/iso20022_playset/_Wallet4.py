# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import CardDataReading12Code
from . import Frequency12Code
from . import ISOMax3ACountryCode
from . import LocalData20
from . import Max10PositiveNumber
from . import Max35Text
from . import Max5PositiveNumber
from . import Max70Text
from . import Max99Text
from . import RiskAssessment1Code

class Wallet4(base_types._BaseFieldType):

	__slots__ = ["_AcctAge", "_AcctCtry", "_AcctEmailAge", "_Actvty", "_ActvtyIntrvl", "_CardDataNtryMd", "_DaysSncLastActvty", "_LastWlltChng", "_NtlData", "_PANAge", "_PrvdrAcctScore", "_PrvdrAdr", "_PrvdrBizNm", "_PrvdrDvcScore", "_PrvdrId", "_PrvdrLclData", "_PrvdrLglCorpNm", "_PrvdrNm", "_PrvdrPhneScore", "_PrvdrRskAssmnt", "_PrvdrRskAssmntMdlVrsn", "_PrvdrRsnCd", "_PrvtData", "_SspdCrds", "_UsrAcctAge"]
	@property
	def AcctAge(self):
		return self._AcctAge

	@AcctAge.setter
	def AcctAge(self, value):
		self._AcctAge = value if value is not None else base_types.UninitialisedField(self, 'AcctAge', Max5PositiveNumber, False)

	@AcctAge.deleter
	def AcctAge(self):
		del self._AcctAge
		self._AcctAge = base_types.UninitialisedField(self, 'AcctAge', Max5PositiveNumber, False)

	@property
	def AcctCtry(self):
		return self._AcctCtry

	@AcctCtry.setter
	def AcctCtry(self, value):
		self._AcctCtry = value if value is not None else base_types.UninitialisedField(self, 'AcctCtry', ISOMax3ACountryCode, False)

	@AcctCtry.deleter
	def AcctCtry(self):
		del self._AcctCtry
		self._AcctCtry = base_types.UninitialisedField(self, 'AcctCtry', ISOMax3ACountryCode, False)

	@property
	def AcctEmailAge(self):
		return self._AcctEmailAge

	@AcctEmailAge.setter
	def AcctEmailAge(self, value):
		self._AcctEmailAge = value if value is not None else base_types.UninitialisedField(self, 'AcctEmailAge', Max5PositiveNumber, False)

	@AcctEmailAge.deleter
	def AcctEmailAge(self):
		del self._AcctEmailAge
		self._AcctEmailAge = base_types.UninitialisedField(self, 'AcctEmailAge', Max5PositiveNumber, False)

	@property
	def Actvty(self):
		return self._Actvty

	@Actvty.setter
	def Actvty(self, value):
		self._Actvty = value if value is not None else base_types.UninitialisedField(self, 'Actvty', Max10PositiveNumber, False)

	@Actvty.deleter
	def Actvty(self):
		del self._Actvty
		self._Actvty = base_types.UninitialisedField(self, 'Actvty', Max10PositiveNumber, False)

	@property
	def ActvtyIntrvl(self):
		return self._ActvtyIntrvl

	@ActvtyIntrvl.setter
	def ActvtyIntrvl(self, value):
		self._ActvtyIntrvl = value if value is not None else base_types.UninitialisedField(self, 'ActvtyIntrvl', Frequency12Code, False)

	@ActvtyIntrvl.deleter
	def ActvtyIntrvl(self):
		del self._ActvtyIntrvl
		self._ActvtyIntrvl = base_types.UninitialisedField(self, 'ActvtyIntrvl', Frequency12Code, False)

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading12Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading12Code, False)

	@property
	def DaysSncLastActvty(self):
		return self._DaysSncLastActvty

	@DaysSncLastActvty.setter
	def DaysSncLastActvty(self, value):
		self._DaysSncLastActvty = value if value is not None else base_types.UninitialisedField(self, 'DaysSncLastActvty', Max5PositiveNumber, False)

	@DaysSncLastActvty.deleter
	def DaysSncLastActvty(self):
		del self._DaysSncLastActvty
		self._DaysSncLastActvty = base_types.UninitialisedField(self, 'DaysSncLastActvty', Max5PositiveNumber, False)

	@property
	def LastWlltChng(self):
		return self._LastWlltChng

	@LastWlltChng.setter
	def LastWlltChng(self, value):
		self._LastWlltChng = value if value is not None else base_types.UninitialisedField(self, 'LastWlltChng', Max5PositiveNumber, False)

	@LastWlltChng.deleter
	def LastWlltChng(self):
		del self._LastWlltChng
		self._LastWlltChng = base_types.UninitialisedField(self, 'LastWlltChng', Max5PositiveNumber, False)

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
	def PANAge(self):
		return self._PANAge

	@PANAge.setter
	def PANAge(self, value):
		self._PANAge = value if value is not None else base_types.UninitialisedField(self, 'PANAge', Max5PositiveNumber, False)

	@PANAge.deleter
	def PANAge(self):
		del self._PANAge
		self._PANAge = base_types.UninitialisedField(self, 'PANAge', Max5PositiveNumber, False)

	@property
	def PrvdrAcctScore(self):
		return self._PrvdrAcctScore

	@PrvdrAcctScore.setter
	def PrvdrAcctScore(self, value):
		self._PrvdrAcctScore = value if value is not None else base_types.UninitialisedField(self, 'PrvdrAcctScore', Max5PositiveNumber, False)

	@PrvdrAcctScore.deleter
	def PrvdrAcctScore(self):
		del self._PrvdrAcctScore
		self._PrvdrAcctScore = base_types.UninitialisedField(self, 'PrvdrAcctScore', Max5PositiveNumber, False)

	@property
	def PrvdrAdr(self):
		return self._PrvdrAdr

	@PrvdrAdr.setter
	def PrvdrAdr(self, value):
		self._PrvdrAdr = value if value is not None else base_types.UninitialisedField(self, 'PrvdrAdr', Address4, False)

	@PrvdrAdr.deleter
	def PrvdrAdr(self):
		del self._PrvdrAdr
		self._PrvdrAdr = base_types.UninitialisedField(self, 'PrvdrAdr', Address4, False)

	@property
	def PrvdrBizNm(self):
		return self._PrvdrBizNm

	@PrvdrBizNm.setter
	def PrvdrBizNm(self, value):
		self._PrvdrBizNm = value if value is not None else base_types.UninitialisedField(self, 'PrvdrBizNm', Max35Text, False)

	@PrvdrBizNm.deleter
	def PrvdrBizNm(self):
		del self._PrvdrBizNm
		self._PrvdrBizNm = base_types.UninitialisedField(self, 'PrvdrBizNm', Max35Text, False)

	@property
	def PrvdrDvcScore(self):
		return self._PrvdrDvcScore

	@PrvdrDvcScore.setter
	def PrvdrDvcScore(self, value):
		self._PrvdrDvcScore = value if value is not None else base_types.UninitialisedField(self, 'PrvdrDvcScore', Max5PositiveNumber, False)

	@PrvdrDvcScore.deleter
	def PrvdrDvcScore(self):
		del self._PrvdrDvcScore
		self._PrvdrDvcScore = base_types.UninitialisedField(self, 'PrvdrDvcScore', Max5PositiveNumber, False)

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if value is not None else base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@property
	def PrvdrLclData(self):
		return self._PrvdrLclData

	@PrvdrLclData.setter
	def PrvdrLclData(self, value):
		self._PrvdrLclData = value if value is not None else base_types.UninitialisedField(self, 'PrvdrLclData', LocalData20, True)

	@PrvdrLclData.deleter
	def PrvdrLclData(self):
		del self._PrvdrLclData
		self._PrvdrLclData = base_types.UninitialisedField(self, 'PrvdrLclData', LocalData20, True)

	@property
	def PrvdrLglCorpNm(self):
		return self._PrvdrLglCorpNm

	@PrvdrLglCorpNm.setter
	def PrvdrLglCorpNm(self, value):
		self._PrvdrLglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'PrvdrLglCorpNm', Max99Text, False)

	@PrvdrLglCorpNm.deleter
	def PrvdrLglCorpNm(self):
		del self._PrvdrLglCorpNm
		self._PrvdrLglCorpNm = base_types.UninitialisedField(self, 'PrvdrLglCorpNm', Max99Text, False)

	@property
	def PrvdrNm(self):
		return self._PrvdrNm

	@PrvdrNm.setter
	def PrvdrNm(self, value):
		self._PrvdrNm = value if value is not None else base_types.UninitialisedField(self, 'PrvdrNm', Max70Text, False)

	@PrvdrNm.deleter
	def PrvdrNm(self):
		del self._PrvdrNm
		self._PrvdrNm = base_types.UninitialisedField(self, 'PrvdrNm', Max70Text, False)

	@property
	def PrvdrPhneScore(self):
		return self._PrvdrPhneScore

	@PrvdrPhneScore.setter
	def PrvdrPhneScore(self, value):
		self._PrvdrPhneScore = value if value is not None else base_types.UninitialisedField(self, 'PrvdrPhneScore', Max5PositiveNumber, False)

	@PrvdrPhneScore.deleter
	def PrvdrPhneScore(self):
		del self._PrvdrPhneScore
		self._PrvdrPhneScore = base_types.UninitialisedField(self, 'PrvdrPhneScore', Max5PositiveNumber, False)

	@property
	def PrvdrRskAssmnt(self):
		return self._PrvdrRskAssmnt

	@PrvdrRskAssmnt.setter
	def PrvdrRskAssmnt(self, value):
		self._PrvdrRskAssmnt = value if value is not None else base_types.UninitialisedField(self, 'PrvdrRskAssmnt', RiskAssessment1Code, False)

	@PrvdrRskAssmnt.deleter
	def PrvdrRskAssmnt(self):
		del self._PrvdrRskAssmnt
		self._PrvdrRskAssmnt = base_types.UninitialisedField(self, 'PrvdrRskAssmnt', RiskAssessment1Code, False)

	@property
	def PrvdrRskAssmntMdlVrsn(self):
		return self._PrvdrRskAssmntMdlVrsn

	@PrvdrRskAssmntMdlVrsn.setter
	def PrvdrRskAssmntMdlVrsn(self, value):
		self._PrvdrRskAssmntMdlVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrvdrRskAssmntMdlVrsn', Max35Text, False)

	@PrvdrRskAssmntMdlVrsn.deleter
	def PrvdrRskAssmntMdlVrsn(self):
		del self._PrvdrRskAssmntMdlVrsn
		self._PrvdrRskAssmntMdlVrsn = base_types.UninitialisedField(self, 'PrvdrRskAssmntMdlVrsn', Max35Text, False)

	@property
	def PrvdrRsnCd(self):
		return self._PrvdrRsnCd

	@PrvdrRsnCd.setter
	def PrvdrRsnCd(self, value):
		self._PrvdrRsnCd = value if value is not None else base_types.UninitialisedField(self, 'PrvdrRsnCd', Max35Text, False)

	@PrvdrRsnCd.deleter
	def PrvdrRsnCd(self):
		del self._PrvdrRsnCd
		self._PrvdrRsnCd = base_types.UninitialisedField(self, 'PrvdrRsnCd', Max35Text, False)

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
	def SspdCrds(self):
		return self._SspdCrds

	@SspdCrds.setter
	def SspdCrds(self, value):
		self._SspdCrds = value if value is not None else base_types.UninitialisedField(self, 'SspdCrds', Max5PositiveNumber, False)

	@SspdCrds.deleter
	def SspdCrds(self):
		del self._SspdCrds
		self._SspdCrds = base_types.UninitialisedField(self, 'SspdCrds', Max5PositiveNumber, False)

	@property
	def UsrAcctAge(self):
		return self._UsrAcctAge

	@UsrAcctAge.setter
	def UsrAcctAge(self, value):
		self._UsrAcctAge = value if value is not None else base_types.UninitialisedField(self, 'UsrAcctAge', Max5PositiveNumber, False)

	@UsrAcctAge.deleter
	def UsrAcctAge(self):
		del self._UsrAcctAge
		self._UsrAcctAge = base_types.UninitialisedField(self, 'UsrAcctAge', Max5PositiveNumber, False)

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