# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import YesNoIndicator

class PercentageRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_BdryRate", "_Incl"]
	@property
	def BdryRate(self):
		return self._BdryRate

	@BdryRate.setter
	def BdryRate(self, value):
		self._BdryRate = value if value is not None else base_types.UninitialisedField(self, 'BdryRate', PercentageRate, False)

	@BdryRate.deleter
	def BdryRate(self):
		del self._BdryRate
		self._BdryRate = base_types.UninitialisedField(self, 'BdryRate', PercentageRate, False)

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if value is not None else base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BdryRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))