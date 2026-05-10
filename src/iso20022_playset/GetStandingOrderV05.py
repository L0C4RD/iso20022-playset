import base_types
import SupplementaryData1
import StandingOrderQuery5
import MessageHeader4

class GetStandingOrderV05(base_types._BaseFieldType):

	__slots__ = ["_StgOrdrQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def StgOrdrQryDef(self):
		return self._StgOrdrQryDef

	@StgOrdrQryDef.setter
	def StgOrdrQryDef(self, value):
		self._StgOrdrQryDef = value if type(value) != auto else self.make_default("StgOrdrQryDef")

	@StgOrdrQryDef.deleter
	def StgOrdrQryDef(self):
		del self._StgOrdrQryDef
		self._StgOrdrQryDef = None

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
		base_types.FieldEntry(name='StgOrdrQryDef', type=StandingOrderQuery5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

