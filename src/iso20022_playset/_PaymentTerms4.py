# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrPercentage2Choice
from . import PaymentCodeOrOther1Choice

class PaymentTerms4(base_types._BaseFieldType):

	__slots__ = ["_AmtOrPctg", "_PmtTerms"]
	@property
	def AmtOrPctg(self):
		return self._AmtOrPctg

	@AmtOrPctg.setter
	def AmtOrPctg(self, value):
		self._AmtOrPctg = value if value is not None else base_types.UninitialisedField(self, 'AmtOrPctg', AmountOrPercentage2Choice, False)

	@AmtOrPctg.deleter
	def AmtOrPctg(self):
		del self._AmtOrPctg
		self._AmtOrPctg = base_types.UninitialisedField(self, 'AmtOrPctg', AmountOrPercentage2Choice, False)

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if value is not None else base_types.UninitialisedField(self, 'PmtTerms', PaymentCodeOrOther1Choice, False)

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = base_types.UninitialisedField(self, 'PmtTerms', PaymentCodeOrOther1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOrPctg', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTerms', type=PaymentCodeOrOther1Choice, min=1, max=1, mutex_group=None, array=False),
	))