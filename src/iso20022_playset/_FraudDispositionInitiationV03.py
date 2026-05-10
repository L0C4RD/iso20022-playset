from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .AdditionalFee3 import AdditionalFee3
from .Header71 import Header71
from .ProtectedData2 import ProtectedData2
from .CardData15 import CardData15
from .Token2 import Token2
from .Max70Text import Max70Text
from .AdditionalInformation30 import AdditionalInformation30
from .Jurisdiction2 import Jurisdiction2
from .FraudDispositionStatus2 import FraudDispositionStatus2
from .ReportedFraud5 import ReportedFraud5
from .Cardholder22 import Cardholder22
from .Reconciliation4 import Reconciliation4
from .ContentInformationType41 import ContentInformationType41
from .SettlementService6 import SettlementService6
from .ProgrammeMode5 import ProgrammeMode5
from .AdditionalData2 import AdditionalData2
from .PartyIdentification286 import PartyIdentification286

class FraudDispositionInitiationV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_SctyTrlr", "_Acqrr", "_Hdr", "_AddtlData", "_Rcvr", "_Sndr", "_Dstn", "_Crdhldr", "_Issr", "_Card", "_FrdTxId", "_AddtlInf", "_RptdFrd", "_Rcncltn", "_AddtlFee", "_Tkn", "_Jursdctn", "_FrdDspstnSts", "_Orgtr", "_Prgrmm", "_SttlmSvc", "_PrtctdData"]
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
	def FrdTxId(self):
		return self._FrdTxId

	@FrdTxId.setter
	def FrdTxId(self, value):
		self._FrdTxId = value if type(value) != base_types.auto else self.make_default("FrdTxId")

	@FrdTxId.deleter
	def FrdTxId(self):
		del self._FrdTxId
		self._FrdTxId = None

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
	def RptdFrd(self):
		return self._RptdFrd

	@RptdFrd.setter
	def RptdFrd(self, value):
		self._RptdFrd = value if type(value) != base_types.auto else self.make_default("RptdFrd")

	@RptdFrd.deleter
	def RptdFrd(self):
		del self._RptdFrd
		self._RptdFrd = None

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
	def FrdDspstnSts(self):
		return self._FrdDspstnSts

	@FrdDspstnSts.setter
	def FrdDspstnSts(self, value):
		self._FrdDspstnSts = value if type(value) != base_types.auto else self.make_default("FrdDspstnSts")

	@FrdDspstnSts.deleter
	def FrdDspstnSts(self):
		del self._FrdDspstnSts
		self._FrdDspstnSts = None

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
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != base_types.auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=PartyIdentification286, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=CardData15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdTxId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptdFrd', type=ReportedFraud5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tkn', type=Token2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdDspstnSts', type=FraudDispositionStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
	))

