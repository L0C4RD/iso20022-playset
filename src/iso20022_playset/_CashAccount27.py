# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveOrHistoricCurrencyCode
from . import BranchAndFinancialInstitutionIdentification5
from . import CashAccountType2
from . import Max70Text
from . import PartyIdentification41

class CashAccount27(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Id", "_Nm", "_Ownr", "_Svcr", "_Tp"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentification4Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentification4Choice, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@property
	def Ownr(self):
		return self._Ownr

	@Ownr.setter
	def Ownr(self, value):
		self._Ownr = value if value is not None else base_types.UninitialisedField(self, 'Ownr', PartyIdentification41, False)

	@Ownr.deleter
	def Ownr(self):
		del self._Ownr
		self._Ownr = base_types.UninitialisedField(self, 'Ownr', PartyIdentification41, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification5, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification5, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CashAccountType2, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CashAccountType2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownr', type=PartyIdentification41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=BranchAndFinancialInstitutionIdentification5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CashAccountType2, min=0, max=1, mutex_group=None, array=False),
	))