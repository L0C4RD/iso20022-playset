from . import base_types
from .Max35Text import Max35Text
from .TransactionIdentifier1 import TransactionIdentifier1
from .CustomerOrder1 import CustomerOrder1
from .LoyaltyAccount3 import LoyaltyAccount3
from .LanguageCode import LanguageCode

class CardAcquisitionResponse3(base_types._BaseFieldType):

	__slots__ = ["_LltyAcct", "_PmtBrnd", "_POITxId", "_CstmrOrdr", "_SaleTxId", "_CstmrLang"]
	@property
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if type(value) != base_types.auto else self.make_default("LltyAcct")

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = None

	@property
	def PmtBrnd(self):
		return self._PmtBrnd

	@PmtBrnd.setter
	def PmtBrnd(self, value):
		self._PmtBrnd = value if type(value) != base_types.auto else self.make_default("PmtBrnd")

	@PmtBrnd.deleter
	def PmtBrnd(self):
		del self._PmtBrnd
		self._PmtBrnd = None

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
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if type(value) != base_types.auto else self.make_default("CstmrLang")

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
	))

