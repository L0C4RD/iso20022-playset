# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime1Choice
from . import SettlementDateCode12Choice

class SettlementDate16Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Dt"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', SettlementDateCode12Choice, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', SettlementDateCode12Choice, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime1Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=SettlementDateCode12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=1, array=False),
	))