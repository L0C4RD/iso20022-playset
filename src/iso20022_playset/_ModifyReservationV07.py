# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrentOrDefaultReservation4Choice
from . import MessageHeader1
from . import Reservation4
from . import SupplementaryData1

class ModifyReservationV07(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_NewRsvatnValSet", "_RsvatnId", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def NewRsvatnValSet(self):
		return self._NewRsvatnValSet

	@NewRsvatnValSet.setter
	def NewRsvatnValSet(self, value):
		self._NewRsvatnValSet = value if value is not None else base_types.UninitialisedField(self, 'NewRsvatnValSet', Reservation4, False)

	@NewRsvatnValSet.deleter
	def NewRsvatnValSet(self):
		del self._NewRsvatnValSet
		self._NewRsvatnValSet = base_types.UninitialisedField(self, 'NewRsvatnValSet', Reservation4, False)

	@property
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if value is not None else base_types.UninitialisedField(self, 'RsvatnId', CurrentOrDefaultReservation4Choice, False)

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = base_types.UninitialisedField(self, 'RsvatnId', CurrentOrDefaultReservation4Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewRsvatnValSet', type=Reservation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnId', type=CurrentOrDefaultReservation4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))