# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClearedProduct3 import ClearedProduct3
from ._SupplementaryData1 import SupplementaryData1

class CCPClearedProductReportV03(base_types._BaseFieldType):

	__slots__ = ["_ClrdPdct", "_SplmtryData"]
	@property
	def ClrdPdct(self):
		return self._ClrdPdct

	@ClrdPdct.setter
	def ClrdPdct(self, value):
		self._ClrdPdct = value if type(value) != base_types.auto else self.make_default("ClrdPdct")

	@ClrdPdct.deleter
	def ClrdPdct(self):
		del self._ClrdPdct
		self._ClrdPdct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrdPdct', type=ClearedProduct3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))