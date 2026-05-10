from . import base_types
from ._ATMStatus1Code import ATMStatus1Code
from ._MessageFunction8Code import MessageFunction8Code
from ._ATMConfigurationParameter1 import ATMConfigurationParameter1

class ATMCommandParameters1Choice(base_types._BaseFieldType):

	__slots__ = ["_ATMReqrdGblSts", "_XpctdMsgFctn", "_ReqrdCfgtnParam"]
	@property
	def ATMReqrdGblSts(self):
		return self._ATMReqrdGblSts

	@ATMReqrdGblSts.setter
	def ATMReqrdGblSts(self, value):
		self._ATMReqrdGblSts = value if type(value) != base_types.auto else self.make_default("ATMReqrdGblSts")

	@ATMReqrdGblSts.deleter
	def ATMReqrdGblSts(self):
		del self._ATMReqrdGblSts
		self._ATMReqrdGblSts = None

	@property
	def ReqrdCfgtnParam(self):
		return self._ReqrdCfgtnParam

	@ReqrdCfgtnParam.setter
	def ReqrdCfgtnParam(self, value):
		self._ReqrdCfgtnParam = value if type(value) != base_types.auto else self.make_default("ReqrdCfgtnParam")

	@ReqrdCfgtnParam.deleter
	def ReqrdCfgtnParam(self):
		del self._ReqrdCfgtnParam
		self._ReqrdCfgtnParam = None

	@property
	def XpctdMsgFctn(self):
		return self._XpctdMsgFctn

	@XpctdMsgFctn.setter
	def XpctdMsgFctn(self, value):
		self._XpctdMsgFctn = value if type(value) != base_types.auto else self.make_default("XpctdMsgFctn")

	@XpctdMsgFctn.deleter
	def XpctdMsgFctn(self):
		del self._XpctdMsgFctn
		self._XpctdMsgFctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMReqrdGblSts', type=ATMStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqrdCfgtnParam', type=ATMConfigurationParameter1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XpctdMsgFctn', type=MessageFunction8Code, min=0, max=1, mutex_group=1, array=False),
	))

