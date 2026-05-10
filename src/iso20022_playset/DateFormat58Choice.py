from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .DateType1Code import DateType1Code

class DateFormat58Choice(base_types._BaseFieldType):

	__slots__ = ["_DtCd", "_DtOrDtTm"]
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

	@property
	def DtOrDtTm(self):
		return self._DtOrDtTm

	@DtOrDtTm.setter
	def DtOrDtTm(self, value):
		self._DtOrDtTm = value if type(value) != base_types.auto else self.make_default("DtOrDtTm")

	@DtOrDtTm.deleter
	def DtOrDtTm(self):
		del self._DtOrDtTm
		self._DtOrDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtCd', type=DateType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtOrDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
	))

