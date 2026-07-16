# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialPartyClassification2Choice
from . import TrueFalseIndicator

class FinancialInstitutionSector1(base_types._BaseFieldType):

	__slots__ = ["_ClrThrshld", "_Sctr"]
	@property
	def ClrThrshld(self):
		return self._ClrThrshld

	@ClrThrshld.setter
	def ClrThrshld(self, value):
		self._ClrThrshld = value if value is not None else base_types.UninitialisedField(self, 'ClrThrshld', TrueFalseIndicator, False)

	@ClrThrshld.deleter
	def ClrThrshld(self):
		del self._ClrThrshld
		self._ClrThrshld = base_types.UninitialisedField(self, 'ClrThrshld', TrueFalseIndicator, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', FinancialPartyClassification2Choice, True)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', FinancialPartyClassification2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrThrshld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=FinancialPartyClassification2Choice, min=1, max=None, mutex_group=None, array=True),
	))