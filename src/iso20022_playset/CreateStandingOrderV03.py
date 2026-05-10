import base_types
import StandingOrder10
import SupplementaryData1
import MessageHeader1
import StandingOrderIdentification8

class CreateStandingOrderV03(base_types._BaseFieldType):

	__slots__ = ["_ValSet", "_MsgHdr", "_StgOrdrId", "_SplmtryData"]
	@property
	def ValSet(self):
		return self._ValSet

	@ValSet.setter
	def ValSet(self, value):
		self._ValSet = value if type(value) != auto else self.make_default("ValSet")

	@ValSet.deleter
	def ValSet(self):
		del self._ValSet
		self._ValSet = None

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if type(value) != auto else self.make_default("StgOrdrId")

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValSet', type=StandingOrder10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrId', type=StandingOrderIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

