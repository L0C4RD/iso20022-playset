# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max3Number
from . import RateBasis1Code

class InterestRateContractTerm2(base_types._BaseFieldType):

	__slots__ = ["_Unit", "_Val"]
	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', RateBasis1Code, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', RateBasis1Code, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max3Number, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max3Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Unit', type=RateBasis1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max3Number, min=1, max=1, mutex_group=None, array=False),
	))