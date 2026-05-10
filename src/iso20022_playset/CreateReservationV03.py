from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .Reservation4 import Reservation4
from .MessageHeader1 import MessageHeader1
from .ReservationIdentification4 import ReservationIdentification4

class CreateReservationV03(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_RsvatnId", "_ValSet", "_SplmtryData"]
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
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if type(value) != auto else self.make_default("RsvatnId")

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = None

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
		base_types.FieldEntry(name='RsvatnId', type=ReservationIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSet', type=Reservation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

