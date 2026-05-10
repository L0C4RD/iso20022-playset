from . import base_types
from .Algorithm15Code import Algorithm15Code
from .Algorithm13Code import Algorithm13Code
from .TrueFalseIndicator import TrueFalseIndicator
from .EncryptionFormat1Code import EncryptionFormat1Code
from .Algorithm7Code import Algorithm7Code

class ATMSecurityConfiguration3(base_types._BaseFieldType):

	__slots__ = ["_SmmtrcNcrptnAlgo", "_AsmmtrcKeyStdId", "_NcrptnFrmt", "_AsmmtrcNcrptnAlgo", "_SmmtrcTrnsprtKeyAlgo", "_AsmmtrcNcrptn", "_SmmtrcTrnsprtKey"]
	@property
	def SmmtrcNcrptnAlgo(self):
		return self._SmmtrcNcrptnAlgo

	@SmmtrcNcrptnAlgo.setter
	def SmmtrcNcrptnAlgo(self, value):
		self._SmmtrcNcrptnAlgo = value if type(value) != base_types.auto else self.make_default("SmmtrcNcrptnAlgo")

	@SmmtrcNcrptnAlgo.deleter
	def SmmtrcNcrptnAlgo(self):
		del self._SmmtrcNcrptnAlgo
		self._SmmtrcNcrptnAlgo = None

	@property
	def AsmmtrcKeyStdId(self):
		return self._AsmmtrcKeyStdId

	@AsmmtrcKeyStdId.setter
	def AsmmtrcKeyStdId(self, value):
		self._AsmmtrcKeyStdId = value if type(value) != base_types.auto else self.make_default("AsmmtrcKeyStdId")

	@AsmmtrcKeyStdId.deleter
	def AsmmtrcKeyStdId(self):
		del self._AsmmtrcKeyStdId
		self._AsmmtrcKeyStdId = None

	@property
	def NcrptnFrmt(self):
		return self._NcrptnFrmt

	@NcrptnFrmt.setter
	def NcrptnFrmt(self, value):
		self._NcrptnFrmt = value if type(value) != base_types.auto else self.make_default("NcrptnFrmt")

	@NcrptnFrmt.deleter
	def NcrptnFrmt(self):
		del self._NcrptnFrmt
		self._NcrptnFrmt = None

	@property
	def AsmmtrcNcrptnAlgo(self):
		return self._AsmmtrcNcrptnAlgo

	@AsmmtrcNcrptnAlgo.setter
	def AsmmtrcNcrptnAlgo(self, value):
		self._AsmmtrcNcrptnAlgo = value if type(value) != base_types.auto else self.make_default("AsmmtrcNcrptnAlgo")

	@AsmmtrcNcrptnAlgo.deleter
	def AsmmtrcNcrptnAlgo(self):
		del self._AsmmtrcNcrptnAlgo
		self._AsmmtrcNcrptnAlgo = None

	@property
	def SmmtrcTrnsprtKeyAlgo(self):
		return self._SmmtrcTrnsprtKeyAlgo

	@SmmtrcTrnsprtKeyAlgo.setter
	def SmmtrcTrnsprtKeyAlgo(self, value):
		self._SmmtrcTrnsprtKeyAlgo = value if type(value) != base_types.auto else self.make_default("SmmtrcTrnsprtKeyAlgo")

	@SmmtrcTrnsprtKeyAlgo.deleter
	def SmmtrcTrnsprtKeyAlgo(self):
		del self._SmmtrcTrnsprtKeyAlgo
		self._SmmtrcTrnsprtKeyAlgo = None

	@property
	def AsmmtrcNcrptn(self):
		return self._AsmmtrcNcrptn

	@AsmmtrcNcrptn.setter
	def AsmmtrcNcrptn(self, value):
		self._AsmmtrcNcrptn = value if type(value) != base_types.auto else self.make_default("AsmmtrcNcrptn")

	@AsmmtrcNcrptn.deleter
	def AsmmtrcNcrptn(self):
		del self._AsmmtrcNcrptn
		self._AsmmtrcNcrptn = None

	@property
	def SmmtrcTrnsprtKey(self):
		return self._SmmtrcTrnsprtKey

	@SmmtrcTrnsprtKey.setter
	def SmmtrcTrnsprtKey(self, value):
		self._SmmtrcTrnsprtKey = value if type(value) != base_types.auto else self.make_default("SmmtrcTrnsprtKey")

	@SmmtrcTrnsprtKey.deleter
	def SmmtrcTrnsprtKey(self):
		del self._SmmtrcTrnsprtKey
		self._SmmtrcTrnsprtKey = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SmmtrcNcrptnAlgo', type=Algorithm15Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsmmtrcKeyStdId', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptnFrmt', type=EncryptionFormat1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsmmtrcNcrptnAlgo', type=Algorithm7Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SmmtrcTrnsprtKeyAlgo', type=Algorithm13Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsmmtrcNcrptn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SmmtrcTrnsprtKey', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

