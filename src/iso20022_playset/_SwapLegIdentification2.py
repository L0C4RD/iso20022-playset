# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentIdentification7Choice

class SwapLegIdentification2(base_types._BaseFieldType):

	__slots__ = ["_SwpIn", "_SwpOut"]
	@property
	def SwpIn(self):
		return self._SwpIn

	@SwpIn.setter
	def SwpIn(self, value):
		self._SwpIn = value if value is not None else base_types.UninitialisedField(self, 'SwpIn', FinancialInstrumentIdentification7Choice, False)

	@SwpIn.deleter
	def SwpIn(self):
		del self._SwpIn
		self._SwpIn = base_types.UninitialisedField(self, 'SwpIn', FinancialInstrumentIdentification7Choice, False)

	@property
	def SwpOut(self):
		return self._SwpOut

	@SwpOut.setter
	def SwpOut(self, value):
		self._SwpOut = value if value is not None else base_types.UninitialisedField(self, 'SwpOut', FinancialInstrumentIdentification7Choice, False)

	@SwpOut.deleter
	def SwpOut(self):
		del self._SwpOut
		self._SwpOut = base_types.UninitialisedField(self, 'SwpOut', FinancialInstrumentIdentification7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SwpIn', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwpOut', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=None, array=False),
	))