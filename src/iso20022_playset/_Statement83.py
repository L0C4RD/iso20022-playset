# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndPeriod3Choice
from . import Frequency25Choice
from . import StatementBasis7Choice
from . import StatementType5Choice
from . import UpdateType15Choice

class Statement83(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_StmtBsis", "_StmtDtOrPrd", "_StmtTp", "_UpdTp"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency25Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency25Choice, False)

	@property
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if value is not None else base_types.UninitialisedField(self, 'StmtBsis', StatementBasis7Choice, False)

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = base_types.UninitialisedField(self, 'StmtBsis', StatementBasis7Choice, False)

	@property
	def StmtDtOrPrd(self):
		return self._StmtDtOrPrd

	@StmtDtOrPrd.setter
	def StmtDtOrPrd(self, value):
		self._StmtDtOrPrd = value if value is not None else base_types.UninitialisedField(self, 'StmtDtOrPrd', DateAndPeriod3Choice, False)

	@StmtDtOrPrd.deleter
	def StmtDtOrPrd(self):
		del self._StmtDtOrPrd
		self._StmtDtOrPrd = base_types.UninitialisedField(self, 'StmtDtOrPrd', DateAndPeriod3Choice, False)

	@property
	def StmtTp(self):
		return self._StmtTp

	@StmtTp.setter
	def StmtTp(self, value):
		self._StmtTp = value if value is not None else base_types.UninitialisedField(self, 'StmtTp', StatementType5Choice, False)

	@StmtTp.deleter
	def StmtTp(self):
		del self._StmtTp
		self._StmtTp = base_types.UninitialisedField(self, 'StmtTp', StatementType5Choice, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType15Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtOrPrd', type=DateAndPeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=StatementType5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
	))