# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1Choice
from . import SystemStatus2Choice

class SystemStatus3(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_VldtyTm"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', SystemStatus2Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', SystemStatus2Choice, False)

	@property
	def VldtyTm(self):
		return self._VldtyTm

	@VldtyTm.setter
	def VldtyTm(self, value):
		self._VldtyTm = value if value is not None else base_types.UninitialisedField(self, 'VldtyTm', DateTimePeriod1Choice, False)

	@VldtyTm.deleter
	def VldtyTm(self):
		del self._VldtyTm
		self._VldtyTm = base_types.UninitialisedField(self, 'VldtyTm', DateTimePeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=SystemStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))