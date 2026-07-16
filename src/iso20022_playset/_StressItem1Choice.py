# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RiskFactor1
from . import Strategy1
from . import StressedProduct1

class StressItem1Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdct", "_RskFctr", "_Strtgy"]
	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if value is not None else base_types.UninitialisedField(self, 'Pdct', StressedProduct1, False)

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = base_types.UninitialisedField(self, 'Pdct', StressedProduct1, False)

	@property
	def RskFctr(self):
		return self._RskFctr

	@RskFctr.setter
	def RskFctr(self, value):
		self._RskFctr = value if value is not None else base_types.UninitialisedField(self, 'RskFctr', RiskFactor1, False)

	@RskFctr.deleter
	def RskFctr(self):
		del self._RskFctr
		self._RskFctr = base_types.UninitialisedField(self, 'RskFctr', RiskFactor1, False)

	@property
	def Strtgy(self):
		return self._Strtgy

	@Strtgy.setter
	def Strtgy(self, value):
		self._Strtgy = value if value is not None else base_types.UninitialisedField(self, 'Strtgy', Strategy1, False)

	@Strtgy.deleter
	def Strtgy(self):
		del self._Strtgy
		self._Strtgy = base_types.UninitialisedField(self, 'Strtgy', Strategy1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdct', type=StressedProduct1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RskFctr', type=RiskFactor1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Strtgy', type=Strategy1, min=0, max=1, mutex_group=1, array=False),
	))