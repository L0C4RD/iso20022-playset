# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerOrder1
from . import LanguageCode
from . import LoyaltyAccount3
from . import Max35Text
from . import TransactionIdentifier1

class CardAcquisitionResponse3(base_types._BaseFieldType):

	__slots__ = ["_CstmrLang", "_CstmrOrdr", "_LltyAcct", "_POITxId", "_PmtBrnd", "_SaleTxId"]
	@property
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if value is not None else base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

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
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if value is not None else base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, True)

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, True)

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
	def PmtBrnd(self):
		return self._PmtBrnd

	@PmtBrnd.setter
	def PmtBrnd(self, value):
		self._PmtBrnd = value if value is not None else base_types.UninitialisedField(self, 'PmtBrnd', Max35Text, True)

	@PmtBrnd.deleter
	def PmtBrnd(self):
		del self._PmtBrnd
		self._PmtBrnd = base_types.UninitialisedField(self, 'PmtBrnd', Max35Text, True)

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
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))