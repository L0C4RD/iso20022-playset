from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._CorporateAction78 import CorporateAction78
from ._AccountAndBalance54 import AccountAndBalance54
from ._CorporateActionReversalReason10 import CorporateActionReversalReason10
from ._CorporateActionEventReference4 import CorporateActionEventReference4
from ._PartyIdentification137Choice import PartyIdentification137Choice
from ._CorporateActionNarrative35 import CorporateActionNarrative35
from ._TransactionIdentification1 import TransactionIdentification1
from ._DocumentIdentification38 import DocumentIdentification38
from ._DocumentIdentification37 import DocumentIdentification37
from ._CorporateActionOption246 import CorporateActionOption246
from ._CorporateActionGeneralInformation193 import CorporateActionGeneralInformation193

class CorporateActionMovementReversalAdvice002V16(base_types._BaseFieldType):

	__slots__ = ["_CorpActnConfDtls", "_MvmntConfId", "_RvslRsn", "_OthrDocId", "_CorpActnDtls", "_IssrAgt", "_SubPngAgt", "_EvtsLkg", "_AddtlInf", "_PngAgt", "_CorpActnGnlInf", "_AcctDtls", "_TxId", "_SplmtryData"]
	@property
	def CorpActnConfDtls(self):
		return self._CorpActnConfDtls

	@CorpActnConfDtls.setter
	def CorpActnConfDtls(self, value):
		self._CorpActnConfDtls = value if type(value) != base_types.auto else self.make_default("CorpActnConfDtls")

	@CorpActnConfDtls.deleter
	def CorpActnConfDtls(self):
		del self._CorpActnConfDtls
		self._CorpActnConfDtls = None

	@property
	def MvmntConfId(self):
		return self._MvmntConfId

	@MvmntConfId.setter
	def MvmntConfId(self, value):
		self._MvmntConfId = value if type(value) != base_types.auto else self.make_default("MvmntConfId")

	@MvmntConfId.deleter
	def MvmntConfId(self):
		del self._MvmntConfId
		self._MvmntConfId = None

	@property
	def RvslRsn(self):
		return self._RvslRsn

	@RvslRsn.setter
	def RvslRsn(self, value):
		self._RvslRsn = value if type(value) != base_types.auto else self.make_default("RvslRsn")

	@RvslRsn.deleter
	def RvslRsn(self):
		del self._RvslRsn
		self._RvslRsn = None

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if type(value) != base_types.auto else self.make_default("OthrDocId")

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != base_types.auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if type(value) != base_types.auto else self.make_default("SubPngAgt")

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = None

	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if type(value) != base_types.auto else self.make_default("EvtsLkg")

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != base_types.auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

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
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnConfDtls', type=CorporateActionOption246, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntConfId', type=DocumentIdentification37, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsn', type=CorporateActionReversalReason10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction78, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation193, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=AccountAndBalance54, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

