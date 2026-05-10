from . import base_types
import Receipt7
import SupplementaryData1
import MessageHeader9

class ReceiptV09(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgHdr", "_RctDtls"]
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
	def RctDtls(self):
		return self._RctDtls

	@RctDtls.setter
	def RctDtls(self, value):
		self._RctDtls = value if type(value) != auto else self.make_default("RctDtls")

	@RctDtls.deleter
	def RctDtls(self):
		del self._RctDtls
		self._RctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDtls', type=Receipt7, min=1, max=None, mutex_group=None, array=True),
	))

