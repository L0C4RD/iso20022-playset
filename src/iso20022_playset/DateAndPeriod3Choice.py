from . import base_types
from .Period7Choice import Period7Choice
from .DateAndDateTime2Choice import DateAndDateTime2Choice

class DateAndPeriod3Choice(base_types._BaseFieldType):

	__slots__ = ["_StmtDt", "_StmtPrd"]
	@property
	def StmtDt(self):
		return self._StmtDt

	@StmtDt.setter
	def StmtDt(self, value):
		self._StmtDt = value if type(value) != base_types.auto else self.make_default("StmtDt")

	@StmtDt.deleter
	def StmtDt(self):
		del self._StmtDt
		self._StmtDt = None

	@property
	def StmtPrd(self):
		return self._StmtPrd

	@StmtPrd.setter
	def StmtPrd(self, value):
		self._StmtPrd = value if type(value) != base_types.auto else self.make_default("StmtPrd")

	@StmtPrd.deleter
	def StmtPrd(self):
		del self._StmtPrd
		self._StmtPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtPrd', type=Period7Choice, min=0, max=1, mutex_group=1, array=False),
	))

