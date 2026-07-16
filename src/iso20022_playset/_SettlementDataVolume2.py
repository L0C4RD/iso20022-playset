# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20PositiveDecimalNumber
from . import Max20PositiveNumber

class SettlementDataVolume2(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Vol"]
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

	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if value is not None else base_types.UninitialisedField(self, 'Vol', Max20PositiveNumber, False)

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = base_types.UninitialisedField(self, 'Vol', Max20PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max20PositiveDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
	))