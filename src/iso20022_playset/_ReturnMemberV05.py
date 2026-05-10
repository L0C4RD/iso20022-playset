from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._MessageHeader7 import MessageHeader7
from ._MemberReportOrError7Choice import MemberReportOrError7Choice

class ReturnMemberV05(base_types._BaseFieldType):

	__slots__ = ["_RptOrErr", "_MsgHdr", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != base_types.auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def RptOrErr(self):
		return self._RptOrErr

	@RptOrErr.setter
	def RptOrErr(self, value):
		self._RptOrErr = value if type(value) != base_types.auto else self.make_default("RptOrErr")

	@RptOrErr.deleter
	def RptOrErr(self):
		del self._RptOrErr
		self._RptOrErr = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptOrErr', type=MemberReportOrError7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

