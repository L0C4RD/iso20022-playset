from . import base_types
import UseCases1Code
import Max35Text
import MessageIdentification1
import Max70Text

class References5(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_PrcId", "_AckdMsgId", "_MsgId", "_AttchdDocNm", "_ReqTp"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def PrcId(self):
		return self._PrcId

	@PrcId.setter
	def PrcId(self, value):
		self._PrcId = value if type(value) != auto else self.make_default("PrcId")

	@PrcId.deleter
	def PrcId(self):
		del self._PrcId
		self._PrcId = None

	@property
	def AckdMsgId(self):
		return self._AckdMsgId

	@AckdMsgId.setter
	def AckdMsgId(self, value):
		self._AckdMsgId = value if type(value) != auto else self.make_default("AckdMsgId")

	@AckdMsgId.deleter
	def AckdMsgId(self):
		del self._AckdMsgId
		self._AckdMsgId = None

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

	@property
	def AttchdDocNm(self):
		return self._AttchdDocNm

	@AttchdDocNm.setter
	def AttchdDocNm(self, value):
		self._AttchdDocNm = value if type(value) != auto else self.make_default("AttchdDocNm")

	@AttchdDocNm.deleter
	def AttchdDocNm(self):
		del self._AttchdDocNm
		self._AttchdDocNm = None

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if type(value) != auto else self.make_default("ReqTp")

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckdMsgId', type=MessageIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttchdDocNm', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqTp', type=UseCases1Code, min=1, max=1, mutex_group=None, array=False),
	))

