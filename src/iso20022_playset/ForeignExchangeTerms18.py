import base_types
import ActiveCurrencyAndAmount
import BaseOneRate
import ActiveCurrencyCode

class ForeignExchangeTerms18(base_types._BaseFieldType):

	__slots__ = ["_UnitCcy", "_ConvtdAmt", "_QtdCcy", "_XchgRate"]
	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if type(value) != auto else self.make_default("UnitCcy")

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = None

	@property
	def ConvtdAmt(self):
		return self._ConvtdAmt

	@ConvtdAmt.setter
	def ConvtdAmt(self, value):
		self._ConvtdAmt = value if type(value) != auto else self.make_default("ConvtdAmt")

	@ConvtdAmt.deleter
	def ConvtdAmt(self):
		del self._ConvtdAmt
		self._ConvtdAmt = None

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if type(value) != auto else self.make_default("QtdCcy")

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))

