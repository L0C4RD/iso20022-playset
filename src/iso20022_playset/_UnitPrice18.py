# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import Max15NumericText
from . import UnitOfMeasure3Choice

class UnitPrice18(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Fctr", "_UnitPric"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@property
	def Fctr(self):
		return self._Fctr

	@Fctr.setter
	def Fctr(self, value):
		self._Fctr = value if value is not None else base_types.UninitialisedField(self, 'Fctr', Max15NumericText, False)

	@Fctr.deleter
	def Fctr(self):
		del self._Fctr
		self._Fctr = base_types.UninitialisedField(self, 'Fctr', Max15NumericText, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', UnitOfMeasure3Choice, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', UnitOfMeasure3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctr', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
	))