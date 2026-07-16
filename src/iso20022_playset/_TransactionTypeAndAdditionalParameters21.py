# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveryReceiptType2Code
from . import Max35Text
from . import SecuritiesFinancingTransactionType2Code
from . import YesNoIndicator

class TransactionTypeAndAdditionalParameters21(base_types._BaseFieldType):

	__slots__ = ["_CmonId", "_NonceId", "_Pmt", "_RcncltnInd", "_SctiesFincgTxTp"]
	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if value is not None else base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def RcncltnInd(self):
		return self._RcncltnInd

	@RcncltnInd.setter
	def RcncltnInd(self, value):
		self._RcncltnInd = value if value is not None else base_types.UninitialisedField(self, 'RcncltnInd', YesNoIndicator, False)

	@RcncltnInd.deleter
	def RcncltnInd(self):
		del self._RcncltnInd
		self._RcncltnInd = base_types.UninitialisedField(self, 'RcncltnInd', YesNoIndicator, False)

	@property
	def SctiesFincgTxTp(self):
		return self._SctiesFincgTxTp

	@SctiesFincgTxTp.setter
	def SctiesFincgTxTp(self, value):
		self._SctiesFincgTxTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTxTp', SecuritiesFinancingTransactionType2Code, False)

	@SctiesFincgTxTp.deleter
	def SctiesFincgTxTp(self):
		del self._SctiesFincgTxTp
		self._SctiesFincgTxTp = base_types.UninitialisedField(self, 'SctiesFincgTxTp', SecuritiesFinancingTransactionType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxTp', type=SecuritiesFinancingTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
	))