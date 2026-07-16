# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod5

class AdjustmentRequest1(base_types._BaseFieldType):

	__slots__ = ["_Prd"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DatePeriod5, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DatePeriod5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=DatePeriod5, min=0, max=1, mutex_group=None, array=False),
	))