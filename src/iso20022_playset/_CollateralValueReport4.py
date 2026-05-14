# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._CollateralValueReportOrError6Choice import CollateralValueReportOrError6Choice
from ._PartyIdentification136 import PartyIdentification136
from ._SystemPartyIdentification11 import SystemPartyIdentification11
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class CollateralValueReport4(base_types._BaseFieldType):

	__slots__ = ["_CollValRpt", "_CshAcct", "_CshAcctOwnr", "_CshAcctSvcr", "_SctiesAcctOwnr", "_SctiesAcctSvcr"]
	@property
	def CollValRpt(self):
		return self._CollValRpt

	@CollValRpt.setter
	def CollValRpt(self, value):
		self._CollValRpt = value if type(value) != base_types.auto else self.make_default("CollValRpt")

	@CollValRpt.deleter
	def CollValRpt(self):
		del self._CollValRpt
		self._CollValRpt = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != base_types.auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def SctiesAcctOwnr(self):
		return self._SctiesAcctOwnr

	@SctiesAcctOwnr.setter
	def SctiesAcctOwnr(self, value):
		self._SctiesAcctOwnr = value if type(value) != base_types.auto else self.make_default("SctiesAcctOwnr")

	@SctiesAcctOwnr.deleter
	def SctiesAcctOwnr(self):
		del self._SctiesAcctOwnr
		self._SctiesAcctOwnr = None

	@property
	def SctiesAcctSvcr(self):
		return self._SctiesAcctSvcr

	@SctiesAcctSvcr.setter
	def SctiesAcctSvcr(self, value):
		self._SctiesAcctSvcr = value if type(value) != base_types.auto else self.make_default("SctiesAcctSvcr")

	@SctiesAcctSvcr.deleter
	def SctiesAcctSvcr(self):
		del self._SctiesAcctSvcr
		self._SctiesAcctSvcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollValRpt', type=CollateralValueReportOrError6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))