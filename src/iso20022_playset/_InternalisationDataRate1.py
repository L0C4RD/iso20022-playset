# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate

class InternalisationDataRate1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_VolPctg"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	@property
	def VolPctg(self):
		return self._VolPctg

	@VolPctg.setter
	def VolPctg(self, value):
		self._VolPctg = value if value is not None else base_types.UninitialisedField(self, 'VolPctg', PercentageRate, False)

	@VolPctg.deleter
	def VolPctg(self):
		del self._VolPctg
		self._VolPctg = base_types.UninitialisedField(self, 'VolPctg', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))