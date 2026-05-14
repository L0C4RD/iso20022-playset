# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PositionSearchCriteria4 import PositionSearchCriteria4
from ._Statement89 import Statement89
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesAccountPositionQueryV01(base_types._BaseFieldType):

	__slots__ = ["_SchCrit", "_SplmtryData", "_Stmt"]
	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != base_types.auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if type(value) != base_types.auto else self.make_default("Stmt")

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchCrit', type=PositionSearchCriteria4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Stmt', type=Statement89, min=1, max=1, mutex_group=None, array=False),
	))