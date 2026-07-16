# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMConfigurationParameter1
from . import ATMStatus1Code
from . import MessageFunction8Code

class ATMCommandParameters1Choice(base_types._BaseFieldType):

	__slots__ = ["_ATMReqrdGblSts", "_ReqrdCfgtnParam", "_XpctdMsgFctn"]
	@property
	def ATMReqrdGblSts(self):
		return self._ATMReqrdGblSts

	@ATMReqrdGblSts.setter
	def ATMReqrdGblSts(self, value):
		self._ATMReqrdGblSts = value if value is not None else base_types.UninitialisedField(self, 'ATMReqrdGblSts', ATMStatus1Code, False)

	@ATMReqrdGblSts.deleter
	def ATMReqrdGblSts(self):
		del self._ATMReqrdGblSts
		self._ATMReqrdGblSts = base_types.UninitialisedField(self, 'ATMReqrdGblSts', ATMStatus1Code, False)

	@property
	def ReqrdCfgtnParam(self):
		return self._ReqrdCfgtnParam

	@ReqrdCfgtnParam.setter
	def ReqrdCfgtnParam(self, value):
		self._ReqrdCfgtnParam = value if value is not None else base_types.UninitialisedField(self, 'ReqrdCfgtnParam', ATMConfigurationParameter1, False)

	@ReqrdCfgtnParam.deleter
	def ReqrdCfgtnParam(self):
		del self._ReqrdCfgtnParam
		self._ReqrdCfgtnParam = base_types.UninitialisedField(self, 'ReqrdCfgtnParam', ATMConfigurationParameter1, False)

	@property
	def XpctdMsgFctn(self):
		return self._XpctdMsgFctn

	@XpctdMsgFctn.setter
	def XpctdMsgFctn(self, value):
		self._XpctdMsgFctn = value if value is not None else base_types.UninitialisedField(self, 'XpctdMsgFctn', MessageFunction8Code, False)

	@XpctdMsgFctn.deleter
	def XpctdMsgFctn(self):
		del self._XpctdMsgFctn
		self._XpctdMsgFctn = base_types.UninitialisedField(self, 'XpctdMsgFctn', MessageFunction8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMReqrdGblSts', type=ATMStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqrdCfgtnParam', type=ATMConfigurationParameter1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XpctdMsgFctn', type=MessageFunction8Code, min=0, max=1, mutex_group=1, array=False),
	))