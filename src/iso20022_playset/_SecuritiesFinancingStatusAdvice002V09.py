from . import base_types
from ._SecuritiesFinancingTransactionDetails53 import SecuritiesFinancingTransactionDetails53
from ._MatchingStatus29Choice import MatchingStatus29Choice
from ._ProcessingStatus90Choice import ProcessingStatus90Choice
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionIdentifications35 import TransactionIdentifications35
from ._RepoCallRequestStatus9Choice import RepoCallRequestStatus9Choice
from ._SettlementStatus21Choice import SettlementStatus21Choice

class SecuritiesFinancingStatusAdvice002V09(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_TxDtls", "_PrcgSts", "_SttlmSts", "_MtchgSts", "_RepoCallReqSts", "_SplmtryData", "_IfrrdMtchgSts"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

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
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != base_types.auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def RepoCallReqSts(self):
		return self._RepoCallReqSts

	@RepoCallReqSts.setter
	def RepoCallReqSts(self, value):
		self._RepoCallReqSts = value if type(value) != base_types.auto else self.make_default("RepoCallReqSts")

	@RepoCallReqSts.deleter
	def RepoCallReqSts(self):
		del self._RepoCallReqSts
		self._RepoCallReqSts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications35, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=SecuritiesFinancingTransactionDetails53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus90Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus21Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RepoCallReqSts', type=RepoCallRequestStatus9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus29Choice, min=0, max=1, mutex_group=None, array=False),
	))

