from . import base_types
from ._Max35Text import Max35Text
from ._RequestDetails4 import RequestDetails4

class RequestDetails5(base_types._BaseFieldType):

	__slots__ = ["_ReqRef", "_RptKey", "_Tp"]
	@property
	def ReqRef(self):
		return self._ReqRef

	@ReqRef.setter
	def ReqRef(self, value):
		self._ReqRef = value if type(value) != base_types.auto else self.make_default("ReqRef")

	@ReqRef.deleter
	def ReqRef(self):
		del self._ReqRef
		self._ReqRef = None

	@property
	def RptKey(self):
		return self._RptKey

	@RptKey.setter
	def RptKey(self, value):
		self._RptKey = value if type(value) != base_types.auto else self.make_default("RptKey")

	@RptKey.deleter
	def RptKey(self):
		del self._RptKey
		self._RptKey = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptKey', type=RequestDetails4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

