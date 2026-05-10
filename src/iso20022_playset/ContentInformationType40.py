from . import base_types
from .EnvelopedData11 import EnvelopedData11
from .ContentType2Code import ContentType2Code

class ContentInformationType40(base_types._BaseFieldType):

	__slots__ = ["_EnvlpdData", "_CnttTp"]
	@property
	def EnvlpdData(self):
		return self._EnvlpdData

	@EnvlpdData.setter
	def EnvlpdData(self, value):
		self._EnvlpdData = value if type(value) != base_types.auto else self.make_default("EnvlpdData")

	@EnvlpdData.deleter
	def EnvlpdData(self):
		del self._EnvlpdData
		self._EnvlpdData = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
	))

