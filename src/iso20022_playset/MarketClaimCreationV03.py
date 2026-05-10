import base_types
import SettlementParties123
import CorporateActionOption234
import SupplementaryData1
import MarketClaimType1Code
import SettlementParties124
import RelatedSettlementInstruction2
import AccountIdentification70
import CorporateAction59
import CorporateActionGeneralInformation181
import References25

class MarketClaimCreationV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_DlvrgSttlmPties", "_TxRef", "_AcctDtls", "_CorpActnGnlInf", "_RcvgSttlmPties", "_RltdSttlmInstrDtls", "_MktClmDtls", "_MktClmTp", "_CorpActnDtls"]
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
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

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

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

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
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def RltdSttlmInstrDtls(self):
		return self._RltdSttlmInstrDtls

	@RltdSttlmInstrDtls.setter
	def RltdSttlmInstrDtls(self, value):
		self._RltdSttlmInstrDtls = value if type(value) != auto else self.make_default("RltdSttlmInstrDtls")

	@RltdSttlmInstrDtls.deleter
	def RltdSttlmInstrDtls(self):
		del self._RltdSttlmInstrDtls
		self._RltdSttlmInstrDtls = None

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
	def MktClmTp(self):
		return self._MktClmTp

	@MktClmTp.setter
	def MktClmTp(self, value):
		self._MktClmTp = value if type(value) != auto else self.make_default("MktClmTp")

	@MktClmTp.deleter
	def MktClmTp(self):
		del self._MktClmTp
		self._MktClmTp = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties123, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRef', type=References25, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrDtls', type=RelatedSettlementInstruction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmTp', type=MarketClaimType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction59, min=0, max=1, mutex_group=None, array=False),
	))

