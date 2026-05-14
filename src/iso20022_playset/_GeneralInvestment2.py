# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountOwnershipType6Code import AccountOwnershipType6Code
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._AdditionalInformation15 import AdditionalInformation15
from ._DateAndAmount2 import DateAndAmount2
from ._GeneralInvestmentAccountType2Choice import GeneralInvestmentAccountType2Choice

class GeneralInvestment2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CurInvstmtAmt", "_EstmtdVal", "_OwnrshTp", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CurInvstmtAmt(self):
		return self._CurInvstmtAmt

	@CurInvstmtAmt.setter
	def CurInvstmtAmt(self, value):
		self._CurInvstmtAmt = value if type(value) != base_types.auto else self.make_default("CurInvstmtAmt")

	@CurInvstmtAmt.deleter
	def CurInvstmtAmt(self):
		del self._CurInvstmtAmt
		self._CurInvstmtAmt = None

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if type(value) != base_types.auto else self.make_default("EstmtdVal")

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = None

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if type(value) != base_types.auto else self.make_default("OwnrshTp")

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurInvstmtAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshTp', type=AccountOwnershipType6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GeneralInvestmentAccountType2Choice, min=0, max=1, mutex_group=None, array=False),
	))