import base_types
import MessageHeader1
import SupplementaryData1
import BusinessInformationQueryDefinition3

class GetGeneralBusinessInformationV04(base_types._BaseFieldType):

	__slots__ = ["_GnlBizInfQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def GnlBizInfQryDef(self):
		return self._GnlBizInfQryDef

	@GnlBizInfQryDef.setter
	def GnlBizInfQryDef(self, value):
		self._GnlBizInfQryDef = value if type(value) != auto else self.make_default("GnlBizInfQryDef")

	@GnlBizInfQryDef.deleter
	def GnlBizInfQryDef(self):
		del self._GnlBizInfQryDef
		self._GnlBizInfQryDef = None

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
		base_types.FieldEntry(name='GnlBizInfQryDef', type=BusinessInformationQueryDefinition3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

