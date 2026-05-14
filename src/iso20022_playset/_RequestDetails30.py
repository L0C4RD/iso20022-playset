from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification242Choice import PartyIdentification242Choice

class RequestDetails30(base_types._BaseFieldType):

	__slots__ = ["_AddtlReqInf", "_RqstrId", "_Tp"]
	@property
	def AddtlReqInf(self):
		return self._AddtlReqInf

	@AddtlReqInf.setter
	def AddtlReqInf(self, value):
		self._AddtlReqInf = value if type(value) != base_types.auto else self.make_default("AddtlReqInf")

	@AddtlReqInf.deleter
	def AddtlReqInf(self):
		del self._AddtlReqInf
		self._AddtlReqInf = None

	@property
	def RqstrId(self):
		return self._RqstrId

	@RqstrId.setter
	def RqstrId(self, value):
		self._RqstrId = value if type(value) != base_types.auto else self.make_default("RqstrId")

	@RqstrId.deleter
	def RqstrId(self):
		del self._RqstrId
		self._RqstrId = None

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
		base_types.FieldEntry(name='AddtlReqInf', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RqstrId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

