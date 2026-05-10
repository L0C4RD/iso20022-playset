from . import base_types
import CorporateActionOption234
import DocumentIdentification9
import MarketClaimCancellationRequestStatus2Choice
import References26
import SupplementaryData1
import CorporateActionGeneralInformation181

class MarketClaimCancellationRequestStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_MktClmCxlReqSts", "_MktClmDtls", "_CorpActnGnlInf", "_SplmtryData", "_MktClmCxlReqId", "_TxRef"]
	@property
	def MktClmCxlReqSts(self):
		return self._MktClmCxlReqSts

	@MktClmCxlReqSts.setter
	def MktClmCxlReqSts(self, value):
		self._MktClmCxlReqSts = value if type(value) != auto else self.make_default("MktClmCxlReqSts")

	@MktClmCxlReqSts.deleter
	def MktClmCxlReqSts(self):
		del self._MktClmCxlReqSts
		self._MktClmCxlReqSts = None

	@property
	def MktClmDtls(self):
		return self._MktClmDtls

	@MktClmDtls.setter
	def MktClmDtls(self, value):
		self._MktClmDtls = value if type(value) != auto else self.make_default("MktClmDtls")

	@MktClmDtls.deleter
	def MktClmDtls(self):
		del self._MktClmDtls
		self._MktClmDtls = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def MktClmCxlReqId(self):
		return self._MktClmCxlReqId

	@MktClmCxlReqId.setter
	def MktClmCxlReqId(self, value):
		self._MktClmCxlReqId = value if type(value) != auto else self.make_default("MktClmCxlReqId")

	@MktClmCxlReqId.deleter
	def MktClmCxlReqId(self):
		del self._MktClmCxlReqId
		self._MktClmCxlReqId = None

	@property
	def TxRef(self):
		return self._TxRef

	@TxRef.setter
	def TxRef(self, value):
		self._TxRef = value if type(value) != auto else self.make_default("TxRef")

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktClmCxlReqSts', type=MarketClaimCancellationRequestStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MktClmCxlReqId', type=DocumentIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRef', type=References26, min=1, max=1, mutex_group=None, array=False),
	))

