# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity25Choice
from . import TrueFalseIndicator

class MinimumExecutable1(base_types._BaseFieldType):

	__slots__ = ["_FrstExctnOnly", "_Sz"]
	@property
	def FrstExctnOnly(self):
		return self._FrstExctnOnly

	@FrstExctnOnly.setter
	def FrstExctnOnly(self, value):
		self._FrstExctnOnly = value if value is not None else base_types.UninitialisedField(self, 'FrstExctnOnly', TrueFalseIndicator, False)

	@FrstExctnOnly.deleter
	def FrstExctnOnly(self):
		del self._FrstExctnOnly
		self._FrstExctnOnly = base_types.UninitialisedField(self, 'FrstExctnOnly', TrueFalseIndicator, False)

	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if value is not None else base_types.UninitialisedField(self, 'Sz', FinancialInstrumentQuantity25Choice, False)

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = base_types.UninitialisedField(self, 'Sz', FinancialInstrumentQuantity25Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstExctnOnly', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sz', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
	))