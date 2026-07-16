# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class Value(base_types._BaseFieldType):

	__slots__ = ["_AltrnCcyItm", "_BaseCcyItm"]
	@property
	def AltrnCcyItm(self):
		return self._AltrnCcyItm

	@AltrnCcyItm.setter
	def AltrnCcyItm(self, value):
		self._AltrnCcyItm = value if value is not None else base_types.UninitialisedField(self, 'AltrnCcyItm', ActiveOrHistoricCurrencyAndAmount, True)

	@AltrnCcyItm.deleter
	def AltrnCcyItm(self):
		del self._AltrnCcyItm
		self._AltrnCcyItm = base_types.UninitialisedField(self, 'AltrnCcyItm', ActiveOrHistoricCurrencyAndAmount, True)

	@property
	def BaseCcyItm(self):
		return self._BaseCcyItm

	@BaseCcyItm.setter
	def BaseCcyItm(self, value):
		self._BaseCcyItm = value if value is not None else base_types.UninitialisedField(self, 'BaseCcyItm', ActiveOrHistoricCurrencyAndAmount, False)

	@BaseCcyItm.deleter
	def BaseCcyItm(self):
		del self._BaseCcyItm
		self._BaseCcyItm = base_types.UninitialisedField(self, 'BaseCcyItm', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnCcyItm', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BaseCcyItm', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))