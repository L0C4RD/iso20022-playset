from . import base_types
from ._AmountAndCurrencyExchangeDetails6 import AmountAndCurrencyExchangeDetails6
from ._AmountAndCurrencyExchangeDetails5 import AmountAndCurrencyExchangeDetails5

class AmountAndCurrencyExchange4(base_types._BaseFieldType):

	__slots__ = ["_CntrValAmt", "_AnncdPstngAmt", "_TxAmt", "_InstdAmt", "_PrtryAmt"]
	@property
	def CntrValAmt(self):
		return self._CntrValAmt

	@CntrValAmt.setter
	def CntrValAmt(self, value):
		self._CntrValAmt = value if type(value) != base_types.auto else self.make_default("CntrValAmt")

	@CntrValAmt.deleter
	def CntrValAmt(self):
		del self._CntrValAmt
		self._CntrValAmt = None

	@property
	def AnncdPstngAmt(self):
		return self._AnncdPstngAmt

	@AnncdPstngAmt.setter
	def AnncdPstngAmt(self, value):
		self._AnncdPstngAmt = value if type(value) != base_types.auto else self.make_default("AnncdPstngAmt")

	@AnncdPstngAmt.deleter
	def AnncdPstngAmt(self):
		del self._AnncdPstngAmt
		self._AnncdPstngAmt = None

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if type(value) != base_types.auto else self.make_default("TxAmt")

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = None

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != base_types.auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def PrtryAmt(self):
		return self._PrtryAmt

	@PrtryAmt.setter
	def PrtryAmt(self, value):
		self._PrtryAmt = value if type(value) != base_types.auto else self.make_default("PrtryAmt")

	@PrtryAmt.deleter
	def PrtryAmt(self):
		del self._PrtryAmt
		self._PrtryAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrValAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AnncdPstngAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmt', type=AmountAndCurrencyExchangeDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryAmt', type=AmountAndCurrencyExchangeDetails6, min=0, max=None, mutex_group=None, array=True),
	))

