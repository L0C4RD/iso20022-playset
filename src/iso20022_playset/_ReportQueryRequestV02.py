from . import base_types
from ._ReportQueryCriteria3 import ReportQueryCriteria3
from ._SupplementaryData1 import SupplementaryData1
from ._MessageHeader7 import MessageHeader7

class ReportQueryRequestV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RptQryCrit", "_MsgHdr"]
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
	def RptQryCrit(self):
		return self._RptQryCrit

	@RptQryCrit.setter
	def RptQryCrit(self, value):
		self._RptQryCrit = value if type(value) != base_types.auto else self.make_default("RptQryCrit")

	@RptQryCrit.deleter
	def RptQryCrit(self):
		del self._RptQryCrit
		self._RptQryCrit = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptQryCrit', type=ReportQueryCriteria3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader7, min=1, max=1, mutex_group=None, array=False),
	))

