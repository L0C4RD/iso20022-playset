from . import base_types
from ._KEKIdentifier2 import KEKIdentifier2
from ._Number import Number
from ._Max500Binary import Max500Binary
from ._AlgorithmIdentification13 import AlgorithmIdentification13

class KEK4(base_types._BaseFieldType):

	__slots__ = ["_KeyNcrptnAlgo", "_Vrsn", "_NcrptdKey", "_KEKId"]
	@property
	def KeyNcrptnAlgo(self):
		return self._KeyNcrptnAlgo

	@KeyNcrptnAlgo.setter
	def KeyNcrptnAlgo(self, value):
		self._KeyNcrptnAlgo = value if type(value) != base_types.auto else self.make_default("KeyNcrptnAlgo")

	@KeyNcrptnAlgo.deleter
	def KeyNcrptnAlgo(self):
		del self._KeyNcrptnAlgo
		self._KeyNcrptnAlgo = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def NcrptdKey(self):
		return self._NcrptdKey

	@NcrptdKey.setter
	def NcrptdKey(self, value):
		self._NcrptdKey = value if type(value) != base_types.auto else self.make_default("NcrptdKey")

	@NcrptdKey.deleter
	def NcrptdKey(self):
		del self._NcrptdKey
		self._NcrptdKey = None

	@property
	def KEKId(self):
		return self._KEKId

	@KEKId.setter
	def KEKId(self, value):
		self._KEKId = value if type(value) != base_types.auto else self.make_default("KEKId")

	@KEKId.deleter
	def KEKId(self):
		del self._KEKId
		self._KEKId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeyNcrptnAlgo', type=AlgorithmIdentification13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdKey', type=Max500Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KEKId', type=KEKIdentifier2, min=1, max=1, mutex_group=None, array=False),
	))

