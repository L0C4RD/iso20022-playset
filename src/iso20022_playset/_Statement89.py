# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndPeriod3Choice
from . import StatementType7Choice
from . import TrueFalseIndicator

class Statement89(base_types._BaseFieldType):

	__slots__ = ["_DtOrPrd", "_HstrcData", "_StmtTp"]
	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if value is not None else base_types.UninitialisedField(self, 'DtOrPrd', DateAndPeriod3Choice, False)

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = base_types.UninitialisedField(self, 'DtOrPrd', DateAndPeriod3Choice, False)

	@property
	def HstrcData(self):
		return self._HstrcData

	@HstrcData.setter
	def HstrcData(self, value):
		self._HstrcData = value if value is not None else base_types.UninitialisedField(self, 'HstrcData', TrueFalseIndicator, False)

	@HstrcData.deleter
	def HstrcData(self):
		del self._HstrcData
		self._HstrcData = base_types.UninitialisedField(self, 'HstrcData', TrueFalseIndicator, False)

	@property
	def StmtTp(self):
		return self._StmtTp

	@StmtTp.setter
	def StmtTp(self, value):
		self._StmtTp = value if value is not None else base_types.UninitialisedField(self, 'StmtTp', StatementType7Choice, False)

	@StmtTp.deleter
	def StmtTp(self):
		del self._StmtTp
		self._StmtTp = base_types.UninitialisedField(self, 'StmtTp', StatementType7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOrPrd', type=DateAndPeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstrcData', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=StatementType7Choice, min=0, max=1, mutex_group=None, array=False),
	))