from . import base_types
from .Max35Text import Max35Text
from .DeliveryReceiptType2Code import DeliveryReceiptType2Code
from .YesNoIndicator import YesNoIndicator
from .SecuritiesFinancingTransactionType2Code import SecuritiesFinancingTransactionType2Code

class TransactionTypeAndAdditionalParameters21(base_types._BaseFieldType):

	__slots__ = ["_NonceId", "_CmonId", "_SctiesFincgTxTp", "_Pmt", "_RcncltnInd"]
	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if type(value) != base_types.auto else self.make_default("NonceId")

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = None

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if type(value) != base_types.auto else self.make_default("CmonId")

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = None

	@property
	def SctiesFincgTxTp(self):
		return self._SctiesFincgTxTp

	@SctiesFincgTxTp.setter
	def SctiesFincgTxTp(self, value):
		self._SctiesFincgTxTp = value if type(value) != base_types.auto else self.make_default("SctiesFincgTxTp")

	@SctiesFincgTxTp.deleter
	def SctiesFincgTxTp(self):
		del self._SctiesFincgTxTp
		self._SctiesFincgTxTp = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def RcncltnInd(self):
		return self._RcncltnInd

	@RcncltnInd.setter
	def RcncltnInd(self, value):
		self._RcncltnInd = value if type(value) != base_types.auto else self.make_default("RcncltnInd")

	@RcncltnInd.deleter
	def RcncltnInd(self):
		del self._RcncltnInd
		self._RcncltnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxTp', type=SecuritiesFinancingTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

