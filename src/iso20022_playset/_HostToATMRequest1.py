# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommandIdentification1
from . import ATMEnvironment9
from . import MessageFunction8Code

class HostToATMRequest1(base_types._BaseFieldType):

	__slots__ = ["_CmdId", "_Envt", "_XpctdMsgFctn"]
	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if value is not None else base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment9, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment9, False)

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
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdMsgFctn', type=MessageFunction8Code, min=1, max=1, mutex_group=None, array=False),
	))