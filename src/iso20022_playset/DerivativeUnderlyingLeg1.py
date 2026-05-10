from . import base_types
from .FinancialInstrumentAttributes88 import FinancialInstrumentAttributes88
from .DefinedAttributes1Choice import DefinedAttributes1Choice

class DerivativeUnderlyingLeg1(base_types._BaseFieldType):

	__slots__ = ["_DfndAttrbts", "_CtrctAttrbts"]
	@property
	def DfndAttrbts(self):
		return self._DfndAttrbts

	@DfndAttrbts.setter
	def DfndAttrbts(self, value):
		self._DfndAttrbts = value if type(value) != base_types.auto else self.make_default("DfndAttrbts")

	@DfndAttrbts.deleter
	def DfndAttrbts(self):
		del self._DfndAttrbts
		self._DfndAttrbts = None

	@property
	def CtrctAttrbts(self):
		return self._CtrctAttrbts

	@CtrctAttrbts.setter
	def CtrctAttrbts(self, value):
		self._CtrctAttrbts = value if type(value) != base_types.auto else self.make_default("CtrctAttrbts")

	@CtrctAttrbts.deleter
	def CtrctAttrbts(self):
		del self._CtrctAttrbts
		self._CtrctAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfndAttrbts', type=DefinedAttributes1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctAttrbts', type=FinancialInstrumentAttributes88, min=1, max=1, mutex_group=None, array=False),
	))

