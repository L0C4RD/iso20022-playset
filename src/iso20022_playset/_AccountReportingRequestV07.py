from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._ReportingRequest7 import ReportingRequest7
from ._GroupHeader117 import GroupHeader117

class AccountReportingRequestV07(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RptgReq", "_GrpHdr"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def RptgReq(self):
		return self._RptgReq

	@RptgReq.setter
	def RptgReq(self, value):
		self._RptgReq = value if type(value) != base_types.auto else self.make_default("RptgReq")

	@RptgReq.deleter
	def RptgReq(self):
		del self._RptgReq
		self._RptgReq = None

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgReq', type=ReportingRequest7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

