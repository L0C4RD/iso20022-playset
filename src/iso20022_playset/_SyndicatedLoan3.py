# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ExchangeRate1
from . import PercentageRate
from . import TradeParty6

class SyndicatedLoan3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Brrwr", "_Lndr", "_Shr", "_XchgRateInf"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if value is not None else base_types.UninitialisedField(self, 'Brrwr', TradeParty6, False)

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = base_types.UninitialisedField(self, 'Brrwr', TradeParty6, False)

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if value is not None else base_types.UninitialisedField(self, 'Lndr', TradeParty6, False)

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = base_types.UninitialisedField(self, 'Lndr', TradeParty6, False)

	@property
	def Shr(self):
		return self._Shr

	@Shr.setter
	def Shr(self, value):
		self._Shr = value if value is not None else base_types.UninitialisedField(self, 'Shr', PercentageRate, False)

	@Shr.deleter
	def Shr(self):
		del self._Shr
		self._Shr = base_types.UninitialisedField(self, 'Shr', PercentageRate, False)

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if value is not None else base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRate1, False)

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=TradeParty6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Shr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRate1, min=0, max=1, mutex_group=None, array=False),
	))