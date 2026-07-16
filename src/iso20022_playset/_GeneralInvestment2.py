# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOwnershipType6Code
from . import ActiveCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import DateAndAmount2
from . import GeneralInvestmentAccountType2Choice

class GeneralInvestment2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CurInvstmtAmt", "_EstmtdVal", "_OwnrshTp", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def CurInvstmtAmt(self):
		return self._CurInvstmtAmt

	@CurInvstmtAmt.setter
	def CurInvstmtAmt(self, value):
		self._CurInvstmtAmt = value if value is not None else base_types.UninitialisedField(self, 'CurInvstmtAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@CurInvstmtAmt.deleter
	def CurInvstmtAmt(self):
		del self._CurInvstmtAmt
		self._CurInvstmtAmt = base_types.UninitialisedField(self, 'CurInvstmtAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if value is not None else base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if value is not None else base_types.UninitialisedField(self, 'OwnrshTp', AccountOwnershipType6Code, False)

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = base_types.UninitialisedField(self, 'OwnrshTp', AccountOwnershipType6Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', GeneralInvestmentAccountType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', GeneralInvestmentAccountType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurInvstmtAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshTp', type=AccountOwnershipType6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GeneralInvestmentAccountType2Choice, min=0, max=1, mutex_group=None, array=False),
	))