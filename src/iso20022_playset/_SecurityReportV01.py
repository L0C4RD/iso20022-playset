from . import base_types
from ._MessageHeader12 import MessageHeader12
from ._Pagination1 import Pagination1
from ._SecurityOrOperationalError4Choice import SecurityOrOperationalError4Choice
from ._SupplementaryData1 import SupplementaryData1

class SecurityReportV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_Pgntn", "_SctyRptOrErr", "_SplmtryData"]
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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def SctyRptOrErr(self):
		return self._SctyRptOrErr

	@SctyRptOrErr.setter
	def SctyRptOrErr(self, value):
		self._SctyRptOrErr = value if type(value) != base_types.auto else self.make_default("SctyRptOrErr")

	@SctyRptOrErr.deleter
	def SctyRptOrErr(self):
		del self._SctyRptOrErr
		self._SctyRptOrErr = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyRptOrErr', type=SecurityOrOperationalError4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

