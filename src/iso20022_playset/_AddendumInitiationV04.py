# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._AcceptorData1 import AcceptorData1
from ._AcquirerData1 import AcquirerData1
from ._AdditionalFee4 import AdditionalFee4
from ._CardData14 import CardData14
from ._ContentInformationType41 import ContentInformationType41
from ._Customer4 import Customer4
from ._DestinationData1 import DestinationData1
from ._EncryptedData2 import EncryptedData2
from ._Header72 import Header72
from ._IssuerData1 import IssuerData1
from ._Jurisdiction2 import Jurisdiction2
from ._Max1000Text import Max1000Text
from ._Max70Text import Max70Text
from ._OriginalDataElements6 import OriginalDataElements6
from ._OriginatorData2 import OriginatorData2
from ._ProgrammeMode6 import ProgrammeMode6
from ._ReceiverData1 import ReceiverData1
from ._Reconciliation5 import Reconciliation5
from ._SenderData1 import SenderData1
from ._SettlementService7 import SettlementService7
from ._Token5 import Token5
from ._TransactionIdentification62 import TransactionIdentification62
from ._TransactionSpecificData1 import TransactionSpecificData1

class AddendumInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_Acqrr", "_AddtlFee", "_Card", "_Cstmr", "_DataSrc", "_Dstn", "_Hdr", "_Issr", "_Jursdctn", "_NtlData", "_OrgnlDataElmts", "_Orgtr", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Rcncltn", "_Rcvr", "_SctyTrlr", "_Sndr", "_SttlmSvc", "_Tkn", "_TxDesc", "_TxId", "_TxSpcfcData"]
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
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if type(value) != base_types.auto else self.make_default("Cstmr")

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = None

	@property
	def DataSrc(self):
		return self._DataSrc

	@DataSrc.setter
	def DataSrc(self, value):
		self._DataSrc = value if type(value) != base_types.auto else self.make_default("DataSrc")

	@DataSrc.deleter
	def DataSrc(self):
		del self._DataSrc
		self._DataSrc = None

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def OrgnlDataElmts(self):
		return self._OrgnlDataElmts

	@OrgnlDataElmts.setter
	def OrgnlDataElmts(self, value):
		self._OrgnlDataElmts = value if type(value) != base_types.auto else self.make_default("OrgnlDataElmts")

	@OrgnlDataElmts.deleter
	def OrgnlDataElmts(self):
		del self._OrgnlDataElmts
		self._OrgnlDataElmts = None

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
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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
	def TxDesc(self):
		return self._TxDesc

	@TxDesc.setter
	def TxDesc(self, value):
		self._TxDesc = value if type(value) != base_types.auto else self.make_default("TxDesc")

	@TxDesc.deleter
	def TxDesc(self):
		del self._TxDesc
		self._TxDesc = None

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
	def TxSpcfcData(self):
		return self._TxSpcfcData

	@TxSpcfcData.setter
	def TxSpcfcData(self, value):
		self._TxSpcfcData = value if type(value) != base_types.auto else self.make_default("TxSpcfcData")

	@TxSpcfcData.deleter
	def TxSpcfcData(self):
		del self._TxSpcfcData
		self._TxSpcfcData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=AcceptorData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cstmr', type=Customer4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSrc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlDataElmts', type=OriginalDataElements6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification62, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSpcfcData', type=TransactionSpecificData1, min=0, max=1, mutex_group=None, array=False),
	))