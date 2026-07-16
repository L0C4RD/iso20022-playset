# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FloatingInterestRate6
from . import PercentageRate

class InterestRate6Choice(base_types._BaseFieldType):

	__slots__ = ["_Fltg", "_Fxd"]
	@property
	def Fltg(self):
		return self._Fltg

	@Fltg.setter
	def Fltg(self, value):
		self._Fltg = value if value is not None else base_types.UninitialisedField(self, 'Fltg', FloatingInterestRate6, False)

	@Fltg.deleter
	def Fltg(self):
		del self._Fltg
		self._Fltg = base_types.UninitialisedField(self, 'Fltg', FloatingInterestRate6, False)

	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if value is not None else base_types.UninitialisedField(self, 'Fxd', PercentageRate, False)

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = base_types.UninitialisedField(self, 'Fxd', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fltg', type=FloatingInterestRate6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fxd', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))