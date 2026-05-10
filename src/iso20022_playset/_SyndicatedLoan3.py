from . import base_types
from ._PercentageRate import PercentageRate
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._TradeParty6 import TradeParty6
from ._ExchangeRate1 import ExchangeRate1

class SyndicatedLoan3(base_types._BaseFieldType):

	__slots__ = ["_Shr", "_Lndr", "_Amt", "_Brrwr", "_XchgRateInf"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if type(value) != base_types.auto else self.make_default("Brrwr")

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = None

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if type(value) != base_types.auto else self.make_default("Lndr")

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = None

	@property
	def Shr(self):
		return self._Shr

	@Shr.setter
	def Shr(self, value):
		self._Shr = value if type(value) != base_types.auto else self.make_default("Shr")

	@Shr.deleter
	def Shr(self):
		del self._Shr
		self._Shr = None

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if type(value) != base_types.auto else self.make_default("XchgRateInf")

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=TradeParty6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Shr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRate1, min=0, max=1, mutex_group=None, array=False),
	))

