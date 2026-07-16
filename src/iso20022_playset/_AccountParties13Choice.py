# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestmentAccountOwnershipInformation17

class AccountParties13Choice(base_types._BaseFieldType):

	__slots__ = ["_JntOwnr", "_Nmnee", "_PmryOwnr", "_Trstee"]
	@property
	def JntOwnr(self):
		return self._JntOwnr

	@JntOwnr.setter
	def JntOwnr(self, value):
		self._JntOwnr = value if value is not None else base_types.UninitialisedField(self, 'JntOwnr', InvestmentAccountOwnershipInformation17, True)

	@JntOwnr.deleter
	def JntOwnr(self):
		del self._JntOwnr
		self._JntOwnr = base_types.UninitialisedField(self, 'JntOwnr', InvestmentAccountOwnershipInformation17, True)

	@property
	def Nmnee(self):
		return self._Nmnee

	@Nmnee.setter
	def Nmnee(self, value):
		self._Nmnee = value if value is not None else base_types.UninitialisedField(self, 'Nmnee', InvestmentAccountOwnershipInformation17, False)

	@Nmnee.deleter
	def Nmnee(self):
		del self._Nmnee
		self._Nmnee = base_types.UninitialisedField(self, 'Nmnee', InvestmentAccountOwnershipInformation17, False)

	@property
	def PmryOwnr(self):
		return self._PmryOwnr

	@PmryOwnr.setter
	def PmryOwnr(self, value):
		self._PmryOwnr = value if value is not None else base_types.UninitialisedField(self, 'PmryOwnr', InvestmentAccountOwnershipInformation17, False)

	@PmryOwnr.deleter
	def PmryOwnr(self):
		del self._PmryOwnr
		self._PmryOwnr = base_types.UninitialisedField(self, 'PmryOwnr', InvestmentAccountOwnershipInformation17, False)

	@property
	def Trstee(self):
		return self._Trstee

	@Trstee.setter
	def Trstee(self, value):
		self._Trstee = value if value is not None else base_types.UninitialisedField(self, 'Trstee', InvestmentAccountOwnershipInformation17, True)

	@Trstee.deleter
	def Trstee(self):
		del self._Trstee
		self._Trstee = base_types.UninitialisedField(self, 'Trstee', InvestmentAccountOwnershipInformation17, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='JntOwnr', type=InvestmentAccountOwnershipInformation17, min=1, max=5, mutex_group=1, array=True),
		base_types.FieldEntry(name='Nmnee', type=InvestmentAccountOwnershipInformation17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmryOwnr', type=InvestmentAccountOwnershipInformation17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trstee', type=InvestmentAccountOwnershipInformation17, min=1, max=5, mutex_group=1, array=True),
	))