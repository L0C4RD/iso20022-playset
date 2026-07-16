# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestorType4Code
from . import TargetMarket1Code

class TargetMarket5Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Tp"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', TargetMarket1Code, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', TargetMarket1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', InvestorType4Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', InvestorType4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=TargetMarket1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=InvestorType4Code, min=0, max=1, mutex_group=1, array=False),
	))