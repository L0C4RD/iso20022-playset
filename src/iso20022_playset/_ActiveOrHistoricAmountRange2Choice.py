# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmountRange2
from . import ImpliedCurrencyAndAmountRange1

class ActiveOrHistoricAmountRange2Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyAndAmtRg", "_ImpldCcyAndAmtRg"]
	@property
	def CcyAndAmtRg(self):
		return self._CcyAndAmtRg

	@CcyAndAmtRg.setter
	def CcyAndAmtRg(self, value):
		self._CcyAndAmtRg = value if value is not None else base_types.UninitialisedField(self, 'CcyAndAmtRg', ActiveOrHistoricCurrencyAndAmountRange2, False)

	@CcyAndAmtRg.deleter
	def CcyAndAmtRg(self):
		del self._CcyAndAmtRg
		self._CcyAndAmtRg = base_types.UninitialisedField(self, 'CcyAndAmtRg', ActiveOrHistoricCurrencyAndAmountRange2, False)

	@property
	def ImpldCcyAndAmtRg(self):
		return self._ImpldCcyAndAmtRg

	@ImpldCcyAndAmtRg.setter
	def ImpldCcyAndAmtRg(self, value):
		self._ImpldCcyAndAmtRg = value if value is not None else base_types.UninitialisedField(self, 'ImpldCcyAndAmtRg', ImpliedCurrencyAndAmountRange1, False)

	@ImpldCcyAndAmtRg.deleter
	def ImpldCcyAndAmtRg(self):
		del self._ImpldCcyAndAmtRg
		self._ImpldCcyAndAmtRg = base_types.UninitialisedField(self, 'ImpldCcyAndAmtRg', ImpliedCurrencyAndAmountRange1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyAndAmtRg', type=ActiveOrHistoricCurrencyAndAmountRange2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ImpldCcyAndAmtRg', type=ImpliedCurrencyAndAmountRange1, min=0, max=1, mutex_group=1, array=False),
	))