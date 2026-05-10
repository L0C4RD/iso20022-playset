from . import base_types
from ._Max35Text import Max35Text
from ._GenericIdentification177 import GenericIdentification177
from ._DocumentType7Code import DocumentType7Code
from ._TrueFalseIndicator import TrueFalseIndicator

class MessageStatusRequestData2(base_types._BaseFieldType):

	__slots__ = ["_DocQlfr", "_RctRprntFlg", "_InitgPty", "_XchgId"]
	@property
	def DocQlfr(self):
		return self._DocQlfr

	@DocQlfr.setter
	def DocQlfr(self, value):
		self._DocQlfr = value if type(value) != base_types.auto else self.make_default("DocQlfr")

	@DocQlfr.deleter
	def DocQlfr(self):
		del self._DocQlfr
		self._DocQlfr = None

	@property
	def RctRprntFlg(self):
		return self._RctRprntFlg

	@RctRprntFlg.setter
	def RctRprntFlg(self, value):
		self._RctRprntFlg = value if type(value) != base_types.auto else self.make_default("RctRprntFlg")

	@RctRprntFlg.deleter
	def RctRprntFlg(self):
		del self._RctRprntFlg
		self._RctRprntFlg = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocQlfr', type=DocumentType7Code, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='RctRprntFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

