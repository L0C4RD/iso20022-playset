from . import base_types
from ._FinancialInstrumentIdentification7Choice import FinancialInstrumentIdentification7Choice

class SwapLegIdentification2(base_types._BaseFieldType):

	__slots__ = ["_SwpIn", "_SwpOut"]
	@property
	def SwpIn(self):
		return self._SwpIn

	@SwpIn.setter
	def SwpIn(self, value):
		self._SwpIn = value if type(value) != base_types.auto else self.make_default("SwpIn")

	@SwpIn.deleter
	def SwpIn(self):
		del self._SwpIn
		self._SwpIn = None

	@property
	def SwpOut(self):
		return self._SwpOut

	@SwpOut.setter
	def SwpOut(self, value):
		self._SwpOut = value if type(value) != base_types.auto else self.make_default("SwpOut")

	@SwpOut.deleter
	def SwpOut(self):
		del self._SwpOut
		self._SwpOut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SwpIn', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwpOut', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=None, array=False),
	))

