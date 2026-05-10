from . import base_types
from .Max35Text import Max35Text
from .Max350Text import Max350Text

class ResponseDetails1(base_types._BaseFieldType):

	__slots__ = ["_AddtlDtls", "_RspnCd"]
	@property
	def AddtlDtls(self):
		return self._AddtlDtls

	@AddtlDtls.setter
	def AddtlDtls(self, value):
		self._AddtlDtls = value if type(value) != base_types.auto else self.make_default("AddtlDtls")

	@AddtlDtls.deleter
	def AddtlDtls(self):
		del self._AddtlDtls
		self._AddtlDtls = None

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if type(value) != base_types.auto else self.make_default("RspnCd")

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

