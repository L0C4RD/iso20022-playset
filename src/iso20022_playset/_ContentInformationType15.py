from . import base_types
from ._ContentType2Code import ContentType2Code
from ._AuthenticatedData4 import AuthenticatedData4

class ContentInformationType15(base_types._BaseFieldType):

	__slots__ = ["_AuthntcdData", "_CnttTp"]
	@property
	def AuthntcdData(self):
		return self._AuthntcdData

	@AuthntcdData.setter
	def AuthntcdData(self, value):
		self._AuthntcdData = value if type(value) != base_types.auto else self.make_default("AuthntcdData")

	@AuthntcdData.deleter
	def AuthntcdData(self):
		del self._AuthntcdData
		self._AuthntcdData = None

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
		base_types.FieldEntry(name='AuthntcdData', type=AuthenticatedData4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
	))

