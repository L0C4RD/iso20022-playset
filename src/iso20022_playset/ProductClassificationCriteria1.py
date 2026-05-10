from . import base_types
from .CFIOct2015Identifier import CFIOct2015Identifier
from .Max52Text import Max52Text

class ProductClassificationCriteria1(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnFinInstrm", "_UnqPdctIdr"]
	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if type(value) != base_types.auto else self.make_default("ClssfctnFinInstrm")

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = None

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != base_types.auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqPdctIdr', type=Max52Text, min=0, max=None, mutex_group=None, array=True),
	))

