# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData2 import AdditionalData2
from ._AdditionalFee3 import AdditionalFee3
from ._CardData15 import CardData15
from ._Cardholder22 import Cardholder22
from ._ContentInformationType41 import ContentInformationType41
from ._CorrectionIdentification1 import CorrectionIdentification1
from ._CustomerDevice5 import CustomerDevice5
from ._DataRecord1Choice import DataRecord1Choice
from ._Exact12Text import Exact12Text
from ._Exact15Text import Exact15Text
from ._Header71 import Header71
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._Jurisdiction2 import Jurisdiction2
from ._Max12NumericText import Max12NumericText
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._OutputFormat5Code import OutputFormat5Code
from ._PartyIdentification284 import PartyIdentification284
from ._PartyIdentification286 import PartyIdentification286
from ._PartyIdentification287 import PartyIdentification287
from ._PointOfInteractionComponent16 import PointOfInteractionComponent16
from ._ProgrammeMode5 import ProgrammeMode5
from ._ProtectedData2 import ProtectedData2
from ._Reconciliation4 import Reconciliation4
from ._SettlementService6 import SettlementService6
from ._SupplementaryData1 import SupplementaryData1
from ._Terminal7 import Terminal7
from ._Token2 import Token2
from ._Wallet3 import Wallet3

class FileActionResponseV03(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_Acqrr", "_ActnDt", "_AddtlData", "_AddtlFee", "_Card", "_Crdhldr", "_Crrctn", "_CstmrDvc", "_DataRcrd", "_Dstn", "_FileNm", "_FileSctyCd", "_Frmt", "_Hdr", "_Issr", "_Jursdctn", "_LifeCyclId", "_Orgtr", "_POICmpnt", "_Prgrmm", "_PrtctdData", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_RspnCd", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SplmtryData", "_SttlmSvc", "_SysTracAudtNb", "_Termnl", "_Tkn", "_TrnsmssnDtTm", "_Wllt"]
	@property
	def Accptr(self):
		return self._Accptr

	@Accptr.setter
	def Accptr(self, value):
		self._Accptr = value if type(value) != base_types.auto else self.make_default("Accptr")

	@Accptr.deleter
	def Accptr(self):
		del self._Accptr
		self._Accptr = None

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if type(value) != base_types.auto else self.make_default("Acqrr")

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = None

	@property
	def ActnDt(self):
		return self._ActnDt

	@ActnDt.setter
	def ActnDt(self, value):
		self._ActnDt = value if type(value) != base_types.auto else self.make_default("ActnDt")

	@ActnDt.deleter
	def ActnDt(self):
		del self._ActnDt
		self._ActnDt = None

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
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if type(value) != base_types.auto else self.make_default("Crdhldr")

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = None

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if type(value) != base_types.auto else self.make_default("Crrctn")

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = None

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if type(value) != base_types.auto else self.make_default("CstmrDvc")

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = None

	@property
	def DataRcrd(self):
		return self._DataRcrd

	@DataRcrd.setter
	def DataRcrd(self, value):
		self._DataRcrd = value if type(value) != base_types.auto else self.make_default("DataRcrd")

	@DataRcrd.deleter
	def DataRcrd(self):
		del self._DataRcrd
		self._DataRcrd = None

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
	def FileNm(self):
		return self._FileNm

	@FileNm.setter
	def FileNm(self, value):
		self._FileNm = value if type(value) != base_types.auto else self.make_default("FileNm")

	@FileNm.deleter
	def FileNm(self):
		del self._FileNm
		self._FileNm = None

	@property
	def FileSctyCd(self):
		return self._FileSctyCd

	@FileSctyCd.setter
	def FileSctyCd(self, value):
		self._FileSctyCd = value if type(value) != base_types.auto else self.make_default("FileSctyCd")

	@FileSctyCd.deleter
	def FileSctyCd(self):
		del self._FileSctyCd
		self._FileSctyCd = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

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
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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
	def POICmpnt(self):
		return self._POICmpnt

	@POICmpnt.setter
	def POICmpnt(self, value):
		self._POICmpnt = value if type(value) != base_types.auto else self.make_default("POICmpnt")

	@POICmpnt.deleter
	def POICmpnt(self):
		del self._POICmpnt
		self._POICmpnt = None

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
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if type(value) != base_types.auto else self.make_default("Pyee")

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = None

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if type(value) != base_types.auto else self.make_default("Pyer")

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = None

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
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if type(value) != base_types.auto else self.make_default("RspnCd")

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = None

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
	def Termnl(self):
		return self._Termnl

	@Termnl.setter
	def Termnl(self, value):
		self._Termnl = value if type(value) != base_types.auto else self.make_default("Termnl")

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = None

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if type(value) != base_types.auto else self.make_default("Tkn")

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = None

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

	@property
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if type(value) != base_types.auto else self.make_default("Wllt")

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=PartyIdentification284, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crrctn', type=CorrectionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataRcrd', type=DataRecord1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileSctyCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpnt', type=PointOfInteractionComponent16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pyee', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=Wallet3, min=0, max=1, mutex_group=None, array=False),
	))