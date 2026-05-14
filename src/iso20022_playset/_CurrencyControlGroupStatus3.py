# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ISODateTime import ISODateTime
from ._OriginalMessage7 import OriginalMessage7
from ._Period4Choice import Period4Choice
from ._StatisticalReportingStatus1Code import StatisticalReportingStatus1Code
from ._TradeParty6 import TradeParty6
from ._ValidationStatusReason3 import ValidationStatusReason3

class CurrencyControlGroupStatus3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlRefs", "_RegnAgt", "_RptgPrd", "_RptgPty", "_Sts", "_StsDtTm", "_StsRsn"]
	@property
	def OrgnlRefs(self):
		return self._OrgnlRefs

	@OrgnlRefs.setter
	def OrgnlRefs(self, value):
		self._OrgnlRefs = value if type(value) != base_types.auto else self.make_default("OrgnlRefs")

	@OrgnlRefs.deleter
	def OrgnlRefs(self):
		del self._OrgnlRefs
		self._OrgnlRefs = None

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != base_types.auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != base_types.auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if type(value) != base_types.auto else self.make_default("StsDtTm")

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlRefs', type=OriginalMessage7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=StatisticalReportingStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=ValidationStatusReason3, min=0, max=None, mutex_group=None, array=True),
	))