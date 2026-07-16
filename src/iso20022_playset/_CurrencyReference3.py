# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ExchangeRateInformation1

class CurrencyReference3(base_types._BaseFieldType):

	__slots__ = ["_SrcCcy", "_TrgtCcy", "_XchgRateInf"]
	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if value is not None else base_types.UninitialisedField(self, 'SrcCcy', ActiveCurrencyCode, False)

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = base_types.UninitialisedField(self, 'SrcCcy', ActiveCurrencyCode, False)

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcy', ActiveCurrencyCode, False)

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = base_types.UninitialisedField(self, 'TrgtCcy', ActiveCurrencyCode, False)

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if value is not None else base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRateInformation1, True)

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRateInformation1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrcCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRateInformation1, min=0, max=None, mutex_group=None, array=True),
	))