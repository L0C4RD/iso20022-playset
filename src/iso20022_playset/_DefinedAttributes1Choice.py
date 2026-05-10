from . import base_types
from ._FinancialInstrumentAttributes90 import FinancialInstrumentAttributes90
from ._FinancialInstrumentAttributes89 import FinancialInstrumentAttributes89

class DefinedAttributes1Choice(base_types._BaseFieldType):

	__slots__ = ["_ValDfndAttrbts", "_QtyDfndAttrbts"]
	@property
	def QtyDfndAttrbts(self):
		return self._QtyDfndAttrbts

	@QtyDfndAttrbts.setter
	def QtyDfndAttrbts(self, value):
		self._QtyDfndAttrbts = value if type(value) != base_types.auto else self.make_default("QtyDfndAttrbts")

	@QtyDfndAttrbts.deleter
	def QtyDfndAttrbts(self):
		del self._QtyDfndAttrbts
		self._QtyDfndAttrbts = None

	@property
	def ValDfndAttrbts(self):
		return self._ValDfndAttrbts

	@ValDfndAttrbts.setter
	def ValDfndAttrbts(self, value):
		self._ValDfndAttrbts = value if type(value) != base_types.auto else self.make_default("ValDfndAttrbts")

	@ValDfndAttrbts.deleter
	def ValDfndAttrbts(self):
		del self._ValDfndAttrbts
		self._ValDfndAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyDfndAttrbts', type=FinancialInstrumentAttributes89, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValDfndAttrbts', type=FinancialInstrumentAttributes90, min=0, max=1, mutex_group=1, array=False),
	))

