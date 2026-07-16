# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstitutionIdentification10
from . import Max35Text
from . import PartyIdentification113

class Cheque9(base_types._BaseFieldType):

	__slots__ = ["_DrweeId", "_DrwrId", "_Nb", "_PyeeId"]
	@property
	def DrweeId(self):
		return self._DrweeId

	@DrweeId.setter
	def DrweeId(self, value):
		self._DrweeId = value if value is not None else base_types.UninitialisedField(self, 'DrweeId', FinancialInstitutionIdentification10, False)

	@DrweeId.deleter
	def DrweeId(self):
		del self._DrweeId
		self._DrweeId = base_types.UninitialisedField(self, 'DrweeId', FinancialInstitutionIdentification10, False)

	@property
	def DrwrId(self):
		return self._DrwrId

	@DrwrId.setter
	def DrwrId(self, value):
		self._DrwrId = value if value is not None else base_types.UninitialisedField(self, 'DrwrId', PartyIdentification113, False)

	@DrwrId.deleter
	def DrwrId(self):
		del self._DrwrId
		self._DrwrId = base_types.UninitialisedField(self, 'DrwrId', PartyIdentification113, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def PyeeId(self):
		return self._PyeeId

	@PyeeId.setter
	def PyeeId(self, value):
		self._PyeeId = value if value is not None else base_types.UninitialisedField(self, 'PyeeId', PartyIdentification113, False)

	@PyeeId.deleter
	def PyeeId(self):
		del self._PyeeId
		self._PyeeId = base_types.UninitialisedField(self, 'PyeeId', PartyIdentification113, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrweeId', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwrId', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeId', type=PartyIdentification113, min=1, max=1, mutex_group=None, array=False),
	))