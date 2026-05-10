from . import base_types
from ._AdditionalData2 import AdditionalData2
from ._AdditionalFee3 import AdditionalFee3
from ._CardServiceType5Code import CardServiceType5Code
from ._ContentInformationType41 import ContentInformationType41
from ._Exact12Text import Exact12Text
from ._Exact15Text import Exact15Text
from ._Header71 import Header71
from ._ISO8583MessageReasonCode import ISO8583MessageReasonCode
from ._ISODateTime import ISODateTime
from ._Jurisdiction2 import Jurisdiction2
from ._KeyExchangeData1 import KeyExchangeData1
from ._KeyType1Code import KeyType1Code
from ._Max12NumericText import Max12NumericText
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._ProcessingResult26 import ProcessingResult26
from ._ProgrammeMode5 import ProgrammeMode5
from ._ProtectedData2 import ProtectedData2
from ._Reconciliation4 import Reconciliation4
from ._SettlementService6 import SettlementService6
from ._SupplementaryData1 import SupplementaryData1

class KeyExchangeInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AddtlFee", "_AltrnMsgRsn", "_Hdr", "_Jursdctn", "_KeyXchgData", "_KeyXchgFctn", "_KeyXchgTp", "_LifeCyclId", "_MsgRsn", "_OthrKeyXchgFctn", "_OthrKeyXchgTp", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_Rcncltn", "_RtrvlRefNb", "_SctyTrlr", "_SplmtryData", "_SttlmSvc", "_SysTracAudtNb", "_TrnsmssnDtTm"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if type(value) != base_types.auto else self.make_default("AddtlFee")

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = None

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if type(value) != base_types.auto else self.make_default("AltrnMsgRsn")

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if type(value) != base_types.auto else self.make_default("Jursdctn")

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = None

	@property
	def KeyXchgData(self):
		return self._KeyXchgData

	@KeyXchgData.setter
	def KeyXchgData(self, value):
		self._KeyXchgData = value if type(value) != base_types.auto else self.make_default("KeyXchgData")

	@KeyXchgData.deleter
	def KeyXchgData(self):
		del self._KeyXchgData
		self._KeyXchgData = None

	@property
	def KeyXchgFctn(self):
		return self._KeyXchgFctn

	@KeyXchgFctn.setter
	def KeyXchgFctn(self, value):
		self._KeyXchgFctn = value if type(value) != base_types.auto else self.make_default("KeyXchgFctn")

	@KeyXchgFctn.deleter
	def KeyXchgFctn(self):
		del self._KeyXchgFctn
		self._KeyXchgFctn = None

	@property
	def KeyXchgTp(self):
		return self._KeyXchgTp

	@KeyXchgTp.setter
	def KeyXchgTp(self, value):
		self._KeyXchgTp = value if type(value) != base_types.auto else self.make_default("KeyXchgTp")

	@KeyXchgTp.deleter
	def KeyXchgTp(self):
		del self._KeyXchgTp
		self._KeyXchgTp = None

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if type(value) != base_types.auto else self.make_default("LifeCyclId")

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = None

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if type(value) != base_types.auto else self.make_default("MsgRsn")

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = None

	@property
	def OthrKeyXchgFctn(self):
		return self._OthrKeyXchgFctn

	@OthrKeyXchgFctn.setter
	def OthrKeyXchgFctn(self, value):
		self._OthrKeyXchgFctn = value if type(value) != base_types.auto else self.make_default("OthrKeyXchgFctn")

	@OthrKeyXchgFctn.deleter
	def OthrKeyXchgFctn(self):
		del self._OthrKeyXchgFctn
		self._OthrKeyXchgFctn = None

	@property
	def OthrKeyXchgTp(self):
		return self._OthrKeyXchgTp

	@OthrKeyXchgTp.setter
	def OthrKeyXchgTp(self, value):
		self._OthrKeyXchgTp = value if type(value) != base_types.auto else self.make_default("OthrKeyXchgTp")

	@OthrKeyXchgTp.deleter
	def OthrKeyXchgTp(self):
		del self._OthrKeyXchgTp
		self._OthrKeyXchgTp = None

	@property
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if type(value) != base_types.auto else self.make_default("PrcgRslt")

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = None

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if type(value) != base_types.auto else self.make_default("Prgrmm")

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = None

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != base_types.auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if type(value) != base_types.auto else self.make_default("Rcncltn")

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = None

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if type(value) != base_types.auto else self.make_default("RtrvlRefNb")

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

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
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if type(value) != base_types.auto else self.make_default("SttlmSvc")

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = None

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if type(value) != base_types.auto else self.make_default("SysTracAudtNb")

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = None

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if type(value) != base_types.auto else self.make_default("TrnsmssnDtTm")

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyXchgData', type=KeyExchangeData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyXchgFctn', type=CardServiceType5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyXchgTp', type=KeyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrKeyXchgFctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrKeyXchgTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

