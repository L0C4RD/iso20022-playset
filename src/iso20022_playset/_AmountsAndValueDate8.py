# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyOrDigitalTokenAmount2Choice
from . import ISODate

class AmountsAndValueDate8(base_types._BaseFieldType):

	__slots__ = ["_SttlmDt", "_TradgSdBuyAmt", "_TradgSdSellAmt"]
	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def TradgSdBuyAmt(self):
		return self._TradgSdBuyAmt

	@TradgSdBuyAmt.setter
	def TradgSdBuyAmt(self, value):
		self._TradgSdBuyAmt = value if value is not None else base_types.UninitialisedField(self, 'TradgSdBuyAmt', CurrencyOrDigitalTokenAmount2Choice, False)

	@TradgSdBuyAmt.deleter
	def TradgSdBuyAmt(self):
		del self._TradgSdBuyAmt
		self._TradgSdBuyAmt = base_types.UninitialisedField(self, 'TradgSdBuyAmt', CurrencyOrDigitalTokenAmount2Choice, False)

	@property
	def TradgSdSellAmt(self):
		return self._TradgSdSellAmt

	@TradgSdSellAmt.setter
	def TradgSdSellAmt(self, value):
		self._TradgSdSellAmt = value if value is not None else base_types.UninitialisedField(self, 'TradgSdSellAmt', CurrencyOrDigitalTokenAmount2Choice, False)

	@TradgSdSellAmt.deleter
	def TradgSdSellAmt(self):
		del self._TradgSdSellAmt
		self._TradgSdSellAmt = base_types.UninitialisedField(self, 'TradgSdSellAmt', CurrencyOrDigitalTokenAmount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdBuyAmt', type=CurrencyOrDigitalTokenAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdSellAmt', type=CurrencyOrDigitalTokenAmount2Choice, min=1, max=1, mutex_group=None, array=False),
	))