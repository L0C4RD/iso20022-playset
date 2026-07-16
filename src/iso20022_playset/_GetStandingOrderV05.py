# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader4
from . import StandingOrderQuery5
from . import SupplementaryData1

class GetStandingOrderV05(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_StgOrdrQryDef"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader4, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader4, False)

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
	def StgOrdrQryDef(self):
		return self._StgOrdrQryDef

	@StgOrdrQryDef.setter
	def StgOrdrQryDef(self, value):
		self._StgOrdrQryDef = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrQryDef', StandingOrderQuery5, False)

	@StgOrdrQryDef.deleter
	def StgOrdrQryDef(self):
		del self._StgOrdrQryDef
		self._StgOrdrQryDef = base_types.UninitialisedField(self, 'StgOrdrQryDef', StandingOrderQuery5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgOrdrQryDef', type=StandingOrderQuery5, min=0, max=1, mutex_group=None, array=False),
	))