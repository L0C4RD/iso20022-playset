# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerOrder1 import CustomerOrder1
from ._LoyaltyResult3 import LoyaltyResult3
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._PaymentReceipt6 import PaymentReceipt6
from ._RetailerPaymentResult7 import RetailerPaymentResult7
from ._TransactionIdentifier1 import TransactionIdentifier1

class PaymentResponse7(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_IssrRefData", "_LltyRslt", "_POIRcncltnId", "_POITxId", "_PmtRct", "_RtlrPmtRslt", "_SaleRefId", "_SaleTxId"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != base_types.auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if type(value) != base_types.auto else self.make_default("IssrRefData")

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = None

	@property
	def LltyRslt(self):
		return self._LltyRslt

	@LltyRslt.setter
	def LltyRslt(self, value):
		self._LltyRslt = value if type(value) != base_types.auto else self.make_default("LltyRslt")

	@LltyRslt.deleter
	def LltyRslt(self):
		del self._LltyRslt
		self._LltyRslt = None

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != base_types.auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if type(value) != base_types.auto else self.make_default("POITxId")

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = None

	@property
	def PmtRct(self):
		return self._PmtRct

	@PmtRct.setter
	def PmtRct(self, value):
		self._PmtRct = value if type(value) != base_types.auto else self.make_default("PmtRct")

	@PmtRct.deleter
	def PmtRct(self):
		del self._PmtRct
		self._PmtRct = None

	@property
	def RtlrPmtRslt(self):
		return self._RtlrPmtRslt

	@RtlrPmtRslt.setter
	def RtlrPmtRslt(self, value):
		self._RtlrPmtRslt = value if type(value) != base_types.auto else self.make_default("RtlrPmtRslt")

	@RtlrPmtRslt.deleter
	def RtlrPmtRslt(self):
		del self._RtlrPmtRslt
		self._RtlrPmtRslt = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != base_types.auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

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