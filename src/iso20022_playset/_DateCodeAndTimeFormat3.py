from . import base_types
from ._DateCode21Choice import DateCode21Choice
from ._ISOTime import ISOTime

class DateCodeAndTimeFormat3(base_types._BaseFieldType):

	__slots__ = ["_Tm", "_DtCd"]
	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if type(value) != base_types.auto else self.make_default("DtCd")

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtCd', type=DateCode21Choice, min=1, max=1, mutex_group=None, array=False),
	))

