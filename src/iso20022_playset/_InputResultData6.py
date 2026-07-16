# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CapturedSignature1
from . import ContentInformationType39
from . import InputCommand1Code
from . import Max20000Text
from . import Number
from . import TrueFalseIndicator

class InputResultData6(base_types._BaseFieldType):

	__slots__ = ["_ConfdFlg", "_FctnKey", "_ImgCaptrdSgntr", "_InptCmd", "_InptMsg", "_Pwd"]
	@property
	def ConfdFlg(self):
		return self._ConfdFlg

	@ConfdFlg.setter
	def ConfdFlg(self, value):
		self._ConfdFlg = value if value is not None else base_types.UninitialisedField(self, 'ConfdFlg', TrueFalseIndicator, False)

	@ConfdFlg.deleter
	def ConfdFlg(self):
		del self._ConfdFlg
		self._ConfdFlg = base_types.UninitialisedField(self, 'ConfdFlg', TrueFalseIndicator, False)

	@property
	def FctnKey(self):
		return self._FctnKey

	@FctnKey.setter
	def FctnKey(self, value):
		self._FctnKey = value if value is not None else base_types.UninitialisedField(self, 'FctnKey', Number, False)

	@FctnKey.deleter
	def FctnKey(self):
		del self._FctnKey
		self._FctnKey = base_types.UninitialisedField(self, 'FctnKey', Number, False)

	@property
	def ImgCaptrdSgntr(self):
		return self._ImgCaptrdSgntr

	@ImgCaptrdSgntr.setter
	def ImgCaptrdSgntr(self, value):
		self._ImgCaptrdSgntr = value if value is not None else base_types.UninitialisedField(self, 'ImgCaptrdSgntr', CapturedSignature1, False)

	@ImgCaptrdSgntr.deleter
	def ImgCaptrdSgntr(self):
		del self._ImgCaptrdSgntr
		self._ImgCaptrdSgntr = base_types.UninitialisedField(self, 'ImgCaptrdSgntr', CapturedSignature1, False)

	@property
	def InptCmd(self):
		return self._InptCmd

	@InptCmd.setter
	def InptCmd(self, value):
		self._InptCmd = value if value is not None else base_types.UninitialisedField(self, 'InptCmd', InputCommand1Code, False)

	@InptCmd.deleter
	def InptCmd(self):
		del self._InptCmd
		self._InptCmd = base_types.UninitialisedField(self, 'InptCmd', InputCommand1Code, False)

	@property
	def InptMsg(self):
		return self._InptMsg

	@InptMsg.setter
	def InptMsg(self, value):
		self._InptMsg = value if value is not None else base_types.UninitialisedField(self, 'InptMsg', Max20000Text, False)

	@InptMsg.deleter
	def InptMsg(self):
		del self._InptMsg
		self._InptMsg = base_types.UninitialisedField(self, 'InptMsg', Max20000Text, False)

	@property
	def Pwd(self):
		return self._Pwd

	@Pwd.setter
	def Pwd(self, value):
		self._Pwd = value if value is not None else base_types.UninitialisedField(self, 'Pwd', ContentInformationType39, False)

	@Pwd.deleter
	def Pwd(self):
		del self._Pwd
		self._Pwd = base_types.UninitialisedField(self, 'Pwd', ContentInformationType39, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctnKey', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgCaptrdSgntr', type=CapturedSignature1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptCmd', type=InputCommand1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptMsg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pwd', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
	))