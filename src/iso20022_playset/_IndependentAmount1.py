# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._IndependentAmountConventionType1Code import IndependentAmountConventionType1Code

class IndependentAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cnvntn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Cnvntn(self):
		return self._Cnvntn

	@Cnvntn.setter
	def Cnvntn(self, value):
		self._Cnvntn = value if type(value) != base_types.auto else self.make_default("Cnvntn")

	@Cnvntn.deleter
	def Cnvntn(self):
		del self._Cnvntn
		self._Cnvntn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnvntn', type=IndependentAmountConventionType1Code, min=1, max=1, mutex_group=None, array=False),
	))