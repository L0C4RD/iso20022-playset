import base_types
import Max37Text
import Max19HexBinaryText

class Track2Data1Choice(base_types._BaseFieldType):

	__slots__ = ["_HexBinryVal", "_TxtVal"]
	@property
	def HexBinryVal(self):
		return self._HexBinryVal

	@HexBinryVal.setter
	def HexBinryVal(self, value):
		self._HexBinryVal = value if type(value) != auto else self.make_default("HexBinryVal")

	@HexBinryVal.deleter
	def HexBinryVal(self):
		del self._HexBinryVal
		self._HexBinryVal = None

	@property
	def TxtVal(self):
		return self._TxtVal

	@TxtVal.setter
	def TxtVal(self, value):
		self._TxtVal = value if type(value) != auto else self.make_default("TxtVal")

	@TxtVal.deleter
	def TxtVal(self):
		del self._TxtVal
		self._TxtVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HexBinryVal', type=Max19HexBinaryText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxtVal', type=Max37Text, min=0, max=1, mutex_group=1, array=False),
	))

