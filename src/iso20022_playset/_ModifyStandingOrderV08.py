# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader1
from . import StandingOrder10
from . import StandingOrderIdentification8
from . import SupplementaryData1

class ModifyStandingOrderV08(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_NewStgOrdrValSet", "_SplmtryData", "_StgOrdrId"]
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
	def NewStgOrdrValSet(self):
		return self._NewStgOrdrValSet

	@NewStgOrdrValSet.setter
	def NewStgOrdrValSet(self, value):
		self._NewStgOrdrValSet = value if value is not None else base_types.UninitialisedField(self, 'NewStgOrdrValSet', StandingOrder10, False)

	@NewStgOrdrValSet.deleter
	def NewStgOrdrValSet(self):
		del self._NewStgOrdrValSet
		self._NewStgOrdrValSet = base_types.UninitialisedField(self, 'NewStgOrdrValSet', StandingOrder10, False)

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

	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrId', StandingOrderIdentification8, False)

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = base_types.UninitialisedField(self, 'StgOrdrId', StandingOrderIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewStgOrdrValSet', type=StandingOrder10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgOrdrId', type=StandingOrderIdentification8, min=1, max=1, mutex_group=None, array=False),
	))