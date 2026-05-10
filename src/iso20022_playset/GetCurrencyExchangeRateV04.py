from . import base_types
import MessageHeader1
import SupplementaryData1
import CurrencyQueryDefinition3

class GetCurrencyExchangeRateV04(base_types._BaseFieldType):

	__slots__ = ["_CcyQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def CcyQryDef(self):
		return self._CcyQryDef

	@CcyQryDef.setter
	def CcyQryDef(self, value):
		self._CcyQryDef = value if type(value) != auto else self.make_default("CcyQryDef")

	@CcyQryDef.deleter
	def CcyQryDef(self):
		del self._CcyQryDef
		self._CcyQryDef = None

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
		base_types.FieldEntry(name='CcyQryDef', type=CurrencyQueryDefinition3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

