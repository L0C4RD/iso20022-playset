# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BilateralLimit4
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccountType2Choice
from . import CashBalance13
from . import Limit5
from . import Max70Text
from . import PartyIdentification272
from . import ProxyAccountIdentification1
from . import StandingOrder11

class CashAccountData1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CurBilLmt", "_CurMulLmt", "_MulBal", "_Nm", "_Ownr", "_Prxy", "_StgOrdr", "_Svcr", "_Tp"]
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
	def CurBilLmt(self):
		return self._CurBilLmt

	@CurBilLmt.setter
	def CurBilLmt(self, value):
		self._CurBilLmt = value if value is not None else base_types.UninitialisedField(self, 'CurBilLmt', BilateralLimit4, True)

	@CurBilLmt.deleter
	def CurBilLmt(self):
		del self._CurBilLmt
		self._CurBilLmt = base_types.UninitialisedField(self, 'CurBilLmt', BilateralLimit4, True)

	@property
	def CurMulLmt(self):
		return self._CurMulLmt

	@CurMulLmt.setter
	def CurMulLmt(self, value):
		self._CurMulLmt = value if value is not None else base_types.UninitialisedField(self, 'CurMulLmt', Limit5, False)

	@CurMulLmt.deleter
	def CurMulLmt(self):
		del self._CurMulLmt
		self._CurMulLmt = base_types.UninitialisedField(self, 'CurMulLmt', Limit5, False)

	@property
	def MulBal(self):
		return self._MulBal

	@MulBal.setter
	def MulBal(self, value):
		self._MulBal = value if value is not None else base_types.UninitialisedField(self, 'MulBal', CashBalance13, True)

	@MulBal.deleter
	def MulBal(self):
		del self._MulBal
		self._MulBal = base_types.UninitialisedField(self, 'MulBal', CashBalance13, True)

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
		self._Ownr = value if value is not None else base_types.UninitialisedField(self, 'Ownr', PartyIdentification272, False)

	@Ownr.deleter
	def Ownr(self):
		del self._Ownr
		self._Ownr = base_types.UninitialisedField(self, 'Ownr', PartyIdentification272, False)

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if value is not None else base_types.UninitialisedField(self, 'Prxy', ProxyAccountIdentification1, False)

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = base_types.UninitialisedField(self, 'Prxy', ProxyAccountIdentification1, False)

	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if value is not None else base_types.UninitialisedField(self, 'StgOrdr', StandingOrder11, True)

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = base_types.UninitialisedField(self, 'StgOrdr', StandingOrder11, True)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification8, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CashAccountType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CashAccountType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurBilLmt', type=BilateralLimit4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurMulLmt', type=Limit5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulBal', type=CashBalance13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=ProxyAccountIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdr', type=StandingOrder11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Svcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CashAccountType2Choice, min=0, max=1, mutex_group=None, array=False),
	))