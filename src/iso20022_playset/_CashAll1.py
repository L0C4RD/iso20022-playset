# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import YesNoIndicator

class CashAll1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Ind"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if value is not None else base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))