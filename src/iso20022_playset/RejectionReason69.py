from . import base_types
from .Max350Text import Max350Text
from .MessageRejectedReason2Code import MessageRejectedReason2Code
from .LinkedMessage6Choice import LinkedMessage6Choice

class RejectionReason69(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Rsn", "_LkdMsg"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def LkdMsg(self):
		return self._LkdMsg

	@LkdMsg.setter
	def LkdMsg(self, value):
		self._LkdMsg = value if type(value) != auto else self.make_default("LkdMsg")

	@LkdMsg.deleter
	def LkdMsg(self):
		del self._LkdMsg
		self._LkdMsg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=MessageRejectedReason2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkdMsg', type=LinkedMessage6Choice, min=0, max=1, mutex_group=None, array=False),
	))

