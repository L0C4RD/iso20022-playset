import base_types
import AmountAndDirection14

class BalanceAmounts4(base_types._BaseFieldType):

	__slots__ = ["_HldgVal", "_AcrdIntrstAmt", "_ElgblCollVal", "_BookVal", "_PrvsHldgVal"]
	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if type(value) != auto else self.make_default("HldgVal")

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def ElgblCollVal(self):
		return self._ElgblCollVal

	@ElgblCollVal.setter
	def ElgblCollVal(self, value):
		self._ElgblCollVal = value if type(value) != auto else self.make_default("ElgblCollVal")

	@ElgblCollVal.deleter
	def ElgblCollVal(self):
		del self._ElgblCollVal
		self._ElgblCollVal = None

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if type(value) != auto else self.make_default("BookVal")

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = None

	@property
	def PrvsHldgVal(self):
		return self._PrvsHldgVal

	@PrvsHldgVal.setter
	def PrvsHldgVal(self, value):
		self._PrvsHldgVal = value if type(value) != auto else self.make_default("PrvsHldgVal")

	@PrvsHldgVal.deleter
	def PrvsHldgVal(self):
		del self._PrvsHldgVal
		self._PrvsHldgVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldgVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblCollVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsHldgVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
	))

