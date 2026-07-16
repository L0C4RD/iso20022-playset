# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Period7Choice

class DateAndPeriod3Choice(base_types._BaseFieldType):

	__slots__ = ["_StmtDt", "_StmtPrd"]
	@property
	def StmtDt(self):
		return self._StmtDt

	@StmtDt.setter
	def StmtDt(self, value):
		self._StmtDt = value if value is not None else base_types.UninitialisedField(self, 'StmtDt', DateAndDateTime2Choice, False)

	@StmtDt.deleter
	def StmtDt(self):
		del self._StmtDt
		self._StmtDt = base_types.UninitialisedField(self, 'StmtDt', DateAndDateTime2Choice, False)

	@property
	def StmtPrd(self):
		return self._StmtPrd

	@StmtPrd.setter
	def StmtPrd(self, value):
		self._StmtPrd = value if value is not None else base_types.UninitialisedField(self, 'StmtPrd', Period7Choice, False)

	@StmtPrd.deleter
	def StmtPrd(self):
		del self._StmtPrd
		self._StmtPrd = base_types.UninitialisedField(self, 'StmtPrd', Period7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtPrd', type=Period7Choice, min=0, max=1, mutex_group=1, array=False),
	))