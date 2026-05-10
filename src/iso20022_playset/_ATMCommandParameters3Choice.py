from . import base_types
from .MessageFunction8Code import MessageFunction8Code
from .ATMConfigurationParameter1 import ATMConfigurationParameter1
from .ATMConfigurationParameter2 import ATMConfigurationParameter2
from .ATMCommandParameters1 import ATMCommandParameters1
from .ATMSecurityScheme4Code import ATMSecurityScheme4Code
from .ATMStatus1Code import ATMStatus1Code

class ATMCommandParameters3Choice(base_types._BaseFieldType):

	__slots__ = ["_SctyDvc", "_Key", "_ReqrdCfgtnParam", "_ReqrdSctySchme", "_XpctdMsgFctn", "_ATMReqrdGblSts"]
	@property
	def SctyDvc(self):
		return self._SctyDvc

	@SctyDvc.setter
	def SctyDvc(self, value):
		self._SctyDvc = value if type(value) != base_types.auto else self.make_default("SctyDvc")

	@SctyDvc.deleter
	def SctyDvc(self):
		del self._SctyDvc
		self._SctyDvc = None

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != base_types.auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

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
	def ReqrdSctySchme(self):
		return self._ReqrdSctySchme

	@ReqrdSctySchme.setter
	def ReqrdSctySchme(self, value):
		self._ReqrdSctySchme = value if type(value) != base_types.auto else self.make_default("ReqrdSctySchme")

	@ReqrdSctySchme.deleter
	def ReqrdSctySchme(self):
		del self._ReqrdSctySchme
		self._ReqrdSctySchme = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyDvc', type=ATMCommandParameters1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Key', type=ATMConfigurationParameter2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqrdCfgtnParam', type=ATMConfigurationParameter1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqrdSctySchme', type=ATMSecurityScheme4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XpctdMsgFctn', type=MessageFunction8Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ATMReqrdGblSts', type=ATMStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))

