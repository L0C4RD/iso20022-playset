import base_types
import CorporateActionOption234
import DocumentIdentification9
import CorporateActionGeneralInformation181
import AccountIdentification70
import MarketClaimProcessingStatus1Choice
import SupplementaryData1
import References26

class MarketClaimStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TxRef", "_MktClmDtls", "_CorpActnGnlInf", "_AcctDtls", "_MktClmPrcgSts", "_MktClmCreId"]
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
	def MktClmPrcgSts(self):
		return self._MktClmPrcgSts

	@MktClmPrcgSts.setter
	def MktClmPrcgSts(self, value):
		self._MktClmPrcgSts = value if type(value) != auto else self.make_default("MktClmPrcgSts")

	@MktClmPrcgSts.deleter
	def MktClmPrcgSts(self):
		del self._MktClmPrcgSts
		self._MktClmPrcgSts = None

	@property
	def MktClmCreId(self):
		return self._MktClmCreId

	@MktClmCreId.setter
	def MktClmCreId(self, value):
		self._MktClmCreId = value if type(value) != auto else self.make_default("MktClmCreId")

	@MktClmCreId.deleter
	def MktClmCreId(self):
		del self._MktClmCreId
		self._MktClmCreId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRef', type=References26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmDtls', type=CorporateActionOption234, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation181, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification70, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmPrcgSts', type=MarketClaimProcessingStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCreId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
	))

