# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity35Choice import FinancialInstrumentQuantity35Choice

class CorporateActionQuantity12(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_IncrmtlDnmtn"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if type(value) != base_types.auto else self.make_default("BaseDnmtn")

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = None

	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if type(value) != base_types.auto else self.make_default("IncrmtlDnmtn")

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
	))