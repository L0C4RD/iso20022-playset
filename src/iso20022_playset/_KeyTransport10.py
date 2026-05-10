from . import base_types
from ._AlgorithmIdentification35 import AlgorithmIdentification35
from ._Number import Number
from ._Max5000Binary import Max5000Binary
from ._Recipient13Choice import Recipient13Choice

class KeyTransport10(base_types._BaseFieldType):

	__slots__ = ["_RcptId", "_Vrsn", "_KeyNcrptnAlgo", "_NcrptdKey"]
	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if type(value) != base_types.auto else self.make_default("RcptId")

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = None

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
	def NcrptdKey(self):
		return self._NcrptdKey

	@NcrptdKey.setter
	def NcrptdKey(self, value):
		self._NcrptdKey = value if type(value) != base_types.auto else self.make_default("NcrptdKey")

	@NcrptdKey.deleter
	def NcrptdKey(self):
		del self._NcrptdKey
		self._NcrptdKey = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcptId', type=Recipient13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyNcrptnAlgo', type=AlgorithmIdentification35, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdKey', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
	))

