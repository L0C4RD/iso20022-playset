from . import base_types
import Max140Text
import Max35Text

class AuthorityRequestType1(base_types._BaseFieldType):

	__slots__ = ["_MsgNmId", "_MsgNm"]
	@property
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if type(value) != auto else self.make_default("MsgNmId")

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = None

	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if type(value) != auto else self.make_default("MsgNm")

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

