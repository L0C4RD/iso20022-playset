# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate

class RateType4Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Pctg"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))