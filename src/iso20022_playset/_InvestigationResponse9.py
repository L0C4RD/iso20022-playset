# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationData6
from . import InvestigationStatus2
from . import Max35Text
from . import Party40Choice

class InvestigationResponse9(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnData", "_InvstgtnSts", "_MsgId", "_NxtRspndr", "_RspndrInvstgtnId"]
	@property
	def InvstgtnData(self):
		return self._InvstgtnData

	@InvstgtnData.setter
	def InvstgtnData(self, value):
		self._InvstgtnData = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnData', InvestigationData6, True)

	@InvstgtnData.deleter
	def InvstgtnData(self):
		del self._InvstgtnData
		self._InvstgtnData = base_types.UninitialisedField(self, 'InvstgtnData', InvestigationData6, True)

	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnSts', InvestigationStatus2, False)

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = base_types.UninitialisedField(self, 'InvstgtnSts', InvestigationStatus2, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def NxtRspndr(self):
		return self._NxtRspndr

	@NxtRspndr.setter
	def NxtRspndr(self, value):
		self._NxtRspndr = value if value is not None else base_types.UninitialisedField(self, 'NxtRspndr', Party40Choice, False)

	@NxtRspndr.deleter
	def NxtRspndr(self):
		del self._NxtRspndr
		self._NxtRspndr = base_types.UninitialisedField(self, 'NxtRspndr', Party40Choice, False)

	@property
	def RspndrInvstgtnId(self):
		return self._RspndrInvstgtnId

	@RspndrInvstgtnId.setter
	def RspndrInvstgtnId(self, value):
		self._RspndrInvstgtnId = value if value is not None else base_types.UninitialisedField(self, 'RspndrInvstgtnId', Max35Text, False)

	@RspndrInvstgtnId.deleter
	def RspndrInvstgtnId(self):
		del self._RspndrInvstgtnId
		self._RspndrInvstgtnId = base_types.UninitialisedField(self, 'RspndrInvstgtnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstgtnData', type=InvestigationData6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstgtnSts', type=InvestigationStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtRspndr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndrInvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))