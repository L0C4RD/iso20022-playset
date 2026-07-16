# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSearchCriteria4
from . import Statement89
from . import SupplementaryData1

class SecuritiesAccountPositionQueryV01(base_types._BaseFieldType):

	__slots__ = ["_SchCrit", "_SplmtryData", "_Stmt"]
	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', PositionSearchCriteria4, False)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', PositionSearchCriteria4, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if value is not None else base_types.UninitialisedField(self, 'Stmt', Statement89, False)

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = base_types.UninitialisedField(self, 'Stmt', Statement89, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchCrit', type=PositionSearchCriteria4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Stmt', type=Statement89, min=1, max=1, mutex_group=None, array=False),
	))