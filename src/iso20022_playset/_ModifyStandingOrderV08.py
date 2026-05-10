from . import base_types
from ._StandingOrderIdentification8 import StandingOrderIdentification8
from ._SupplementaryData1 import SupplementaryData1
from ._MessageHeader1 import MessageHeader1
from ._StandingOrder10 import StandingOrder10

class ModifyStandingOrderV08(base_types._BaseFieldType):

	__slots__ = ["_StgOrdrId", "_MsgHdr", "_SplmtryData", "_NewStgOrdrValSet"]
	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if type(value) != base_types.auto else self.make_default("StgOrdrId")

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = None

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

	@property
	def NewStgOrdrValSet(self):
		return self._NewStgOrdrValSet

	@NewStgOrdrValSet.setter
	def NewStgOrdrValSet(self, value):
		self._NewStgOrdrValSet = value if type(value) != base_types.auto else self.make_default("NewStgOrdrValSet")

	@NewStgOrdrValSet.deleter
	def NewStgOrdrValSet(self):
		del self._NewStgOrdrValSet
		self._NewStgOrdrValSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgOrdrId', type=StandingOrderIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewStgOrdrValSet', type=StandingOrder10, min=1, max=1, mutex_group=None, array=False),
	))

