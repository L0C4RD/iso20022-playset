# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionGeneralInformation181
from . import CorporateActionOption234
from . import DocumentIdentification9
from . import MarketClaimCancellationRequestStatus2Choice
from . import References26
from . import SupplementaryData1

class MarketClaimCancellationRequestStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_MktClmCxlReqId", "_MktClmCxlReqSts", "_MktClmDtls", "_SplmtryData", "_TxRef"]
	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation181, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation181, False)

	@property
	def MktClmCxlReqId(self):
		return self._MktClmCxlReqId

	@MktClmCxlReqId.setter
	def MktClmCxlReqId(self, value):
		self._MktClmCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'MktClmCxlReqId', DocumentIdentification9, False)

	@MktClmCxlReqId.deleter
	def MktClmCxlReqId(self):
		del self._MktClmCxlReqId
		self._MktClmCxlReqId = base_types.UninitialisedField(self, 'MktClmCxlReqId', DocumentIdentification9, False)

	@property
	def MktClmCxlReqSts(self):
		return self._MktClmCxlReqSts

	@MktClmCxlReqSts.setter
	def MktClmCxlReqSts(self, value):
		self._MktClmCxlReqSts = value if value is not None else base_types.UninitialisedField(self, 'MktClmCxlReqSts', MarketClaimCancellationRequestStatus2Choice, False)

	@MktClmCxlReqSts.deleter
	def MktClmCxlReqSts(self):
		del self._MktClmCxlReqSts
		self._MktClmCxlReqSts = base_types.UninitialisedField(self, 'MktClmCxlReqSts', MarketClaimCancellationRequestStatus2Choice, False)

	@property
	def MktClmDtls(self):
		return self._MktClmDtls

	@MktClmDtls.setter
	def MktClmDtls(self, value):
		self._MktClmDtls = value if value is not None else base_types.UninitialisedField(self, 'MktClmDtls', CorporateActionOption234, False)

	@MktClmDtls.deleter
	def MktClmDtls(self):
		del self._MktClmDtls
		self._MktClmDtls = base_types.UninitialisedField(self, 'MktClmDtls', CorporateActionOption234, False)

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
	def TxRef(self):
		return self._TxRef

	@TxRef.setter
	def TxRef(self, value):
		self._TxRef = value if value is not None else base_types.UninitialisedField(self, 'TxRef', References26, False)

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = base_types.UninitialisedField(self, 'TxRef', References26, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCxlReqId', type=DocumentIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCxlReqSts', type=MarketClaimCancellationRequestStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRef', type=References26, min=1, max=1, mutex_group=None, array=False),
	))