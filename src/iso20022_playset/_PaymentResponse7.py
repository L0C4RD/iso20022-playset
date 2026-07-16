# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerOrder1
from . import LoyaltyResult3
from . import Max140Text
from . import Max35Text
from . import PaymentReceipt6
from . import RetailerPaymentResult7
from . import TransactionIdentifier1

class PaymentResponse7(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_IssrRefData", "_LltyRslt", "_POIRcncltnId", "_POITxId", "_PmtRct", "_RtlrPmtRslt", "_SaleRefId", "_SaleTxId"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if value is not None else base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

	@property
	def LltyRslt(self):
		return self._LltyRslt

	@LltyRslt.setter
	def LltyRslt(self, value):
		self._LltyRslt = value if value is not None else base_types.UninitialisedField(self, 'LltyRslt', LoyaltyResult3, True)

	@LltyRslt.deleter
	def LltyRslt(self):
		del self._LltyRslt
		self._LltyRslt = base_types.UninitialisedField(self, 'LltyRslt', LoyaltyResult3, True)

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if value is not None else base_types.UninitialisedField(self, 'POITxId', TransactionIdentifier1, False)

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = base_types.UninitialisedField(self, 'POITxId', TransactionIdentifier1, False)

	@property
	def PmtRct(self):
		return self._PmtRct

	@PmtRct.setter
	def PmtRct(self, value):
		self._PmtRct = value if value is not None else base_types.UninitialisedField(self, 'PmtRct', PaymentReceipt6, True)

	@PmtRct.deleter
	def PmtRct(self):
		del self._PmtRct
		self._PmtRct = base_types.UninitialisedField(self, 'PmtRct', PaymentReceipt6, True)

	@property
	def RtlrPmtRslt(self):
		return self._RtlrPmtRslt

	@RtlrPmtRslt.setter
	def RtlrPmtRslt(self, value):
		self._RtlrPmtRslt = value if value is not None else base_types.UninitialisedField(self, 'RtlrPmtRslt', RetailerPaymentResult7, False)

	@RtlrPmtRslt.deleter
	def RtlrPmtRslt(self):
		del self._RtlrPmtRslt
		self._RtlrPmtRslt = base_types.UninitialisedField(self, 'RtlrPmtRslt', RetailerPaymentResult7, False)

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if value is not None else base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if value is not None else base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyRslt', type=LoyaltyResult3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRct', type=PaymentReceipt6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtlrPmtRslt', type=RetailerPaymentResult7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))