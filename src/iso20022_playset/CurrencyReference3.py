from . import base_types
from .ExchangeRateInformation1 import ExchangeRateInformation1
from .ActiveCurrencyCode import ActiveCurrencyCode

class CurrencyReference3(base_types._BaseFieldType):

	__slots__ = ["_XchgRateInf", "_SrcCcy", "_TrgtCcy"]
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

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if type(value) != base_types.auto else self.make_default("SrcCcy")

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = None

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if type(value) != base_types.auto else self.make_default("TrgtCcy")

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRateInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SrcCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

