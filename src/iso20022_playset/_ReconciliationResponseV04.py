# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData2 import AdditionalData2
from ._AdditionalFee3 import AdditionalFee3
from ._CardServiceType4Code import CardServiceType4Code
from ._ContentInformationType41 import ContentInformationType41
from ._Exact12Text import Exact12Text
from ._Exact15Text import Exact15Text
from ._Exact3NumericText import Exact3NumericText
from ._Header71 import Header71
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._ISODateTime import ISODateTime
from ._Jurisdiction2 import Jurisdiction2
from ._Max12NumericText import Max12NumericText
from ._Max35Text import Max35Text
from ._PartyIdentification286 import PartyIdentification286
from ._ProcessingResult23 import ProcessingResult23
from ._ProgrammeMode5 import ProgrammeMode5
from ._ProtectedData2 import ProtectedData2
from ._Reconciliation4 import Reconciliation4
from ._ReconciliationActivityType1Code import ReconciliationActivityType1Code
from ._ReconciliationFunction1Code import ReconciliationFunction1Code
from ._SettlementService6 import SettlementService6
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionTotals14 import TransactionTotals14

class ReconciliationResponseV04(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AddtlFee", "_Dstn", "_Hdr", "_Jursdctn", "_LifeCyclId", "_OrgnlRspnCd", "_Orgtr", "_OthrRcncltnActvtyTp", "_OthrRcncltnTp", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_Rcncltn", "_RcncltnActvtyTp", "_RcncltnFctn", "_RcncltnTp", "_RcncltnTtls", "_Rcvr", "_ReqdCcy", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SplmtryData", "_SttlmSvc", "_SysTracAudtNb", "_TrnsmssnDtTm"]
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
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if type(value) != base_types.auto else self.make_default("Dstn")

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = None

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
	def OrgnlRspnCd(self):
		return self._OrgnlRspnCd

	@OrgnlRspnCd.setter
	def OrgnlRspnCd(self, value):
		self._OrgnlRspnCd = value if type(value) != base_types.auto else self.make_default("OrgnlRspnCd")

	@OrgnlRspnCd.deleter
	def OrgnlRspnCd(self):
		del self._OrgnlRspnCd
		self._OrgnlRspnCd = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != base_types.auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def OthrRcncltnActvtyTp(self):
		return self._OthrRcncltnActvtyTp

	@OthrRcncltnActvtyTp.setter
	def OthrRcncltnActvtyTp(self, value):
		self._OthrRcncltnActvtyTp = value if type(value) != base_types.auto else self.make_default("OthrRcncltnActvtyTp")

	@OthrRcncltnActvtyTp.deleter
	def OthrRcncltnActvtyTp(self):
		del self._OthrRcncltnActvtyTp
		self._OthrRcncltnActvtyTp = None

	@property
	def OthrRcncltnTp(self):
		return self._OthrRcncltnTp

	@OthrRcncltnTp.setter
	def OthrRcncltnTp(self, value):
		self._OthrRcncltnTp = value if type(value) != base_types.auto else self.make_default("OthrRcncltnTp")

	@OthrRcncltnTp.deleter
	def OthrRcncltnTp(self):
		del self._OthrRcncltnTp
		self._OthrRcncltnTp = None

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
	def RcncltnActvtyTp(self):
		return self._RcncltnActvtyTp

	@RcncltnActvtyTp.setter
	def RcncltnActvtyTp(self, value):
		self._RcncltnActvtyTp = value if type(value) != base_types.auto else self.make_default("RcncltnActvtyTp")

	@RcncltnActvtyTp.deleter
	def RcncltnActvtyTp(self):
		del self._RcncltnActvtyTp
		self._RcncltnActvtyTp = None

	@property
	def RcncltnFctn(self):
		return self._RcncltnFctn

	@RcncltnFctn.setter
	def RcncltnFctn(self, value):
		self._RcncltnFctn = value if type(value) != base_types.auto else self.make_default("RcncltnFctn")

	@RcncltnFctn.deleter
	def RcncltnFctn(self):
		del self._RcncltnFctn
		self._RcncltnFctn = None

	@property
	def RcncltnTp(self):
		return self._RcncltnTp

	@RcncltnTp.setter
	def RcncltnTp(self, value):
		self._RcncltnTp = value if type(value) != base_types.auto else self.make_default("RcncltnTp")

	@RcncltnTp.deleter
	def RcncltnTp(self):
		del self._RcncltnTp
		self._RcncltnTp = None

	@property
	def RcncltnTtls(self):
		return self._RcncltnTtls

	@RcncltnTtls.setter
	def RcncltnTtls(self, value):
		self._RcncltnTtls = value if type(value) != base_types.auto else self.make_default("RcncltnTtls")

	@RcncltnTtls.deleter
	def RcncltnTtls(self):
		del self._RcncltnTtls
		self._RcncltnTtls = None

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if type(value) != base_types.auto else self.make_default("Rcvr")

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = None

	@property
	def ReqdCcy(self):
		return self._ReqdCcy

	@ReqdCcy.setter
	def ReqdCcy(self, value):
		self._ReqdCcy = value if type(value) != base_types.auto else self.make_default("ReqdCcy")

	@ReqdCcy.deleter
	def ReqdCcy(self):
		del self._ReqdCcy
		self._ReqdCcy = None

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
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != base_types.auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

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
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcncltnActvtyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcncltnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnActvtyTp', type=ReconciliationActivityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFctn', type=ReconciliationFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTp', type=CardServiceType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTtls', type=TransactionTotals14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdCcy', type=Exact3NumericText, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))