from . import base_types
from .CurrencyOrDigitalTokenAmount2Choice import CurrencyOrDigitalTokenAmount2Choice
from .ISODate import ISODate

class AmountsAndValueDate8(base_types._BaseFieldType):

	__slots__ = ["_TradgSdSellAmt", "_TradgSdBuyAmt", "_SttlmDt"]
	@property
	def TradgSdSellAmt(self):
		return self._TradgSdSellAmt

	@TradgSdSellAmt.setter
	def TradgSdSellAmt(self, value):
		self._TradgSdSellAmt = value if type(value) != auto else self.make_default("TradgSdSellAmt")

	@TradgSdSellAmt.deleter
	def TradgSdSellAmt(self):
		del self._TradgSdSellAmt
		self._TradgSdSellAmt = None

	@property
	def TradgSdBuyAmt(self):
		return self._TradgSdBuyAmt

	@TradgSdBuyAmt.setter
	def TradgSdBuyAmt(self, value):
		self._TradgSdBuyAmt = value if type(value) != auto else self.make_default("TradgSdBuyAmt")

	@TradgSdBuyAmt.deleter
	def TradgSdBuyAmt(self):
		del self._TradgSdBuyAmt
		self._TradgSdBuyAmt = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgSdSellAmt', type=CurrencyOrDigitalTokenAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdBuyAmt', type=CurrencyOrDigitalTokenAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

