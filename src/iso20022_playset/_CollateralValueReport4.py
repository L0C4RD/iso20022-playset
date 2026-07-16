# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import CollateralValueReportOrError6Choice
from . import PartyIdentification136
from . import SystemPartyIdentification11
from . import SystemPartyIdentification8

class CollateralValueReport4(base_types._BaseFieldType):

	__slots__ = ["_CollValRpt", "_CshAcct", "_CshAcctOwnr", "_CshAcctSvcr", "_SctiesAcctOwnr", "_SctiesAcctSvcr"]
	@property
	def CollValRpt(self):
		return self._CollValRpt

	@CollValRpt.setter
	def CollValRpt(self, value):
		self._CollValRpt = value if value is not None else base_types.UninitialisedField(self, 'CollValRpt', CollateralValueReportOrError6Choice, True)

	@CollValRpt.deleter
	def CollValRpt(self):
		del self._CollValRpt
		self._CollValRpt = base_types.UninitialisedField(self, 'CollValRpt', CollateralValueReportOrError6Choice, True)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccount40, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccount40, False)

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification11, False)

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification11, False)

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
		base_types.FieldEntry(name='CollValRpt', type=CollateralValueReportOrError6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))