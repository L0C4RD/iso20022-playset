# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LoyaltyTransactionType1Code import LoyaltyTransactionType1Code
from ._PaymentTransaction183 import PaymentTransaction183
from ._Product6 import Product6
from ._TransactionIdentifier1 import TransactionIdentifier1

class LoyaltyTransaction8(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_LltyTxTp", "_OrgnlPOITx", "_SaleItm", "_SaleTxId", "_TtlAmt"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def LltyTxTp(self):
		return self._LltyTxTp

	@LltyTxTp.setter
	def LltyTxTp(self, value):
		self._LltyTxTp = value if type(value) != base_types.auto else self.make_default("LltyTxTp")

	@LltyTxTp.deleter
	def LltyTxTp(self):
		del self._LltyTxTp
		self._LltyTxTp = None

	@property
	def OrgnlPOITx(self):
		return self._OrgnlPOITx

	@OrgnlPOITx.setter
	def OrgnlPOITx(self, value):
		self._OrgnlPOITx = value if type(value) != base_types.auto else self.make_default("OrgnlPOITx")

	@OrgnlPOITx.deleter
	def OrgnlPOITx(self):
		del self._OrgnlPOITx
		self._OrgnlPOITx = None

	@property
	def SaleItm(self):
		return self._SaleItm

	@SaleItm.setter
	def SaleItm(self, value):
		self._SaleItm = value if type(value) != base_types.auto else self.make_default("SaleItm")

	@SaleItm.deleter
	def SaleItm(self):
		del self._SaleItm
		self._SaleItm = None

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

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyTxTp', type=LoyaltyTransactionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPOITx', type=PaymentTransaction183, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleItm', type=Product6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))