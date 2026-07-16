# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification70
from . import CorporateActionGeneralInformation181
from . import CorporateActionOption234
from . import DocumentIdentification9
from . import MarketClaimProcessingStatus2Choice
from . import References26
from . import SupplementaryData1

class MarketClaimStatusAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_CorpActnGnlInf", "_MktClmCreId", "_MktClmDtls", "_MktClmPrcgSts", "_SplmtryData", "_TxRef"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', AccountIdentification70, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', AccountIdentification70, False)

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
	def MktClmCreId(self):
		return self._MktClmCreId

	@MktClmCreId.setter
	def MktClmCreId(self, value):
		self._MktClmCreId = value if value is not None else base_types.UninitialisedField(self, 'MktClmCreId', DocumentIdentification9, False)

	@MktClmCreId.deleter
	def MktClmCreId(self):
		del self._MktClmCreId
		self._MktClmCreId = base_types.UninitialisedField(self, 'MktClmCreId', DocumentIdentification9, False)

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
	def MktClmPrcgSts(self):
		return self._MktClmPrcgSts

	@MktClmPrcgSts.setter
	def MktClmPrcgSts(self, value):
		self._MktClmPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'MktClmPrcgSts', MarketClaimProcessingStatus2Choice, False)

	@MktClmPrcgSts.deleter
	def MktClmPrcgSts(self):
		del self._MktClmPrcgSts
		self._MktClmPrcgSts = base_types.UninitialisedField(self, 'MktClmPrcgSts', MarketClaimProcessingStatus2Choice, False)

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
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification70, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCreId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmPrcgSts', type=MarketClaimProcessingStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRef', type=References26, min=1, max=1, mutex_group=None, array=False),
	))