from . import base_types
from ._DateAndPeriod3Choice import DateAndPeriod3Choice
from ._StatementType7Choice import StatementType7Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class Statement89(base_types._BaseFieldType):

	__slots__ = ["_DtOrPrd", "_HstrcData", "_StmtTp"]
	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if type(value) != base_types.auto else self.make_default("DtOrPrd")

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = None

	@property
	def HstrcData(self):
		return self._HstrcData

	@HstrcData.setter
	def HstrcData(self, value):
		self._HstrcData = value if type(value) != base_types.auto else self.make_default("HstrcData")

	@HstrcData.deleter
	def HstrcData(self):
		del self._HstrcData
		self._HstrcData = None

	@property
	def StmtTp(self):
		return self._StmtTp

	@StmtTp.setter
	def StmtTp(self, value):
		self._StmtTp = value if type(value) != base_types.auto else self.make_default("StmtTp")

	@StmtTp.deleter
	def StmtTp(self):
		del self._StmtTp
		self._StmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOrPrd', type=DateAndPeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstrcData', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=StatementType7Choice, min=0, max=1, mutex_group=None, array=False),
	))

