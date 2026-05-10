import base_types
import DateCode26Choice
import ISOTime

class DateCodeAndTimeFormat4(base_types._BaseFieldType):

	__slots__ = ["_DtCd", "_Tm"]
	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if type(value) != auto else self.make_default("DtCd")

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtCd', type=DateCode26Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
	))

