import base_types
import ExchangeConfiguration9
import GenericIdentification176
import ReconciliationCriteria1Code
import TerminalManagementAction3Code
import Max35Text
import AcquirerHostConfiguration10
import AcquirerProtocolExchangeBehavior2
import MessageItemCondition2
import TypeOfAmount8Code
import TrueFalseIndicator
import Max256Text
import BatchTransactionType1Code

class AcquirerProtocolParameters17(base_types._BaseFieldType):

	__slots__ = ["_BtchDgtlSgntr", "_FileTrfBtch", "_CmpltnAdvcMndtd", "_RcncltnXchg", "_AcqrrId", "_PrtctCardData", "_Hst", "_CardDataVrfctn", "_RcncltnErr", "_Vrsn", "_SpltTtlCrit", "_OffLineTx", "_TtlsPerCcy", "_ApplId", "_MsgItm", "_AmtQlfrForRsvatn", "_RcncltnByAcqrr", "_ActnTp", "_PrvtCardData", "_SpltTtls", "_MndtrySctyTrlr", "_NtfyOffLineCxl", "_BtchTrfCntt", "_OnLineTx"]
	@property
	def BtchDgtlSgntr(self):
		return self._BtchDgtlSgntr

	@BtchDgtlSgntr.setter
	def BtchDgtlSgntr(self, value):
		self._BtchDgtlSgntr = value if type(value) != auto else self.make_default("BtchDgtlSgntr")

	@BtchDgtlSgntr.deleter
	def BtchDgtlSgntr(self):
		del self._BtchDgtlSgntr
		self._BtchDgtlSgntr = None

	@property
	def FileTrfBtch(self):
		return self._FileTrfBtch

	@FileTrfBtch.setter
	def FileTrfBtch(self, value):
		self._FileTrfBtch = value if type(value) != auto else self.make_default("FileTrfBtch")

	@FileTrfBtch.deleter
	def FileTrfBtch(self):
		del self._FileTrfBtch
		self._FileTrfBtch = None

	@property
	def CmpltnAdvcMndtd(self):
		return self._CmpltnAdvcMndtd

	@CmpltnAdvcMndtd.setter
	def CmpltnAdvcMndtd(self, value):
		self._CmpltnAdvcMndtd = value if type(value) != auto else self.make_default("CmpltnAdvcMndtd")

	@CmpltnAdvcMndtd.deleter
	def CmpltnAdvcMndtd(self):
		del self._CmpltnAdvcMndtd
		self._CmpltnAdvcMndtd = None

	@property
	def RcncltnXchg(self):
		return self._RcncltnXchg

	@RcncltnXchg.setter
	def RcncltnXchg(self, value):
		self._RcncltnXchg = value if type(value) != auto else self.make_default("RcncltnXchg")

	@RcncltnXchg.deleter
	def RcncltnXchg(self):
		del self._RcncltnXchg
		self._RcncltnXchg = None

	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if type(value) != auto else self.make_default("AcqrrId")

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = None

	@property
	def PrtctCardData(self):
		return self._PrtctCardData

	@PrtctCardData.setter
	def PrtctCardData(self, value):
		self._PrtctCardData = value if type(value) != auto else self.make_default("PrtctCardData")

	@PrtctCardData.deleter
	def PrtctCardData(self):
		del self._PrtctCardData
		self._PrtctCardData = None

	@property
	def Hst(self):
		return self._Hst

	@Hst.setter
	def Hst(self, value):
		self._Hst = value if type(value) != auto else self.make_default("Hst")

	@Hst.deleter
	def Hst(self):
		del self._Hst
		self._Hst = None

	@property
	def CardDataVrfctn(self):
		return self._CardDataVrfctn

	@CardDataVrfctn.setter
	def CardDataVrfctn(self, value):
		self._CardDataVrfctn = value if type(value) != auto else self.make_default("CardDataVrfctn")

	@CardDataVrfctn.deleter
	def CardDataVrfctn(self):
		del self._CardDataVrfctn
		self._CardDataVrfctn = None

	@property
	def RcncltnErr(self):
		return self._RcncltnErr

	@RcncltnErr.setter
	def RcncltnErr(self, value):
		self._RcncltnErr = value if type(value) != auto else self.make_default("RcncltnErr")

	@RcncltnErr.deleter
	def RcncltnErr(self):
		del self._RcncltnErr
		self._RcncltnErr = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def SpltTtlCrit(self):
		return self._SpltTtlCrit

	@SpltTtlCrit.setter
	def SpltTtlCrit(self, value):
		self._SpltTtlCrit = value if type(value) != auto else self.make_default("SpltTtlCrit")

	@SpltTtlCrit.deleter
	def SpltTtlCrit(self):
		del self._SpltTtlCrit
		self._SpltTtlCrit = None

	@property
	def OffLineTx(self):
		return self._OffLineTx

	@OffLineTx.setter
	def OffLineTx(self, value):
		self._OffLineTx = value if type(value) != auto else self.make_default("OffLineTx")

	@OffLineTx.deleter
	def OffLineTx(self):
		del self._OffLineTx
		self._OffLineTx = None

	@property
	def TtlsPerCcy(self):
		return self._TtlsPerCcy

	@TtlsPerCcy.setter
	def TtlsPerCcy(self, value):
		self._TtlsPerCcy = value if type(value) != auto else self.make_default("TtlsPerCcy")

	@TtlsPerCcy.deleter
	def TtlsPerCcy(self):
		del self._TtlsPerCcy
		self._TtlsPerCcy = None

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if type(value) != auto else self.make_default("ApplId")

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = None

	@property
	def MsgItm(self):
		return self._MsgItm

	@MsgItm.setter
	def MsgItm(self, value):
		self._MsgItm = value if type(value) != auto else self.make_default("MsgItm")

	@MsgItm.deleter
	def MsgItm(self):
		del self._MsgItm
		self._MsgItm = None

	@property
	def AmtQlfrForRsvatn(self):
		return self._AmtQlfrForRsvatn

	@AmtQlfrForRsvatn.setter
	def AmtQlfrForRsvatn(self, value):
		self._AmtQlfrForRsvatn = value if type(value) != auto else self.make_default("AmtQlfrForRsvatn")

	@AmtQlfrForRsvatn.deleter
	def AmtQlfrForRsvatn(self):
		del self._AmtQlfrForRsvatn
		self._AmtQlfrForRsvatn = None

	@property
	def RcncltnByAcqrr(self):
		return self._RcncltnByAcqrr

	@RcncltnByAcqrr.setter
	def RcncltnByAcqrr(self, value):
		self._RcncltnByAcqrr = value if type(value) != auto else self.make_default("RcncltnByAcqrr")

	@RcncltnByAcqrr.deleter
	def RcncltnByAcqrr(self):
		del self._RcncltnByAcqrr
		self._RcncltnByAcqrr = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def PrvtCardData(self):
		return self._PrvtCardData

	@PrvtCardData.setter
	def PrvtCardData(self, value):
		self._PrvtCardData = value if type(value) != auto else self.make_default("PrvtCardData")

	@PrvtCardData.deleter
	def PrvtCardData(self):
		del self._PrvtCardData
		self._PrvtCardData = None

	@property
	def SpltTtls(self):
		return self._SpltTtls

	@SpltTtls.setter
	def SpltTtls(self, value):
		self._SpltTtls = value if type(value) != auto else self.make_default("SpltTtls")

	@SpltTtls.deleter
	def SpltTtls(self):
		del self._SpltTtls
		self._SpltTtls = None

	@property
	def MndtrySctyTrlr(self):
		return self._MndtrySctyTrlr

	@MndtrySctyTrlr.setter
	def MndtrySctyTrlr(self, value):
		self._MndtrySctyTrlr = value if type(value) != auto else self.make_default("MndtrySctyTrlr")

	@MndtrySctyTrlr.deleter
	def MndtrySctyTrlr(self):
		del self._MndtrySctyTrlr
		self._MndtrySctyTrlr = None

	@property
	def NtfyOffLineCxl(self):
		return self._NtfyOffLineCxl

	@NtfyOffLineCxl.setter
	def NtfyOffLineCxl(self, value):
		self._NtfyOffLineCxl = value if type(value) != auto else self.make_default("NtfyOffLineCxl")

	@NtfyOffLineCxl.deleter
	def NtfyOffLineCxl(self):
		del self._NtfyOffLineCxl
		self._NtfyOffLineCxl = None

	@property
	def BtchTrfCntt(self):
		return self._BtchTrfCntt

	@BtchTrfCntt.setter
	def BtchTrfCntt(self, value):
		self._BtchTrfCntt = value if type(value) != auto else self.make_default("BtchTrfCntt")

	@BtchTrfCntt.deleter
	def BtchTrfCntt(self):
		del self._BtchTrfCntt
		self._BtchTrfCntt = None

	@property
	def OnLineTx(self):
		return self._OnLineTx

	@OnLineTx.setter
	def OnLineTx(self, value):
		self._OnLineTx = value if type(value) != auto else self.make_default("OnLineTx")

	@OnLineTx.deleter
	def OnLineTx(self):
		del self._OnLineTx
		self._OnLineTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchDgtlSgntr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileTrfBtch', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvcMndtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnXchg', type=ExchangeConfiguration9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrId', type=GenericIdentification176, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctCardData', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hst', type=AcquirerHostConfiguration10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardDataVrfctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnErr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltTtlCrit', type=ReconciliationCriteria1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffLineTx', type=AcquirerProtocolExchangeBehavior2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsPerCcy', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgItm', type=MessageItemCondition2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtQlfrForRsvatn', type=TypeOfAmount8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnByAcqrr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtCardData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltTtls', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtrySctyTrlr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfyOffLineCxl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrfCntt', type=BatchTransactionType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OnLineTx', type=AcquirerProtocolExchangeBehavior2, min=0, max=1, mutex_group=None, array=False),
	))

