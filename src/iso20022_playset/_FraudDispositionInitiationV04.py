# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import AcquirerData1
from . import AdditionalFee4
from . import CardData17
from . import Cardholder23
from . import ContentInformationType41
from . import DestinationData1
from . import EncryptedData2
from . import FraudDispositionStatus3
from . import Header72
from . import IssuerData1
from . import Jurisdiction2
from . import Max70Text
from . import OriginatorData2
from . import ProgrammeMode6
from . import ReceiverData1
from . import Reconciliation5
from . import ReportedFraud7
from . import SenderData1
from . import SettlementService7
from . import Token5

class FraudDispositionInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_Acqrr", "_AddtlFee", "_AddtlInf", "_Card", "_Crdhldr", "_Dstn", "_FrdDspstnSts", "_FrdTxId", "_Hdr", "_Issr", "_Jursdctn", "_NtlData", "_Orgtr", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Rcncltn", "_Rcvr", "_RptdFrd", "_SctyTrlr", "_Sndr", "_SttlmSvc", "_Tkn"]
	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if value is not None else base_types.UninitialisedField(self, 'Acqrr', AcquirerData1, False)

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = base_types.UninitialisedField(self, 'Acqrr', AcquirerData1, False)

	@property
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if value is not None else base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', ATICALaxProcessing, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', ATICALaxProcessing, True)

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', CardData17, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', CardData17, False)

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if value is not None else base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, True)

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, True)

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if value is not None else base_types.UninitialisedField(self, 'Dstn', DestinationData1, False)

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = base_types.UninitialisedField(self, 'Dstn', DestinationData1, False)

	@property
	def FrdDspstnSts(self):
		return self._FrdDspstnSts

	@FrdDspstnSts.setter
	def FrdDspstnSts(self, value):
		self._FrdDspstnSts = value if value is not None else base_types.UninitialisedField(self, 'FrdDspstnSts', FraudDispositionStatus3, False)

	@FrdDspstnSts.deleter
	def FrdDspstnSts(self):
		del self._FrdDspstnSts
		self._FrdDspstnSts = base_types.UninitialisedField(self, 'FrdDspstnSts', FraudDispositionStatus3, False)

	@property
	def FrdTxId(self):
		return self._FrdTxId

	@FrdTxId.setter
	def FrdTxId(self, value):
		self._FrdTxId = value if value is not None else base_types.UninitialisedField(self, 'FrdTxId', Max70Text, False)

	@FrdTxId.deleter
	def FrdTxId(self):
		del self._FrdTxId
		self._FrdTxId = base_types.UninitialisedField(self, 'FrdTxId', Max70Text, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header72, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header72, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', IssuerData1, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', IssuerData1, False)

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if value is not None else base_types.UninitialisedField(self, 'Jursdctn', Jurisdiction2, False)

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = base_types.UninitialisedField(self, 'Jursdctn', Jurisdiction2, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', OriginatorData2, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', OriginatorData2, False)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, False)

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdData', EncryptedData2, True)

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = base_types.UninitialisedField(self, 'PrtctdData', EncryptedData2, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if value is not None else base_types.UninitialisedField(self, 'Rcncltn', Reconciliation5, False)

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = base_types.UninitialisedField(self, 'Rcncltn', Reconciliation5, False)

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if value is not None else base_types.UninitialisedField(self, 'Rcvr', ReceiverData1, False)

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = base_types.UninitialisedField(self, 'Rcvr', ReceiverData1, False)

	@property
	def RptdFrd(self):
		return self._RptdFrd

	@RptdFrd.setter
	def RptdFrd(self, value):
		self._RptdFrd = value if value is not None else base_types.UninitialisedField(self, 'RptdFrd', ReportedFraud7, False)

	@RptdFrd.deleter
	def RptdFrd(self):
		del self._RptdFrd
		self._RptdFrd = base_types.UninitialisedField(self, 'RptdFrd', ReportedFraud7, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType41, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType41, False)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', SenderData1, False)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', SenderData1, False)

	@property
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if value is not None else base_types.UninitialisedField(self, 'SttlmSvc', SettlementService7, False)

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = base_types.UninitialisedField(self, 'SttlmSvc', SettlementService7, False)

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if value is not None else base_types.UninitialisedField(self, 'Tkn', Token5, False)

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = base_types.UninitialisedField(self, 'Tkn', Token5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdDspstnSts', type=FraudDispositionStatus3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdTxId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdFrd', type=ReportedFraud7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
	))