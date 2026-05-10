import base_types
import ATMCommandIdentification1
import ATMEnvironment9
import MessageFunction8Code

class HostToATMRequest1(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_XpctdMsgFctn", "_CmdId"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def XpctdMsgFctn(self):
		return self._XpctdMsgFctn

	@XpctdMsgFctn.setter
	def XpctdMsgFctn(self, value):
		self._XpctdMsgFctn = value if type(value) != auto else self.make_default("XpctdMsgFctn")

	@XpctdMsgFctn.deleter
	def XpctdMsgFctn(self):
		del self._XpctdMsgFctn
		self._XpctdMsgFctn = None

	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if type(value) != auto else self.make_default("CmdId")

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=ATMEnvironment9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdMsgFctn', type=MessageFunction8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

