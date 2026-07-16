# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmountRange2
from . import RateType4Choice

class Rate4(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_VldtyRg"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', RateType4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', RateType4Choice, False)

	@property
	def VldtyRg(self):
		return self._VldtyRg

	@VldtyRg.setter
	def VldtyRg(self, value):
		self._VldtyRg = value if value is not None else base_types.UninitialisedField(self, 'VldtyRg', ActiveOrHistoricCurrencyAndAmountRange2, False)

	@VldtyRg.deleter
	def VldtyRg(self):
		del self._VldtyRg
		self._VldtyRg = base_types.UninitialisedField(self, 'VldtyRg', ActiveOrHistoricCurrencyAndAmountRange2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=RateType4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyRg', type=ActiveOrHistoricCurrencyAndAmountRange2, min=0, max=1, mutex_group=None, array=False),
	))