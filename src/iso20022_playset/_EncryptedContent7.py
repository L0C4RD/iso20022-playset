from . import base_types
from ._AlgorithmIdentification32 import AlgorithmIdentification32
from ._ContentType2Code import ContentType2Code
from ._Max100KBinary import Max100KBinary

class EncryptedContent7(base_types._BaseFieldType):

	__slots__ = ["_CnttNcrptnAlgo", "_CnttTp", "_NcrptdData"]
	@property
	def CnttNcrptnAlgo(self):
		return self._CnttNcrptnAlgo

	@CnttNcrptnAlgo.setter
	def CnttNcrptnAlgo(self, value):
		self._CnttNcrptnAlgo = value if type(value) != base_types.auto else self.make_default("CnttNcrptnAlgo")

	@CnttNcrptnAlgo.deleter
	def CnttNcrptnAlgo(self):
		del self._CnttNcrptnAlgo
		self._CnttNcrptnAlgo = None

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if type(value) != base_types.auto else self.make_default("CnttTp")

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = None

	@property
	def NcrptdData(self):
		return self._NcrptdData

	@NcrptdData.setter
	def NcrptdData(self, value):
		self._NcrptdData = value if type(value) != base_types.auto else self.make_default("NcrptdData")

	@NcrptdData.deleter
	def NcrptdData(self):
		del self._NcrptdData
		self._NcrptdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttNcrptnAlgo', type=AlgorithmIdentification32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdData', type=Max100KBinary, min=1, max=1, mutex_group=None, array=False),
	))

