from . import base_types
import DateFormat3Choice
import DateMode1Code

class DateFormat1(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtMd"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def DtMd(self):
		return self._DtMd

	@DtMd.setter
	def DtMd(self, value):
		self._DtMd = value if type(value) != auto else self.make_default("DtMd")

	@DtMd.deleter
	def DtMd(self):
		del self._DtMd
		self._DtMd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateFormat3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtMd', type=DateMode1Code, min=0, max=1, mutex_group=None, array=False),
	))

