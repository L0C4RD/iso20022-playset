# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDayQuery2
from . import MessageHeader9
from . import SupplementaryData1

class GetBusinessDayInformationV05(base_types._BaseFieldType):

	__slots__ = ["_BizDayInfQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def BizDayInfQryDef(self):
		return self._BizDayInfQryDef

	@BizDayInfQryDef.setter
	def BizDayInfQryDef(self, value):
		self._BizDayInfQryDef = value if value is not None else base_types.UninitialisedField(self, 'BizDayInfQryDef', BusinessDayQuery2, False)

	@BizDayInfQryDef.deleter
	def BizDayInfQryDef(self):
		del self._BizDayInfQryDef
		self._BizDayInfQryDef = base_types.UninitialisedField(self, 'BizDayInfQryDef', BusinessDayQuery2, False)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

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
		base_types.FieldEntry(name='BizDayInfQryDef', type=BusinessDayQuery2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))