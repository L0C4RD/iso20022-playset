# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification70
from . import CorporateAction59
from . import CorporateActionGeneralInformation181
from . import CorporateActionOption234
from . import MarketClaimType1Code
from . import References25
from . import RelatedSettlementInstruction2
from . import SettlementParties123
from . import SettlementParties124
from . import SupplementaryData1
from . import YesNoIndicator

class MarketClaimCreationV04(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_CorpActnDtls", "_CorpActnGnlInf", "_DlvrgSttlmPties", "_MktClmDtls", "_MktClmSttlmInd", "_MktClmTp", "_RcvgSttlmPties", "_RltdSttlmInstrDtls", "_SplmtryData", "_TxRef"]
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
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction59, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction59, False)

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
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties123, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties123, False)

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
	def MktClmSttlmInd(self):
		return self._MktClmSttlmInd

	@MktClmSttlmInd.setter
	def MktClmSttlmInd(self, value):
		self._MktClmSttlmInd = value if value is not None else base_types.UninitialisedField(self, 'MktClmSttlmInd', YesNoIndicator, False)

	@MktClmSttlmInd.deleter
	def MktClmSttlmInd(self):
		del self._MktClmSttlmInd
		self._MktClmSttlmInd = base_types.UninitialisedField(self, 'MktClmSttlmInd', YesNoIndicator, False)

	@property
	def MktClmTp(self):
		return self._MktClmTp

	@MktClmTp.setter
	def MktClmTp(self, value):
		self._MktClmTp = value if value is not None else base_types.UninitialisedField(self, 'MktClmTp', MarketClaimType1Code, False)

	@MktClmTp.deleter
	def MktClmTp(self):
		del self._MktClmTp
		self._MktClmTp = base_types.UninitialisedField(self, 'MktClmTp', MarketClaimType1Code, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties124, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties124, False)

	@property
	def RltdSttlmInstrDtls(self):
		return self._RltdSttlmInstrDtls

	@RltdSttlmInstrDtls.setter
	def RltdSttlmInstrDtls(self, value):
		self._RltdSttlmInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmInstrDtls', RelatedSettlementInstruction2, False)

	@RltdSttlmInstrDtls.deleter
	def RltdSttlmInstrDtls(self):
		del self._RltdSttlmInstrDtls
		self._RltdSttlmInstrDtls = base_types.UninitialisedField(self, 'RltdSttlmInstrDtls', RelatedSettlementInstruction2, False)

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
		self._TxRef = value if value is not None else base_types.UninitialisedField(self, 'TxRef', References25, False)

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = base_types.UninitialisedField(self, 'TxRef', References25, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties123, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmSttlmInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmTp', type=MarketClaimType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrDtls', type=RelatedSettlementInstruction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRef', type=References25, min=1, max=1, mutex_group=None, array=False),
	))