# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MatchingStatus26Choice
from . import ProcessingStatus102Choice
from . import RepoCallRequestStatus7Choice
from . import SecuritiesFinancingTransactionDetails59
from . import SettlementStatus18Choice
from . import SupplementaryData1
from . import TransactionIdentifications53

class SecuritiesFinancingStatusAdviceV11(base_types._BaseFieldType):

	__slots__ = ["_IfrrdMtchgSts", "_MtchgSts", "_PrcgSts", "_RepoCallReqSts", "_SplmtryData", "_SttlmSts", "_TxDtls", "_TxId"]
	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if value is not None else base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus26Choice, False)

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus26Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus26Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus26Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus102Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus102Choice, False)

	@property
	def RepoCallReqSts(self):
		return self._RepoCallReqSts

	@RepoCallReqSts.setter
	def RepoCallReqSts(self, value):
		self._RepoCallReqSts = value if value is not None else base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus7Choice, False)

	@RepoCallReqSts.deleter
	def RepoCallReqSts(self):
		del self._RepoCallReqSts
		self._RepoCallReqSts = base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus7Choice, False)

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
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus18Choice, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus18Choice, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', SecuritiesFinancingTransactionDetails59, False)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', SecuritiesFinancingTransactionDetails59, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifications53, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifications53, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus102Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RepoCallReqSts', type=RepoCallRequestStatus7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=SecuritiesFinancingTransactionDetails59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications53, min=1, max=1, mutex_group=None, array=False),
	))