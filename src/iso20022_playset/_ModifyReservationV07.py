from . import base_types
from ._CurrentOrDefaultReservation4Choice import CurrentOrDefaultReservation4Choice
from ._MessageHeader1 import MessageHeader1
from ._Reservation4 import Reservation4
from ._SupplementaryData1 import SupplementaryData1

class ModifyReservationV07(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_NewRsvatnValSet", "_RsvatnId", "_SplmtryData"]
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
	def NewRsvatnValSet(self):
		return self._NewRsvatnValSet

	@NewRsvatnValSet.setter
	def NewRsvatnValSet(self, value):
		self._NewRsvatnValSet = value if type(value) != base_types.auto else self.make_default("NewRsvatnValSet")

	@NewRsvatnValSet.deleter
	def NewRsvatnValSet(self):
		del self._NewRsvatnValSet
		self._NewRsvatnValSet = None

	@property
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if type(value) != base_types.auto else self.make_default("RsvatnId")

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewRsvatnValSet', type=Reservation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnId', type=CurrentOrDefaultReservation4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

