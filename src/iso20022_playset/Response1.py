from . import base_types
from .ResponseType1Choice import ResponseType1Choice
from .Max140Text import Max140Text

class Response1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_RspnTpDtls"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def RspnTpDtls(self):
		return self._RspnTpDtls

	@RspnTpDtls.setter
	def RspnTpDtls(self, value):
		self._RspnTpDtls = value if type(value) != base_types.auto else self.make_default("RspnTpDtls")

	@RspnTpDtls.deleter
	def RspnTpDtls(self):
		del self._RspnTpDtls
		self._RspnTpDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTpDtls', type=ResponseType1Choice, min=1, max=None, mutex_group=None, array=True),
	))

