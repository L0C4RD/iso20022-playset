from . import base_types
from ._BICFIDec2014Identifier import BICFIDec2014Identifier
from ._Max256Text import Max256Text

class TechnicalIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_TechAdr"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != base_types.auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if type(value) != base_types.auto else self.make_default("TechAdr")

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
	))

