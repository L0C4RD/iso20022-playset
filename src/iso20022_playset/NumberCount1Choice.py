import base_types
import Exact3NumericText
import TotalNumber1

class NumberCount1Choice(base_types._BaseFieldType):

	__slots__ = ["_TtlNb", "_CurInstrNb"]
	@property
	def TtlNb(self):
		return self._TtlNb

	@TtlNb.setter
	def TtlNb(self, value):
		self._TtlNb = value if type(value) != auto else self.make_default("TtlNb")

	@TtlNb.deleter
	def TtlNb(self):
		del self._TtlNb
		self._TtlNb = None

	@property
	def CurInstrNb(self):
		return self._CurInstrNb

	@CurInstrNb.setter
	def CurInstrNb(self, value):
		self._CurInstrNb = value if type(value) != auto else self.make_default("CurInstrNb")

	@CurInstrNb.deleter
	def CurInstrNb(self):
		del self._CurInstrNb
		self._CurInstrNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNb', type=TotalNumber1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CurInstrNb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))

