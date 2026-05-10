from . import base_types
from .ContentType3Code import ContentType3Code
from .EncryptedData2 import EncryptedData2
from .EnvelopedData12 import EnvelopedData12

class ProtectedData2(base_types._BaseFieldType):

	__slots__ = ["_NcrptdData", "_CnttTp", "_EnvlpdData"]
	@property
	def NcrptdData(self):
		return self._NcrptdData

	@NcrptdData.setter
	def NcrptdData(self, value):
		self._NcrptdData = value if type(value) != auto else self.make_default("NcrptdData")

	@NcrptdData.deleter
	def NcrptdData(self):
		del self._NcrptdData
		self._NcrptdData = None

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if type(value) != auto else self.make_default("CnttTp")

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = None

	@property
	def EnvlpdData(self):
		return self._EnvlpdData

	@EnvlpdData.setter
	def EnvlpdData(self, value):
		self._EnvlpdData = value if type(value) != auto else self.make_default("EnvlpdData")

	@EnvlpdData.deleter
	def EnvlpdData(self):
		del self._EnvlpdData
		self._EnvlpdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcrptdData', type=EncryptedData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData12, min=0, max=1, mutex_group=None, array=False),
	))

