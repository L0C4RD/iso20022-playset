from . import base_types
from .Max50Text import Max50Text
from .GenericPersonIdentification1 import GenericPersonIdentification1
from .NoReasonCode import NoReasonCode

class ExecutingParty2Choice(base_types._BaseFieldType):

	__slots__ = ["_Prsn", "_Algo", "_Clnt"]
	@property
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if type(value) != auto else self.make_default("Prsn")

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = None

	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def Clnt(self):
		return self._Clnt

	@Clnt.setter
	def Clnt(self, value):
		self._Clnt = value if type(value) != auto else self.make_default("Clnt")

	@Clnt.deleter
	def Clnt(self):
		del self._Clnt
		self._Clnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prsn', type=GenericPersonIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Algo', type=Max50Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Clnt', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

