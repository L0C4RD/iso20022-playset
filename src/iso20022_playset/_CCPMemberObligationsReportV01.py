# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementAccount1 import SettlementAccount1
from ._SupplementaryData1 import SupplementaryData1

class CCPMemberObligationsReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_SttlmAcct"]
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
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if type(value) != base_types.auto else self.make_default("SttlmAcct")

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAcct', type=SettlementAccount1, min=1, max=None, mutex_group=None, array=True),
	))