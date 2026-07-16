# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import VariableInterest1Rate

class InterestRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_FxdIntrstRate", "_VarblIntrstRate"]
	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'FxdIntrstRate', PercentageRate, False)

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = base_types.UninitialisedField(self, 'FxdIntrstRate', PercentageRate, False)

	@property
	def VarblIntrstRate(self):
		return self._VarblIntrstRate

	@VarblIntrstRate.setter
	def VarblIntrstRate(self, value):
		self._VarblIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'VarblIntrstRate', VariableInterest1Rate, False)

	@VarblIntrstRate.deleter
	def VarblIntrstRate(self):
		del self._VarblIntrstRate
		self._VarblIntrstRate = base_types.UninitialisedField(self, 'VarblIntrstRate', VariableInterest1Rate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxdIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VarblIntrstRate', type=VariableInterest1Rate, min=0, max=1, mutex_group=1, array=False),
	))