from . import base_types
from .SecuritiesFinancingTransactionType2Code import SecuritiesFinancingTransactionType2Code
from .DeliveryReceiptType2Code import DeliveryReceiptType2Code
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .YesNoIndicator import YesNoIndicator

class TransactionTypeAndAdditionalParameters18(base_types._BaseFieldType):

	__slots__ = ["_SctiesFincgTxTp", "_CmonId", "_RcncltnInd", "_Pmt"]
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
	def RcncltnInd(self):
		return self._RcncltnInd

	@RcncltnInd.setter
	def RcncltnInd(self, value):
		self._RcncltnInd = value if type(value) != base_types.auto else self.make_default("RcncltnInd")

	@RcncltnInd.deleter
	def RcncltnInd(self):
		del self._RcncltnInd
		self._RcncltnInd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesFincgTxTp', type=SecuritiesFinancingTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
	))

