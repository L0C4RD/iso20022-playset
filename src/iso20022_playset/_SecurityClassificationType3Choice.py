from . import base_types
from .CFIOct2015Identifier import CFIOct2015Identifier
from .GenericIdentification39 import GenericIdentification39

class SecurityClassificationType3Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_CFI"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if type(value) != base_types.auto else self.make_default("AltrnClssfctn")

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = None

	@property
	def CFI(self):
		return self._CFI

	@CFI.setter
	def CFI(self, value):
		self._CFI = value if type(value) != base_types.auto else self.make_default("CFI")

	@CFI.deleter
	def CFI(self):
		del self._CFI
		self._CFI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification39, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CFI', type=CFIOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
	))

