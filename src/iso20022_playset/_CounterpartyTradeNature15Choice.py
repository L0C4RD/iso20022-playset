# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstitutionSector1
from . import NoReasonCode
from . import NonFinancialInstitutionSector10

class CounterpartyTradeNature15Choice(base_types._BaseFieldType):

	__slots__ = ["_CntrlCntrPty", "_FI", "_NFI", "_Othr"]
	@property
	def CntrlCntrPty(self):
		return self._CntrlCntrPty

	@CntrlCntrPty.setter
	def CntrlCntrPty(self, value):
		self._CntrlCntrPty = value if value is not None else base_types.UninitialisedField(self, 'CntrlCntrPty', NoReasonCode, False)

	@CntrlCntrPty.deleter
	def CntrlCntrPty(self):
		del self._CntrlCntrPty
		self._CntrlCntrPty = base_types.UninitialisedField(self, 'CntrlCntrPty', NoReasonCode, False)

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if value is not None else base_types.UninitialisedField(self, 'FI', FinancialInstitutionSector1, False)

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = base_types.UninitialisedField(self, 'FI', FinancialInstitutionSector1, False)

	@property
	def NFI(self):
		return self._NFI

	@NFI.setter
	def NFI(self, value):
		self._NFI = value if value is not None else base_types.UninitialisedField(self, 'NFI', NonFinancialInstitutionSector10, False)

	@NFI.deleter
	def NFI(self):
		del self._NFI
		self._NFI = base_types.UninitialisedField(self, 'NFI', NonFinancialInstitutionSector10, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', NoReasonCode, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrlCntrPty', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitutionSector1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NFI', type=NonFinancialInstitutionSector10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))