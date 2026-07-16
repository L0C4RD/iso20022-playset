# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MatchingStatus27Choice
from . import ProcessingStatus70Choice
from . import ProprietaryReason4
from . import SettlementStatus26Choice

class SettlementTransactionStatusType2(base_types._BaseFieldType):

	__slots__ = ["_IfrrdMtchgSts", "_MtchgSts", "_PrcgSts", "_Sttld", "_SttlmSts"]
	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if value is not None else base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus27Choice, True)

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus27Choice, True)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus27Choice, True)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus27Choice, True)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus70Choice, True)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus70Choice, True)

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
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus26Choice, True)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus26Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus27Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus27Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus70Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus26Choice, min=0, max=None, mutex_group=None, array=True),
	))