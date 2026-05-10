import base_types
import ImpliedCurrencyAndAmount
import LoyaltyTransactionType1Code
import TransactionIdentifier1
import ActiveCurrencyCode
import Product6
import PaymentTransaction165

class LoyaltyTransaction7(base_types._BaseFieldType):

	__slots__ = ["_SaleItm", "_TtlAmt", "_LltyTxTp", "_SaleTxId", "_Ccy", "_OrgnlPOITx"]
	@property
	def SaleItm(self):
		return self._SaleItm

	@SaleItm.setter
	def SaleItm(self, value):
		self._SaleItm = value if type(value) != auto else self.make_default("SaleItm")

	@SaleItm.deleter
	def SaleItm(self):
		del self._SaleItm
		self._SaleItm = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def LltyTxTp(self):
		return self._LltyTxTp

	@LltyTxTp.setter
	def LltyTxTp(self, value):
		self._LltyTxTp = value if type(value) != auto else self.make_default("LltyTxTp")

	@LltyTxTp.deleter
	def LltyTxTp(self):
		del self._LltyTxTp
		self._LltyTxTp = None

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
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def OrgnlPOITx(self):
		return self._OrgnlPOITx

	@OrgnlPOITx.setter
	def OrgnlPOITx(self, value):
		self._OrgnlPOITx = value if type(value) != auto else self.make_default("OrgnlPOITx")

	@OrgnlPOITx.deleter
	def OrgnlPOITx(self):
		del self._OrgnlPOITx
		self._OrgnlPOITx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleItm', type=Product6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyTxTp', type=LoyaltyTransactionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPOITx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
	))

