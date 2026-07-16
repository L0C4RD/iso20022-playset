# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max35NumericText
from . import Max35Text
from . import PaymentTransaction165
from . import StoredValueAccount2
from . import StoredValueTransactionType3Code
from . import TransactionIdentifier1

class StoredValueData8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_Ccy", "_EANUPC", "_HstTxId", "_ItmAmt", "_OrgnlPOITx", "_PdctCd", "_Prvdr", "_TxTp"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', StoredValueAccount2, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', StoredValueAccount2, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def EANUPC(self):
		return self._EANUPC

	@EANUPC.setter
	def EANUPC(self, value):
		self._EANUPC = value if value is not None else base_types.UninitialisedField(self, 'EANUPC', Max35NumericText, False)

	@EANUPC.deleter
	def EANUPC(self):
		del self._EANUPC
		self._EANUPC = base_types.UninitialisedField(self, 'EANUPC', Max35NumericText, False)

	@property
	def HstTxId(self):
		return self._HstTxId

	@HstTxId.setter
	def HstTxId(self, value):
		self._HstTxId = value if value is not None else base_types.UninitialisedField(self, 'HstTxId', TransactionIdentifier1, False)

	@HstTxId.deleter
	def HstTxId(self):
		del self._HstTxId
		self._HstTxId = base_types.UninitialisedField(self, 'HstTxId', TransactionIdentifier1, False)

	@property
	def ItmAmt(self):
		return self._ItmAmt

	@ItmAmt.setter
	def ItmAmt(self, value):
		self._ItmAmt = value if value is not None else base_types.UninitialisedField(self, 'ItmAmt', ImpliedCurrencyAndAmount, False)

	@ItmAmt.deleter
	def ItmAmt(self):
		del self._ItmAmt
		self._ItmAmt = base_types.UninitialisedField(self, 'ItmAmt', ImpliedCurrencyAndAmount, False)

	@property
	def OrgnlPOITx(self):
		return self._OrgnlPOITx

	@OrgnlPOITx.setter
	def OrgnlPOITx(self, value):
		self._OrgnlPOITx = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPOITx', PaymentTransaction165, False)

	@OrgnlPOITx.deleter
	def OrgnlPOITx(self):
		del self._OrgnlPOITx
		self._OrgnlPOITx = base_types.UninitialisedField(self, 'OrgnlPOITx', PaymentTransaction165, False)

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max35Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max35Text, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', StoredValueTransactionType3Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', StoredValueTransactionType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=StoredValueAccount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EANUPC', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPOITx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=StoredValueTransactionType3Code, min=1, max=1, mutex_group=None, array=False),
	))