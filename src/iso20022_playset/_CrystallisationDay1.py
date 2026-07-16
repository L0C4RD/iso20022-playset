# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max3NumericText
from . import YesNoIndicator

class CrystallisationDay1(base_types._BaseFieldType):

	__slots__ = ["_Day", "_Prd"]
	@property
	def Day(self):
		return self._Day

	@Day.setter
	def Day(self, value):
		self._Day = value if value is not None else base_types.UninitialisedField(self, 'Day', YesNoIndicator, False)

	@Day.deleter
	def Day(self):
		del self._Day
		self._Day = base_types.UninitialisedField(self, 'Day', YesNoIndicator, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Max3NumericText, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Max3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Day', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
	))