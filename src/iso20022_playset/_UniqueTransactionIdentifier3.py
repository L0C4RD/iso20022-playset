from . import base_types
from ._UTIIdentifier import UTIIdentifier

class UniqueTransactionIdentifier3(base_types._BaseFieldType):

	__slots__ = ["_PrrUnqTxIdr", "_UnqTxIdr"]
	@property
	def PrrUnqTxIdr(self):
		return self._PrrUnqTxIdr

	@PrrUnqTxIdr.setter
	def PrrUnqTxIdr(self, value):
		self._PrrUnqTxIdr = value if type(value) != base_types.auto else self.make_default("PrrUnqTxIdr")

	@PrrUnqTxIdr.deleter
	def PrrUnqTxIdr(self):
		del self._PrrUnqTxIdr
		self._PrrUnqTxIdr = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrrUnqTxIdr', type=UTIIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

