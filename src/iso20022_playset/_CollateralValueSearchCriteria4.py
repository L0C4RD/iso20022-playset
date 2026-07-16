# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveOrHistoricCurrencyCode
from . import BranchAndFinancialInstitutionIdentification8
from . import PartyIdentification136
from . import SecurityIdentification19
from . import SystemPartyIdentification8

class CollateralValueSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CshAcctId", "_CshAcctOwnr", "_CshAcctSvcr", "_FinInstrmId", "_SctiesAcctOwnr", "_SctiesAcctSvcr"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, True)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, True)

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification8, False)

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification8, False)

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = base_types.UninitialisedField(self, 'CshAcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, True)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, True)

	@property
	def SctiesAcctOwnr(self):
		return self._SctiesAcctOwnr

	@SctiesAcctOwnr.setter
	def SctiesAcctOwnr(self, value):
		self._SctiesAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctOwnr', SystemPartyIdentification8, False)

	@SctiesAcctOwnr.deleter
	def SctiesAcctOwnr(self):
		del self._SctiesAcctOwnr
		self._SctiesAcctOwnr = base_types.UninitialisedField(self, 'SctiesAcctOwnr', SystemPartyIdentification8, False)

	@property
	def SctiesAcctSvcr(self):
		return self._SctiesAcctSvcr

	@SctiesAcctSvcr.setter
	def SctiesAcctSvcr(self, value):
		self._SctiesAcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctSvcr', PartyIdentification136, False)

	@SctiesAcctSvcr.deleter
	def SctiesAcctSvcr(self):
		del self._SctiesAcctSvcr
		self._SctiesAcctSvcr = base_types.UninitialisedField(self, 'SctiesAcctSvcr', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))