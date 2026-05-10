from . import base_types
from ._StatementType5Choice import StatementType5Choice
from ._Frequency25Choice import Frequency25Choice
from ._UpdateType15Choice import UpdateType15Choice
from ._StatementBasis7Choice import StatementBasis7Choice
from ._DateAndPeriod3Choice import DateAndPeriod3Choice

class Statement83(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_UpdTp", "_StmtTp", "_StmtDtOrPrd", "_StmtBsis"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if type(value) != base_types.auto else self.make_default("StmtBsis")

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = None

	@property
	def StmtDtOrPrd(self):
		return self._StmtDtOrPrd

	@StmtDtOrPrd.setter
	def StmtDtOrPrd(self, value):
		self._StmtDtOrPrd = value if type(value) != base_types.auto else self.make_default("StmtDtOrPrd")

	@StmtDtOrPrd.deleter
	def StmtDtOrPrd(self):
		del self._StmtDtOrPrd
		self._StmtDtOrPrd = None

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

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtOrPrd', type=DateAndPeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=StatementType5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
	))

