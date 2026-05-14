from . import base_types
from ._BillingReportOrError6Choice import BillingReportOrError6Choice
from ._MessageHeader11 import MessageHeader11
from ._SupplementaryData1 import SupplementaryData1

class BillingReportV01(base_types._BaseFieldType):

	__slots__ = ["_BllgRptOrErr", "_MsgHdr", "_SplmtryData"]
	@property
	def BllgRptOrErr(self):
		return self._BllgRptOrErr

	@BllgRptOrErr.setter
	def BllgRptOrErr(self, value):
		self._BllgRptOrErr = value if type(value) != base_types.auto else self.make_default("BllgRptOrErr")

	@BllgRptOrErr.deleter
	def BllgRptOrErr(self):
		del self._BllgRptOrErr
		self._BllgRptOrErr = None

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
		base_types.FieldEntry(name='BllgRptOrErr', type=BillingReportOrError6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

