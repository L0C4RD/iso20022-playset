from . import base_types
from ._OrganisationIdentification31 import OrganisationIdentification31
from ._ModificationProcessingStatus10Choice import ModificationProcessingStatus10Choice
from ._SettlementStatus32Choice import SettlementStatus32Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._MatchingStatus25Choice import MatchingStatus25Choice
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._ProcessingStatus86Choice import ProcessingStatus86Choice
from ._ProcessingStatus87Choice import ProcessingStatus87Choice
from ._ISODateTime import ISODateTime

class StatusTrail12(base_types._BaseFieldType):

	__slots__ = ["_StsDt", "_PrcgSts", "_SttlmSts", "_SndgOrgId", "_ModPrcgSts", "_Sttld", "_CxlSts", "_UsrId", "_SplmtryData", "_IfrrdMtchgSts", "_MtchgSts"]
	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if type(value) != base_types.auto else self.make_default("StsDt")

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != base_types.auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def SndgOrgId(self):
		return self._SndgOrgId

	@SndgOrgId.setter
	def SndgOrgId(self, value):
		self._SndgOrgId = value if type(value) != base_types.auto else self.make_default("SndgOrgId")

	@SndgOrgId.deleter
	def SndgOrgId(self):
		del self._SndgOrgId
		self._SndgOrgId = None

	@property
	def ModPrcgSts(self):
		return self._ModPrcgSts

	@ModPrcgSts.setter
	def ModPrcgSts(self, value):
		self._ModPrcgSts = value if type(value) != base_types.auto else self.make_default("ModPrcgSts")

	@ModPrcgSts.deleter
	def ModPrcgSts(self):
		del self._ModPrcgSts
		self._ModPrcgSts = None

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != base_types.auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if type(value) != base_types.auto else self.make_default("CxlSts")

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = None

	@property
	def UsrId(self):
		return self._UsrId

	@UsrId.setter
	def UsrId(self, value):
		self._UsrId = value if type(value) != base_types.auto else self.make_default("UsrId")

	@UsrId.deleter
	def UsrId(self):
		del self._UsrId
		self._UsrId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if type(value) != base_types.auto else self.make_default("IfrrdMtchgSts")

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != base_types.auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus87Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndgOrgId', type=OrganisationIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModPrcgSts', type=ModificationProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlSts', type=ProcessingStatus86Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus25Choice, min=0, max=1, mutex_group=None, array=False),
	))

