# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSubLevel14
from . import AggregateHoldingBalance2
from . import AggregateHoldingBalance3
from . import BeneficialOwner2
from . import PartyIdentification100
from . import SecuritiesAccount19
from . import SupplementaryData1

class AccountSubLevel13(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_AcctSubLvl4", "_AcctSubLvl4Diff", "_AcctSvcr", "_BalDtls", "_BnfclOwnr", "_SplmtryData"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', SecuritiesAccount19, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', SecuritiesAccount19, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification100, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification100, False)

	@property
	def AcctSubLvl4(self):
		return self._AcctSubLvl4

	@AcctSubLvl4.setter
	def AcctSubLvl4(self, value):
		self._AcctSubLvl4 = value if value is not None else base_types.UninitialisedField(self, 'AcctSubLvl4', AccountSubLevel14, True)

	@AcctSubLvl4.deleter
	def AcctSubLvl4(self):
		del self._AcctSubLvl4
		self._AcctSubLvl4 = base_types.UninitialisedField(self, 'AcctSubLvl4', AccountSubLevel14, True)

	@property
	def AcctSubLvl4Diff(self):
		return self._AcctSubLvl4Diff

	@AcctSubLvl4Diff.setter
	def AcctSubLvl4Diff(self, value):
		self._AcctSubLvl4Diff = value if value is not None else base_types.UninitialisedField(self, 'AcctSubLvl4Diff', AggregateHoldingBalance2, True)

	@AcctSubLvl4Diff.deleter
	def AcctSubLvl4Diff(self):
		del self._AcctSubLvl4Diff
		self._AcctSubLvl4Diff = base_types.UninitialisedField(self, 'AcctSubLvl4Diff', AggregateHoldingBalance2, True)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification100, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification100, False)

	@property
	def BalDtls(self):
		return self._BalDtls

	@BalDtls.setter
	def BalDtls(self, value):
		self._BalDtls = value if value is not None else base_types.UninitialisedField(self, 'BalDtls', AggregateHoldingBalance3, True)

	@BalDtls.deleter
	def BalDtls(self):
		del self._BalDtls
		self._BalDtls = base_types.UninitialisedField(self, 'BalDtls', AggregateHoldingBalance3, True)

	@property
	def BnfclOwnr(self):
		return self._BnfclOwnr

	@BnfclOwnr.setter
	def BnfclOwnr(self, value):
		self._BnfclOwnr = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnr', BeneficialOwner2, True)

	@BnfclOwnr.deleter
	def BnfclOwnr(self):
		del self._BnfclOwnr
		self._BnfclOwnr = base_types.UninitialisedField(self, 'BnfclOwnr', BeneficialOwner2, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSubLvl4', type=AccountSubLevel14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSubLvl4Diff', type=AggregateHoldingBalance2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDtls', type=AggregateHoldingBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfclOwnr', type=BeneficialOwner2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))