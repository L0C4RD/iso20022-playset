# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max3NumericText

class MaximumAmountByPeriod1(base_types._BaseFieldType):

	__slots__ = ["_MaxAmt", "_NbOfDays"]
	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxAmt', ActiveCurrencyAndAmount, False)

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = base_types.UninitialisedField(self, 'MaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Max3NumericText, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Max3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))