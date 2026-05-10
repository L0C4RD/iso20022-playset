from . import base_types
from ._ContentType2Code import ContentType2Code
from ._Max100KBinary import Max100KBinary

class EncapsulatedContent3(base_types._BaseFieldType):

	__slots__ = ["_Cntt", "_CnttTp"]
	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if type(value) != base_types.auto else self.make_default("Cntt")

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = None

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
		base_types.FieldEntry(name='Cntt', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
	))

