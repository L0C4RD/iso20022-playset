from . import base_types
from ._CapturedSignature1 import CapturedSignature1
from ._ContentInformationType39 import ContentInformationType39
from ._InputCommand1Code import InputCommand1Code
from ._Max20000Text import Max20000Text
from ._Number import Number
from ._TrueFalseIndicator import TrueFalseIndicator

class InputResultData6(base_types._BaseFieldType):

	__slots__ = ["_ConfdFlg", "_FctnKey", "_ImgCaptrdSgntr", "_InptCmd", "_InptMsg", "_Pwd"]
	@property
	def ConfdFlg(self):
		return self._ConfdFlg

	@ConfdFlg.setter
	def ConfdFlg(self, value):
		self._ConfdFlg = value if type(value) != base_types.auto else self.make_default("ConfdFlg")

	@ConfdFlg.deleter
	def ConfdFlg(self):
		del self._ConfdFlg
		self._ConfdFlg = None

	@property
	def FctnKey(self):
		return self._FctnKey

	@FctnKey.setter
	def FctnKey(self, value):
		self._FctnKey = value if type(value) != base_types.auto else self.make_default("FctnKey")

	@FctnKey.deleter
	def FctnKey(self):
		del self._FctnKey
		self._FctnKey = None

	@property
	def ImgCaptrdSgntr(self):
		return self._ImgCaptrdSgntr

	@ImgCaptrdSgntr.setter
	def ImgCaptrdSgntr(self, value):
		self._ImgCaptrdSgntr = value if type(value) != base_types.auto else self.make_default("ImgCaptrdSgntr")

	@ImgCaptrdSgntr.deleter
	def ImgCaptrdSgntr(self):
		del self._ImgCaptrdSgntr
		self._ImgCaptrdSgntr = None

	@property
	def InptCmd(self):
		return self._InptCmd

	@InptCmd.setter
	def InptCmd(self, value):
		self._InptCmd = value if type(value) != base_types.auto else self.make_default("InptCmd")

	@InptCmd.deleter
	def InptCmd(self):
		del self._InptCmd
		self._InptCmd = None

	@property
	def InptMsg(self):
		return self._InptMsg

	@InptMsg.setter
	def InptMsg(self, value):
		self._InptMsg = value if type(value) != base_types.auto else self.make_default("InptMsg")

	@InptMsg.deleter
	def InptMsg(self):
		del self._InptMsg
		self._InptMsg = None

	@property
	def Pwd(self):
		return self._Pwd

	@Pwd.setter
	def Pwd(self, value):
		self._Pwd = value if type(value) != base_types.auto else self.make_default("Pwd")

	@Pwd.deleter
	def Pwd(self):
		del self._Pwd
		self._Pwd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctnKey', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgCaptrdSgntr', type=CapturedSignature1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptCmd', type=InputCommand1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptMsg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pwd', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
	))

