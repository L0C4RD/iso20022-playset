# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate

class PercentageTolerance1(base_types._BaseFieldType):

	__slots__ = ["_MnsPct", "_PlusPct"]
	@property
	def MnsPct(self):
		return self._MnsPct

	@MnsPct.setter
	def MnsPct(self, value):
		self._MnsPct = value if value is not None else base_types.UninitialisedField(self, 'MnsPct', PercentageRate, False)

	@MnsPct.deleter
	def MnsPct(self):
		del self._MnsPct
		self._MnsPct = base_types.UninitialisedField(self, 'MnsPct', PercentageRate, False)

	@property
	def PlusPct(self):
		return self._PlusPct

	@PlusPct.setter
	def PlusPct(self, value):
		self._PlusPct = value if value is not None else base_types.UninitialisedField(self, 'PlusPct', PercentageRate, False)

	@PlusPct.deleter
	def PlusPct(self):
		del self._PlusPct
		self._PlusPct = base_types.UninitialisedField(self, 'PlusPct', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MnsPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlusPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))