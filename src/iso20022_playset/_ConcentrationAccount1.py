# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection102
from . import Flows1
from . import Max10NumericText

class ConcentrationAccount1(base_types._BaseFieldType):

	__slots__ = ["_EndOfDay", "_InFlow", "_LatePmtConf", "_OutFlow", "_PeakCdt", "_PeakDbt"]
	@property
	def EndOfDay(self):
		return self._EndOfDay

	@EndOfDay.setter
	def EndOfDay(self, value):
		self._EndOfDay = value if value is not None else base_types.UninitialisedField(self, 'EndOfDay', AmountAndDirection102, False)

	@EndOfDay.deleter
	def EndOfDay(self):
		del self._EndOfDay
		self._EndOfDay = base_types.UninitialisedField(self, 'EndOfDay', AmountAndDirection102, False)

	@property
	def InFlow(self):
		return self._InFlow

	@InFlow.setter
	def InFlow(self, value):
		self._InFlow = value if value is not None else base_types.UninitialisedField(self, 'InFlow', Flows1, False)

	@InFlow.deleter
	def InFlow(self):
		del self._InFlow
		self._InFlow = base_types.UninitialisedField(self, 'InFlow', Flows1, False)

	@property
	def LatePmtConf(self):
		return self._LatePmtConf

	@LatePmtConf.setter
	def LatePmtConf(self, value):
		self._LatePmtConf = value if value is not None else base_types.UninitialisedField(self, 'LatePmtConf', Max10NumericText, False)

	@LatePmtConf.deleter
	def LatePmtConf(self):
		del self._LatePmtConf
		self._LatePmtConf = base_types.UninitialisedField(self, 'LatePmtConf', Max10NumericText, False)

	@property
	def OutFlow(self):
		return self._OutFlow

	@OutFlow.setter
	def OutFlow(self, value):
		self._OutFlow = value if value is not None else base_types.UninitialisedField(self, 'OutFlow', Flows1, False)

	@OutFlow.deleter
	def OutFlow(self):
		del self._OutFlow
		self._OutFlow = base_types.UninitialisedField(self, 'OutFlow', Flows1, False)

	@property
	def PeakCdt(self):
		return self._PeakCdt

	@PeakCdt.setter
	def PeakCdt(self, value):
		self._PeakCdt = value if value is not None else base_types.UninitialisedField(self, 'PeakCdt', ActiveCurrencyAndAmount, False)

	@PeakCdt.deleter
	def PeakCdt(self):
		del self._PeakCdt
		self._PeakCdt = base_types.UninitialisedField(self, 'PeakCdt', ActiveCurrencyAndAmount, False)

	@property
	def PeakDbt(self):
		return self._PeakDbt

	@PeakDbt.setter
	def PeakDbt(self, value):
		self._PeakDbt = value if value is not None else base_types.UninitialisedField(self, 'PeakDbt', ActiveCurrencyAndAmount, False)

	@PeakDbt.deleter
	def PeakDbt(self):
		del self._PeakDbt
		self._PeakDbt = base_types.UninitialisedField(self, 'PeakDbt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndOfDay', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InFlow', type=Flows1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePmtConf', type=Max10NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutFlow', type=Flows1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakCdt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakDbt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))