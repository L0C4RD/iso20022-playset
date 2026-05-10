import base_types
import Max6NumericText

class TotalNumber2(base_types._BaseFieldType):

	__slots__ = ["_TtlOfLkdInstrs", "_CurInstrNb"]
	@property
	def TtlOfLkdInstrs(self):
		return self._TtlOfLkdInstrs

	@TtlOfLkdInstrs.setter
	def TtlOfLkdInstrs(self, value):
		self._TtlOfLkdInstrs = value if type(value) != auto else self.make_default("TtlOfLkdInstrs")

	@TtlOfLkdInstrs.deleter
	def TtlOfLkdInstrs(self):
		del self._TtlOfLkdInstrs
		self._TtlOfLkdInstrs = None

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
		base_types.FieldEntry(name='TtlOfLkdInstrs', type=Max6NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurInstrNb', type=Max6NumericText, min=1, max=1, mutex_group=None, array=False),
	))

