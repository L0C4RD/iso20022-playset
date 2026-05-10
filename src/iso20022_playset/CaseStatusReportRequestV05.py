import base_types
import SupplementaryData1
import Case6
import ReportHeader7

class CaseStatusReportRequestV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_ReqHdr", "_Case"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def ReqHdr(self):
		return self._ReqHdr

	@ReqHdr.setter
	def ReqHdr(self, value):
		self._ReqHdr = value if type(value) != auto else self.make_default("ReqHdr")

	@ReqHdr.deleter
	def ReqHdr(self):
		del self._ReqHdr
		self._ReqHdr = None

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqHdr', type=ReportHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=1, max=1, mutex_group=None, array=False),
	))

