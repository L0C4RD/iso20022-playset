# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessInformationQueryDefinition3
from . import MessageHeader1
from . import SupplementaryData1

class GetGeneralBusinessInformationV04(base_types._BaseFieldType):

	__slots__ = ["_GnlBizInfQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def GnlBizInfQryDef(self):
		return self._GnlBizInfQryDef

	@GnlBizInfQryDef.setter
	def GnlBizInfQryDef(self, value):
		self._GnlBizInfQryDef = value if value is not None else base_types.UninitialisedField(self, 'GnlBizInfQryDef', BusinessInformationQueryDefinition3, False)

	@GnlBizInfQryDef.deleter
	def GnlBizInfQryDef(self):
		del self._GnlBizInfQryDef
		self._GnlBizInfQryDef = base_types.UninitialisedField(self, 'GnlBizInfQryDef', BusinessInformationQueryDefinition3, False)

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
		base_types.FieldEntry(name='GnlBizInfQryDef', type=BusinessInformationQueryDefinition3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))