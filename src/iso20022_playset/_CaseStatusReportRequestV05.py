# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import ReportHeader7
from . import SupplementaryData1

class CaseStatusReportRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Case", "_ReqHdr", "_SplmtryData"]
	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if value is not None else base_types.UninitialisedField(self, 'Case', Case6, False)

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = base_types.UninitialisedField(self, 'Case', Case6, False)

	@property
	def ReqHdr(self):
		return self._ReqHdr

	@ReqHdr.setter
	def ReqHdr(self, value):
		self._ReqHdr = value if value is not None else base_types.UninitialisedField(self, 'ReqHdr', ReportHeader7, False)

	@ReqHdr.deleter
	def ReqHdr(self):
		del self._ReqHdr
		self._ReqHdr = base_types.UninitialisedField(self, 'ReqHdr', ReportHeader7, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqHdr', type=ReportHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))