# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValueCriteriaDefinition4Choice
from . import MessageHeader3
from . import SupplementaryData1

class CollateralValueQueryV02(base_types._BaseFieldType):

	__slots__ = ["_CollValQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def CollValQryDef(self):
		return self._CollValQryDef

	@CollValQryDef.setter
	def CollValQryDef(self, value):
		self._CollValQryDef = value if value is not None else base_types.UninitialisedField(self, 'CollValQryDef', CollateralValueCriteriaDefinition4Choice, False)

	@CollValQryDef.deleter
	def CollValQryDef(self):
		del self._CollValQryDef
		self._CollValQryDef = base_types.UninitialisedField(self, 'CollValQryDef', CollateralValueCriteriaDefinition4Choice, False)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader3, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader3, False)

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
		base_types.FieldEntry(name='CollValQryDef', type=CollateralValueCriteriaDefinition4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))