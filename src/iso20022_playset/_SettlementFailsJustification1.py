# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20PositiveDecimalNumber
from . import SettlementDataRate1Choice

class SettlementFailsJustification1(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Val"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', SettlementDataRate1Choice, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', SettlementDataRate1Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max20PositiveDecimalNumber, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max20PositiveDecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=SettlementDataRate1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max20PositiveDecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))