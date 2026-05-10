from . import base_types
import SecuritiesLendingType3Choice
import ReconciliationFlag2
import ReinvestedCashTypeAndAmount2
import CollateralQualityType1Code
import IssuerJurisdiction1Choice
import CollateralType6Code
import TrueFalseIndicator
import ContractTerm6Choice
import ActiveOrHistoricCurrencyCode
import OrganisationIdentification15Choice

class CollateralData33(base_types._BaseFieldType):

	__slots__ = ["_Mtrty", "_TradRpstry", "_IssrJursdctn", "_Qlty", "_CshCollCcy", "_NetXpsrCollstnInd", "_RcncltnFlg", "_RinvstdCsh", "_Tp", "_CmpntTp", "_PricCcy"]
	@property
	def Mtrty(self):
		return self._Mtrty

	@Mtrty.setter
	def Mtrty(self, value):
		self._Mtrty = value if type(value) != auto else self.make_default("Mtrty")

	@Mtrty.deleter
	def Mtrty(self):
		del self._Mtrty
		self._Mtrty = None

	@property
	def TradRpstry(self):
		return self._TradRpstry

	@TradRpstry.setter
	def TradRpstry(self, value):
		self._TradRpstry = value if type(value) != auto else self.make_default("TradRpstry")

	@TradRpstry.deleter
	def TradRpstry(self):
		del self._TradRpstry
		self._TradRpstry = None

	@property
	def IssrJursdctn(self):
		return self._IssrJursdctn

	@IssrJursdctn.setter
	def IssrJursdctn(self, value):
		self._IssrJursdctn = value if type(value) != auto else self.make_default("IssrJursdctn")

	@IssrJursdctn.deleter
	def IssrJursdctn(self):
		del self._IssrJursdctn
		self._IssrJursdctn = None

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if type(value) != auto else self.make_default("Qlty")

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = None

	@property
	def CshCollCcy(self):
		return self._CshCollCcy

	@CshCollCcy.setter
	def CshCollCcy(self, value):
		self._CshCollCcy = value if type(value) != auto else self.make_default("CshCollCcy")

	@CshCollCcy.deleter
	def CshCollCcy(self):
		del self._CshCollCcy
		self._CshCollCcy = None

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if type(value) != auto else self.make_default("NetXpsrCollstnInd")

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = None

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if type(value) != auto else self.make_default("RcncltnFlg")

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = None

	@property
	def RinvstdCsh(self):
		return self._RinvstdCsh

	@RinvstdCsh.setter
	def RinvstdCsh(self, value):
		self._RinvstdCsh = value if type(value) != auto else self.make_default("RinvstdCsh")

	@RinvstdCsh.deleter
	def RinvstdCsh(self):
		del self._RinvstdCsh
		self._RinvstdCsh = None

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
	def CmpntTp(self):
		return self._CmpntTp

	@CmpntTp.setter
	def CmpntTp(self, value):
		self._CmpntTp = value if type(value) != auto else self.make_default("CmpntTp")

	@CmpntTp.deleter
	def CmpntTp(self):
		del self._CmpntTp
		self._CmpntTp = None

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if type(value) != auto else self.make_default("PricCcy")

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtrty', type=ContractTerm6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRpstry', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrJursdctn', type=IssuerJurisdiction1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlty', type=CollateralQualityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCollCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstdCsh', type=ReinvestedCashTypeAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SecuritiesLendingType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpntTp', type=CollateralType6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

