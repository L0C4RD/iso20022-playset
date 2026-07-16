# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsJustification1
from . import TrueFalseIndicator

class SettlementFailsDerogation1(base_types._BaseFieldType):

	__slots__ = ["_ElgbltyInd", "_Justfn"]
	@property
	def ElgbltyInd(self):
		return self._ElgbltyInd

	@ElgbltyInd.setter
	def ElgbltyInd(self, value):
		self._ElgbltyInd = value if value is not None else base_types.UninitialisedField(self, 'ElgbltyInd', TrueFalseIndicator, False)

	@ElgbltyInd.deleter
	def ElgbltyInd(self):
		del self._ElgbltyInd
		self._ElgbltyInd = base_types.UninitialisedField(self, 'ElgbltyInd', TrueFalseIndicator, False)

	@property
	def Justfn(self):
		return self._Justfn

	@Justfn.setter
	def Justfn(self, value):
		self._Justfn = value if value is not None else base_types.UninitialisedField(self, 'Justfn', SettlementFailsJustification1, False)

	@Justfn.deleter
	def Justfn(self):
		del self._Justfn
		self._Justfn = base_types.UninitialisedField(self, 'Justfn', SettlementFailsJustification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgbltyInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Justfn', type=SettlementFailsJustification1, min=0, max=1, mutex_group=None, array=False),
	))