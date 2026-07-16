# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import IndependentAmountConventionType1Code

class IndependentAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cnvntn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Cnvntn(self):
		return self._Cnvntn

	@Cnvntn.setter
	def Cnvntn(self, value):
		self._Cnvntn = value if value is not None else base_types.UninitialisedField(self, 'Cnvntn', IndependentAmountConventionType1Code, False)

	@Cnvntn.deleter
	def Cnvntn(self):
		del self._Cnvntn
		self._Cnvntn = base_types.UninitialisedField(self, 'Cnvntn', IndependentAmountConventionType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnvntn', type=IndependentAmountConventionType1Code, min=1, max=1, mutex_group=None, array=False),
	))