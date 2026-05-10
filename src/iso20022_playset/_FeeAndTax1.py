from . import base_types
from .Max35Text import Max35Text
from .Tax30 import Tax30
from .Fee1 import Fee1

class FeeAndTax1(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_IndvTax", "_IndvFee"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != base_types.auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != base_types.auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if type(value) != base_types.auto else self.make_default("IndvFee")

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvFee', type=Fee1, min=0, max=None, mutex_group=None, array=True),
	))

