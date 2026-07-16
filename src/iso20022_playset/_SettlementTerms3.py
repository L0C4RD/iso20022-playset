# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount24
from . import FinancialInstitutionIdentification4Choice

class SettlementTerms3(base_types._BaseFieldType):

	__slots__ = ["_CdtrAcct", "_CdtrAgt"]
	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount24, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount24, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', FinancialInstitutionIdentification4Choice, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', FinancialInstitutionIdentification4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=FinancialInstitutionIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
	))