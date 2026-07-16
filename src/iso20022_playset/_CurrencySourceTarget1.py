# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode

class CurrencySourceTarget1(base_types._BaseFieldType):

	__slots__ = ["_SrcCcy", "_TrgtCcy"]
	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if value is not None else base_types.UninitialisedField(self, 'SrcCcy', ActiveOrHistoricCurrencyCode, False)

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = base_types.UninitialisedField(self, 'SrcCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcy', ActiveOrHistoricCurrencyCode, False)

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = base_types.UninitialisedField(self, 'TrgtCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrcCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))