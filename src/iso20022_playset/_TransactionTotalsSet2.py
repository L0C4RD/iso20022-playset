# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyTransactionTotals1
from . import Max2NumericText
from . import Max35Text
from . import Organisation26
from . import PaymentInstrumentType2Code
from . import TransactionTotals8

class TransactionTotalsSet2(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_Brnd", "_CshrId", "_LltyTxTtl", "_POIId", "_PmtInstrmTp", "_RcncltnId", "_SaleId", "_SaleRcncltnId", "_ShftNb", "_SpnsrdMrchnt", "_TxTtl"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if value is not None else base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@property
	def CshrId(self):
		return self._CshrId

	@CshrId.setter
	def CshrId(self, value):
		self._CshrId = value if value is not None else base_types.UninitialisedField(self, 'CshrId', Max35Text, False)

	@CshrId.deleter
	def CshrId(self):
		del self._CshrId
		self._CshrId = base_types.UninitialisedField(self, 'CshrId', Max35Text, False)

	@property
	def LltyTxTtl(self):
		return self._LltyTxTtl

	@LltyTxTtl.setter
	def LltyTxTtl(self, value):
		self._LltyTxTtl = value if value is not None else base_types.UninitialisedField(self, 'LltyTxTtl', LoyaltyTransactionTotals1, True)

	@LltyTxTtl.deleter
	def LltyTxTtl(self):
		del self._LltyTxTtl
		self._LltyTxTtl = base_types.UninitialisedField(self, 'LltyTxTtl', LoyaltyTransactionTotals1, True)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', Max35Text, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', Max35Text, False)

	@property
	def PmtInstrmTp(self):
		return self._PmtInstrmTp

	@PmtInstrmTp.setter
	def PmtInstrmTp(self, value):
		self._PmtInstrmTp = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrmTp', PaymentInstrumentType2Code, False)

	@PmtInstrmTp.deleter
	def PmtInstrmTp(self):
		del self._PmtInstrmTp
		self._PmtInstrmTp = base_types.UninitialisedField(self, 'PmtInstrmTp', PaymentInstrumentType2Code, False)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if value is not None else base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

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
	def ShftNb(self):
		return self._ShftNb

	@ShftNb.setter
	def ShftNb(self, value):
		self._ShftNb = value if value is not None else base_types.UninitialisedField(self, 'ShftNb', Max2NumericText, False)

	@ShftNb.deleter
	def ShftNb(self):
		del self._ShftNb
		self._ShftNb = base_types.UninitialisedField(self, 'ShftNb', Max2NumericText, False)

	@property
	def SpnsrdMrchnt(self):
		return self._SpnsrdMrchnt

	@SpnsrdMrchnt.setter
	def SpnsrdMrchnt(self, value):
		self._SpnsrdMrchnt = value if value is not None else base_types.UninitialisedField(self, 'SpnsrdMrchnt', Organisation26, True)

	@SpnsrdMrchnt.deleter
	def SpnsrdMrchnt(self):
		del self._SpnsrdMrchnt
		self._SpnsrdMrchnt = base_types.UninitialisedField(self, 'SpnsrdMrchnt', Organisation26, True)

	@property
	def TxTtl(self):
		return self._TxTtl

	@TxTtl.setter
	def TxTtl(self, value):
		self._TxTtl = value if value is not None else base_types.UninitialisedField(self, 'TxTtl', TransactionTotals8, False)

	@TxTtl.deleter
	def TxTtl(self):
		del self._TxTtl
		self._TxTtl = base_types.UninitialisedField(self, 'TxTtl', TransactionTotals8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyTxTtl', type=LoyaltyTransactionTotals1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrmTp', type=PaymentInstrumentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShftNb', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrdMrchnt', type=Organisation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtl', type=TransactionTotals8, min=1, max=1, mutex_group=None, array=False),
	))