import base_types
import StatusAdviceReport3
import SupplementaryData1
import StatusReportRecord3
import Max140Text

class MessageReportHeader4(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgRptIdr", "_MsgSts", "_RcrdSts"]
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
	def MsgRptIdr(self):
		return self._MsgRptIdr

	@MsgRptIdr.setter
	def MsgRptIdr(self, value):
		self._MsgRptIdr = value if type(value) != auto else self.make_default("MsgRptIdr")

	@MsgRptIdr.deleter
	def MsgRptIdr(self):
		del self._MsgRptIdr
		self._MsgRptIdr = None

	@property
	def MsgSts(self):
		return self._MsgSts

	@MsgSts.setter
	def MsgSts(self, value):
		self._MsgSts = value if type(value) != auto else self.make_default("MsgSts")

	@MsgSts.deleter
	def MsgSts(self):
		del self._MsgSts
		self._MsgSts = None

	@property
	def RcrdSts(self):
		return self._RcrdSts

	@RcrdSts.setter
	def RcrdSts(self, value):
		self._RcrdSts = value if type(value) != auto else self.make_default("RcrdSts")

	@RcrdSts.deleter
	def RcrdSts(self):
		del self._RcrdSts
		self._RcrdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgRptIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSts', type=StatusAdviceReport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdSts', type=StatusReportRecord3, min=0, max=None, mutex_group=None, array=True),
	))

