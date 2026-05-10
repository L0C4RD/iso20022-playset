from . import base_types
import DatePeriod1
import NotReported1Code

class DateOrBlankQuery2Choice(base_types._BaseFieldType):

	__slots__ = ["_NotRptd", "_Rg"]
	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

	@property
	def Rg(self):
		return self._Rg

	@Rg.setter
	def Rg(self, value):
		self._Rg = value if type(value) != auto else self.make_default("Rg")

	@Rg.deleter
	def Rg(self):
		del self._Rg
		self._Rg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rg', type=DatePeriod1, min=0, max=1, mutex_group=1, array=False),
	))

