from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class MarginResult1Choice(base_types._BaseFieldType):

	__slots__ = ["_XcssAmt", "_DfcitAmt"]
	@property
	def XcssAmt(self):
		return self._XcssAmt

	@XcssAmt.setter
	def XcssAmt(self, value):
		self._XcssAmt = value if type(value) != auto else self.make_default("XcssAmt")

	@XcssAmt.deleter
	def XcssAmt(self):
		del self._XcssAmt
		self._XcssAmt = None

	@property
	def DfcitAmt(self):
		return self._DfcitAmt

	@DfcitAmt.setter
	def DfcitAmt(self, value):
		self._DfcitAmt = value if type(value) != auto else self.make_default("DfcitAmt")

	@DfcitAmt.deleter
	def DfcitAmt(self):
		del self._DfcitAmt
		self._DfcitAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XcssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DfcitAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

