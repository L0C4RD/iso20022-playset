# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import PlusOrMinusIndicator

class Rate2(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Sgn"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))