import base_types
import Max35Text
import Max140Text
import RetailerReversalResult7
import ImpliedCurrencyAndAmount
import PaymentReceipt6
import TransactionIdentifier1

class ReversalResponse9(base_types._BaseFieldType):

	__slots__ = ["_POIRcncltnId", "_SaleRefId", "_RvslTxRslt", "_RvsdAmt", "_SaleTxId", "_Rct", "_IssrRefData", "_POITxId"]
	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def RvslTxRslt(self):
		return self._RvslTxRslt

	@RvslTxRslt.setter
	def RvslTxRslt(self, value):
		self._RvslTxRslt = value if type(value) != auto else self.make_default("RvslTxRslt")

	@RvslTxRslt.deleter
	def RvslTxRslt(self):
		del self._RvslTxRslt
		self._RvslTxRslt = None

	@property
	def RvsdAmt(self):
		return self._RvsdAmt

	@RvsdAmt.setter
	def RvsdAmt(self, value):
		self._RvsdAmt = value if type(value) != auto else self.make_default("RvsdAmt")

	@RvsdAmt.deleter
	def RvsdAmt(self):
		del self._RvsdAmt
		self._RvsdAmt = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def Rct(self):
		return self._Rct

	@Rct.setter
	def Rct(self, value):
		self._Rct = value if type(value) != auto else self.make_default("Rct")

	@Rct.deleter
	def Rct(self):
		del self._Rct
		self._Rct = None

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if type(value) != auto else self.make_default("IssrRefData")

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = None

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if type(value) != auto else self.make_default("POITxId")

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslTxRslt', type=RetailerReversalResult7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rct', type=PaymentReceipt6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))

