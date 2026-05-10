from . import base_types
from ._GenericIdentification175 import GenericIdentification175
from ._NoReasonCode import NoReasonCode
from ._UTIIdentifier import UTIIdentifier

class UniqueTransactionIdentifier3Choice(base_types._BaseFieldType):

	__slots__ = ["_NotAvlbl", "_Prtry", "_UnqTxIdr"]
	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if type(value) != base_types.auto else self.make_default("NotAvlbl")

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='NotAvlbl', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification175, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

