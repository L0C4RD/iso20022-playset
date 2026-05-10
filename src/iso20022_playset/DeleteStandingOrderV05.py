import base_types
import SupplementaryData1
import StandingOrderOrAll4Choice
import MessageHeader1

class DeleteStandingOrderV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgHdr", "_StgOrdrDtls"]
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
	def StgOrdrDtls(self):
		return self._StgOrdrDtls

	@StgOrdrDtls.setter
	def StgOrdrDtls(self, value):
		self._StgOrdrDtls = value if type(value) != auto else self.make_default("StgOrdrDtls")

	@StgOrdrDtls.deleter
	def StgOrdrDtls(self):
		del self._StgOrdrDtls
		self._StgOrdrDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrDtls', type=StandingOrderOrAll4Choice, min=1, max=1, mutex_group=None, array=False),
	))

