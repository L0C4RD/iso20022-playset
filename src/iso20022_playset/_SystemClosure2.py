# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosureReason2Choice
from . import DateTimePeriod1Choice

class SystemClosure2(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_Rsn"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DateTimePeriod1Choice, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DateTimePeriod1Choice, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', ClosureReason2Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', ClosureReason2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ClosureReason2Choice, min=1, max=1, mutex_group=None, array=False),
	))