# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod1
from . import NotReported1Code

class DateOrBlankQuery2Choice(base_types._BaseFieldType):

	__slots__ = ["_NotRptd", "_Rg"]
	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if value is not None else base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@property
	def Rg(self):
		return self._Rg

	@Rg.setter
	def Rg(self, value):
		self._Rg = value if value is not None else base_types.UninitialisedField(self, 'Rg', DatePeriod1, False)

	@Rg.deleter
	def Rg(self):
		del self._Rg
		self._Rg = base_types.UninitialisedField(self, 'Rg', DatePeriod1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rg', type=DatePeriod1, min=0, max=1, mutex_group=1, array=False),
	))