from . import base_types
from .Exact3NumericText import Exact3NumericText

class TotalNumber1(base_types._BaseFieldType):

	__slots__ = ["_CurInstrNb", "_TtlOfLkdInstrs"]
	@property
	def CurInstrNb(self):
		return self._CurInstrNb

	@CurInstrNb.setter
	def CurInstrNb(self, value):
		self._CurInstrNb = value if type(value) != base_types.auto else self.make_default("CurInstrNb")

	@CurInstrNb.deleter
	def CurInstrNb(self):
		del self._CurInstrNb
		self._CurInstrNb = None

	@property
	def TtlOfLkdInstrs(self):
		return self._TtlOfLkdInstrs

	@TtlOfLkdInstrs.setter
	def TtlOfLkdInstrs(self, value):
		self._TtlOfLkdInstrs = value if type(value) != base_types.auto else self.make_default("TtlOfLkdInstrs")

	@TtlOfLkdInstrs.deleter
	def TtlOfLkdInstrs(self):
		del self._TtlOfLkdInstrs
		self._TtlOfLkdInstrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurInstrNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOfLkdInstrs', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
	))

