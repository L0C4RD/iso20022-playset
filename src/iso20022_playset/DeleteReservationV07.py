import base_types
import SupplementaryData1
import ReservationIdentification4
import MessageHeader1

class DeleteReservationV07(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_CurRsvatn", "_SplmtryData"]
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
	def CurRsvatn(self):
		return self._CurRsvatn

	@CurRsvatn.setter
	def CurRsvatn(self, value):
		self._CurRsvatn = value if type(value) != auto else self.make_default("CurRsvatn")

	@CurRsvatn.deleter
	def CurRsvatn(self):
		del self._CurRsvatn
		self._CurRsvatn = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurRsvatn', type=ReservationIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

