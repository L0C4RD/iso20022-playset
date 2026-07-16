# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcquirerHostConfiguration10
from . import AcquirerProtocolExchangeBehavior2
from . import BatchTransactionType1Code
from . import ExchangeConfiguration9
from . import GenericIdentification176
from . import Max256Text
from . import Max35Text
from . import MessageItemCondition2
from . import ReconciliationCriteria1Code
from . import TerminalManagementAction3Code
from . import TrueFalseIndicator
from . import TypeOfAmount8Code

class AcquirerProtocolParameters17(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_ActnTp", "_AmtQlfrForRsvatn", "_ApplId", "_BtchDgtlSgntr", "_BtchTrfCntt", "_CardDataVrfctn", "_CmpltnAdvcMndtd", "_FileTrfBtch", "_Hst", "_MndtrySctyTrlr", "_MsgItm", "_NtfyOffLineCxl", "_OffLineTx", "_OnLineTx", "_PrtctCardData", "_PrvtCardData", "_RcncltnByAcqrr", "_RcncltnErr", "_RcncltnXchg", "_SpltTtlCrit", "_SpltTtls", "_TtlsPerCcy", "_Vrsn"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', GenericIdentification176, True)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', GenericIdentification176, True)

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def AmtQlfrForRsvatn(self):
		return self._AmtQlfrForRsvatn

	@AmtQlfrForRsvatn.setter
	def AmtQlfrForRsvatn(self, value):
		self._AmtQlfrForRsvatn = value if value is not None else base_types.UninitialisedField(self, 'AmtQlfrForRsvatn', TypeOfAmount8Code, True)

	@AmtQlfrForRsvatn.deleter
	def AmtQlfrForRsvatn(self):
		del self._AmtQlfrForRsvatn
		self._AmtQlfrForRsvatn = base_types.UninitialisedField(self, 'AmtQlfrForRsvatn', TypeOfAmount8Code, True)

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if value is not None else base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@property
	def BtchDgtlSgntr(self):
		return self._BtchDgtlSgntr

	@BtchDgtlSgntr.setter
	def BtchDgtlSgntr(self, value):
		self._BtchDgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'BtchDgtlSgntr', TrueFalseIndicator, False)

	@BtchDgtlSgntr.deleter
	def BtchDgtlSgntr(self):
		del self._BtchDgtlSgntr
		self._BtchDgtlSgntr = base_types.UninitialisedField(self, 'BtchDgtlSgntr', TrueFalseIndicator, False)

	@property
	def BtchTrfCntt(self):
		return self._BtchTrfCntt

	@BtchTrfCntt.setter
	def BtchTrfCntt(self, value):
		self._BtchTrfCntt = value if value is not None else base_types.UninitialisedField(self, 'BtchTrfCntt', BatchTransactionType1Code, True)

	@BtchTrfCntt.deleter
	def BtchTrfCntt(self):
		del self._BtchTrfCntt
		self._BtchTrfCntt = base_types.UninitialisedField(self, 'BtchTrfCntt', BatchTransactionType1Code, True)

	@property
	def CardDataVrfctn(self):
		return self._CardDataVrfctn

	@CardDataVrfctn.setter
	def CardDataVrfctn(self, value):
		self._CardDataVrfctn = value if value is not None else base_types.UninitialisedField(self, 'CardDataVrfctn', TrueFalseIndicator, False)

	@CardDataVrfctn.deleter
	def CardDataVrfctn(self):
		del self._CardDataVrfctn
		self._CardDataVrfctn = base_types.UninitialisedField(self, 'CardDataVrfctn', TrueFalseIndicator, False)

	@property
	def CmpltnAdvcMndtd(self):
		return self._CmpltnAdvcMndtd

	@CmpltnAdvcMndtd.setter
	def CmpltnAdvcMndtd(self, value):
		self._CmpltnAdvcMndtd = value if value is not None else base_types.UninitialisedField(self, 'CmpltnAdvcMndtd', TrueFalseIndicator, False)

	@CmpltnAdvcMndtd.deleter
	def CmpltnAdvcMndtd(self):
		del self._CmpltnAdvcMndtd
		self._CmpltnAdvcMndtd = base_types.UninitialisedField(self, 'CmpltnAdvcMndtd', TrueFalseIndicator, False)

	@property
	def FileTrfBtch(self):
		return self._FileTrfBtch

	@FileTrfBtch.setter
	def FileTrfBtch(self, value):
		self._FileTrfBtch = value if value is not None else base_types.UninitialisedField(self, 'FileTrfBtch', TrueFalseIndicator, False)

	@FileTrfBtch.deleter
	def FileTrfBtch(self):
		del self._FileTrfBtch
		self._FileTrfBtch = base_types.UninitialisedField(self, 'FileTrfBtch', TrueFalseIndicator, False)

	@property
	def Hst(self):
		return self._Hst

	@Hst.setter
	def Hst(self, value):
		self._Hst = value if value is not None else base_types.UninitialisedField(self, 'Hst', AcquirerHostConfiguration10, True)

	@Hst.deleter
	def Hst(self):
		del self._Hst
		self._Hst = base_types.UninitialisedField(self, 'Hst', AcquirerHostConfiguration10, True)

	@property
	def MndtrySctyTrlr(self):
		return self._MndtrySctyTrlr

	@MndtrySctyTrlr.setter
	def MndtrySctyTrlr(self, value):
		self._MndtrySctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'MndtrySctyTrlr', TrueFalseIndicator, False)

	@MndtrySctyTrlr.deleter
	def MndtrySctyTrlr(self):
		del self._MndtrySctyTrlr
		self._MndtrySctyTrlr = base_types.UninitialisedField(self, 'MndtrySctyTrlr', TrueFalseIndicator, False)

	@property
	def MsgItm(self):
		return self._MsgItm

	@MsgItm.setter
	def MsgItm(self, value):
		self._MsgItm = value if value is not None else base_types.UninitialisedField(self, 'MsgItm', MessageItemCondition2, True)

	@MsgItm.deleter
	def MsgItm(self):
		del self._MsgItm
		self._MsgItm = base_types.UninitialisedField(self, 'MsgItm', MessageItemCondition2, True)

	@property
	def NtfyOffLineCxl(self):
		return self._NtfyOffLineCxl

	@NtfyOffLineCxl.setter
	def NtfyOffLineCxl(self, value):
		self._NtfyOffLineCxl = value if value is not None else base_types.UninitialisedField(self, 'NtfyOffLineCxl', TrueFalseIndicator, False)

	@NtfyOffLineCxl.deleter
	def NtfyOffLineCxl(self):
		del self._NtfyOffLineCxl
		self._NtfyOffLineCxl = base_types.UninitialisedField(self, 'NtfyOffLineCxl', TrueFalseIndicator, False)

	@property
	def OffLineTx(self):
		return self._OffLineTx

	@OffLineTx.setter
	def OffLineTx(self, value):
		self._OffLineTx = value if value is not None else base_types.UninitialisedField(self, 'OffLineTx', AcquirerProtocolExchangeBehavior2, False)

	@OffLineTx.deleter
	def OffLineTx(self):
		del self._OffLineTx
		self._OffLineTx = base_types.UninitialisedField(self, 'OffLineTx', AcquirerProtocolExchangeBehavior2, False)

	@property
	def OnLineTx(self):
		return self._OnLineTx

	@OnLineTx.setter
	def OnLineTx(self, value):
		self._OnLineTx = value if value is not None else base_types.UninitialisedField(self, 'OnLineTx', AcquirerProtocolExchangeBehavior2, False)

	@OnLineTx.deleter
	def OnLineTx(self):
		del self._OnLineTx
		self._OnLineTx = base_types.UninitialisedField(self, 'OnLineTx', AcquirerProtocolExchangeBehavior2, False)

	@property
	def PrtctCardData(self):
		return self._PrtctCardData

	@PrtctCardData.setter
	def PrtctCardData(self, value):
		self._PrtctCardData = value if value is not None else base_types.UninitialisedField(self, 'PrtctCardData', TrueFalseIndicator, False)

	@PrtctCardData.deleter
	def PrtctCardData(self):
		del self._PrtctCardData
		self._PrtctCardData = base_types.UninitialisedField(self, 'PrtctCardData', TrueFalseIndicator, False)

	@property
	def PrvtCardData(self):
		return self._PrvtCardData

	@PrvtCardData.setter
	def PrvtCardData(self, value):
		self._PrvtCardData = value if value is not None else base_types.UninitialisedField(self, 'PrvtCardData', TrueFalseIndicator, False)

	@PrvtCardData.deleter
	def PrvtCardData(self):
		del self._PrvtCardData
		self._PrvtCardData = base_types.UninitialisedField(self, 'PrvtCardData', TrueFalseIndicator, False)

	@property
	def RcncltnByAcqrr(self):
		return self._RcncltnByAcqrr

	@RcncltnByAcqrr.setter
	def RcncltnByAcqrr(self, value):
		self._RcncltnByAcqrr = value if value is not None else base_types.UninitialisedField(self, 'RcncltnByAcqrr', TrueFalseIndicator, False)

	@RcncltnByAcqrr.deleter
	def RcncltnByAcqrr(self):
		del self._RcncltnByAcqrr
		self._RcncltnByAcqrr = base_types.UninitialisedField(self, 'RcncltnByAcqrr', TrueFalseIndicator, False)

	@property
	def RcncltnErr(self):
		return self._RcncltnErr

	@RcncltnErr.setter
	def RcncltnErr(self, value):
		self._RcncltnErr = value if value is not None else base_types.UninitialisedField(self, 'RcncltnErr', TrueFalseIndicator, False)

	@RcncltnErr.deleter
	def RcncltnErr(self):
		del self._RcncltnErr
		self._RcncltnErr = base_types.UninitialisedField(self, 'RcncltnErr', TrueFalseIndicator, False)

	@property
	def RcncltnXchg(self):
		return self._RcncltnXchg

	@RcncltnXchg.setter
	def RcncltnXchg(self, value):
		self._RcncltnXchg = value if value is not None else base_types.UninitialisedField(self, 'RcncltnXchg', ExchangeConfiguration9, False)

	@RcncltnXchg.deleter
	def RcncltnXchg(self):
		del self._RcncltnXchg
		self._RcncltnXchg = base_types.UninitialisedField(self, 'RcncltnXchg', ExchangeConfiguration9, False)

	@property
	def SpltTtlCrit(self):
		return self._SpltTtlCrit

	@SpltTtlCrit.setter
	def SpltTtlCrit(self, value):
		self._SpltTtlCrit = value if value is not None else base_types.UninitialisedField(self, 'SpltTtlCrit', ReconciliationCriteria1Code, True)

	@SpltTtlCrit.deleter
	def SpltTtlCrit(self):
		del self._SpltTtlCrit
		self._SpltTtlCrit = base_types.UninitialisedField(self, 'SpltTtlCrit', ReconciliationCriteria1Code, True)

	@property
	def SpltTtls(self):
		return self._SpltTtls

	@SpltTtls.setter
	def SpltTtls(self, value):
		self._SpltTtls = value if value is not None else base_types.UninitialisedField(self, 'SpltTtls', TrueFalseIndicator, False)

	@SpltTtls.deleter
	def SpltTtls(self):
		del self._SpltTtls
		self._SpltTtls = base_types.UninitialisedField(self, 'SpltTtls', TrueFalseIndicator, False)

	@property
	def TtlsPerCcy(self):
		return self._TtlsPerCcy

	@TtlsPerCcy.setter
	def TtlsPerCcy(self, value):
		self._TtlsPerCcy = value if value is not None else base_types.UninitialisedField(self, 'TtlsPerCcy', TrueFalseIndicator, False)

	@TtlsPerCcy.deleter
	def TtlsPerCcy(self):
		del self._TtlsPerCcy
		self._TtlsPerCcy = base_types.UninitialisedField(self, 'TtlsPerCcy', TrueFalseIndicator, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=GenericIdentification176, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtQlfrForRsvatn', type=TypeOfAmount8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BtchDgtlSgntr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrfCntt', type=BatchTransactionType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardDataVrfctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvcMndtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileTrfBtch', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hst', type=AcquirerHostConfiguration10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MndtrySctyTrlr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgItm', type=MessageItemCondition2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfyOffLineCxl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffLineTx', type=AcquirerProtocolExchangeBehavior2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineTx', type=AcquirerProtocolExchangeBehavior2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctCardData', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtCardData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnByAcqrr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnErr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnXchg', type=ExchangeConfiguration9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltTtlCrit', type=ReconciliationCriteria1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpltTtls', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsPerCcy', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))