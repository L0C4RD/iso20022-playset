from . import base_types
from .MessageHeader10 import MessageHeader10
from .SupplementaryData1 import SupplementaryData1
from .ReceiptAcknowledgementReport2 import ReceiptAcknowledgementReport2

class ReceiptAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_SplmtryData", "_Rpt"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

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
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageHeader10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rpt', type=ReceiptAcknowledgementReport2, min=1, max=None, mutex_group=None, array=True),
	))

