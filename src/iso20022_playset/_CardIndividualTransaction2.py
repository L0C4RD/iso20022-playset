from . import base_types
from ._CardPaymentServiceType2Code import CardPaymentServiceType2Code
from ._ExternalCardTransactionCategory1Code import ExternalCardTransactionCategory1Code
from ._ExternalRePresentmentReason1Code import ExternalRePresentmentReason1Code
from ._ISODate import ISODate
from ._Max1025Text import Max1025Text
from ._Max35Text import Max35Text
from ._PaymentContext3 import PaymentContext3
from ._Product2 import Product2
from ._TransactionIdentifier1 import TransactionIdentifier1

class CardIndividualTransaction2(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_ICCRltdData", "_Pdct", "_PmtCntxt", "_RePresntmntRsn", "_SaleRcncltnId", "_SaleRefNb", "_SeqNb", "_TxCtgy", "_TxId", "_VldtnDt", "_VldtnSeqNb"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != base_types.auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != base_types.auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	@property
	def PmtCntxt(self):
		return self._PmtCntxt

	@PmtCntxt.setter
	def PmtCntxt(self, value):
		self._PmtCntxt = value if type(value) != base_types.auto else self.make_default("PmtCntxt")

	@PmtCntxt.deleter
	def PmtCntxt(self):
		del self._PmtCntxt
		self._PmtCntxt = None

	@property
	def RePresntmntRsn(self):
		return self._RePresntmntRsn

	@RePresntmntRsn.setter
	def RePresntmntRsn(self, value):
		self._RePresntmntRsn = value if type(value) != base_types.auto else self.make_default("RePresntmntRsn")

	@RePresntmntRsn.deleter
	def RePresntmntRsn(self):
		del self._RePresntmntRsn
		self._RePresntmntRsn = None

	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if type(value) != base_types.auto else self.make_default("SaleRcncltnId")

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = None

	@property
	def SaleRefNb(self):
		return self._SaleRefNb

	@SaleRefNb.setter
	def SaleRefNb(self, value):
		self._SaleRefNb = value if type(value) != base_types.auto else self.make_default("SaleRefNb")

	@SaleRefNb.deleter
	def SaleRefNb(self):
		del self._SaleRefNb
		self._SaleRefNb = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def TxCtgy(self):
		return self._TxCtgy

	@TxCtgy.setter
	def TxCtgy(self, value):
		self._TxCtgy = value if type(value) != base_types.auto else self.make_default("TxCtgy")

	@TxCtgy.deleter
	def TxCtgy(self):
		del self._TxCtgy
		self._TxCtgy = None

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
	def VldtnDt(self):
		return self._VldtnDt

	@VldtnDt.setter
	def VldtnDt(self, value):
		self._VldtnDt = value if type(value) != base_types.auto else self.make_default("VldtnDt")

	@VldtnDt.deleter
	def VldtnDt(self):
		del self._VldtnDt
		self._VldtnDt = None

	@property
	def VldtnSeqNb(self):
		return self._VldtnSeqNb

	@VldtnSeqNb.setter
	def VldtnSeqNb(self, value):
		self._VldtnSeqNb = value if type(value) != base_types.auto else self.make_default("VldtnSeqNb")

	@VldtnSeqNb.deleter
	def VldtnSeqNb(self):
		del self._VldtnSeqNb
		self._VldtnSeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=Product2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCntxt', type=PaymentContext3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RePresntmntRsn', type=ExternalRePresentmentReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCtgy', type=ExternalCardTransactionCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnSeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

