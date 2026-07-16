# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentServiceType2Code
from . import ExternalCardTransactionCategory1Code
from . import ExternalRePresentmentReason1Code
from . import ISODate
from . import Max1025Text
from . import Max35Text
from . import PaymentContext3
from . import Product2
from . import TransactionIdentifier1

class CardIndividualTransaction2(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_ICCRltdData", "_Pdct", "_PmtCntxt", "_RePresntmntRsn", "_SaleRcncltnId", "_SaleRefNb", "_SeqNb", "_TxCtgy", "_TxId", "_VldtnDt", "_VldtnSeqNb"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if value is not None else base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType2Code, False)

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType2Code, False)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max1025Text, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max1025Text, False)

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if value is not None else base_types.UninitialisedField(self, 'Pdct', Product2, False)

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = base_types.UninitialisedField(self, 'Pdct', Product2, False)

	@property
	def PmtCntxt(self):
		return self._PmtCntxt

	@PmtCntxt.setter
	def PmtCntxt(self, value):
		self._PmtCntxt = value if value is not None else base_types.UninitialisedField(self, 'PmtCntxt', PaymentContext3, False)

	@PmtCntxt.deleter
	def PmtCntxt(self):
		del self._PmtCntxt
		self._PmtCntxt = base_types.UninitialisedField(self, 'PmtCntxt', PaymentContext3, False)

	@property
	def RePresntmntRsn(self):
		return self._RePresntmntRsn

	@RePresntmntRsn.setter
	def RePresntmntRsn(self, value):
		self._RePresntmntRsn = value if value is not None else base_types.UninitialisedField(self, 'RePresntmntRsn', ExternalRePresentmentReason1Code, False)

	@RePresntmntRsn.deleter
	def RePresntmntRsn(self):
		del self._RePresntmntRsn
		self._RePresntmntRsn = base_types.UninitialisedField(self, 'RePresntmntRsn', ExternalRePresentmentReason1Code, False)

	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

	@property
	def SaleRefNb(self):
		return self._SaleRefNb

	@SaleRefNb.setter
	def SaleRefNb(self, value):
		self._SaleRefNb = value if value is not None else base_types.UninitialisedField(self, 'SaleRefNb', Max35Text, False)

	@SaleRefNb.deleter
	def SaleRefNb(self):
		del self._SaleRefNb
		self._SaleRefNb = base_types.UninitialisedField(self, 'SaleRefNb', Max35Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@property
	def TxCtgy(self):
		return self._TxCtgy

	@TxCtgy.setter
	def TxCtgy(self, value):
		self._TxCtgy = value if value is not None else base_types.UninitialisedField(self, 'TxCtgy', ExternalCardTransactionCategory1Code, False)

	@TxCtgy.deleter
	def TxCtgy(self):
		del self._TxCtgy
		self._TxCtgy = base_types.UninitialisedField(self, 'TxCtgy', ExternalCardTransactionCategory1Code, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	@property
	def VldtnDt(self):
		return self._VldtnDt

	@VldtnDt.setter
	def VldtnDt(self, value):
		self._VldtnDt = value if value is not None else base_types.UninitialisedField(self, 'VldtnDt', ISODate, False)

	@VldtnDt.deleter
	def VldtnDt(self):
		del self._VldtnDt
		self._VldtnDt = base_types.UninitialisedField(self, 'VldtnDt', ISODate, False)

	@property
	def VldtnSeqNb(self):
		return self._VldtnSeqNb

	@VldtnSeqNb.setter
	def VldtnSeqNb(self, value):
		self._VldtnSeqNb = value if value is not None else base_types.UninitialisedField(self, 'VldtnSeqNb', Max35Text, False)

	@VldtnSeqNb.deleter
	def VldtnSeqNb(self):
		del self._VldtnSeqNb
		self._VldtnSeqNb = base_types.UninitialisedField(self, 'VldtnSeqNb', Max35Text, False)

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