# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BaseOneRate

class CurrencyExchange13(base_types._BaseFieldType):

	__slots__ = ["_SrcCcy", "_TrgtCcy", "_UnitCcy", "_XchgRate"]
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
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if value is not None else base_types.UninitialisedField(self, 'UnitCcy', ActiveCurrencyCode, False)

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = base_types.UninitialisedField(self, 'UnitCcy', ActiveCurrencyCode, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrcCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))