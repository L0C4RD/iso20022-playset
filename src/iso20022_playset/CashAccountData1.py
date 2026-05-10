from . import base_types
import PartyIdentification272
import StandingOrder11
import Limit5
import BranchAndFinancialInstitutionIdentification8
import ProxyAccountIdentification1
import BilateralLimit4
import CashBalance13
import ActiveOrHistoricCurrencyCode
import CashAccountType2Choice
import Max70Text

class CashAccountData1(base_types._BaseFieldType):

	__slots__ = ["_CurMulLmt", "_StgOrdr", "_Ownr", "_CurBilLmt", "_Svcr", "_Prxy", "_MulBal", "_Nm", "_Tp", "_Ccy"]
	@property
	def CurMulLmt(self):
		return self._CurMulLmt

	@CurMulLmt.setter
	def CurMulLmt(self, value):
		self._CurMulLmt = value if type(value) != auto else self.make_default("CurMulLmt")

	@CurMulLmt.deleter
	def CurMulLmt(self):
		del self._CurMulLmt
		self._CurMulLmt = None

	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if type(value) != auto else self.make_default("StgOrdr")

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = None

	@property
	def Ownr(self):
		return self._Ownr

	@Ownr.setter
	def Ownr(self, value):
		self._Ownr = value if type(value) != auto else self.make_default("Ownr")

	@Ownr.deleter
	def Ownr(self):
		del self._Ownr
		self._Ownr = None

	@property
	def CurBilLmt(self):
		return self._CurBilLmt

	@CurBilLmt.setter
	def CurBilLmt(self, value):
		self._CurBilLmt = value if type(value) != auto else self.make_default("CurBilLmt")

	@CurBilLmt.deleter
	def CurBilLmt(self):
		del self._CurBilLmt
		self._CurBilLmt = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def MulBal(self):
		return self._MulBal

	@MulBal.setter
	def MulBal(self, value):
		self._MulBal = value if type(value) != auto else self.make_default("MulBal")

	@MulBal.deleter
	def MulBal(self):
		del self._MulBal
		self._MulBal = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurMulLmt', type=Limit5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdr', type=StandingOrder11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ownr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurBilLmt', type=BilateralLimit4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Svcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=ProxyAccountIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MulBal', type=CashBalance13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CashAccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

