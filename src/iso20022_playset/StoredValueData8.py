import base_types
import StoredValueAccount2
import ActiveCurrencyCode
import Max35NumericText
import ImpliedCurrencyAndAmount
import StoredValueTransactionType3Code
import TransactionIdentifier1
import Max35Text
import PaymentTransaction165

class StoredValueData8(base_types._BaseFieldType):

	__slots__ = ["_HstTxId", "_Prvdr", "_Ccy", "_EANUPC", "_ItmAmt", "_TxTp", "_PdctCd", "_OrgnlPOITx", "_AcctId"]
	@property
	def HstTxId(self):
		return self._HstTxId

	@HstTxId.setter
	def HstTxId(self, value):
		self._HstTxId = value if type(value) != auto else self.make_default("HstTxId")

	@HstTxId.deleter
	def HstTxId(self):
		del self._HstTxId
		self._HstTxId = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

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
	def EANUPC(self):
		return self._EANUPC

	@EANUPC.setter
	def EANUPC(self, value):
		self._EANUPC = value if type(value) != auto else self.make_default("EANUPC")

	@EANUPC.deleter
	def EANUPC(self):
		del self._EANUPC
		self._EANUPC = None

	@property
	def ItmAmt(self):
		return self._ItmAmt

	@ItmAmt.setter
	def ItmAmt(self, value):
		self._ItmAmt = value if type(value) != auto else self.make_default("ItmAmt")

	@ItmAmt.deleter
	def ItmAmt(self):
		del self._ItmAmt
		self._ItmAmt = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

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

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EANUPC', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=StoredValueTransactionType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPOITx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=StoredValueAccount2, min=0, max=1, mutex_group=None, array=False),
	))

