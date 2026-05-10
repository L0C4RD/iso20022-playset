from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MarketClaimCancellationRequestStatus2Choice import MarketClaimCancellationRequestStatus2Choice
from .CorporateActionOption234 import CorporateActionOption234
from .CorporateActionGeneralInformation181 import CorporateActionGeneralInformation181
from .References26 import References26
from .DocumentIdentification9 import DocumentIdentification9

class MarketClaimCancellationRequestStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MktClmDtls", "_CorpActnGnlInf", "_TxRef", "_MktClmCxlReqSts", "_MktClmCxlReqId"]
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
	def MktClmDtls(self):
		return self._MktClmDtls

	@MktClmDtls.setter
	def MktClmDtls(self, value):
		self._MktClmDtls = value if type(value) != base_types.auto else self.make_default("MktClmDtls")

	@MktClmDtls.deleter
	def MktClmDtls(self):
		del self._MktClmDtls
		self._MktClmDtls = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def TxRef(self):
		return self._TxRef

	@TxRef.setter
	def TxRef(self, value):
		self._TxRef = value if type(value) != base_types.auto else self.make_default("TxRef")

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = None

	@property
	def MktClmCxlReqSts(self):
		return self._MktClmCxlReqSts

	@MktClmCxlReqSts.setter
	def MktClmCxlReqSts(self, value):
		self._MktClmCxlReqSts = value if type(value) != base_types.auto else self.make_default("MktClmCxlReqSts")

	@MktClmCxlReqSts.deleter
	def MktClmCxlReqSts(self):
		del self._MktClmCxlReqSts
		self._MktClmCxlReqSts = None

	@property
	def MktClmCxlReqId(self):
		return self._MktClmCxlReqId

	@MktClmCxlReqId.setter
	def MktClmCxlReqId(self, value):
		self._MktClmCxlReqId = value if type(value) != base_types.auto else self.make_default("MktClmCxlReqId")

	@MktClmCxlReqId.deleter
	def MktClmCxlReqId(self):
		del self._MktClmCxlReqId
		self._MktClmCxlReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRef', type=References26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCxlReqSts', type=MarketClaimCancellationRequestStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCxlReqId', type=DocumentIdentification9, min=1, max=1, mutex_group=None, array=False),
	))

