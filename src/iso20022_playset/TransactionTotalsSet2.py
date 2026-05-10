from . import base_types
import LoyaltyTransactionTotals1
import Max2NumericText
import TransactionTotals8
import PaymentInstrumentType2Code
import Organisation26
import Max35Text

class TransactionTotalsSet2(base_types._BaseFieldType):

	__slots__ = ["_SaleRcncltnId", "_Brnd", "_LltyTxTtl", "_SaleId", "_CshrId", "_PmtInstrmTp", "_ShftNb", "_POIId", "_SpnsrdMrchnt", "_TxTtl", "_AcqrrId", "_RcncltnId"]
	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if type(value) != auto else self.make_default("SaleRcncltnId")

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = None

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if type(value) != auto else self.make_default("Brnd")

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = None

	@property
	def LltyTxTtl(self):
		return self._LltyTxTtl

	@LltyTxTtl.setter
	def LltyTxTtl(self, value):
		self._LltyTxTtl = value if type(value) != auto else self.make_default("LltyTxTtl")

	@LltyTxTtl.deleter
	def LltyTxTtl(self):
		del self._LltyTxTtl
		self._LltyTxTtl = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	@property
	def CshrId(self):
		return self._CshrId

	@CshrId.setter
	def CshrId(self, value):
		self._CshrId = value if type(value) != auto else self.make_default("CshrId")

	@CshrId.deleter
	def CshrId(self):
		del self._CshrId
		self._CshrId = None

	@property
	def PmtInstrmTp(self):
		return self._PmtInstrmTp

	@PmtInstrmTp.setter
	def PmtInstrmTp(self, value):
		self._PmtInstrmTp = value if type(value) != auto else self.make_default("PmtInstrmTp")

	@PmtInstrmTp.deleter
	def PmtInstrmTp(self):
		del self._PmtInstrmTp
		self._PmtInstrmTp = None

	@property
	def ShftNb(self):
		return self._ShftNb

	@ShftNb.setter
	def ShftNb(self, value):
		self._ShftNb = value if type(value) != auto else self.make_default("ShftNb")

	@ShftNb.deleter
	def ShftNb(self):
		del self._ShftNb
		self._ShftNb = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def SpnsrdMrchnt(self):
		return self._SpnsrdMrchnt

	@SpnsrdMrchnt.setter
	def SpnsrdMrchnt(self, value):
		self._SpnsrdMrchnt = value if type(value) != auto else self.make_default("SpnsrdMrchnt")

	@SpnsrdMrchnt.deleter
	def SpnsrdMrchnt(self):
		del self._SpnsrdMrchnt
		self._SpnsrdMrchnt = None

	@property
	def TxTtl(self):
		return self._TxTtl

	@TxTtl.setter
	def TxTtl(self, value):
		self._TxTtl = value if type(value) != auto else self.make_default("TxTtl")

	@TxTtl.deleter
	def TxTtl(self):
		del self._TxTtl
		self._TxTtl = None

	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if type(value) != auto else self.make_default("AcqrrId")

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyTxTtl', type=LoyaltyTransactionTotals1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrmTp', type=PaymentInstrumentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShftNb', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrdMrchnt', type=Organisation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtl', type=TransactionTotals8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

