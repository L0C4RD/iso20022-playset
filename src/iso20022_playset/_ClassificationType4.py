from . import base_types
from ._ExternalLegalFramework1Code import ExternalLegalFramework1Code
from ._ExternalRegulatoryInformationType1Code import ExternalRegulatoryInformationType1Code

class ClassificationType4(base_types._BaseFieldType):

	__slots__ = ["_InfTp", "_LglFrmwk"]
	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if type(value) != base_types.auto else self.make_default("InfTp")

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = None

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if type(value) != base_types.auto else self.make_default("LglFrmwk")

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfTp', type=ExternalRegulatoryInformationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=ExternalLegalFramework1Code, min=1, max=None, mutex_group=None, array=True),
	))

