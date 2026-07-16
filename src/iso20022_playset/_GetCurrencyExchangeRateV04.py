# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyQueryDefinition3
from . import MessageHeader1
from . import SupplementaryData1

class GetCurrencyExchangeRateV04(base_types._BaseFieldType):

	__slots__ = ["_CcyQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def CcyQryDef(self):
		return self._CcyQryDef

	@CcyQryDef.setter
	def CcyQryDef(self, value):
		self._CcyQryDef = value if value is not None else base_types.UninitialisedField(self, 'CcyQryDef', CurrencyQueryDefinition3, False)

	@CcyQryDef.deleter
	def CcyQryDef(self):
		del self._CcyQryDef
		self._CcyQryDef = base_types.UninitialisedField(self, 'CcyQryDef', CurrencyQueryDefinition3, False)

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
		base_types.FieldEntry(name='CcyQryDef', type=CurrencyQueryDefinition3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))