from . import base_types
from ._ISODate import ISODate
from ._Number import Number

class OptionDateOrPeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_NtcePrd", "_EarlstExrcDt"]
	@property
	def EarlstExrcDt(self):
		return self._EarlstExrcDt

	@EarlstExrcDt.setter
	def EarlstExrcDt(self, value):
		self._EarlstExrcDt = value if type(value) != base_types.auto else self.make_default("EarlstExrcDt")

	@EarlstExrcDt.deleter
	def EarlstExrcDt(self):
		del self._EarlstExrcDt
		self._EarlstExrcDt = None

	@property
	def NtcePrd(self):
		return self._NtcePrd

	@NtcePrd.setter
	def NtcePrd(self, value):
		self._NtcePrd = value if type(value) != base_types.auto else self.make_default("NtcePrd")

	@NtcePrd.deleter
	def NtcePrd(self):
		del self._NtcePrd
		self._NtcePrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstExrcDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtcePrd', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

