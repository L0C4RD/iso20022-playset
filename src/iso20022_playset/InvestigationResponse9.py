import base_types
import Max35Text
import Party40Choice
import InvestigationStatus2
import InvestigationData6

class InvestigationResponse9(base_types._BaseFieldType):

	__slots__ = ["_RspndrInvstgtnId", "_NxtRspndr", "_InvstgtnSts", "_InvstgtnData", "_MsgId"]
	@property
	def RspndrInvstgtnId(self):
		return self._RspndrInvstgtnId

	@RspndrInvstgtnId.setter
	def RspndrInvstgtnId(self, value):
		self._RspndrInvstgtnId = value if type(value) != auto else self.make_default("RspndrInvstgtnId")

	@RspndrInvstgtnId.deleter
	def RspndrInvstgtnId(self):
		del self._RspndrInvstgtnId
		self._RspndrInvstgtnId = None

	@property
	def NxtRspndr(self):
		return self._NxtRspndr

	@NxtRspndr.setter
	def NxtRspndr(self, value):
		self._NxtRspndr = value if type(value) != auto else self.make_default("NxtRspndr")

	@NxtRspndr.deleter
	def NxtRspndr(self):
		del self._NxtRspndr
		self._NxtRspndr = None

	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if type(value) != auto else self.make_default("InvstgtnSts")

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = None

	@property
	def InvstgtnData(self):
		return self._InvstgtnData

	@InvstgtnData.setter
	def InvstgtnData(self, value):
		self._InvstgtnData = value if type(value) != auto else self.make_default("InvstgtnData")

	@InvstgtnData.deleter
	def InvstgtnData(self):
		del self._InvstgtnData
		self._InvstgtnData = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspndrInvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtRspndr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnSts', type=InvestigationStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnData', type=InvestigationData6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

