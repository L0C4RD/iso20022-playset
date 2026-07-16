# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity43Choice

class CorporateActionQuantity13(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_IncrmtlDnmtn"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if value is not None else base_types.UninitialisedField(self, 'BaseDnmtn', FinancialInstrumentQuantity43Choice, False)

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = base_types.UninitialisedField(self, 'BaseDnmtn', FinancialInstrumentQuantity43Choice, False)

	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if value is not None else base_types.UninitialisedField(self, 'IncrmtlDnmtn', FinancialInstrumentQuantity43Choice, False)

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = base_types.UninitialisedField(self, 'IncrmtlDnmtn', FinancialInstrumentQuantity43Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
	))