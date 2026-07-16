# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import MatchingStatus25Choice
from . import Max35Text
from . import ModificationProcessingStatus10Choice
from . import OrganisationIdentification31
from . import ProcessingStatus86Choice
from . import ProcessingStatus87Choice
from . import ProprietaryReason4
from . import SettlementStatus32Choice
from . import SupplementaryData1

class StatusTrail12(base_types._BaseFieldType):

	__slots__ = ["_CxlSts", "_IfrrdMtchgSts", "_ModPrcgSts", "_MtchgSts", "_PrcgSts", "_SndgOrgId", "_SplmtryData", "_StsDt", "_Sttld", "_SttlmSts", "_UsrId"]
	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if value is not None else base_types.UninitialisedField(self, 'CxlSts', ProcessingStatus86Choice, False)

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = base_types.UninitialisedField(self, 'CxlSts', ProcessingStatus86Choice, False)

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if value is not None else base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus25Choice, False)

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus25Choice, False)

	@property
	def ModPrcgSts(self):
		return self._ModPrcgSts

	@ModPrcgSts.setter
	def ModPrcgSts(self, value):
		self._ModPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'ModPrcgSts', ModificationProcessingStatus10Choice, False)

	@ModPrcgSts.deleter
	def ModPrcgSts(self):
		del self._ModPrcgSts
		self._ModPrcgSts = base_types.UninitialisedField(self, 'ModPrcgSts', ModificationProcessingStatus10Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus25Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus25Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus87Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus87Choice, False)

	@property
	def SndgOrgId(self):
		return self._SndgOrgId

	@SndgOrgId.setter
	def SndgOrgId(self, value):
		self._SndgOrgId = value if value is not None else base_types.UninitialisedField(self, 'SndgOrgId', OrganisationIdentification31, False)

	@SndgOrgId.deleter
	def SndgOrgId(self):
		del self._SndgOrgId
		self._SndgOrgId = base_types.UninitialisedField(self, 'SndgOrgId', OrganisationIdentification31, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, False)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus32Choice, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus32Choice, False)

	@property
	def UsrId(self):
		return self._UsrId

	@UsrId.setter
	def UsrId(self, value):
		self._UsrId = value if value is not None else base_types.UninitialisedField(self, 'UsrId', Max35Text, False)

	@UsrId.deleter
	def UsrId(self):
		del self._UsrId
		self._UsrId = base_types.UninitialisedField(self, 'UsrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlSts', type=ProcessingStatus86Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModPrcgSts', type=ModificationProcessingStatus10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus87Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndgOrgId', type=OrganisationIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))