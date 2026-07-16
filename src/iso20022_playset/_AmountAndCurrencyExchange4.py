# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndCurrencyExchangeDetails5
from . import AmountAndCurrencyExchangeDetails6

class AmountAndCurrencyExchange4(base_types._BaseFieldType):

	__slots__ = ["_AnncdPstngAmt", "_CntrValAmt", "_InstdAmt", "_PrtryAmt", "_TxAmt"]
	@property
	def AnncdPstngAmt(self):
		return self._AnncdPstngAmt

	@AnncdPstngAmt.setter
	def AnncdPstngAmt(self, value):
		self._AnncdPstngAmt = value if value is not None else base_types.UninitialisedField(self, 'AnncdPstngAmt', AmountAndCurrencyExchangeDetails5, False)

	@AnncdPstngAmt.deleter
	def AnncdPstngAmt(self):
		del self._AnncdPstngAmt
		self._AnncdPstngAmt = base_types.UninitialisedField(self, 'AnncdPstngAmt', AmountAndCurrencyExchangeDetails5, False)

	@property
	def CntrValAmt(self):
		return self._CntrValAmt

	@CntrValAmt.setter
	def CntrValAmt(self, value):
		self._CntrValAmt = value if value is not None else base_types.UninitialisedField(self, 'CntrValAmt', AmountAndCurrencyExchangeDetails5, False)

	@CntrValAmt.deleter
	def CntrValAmt(self):
		del self._CntrValAmt
		self._CntrValAmt = base_types.UninitialisedField(self, 'CntrValAmt', AmountAndCurrencyExchangeDetails5, False)

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if value is not None else base_types.UninitialisedField(self, 'InstdAmt', AmountAndCurrencyExchangeDetails5, False)

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = base_types.UninitialisedField(self, 'InstdAmt', AmountAndCurrencyExchangeDetails5, False)

	@property
	def PrtryAmt(self):
		return self._PrtryAmt

	@PrtryAmt.setter
	def PrtryAmt(self, value):
		self._PrtryAmt = value if value is not None else base_types.UninitialisedField(self, 'PrtryAmt', AmountAndCurrencyExchangeDetails6, True)

	@PrtryAmt.deleter
	def PrtryAmt(self):
		del self._PrtryAmt
		self._PrtryAmt = base_types.UninitialisedField(self, 'PrtryAmt', AmountAndCurrencyExchangeDetails6, True)

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if value is not None else base_types.UninitialisedField(self, 'TxAmt', AmountAndCurrencyExchangeDetails5, False)

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = base_types.UninitialisedField(self, 'TxAmt', AmountAndCurrencyExchangeDetails5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnncdPstngAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrValAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryAmt', type=AmountAndCurrencyExchangeDetails6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
	))