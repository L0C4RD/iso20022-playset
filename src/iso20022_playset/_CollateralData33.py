# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CollateralQualityType1Code
from . import CollateralType6Code
from . import ContractTerm6Choice
from . import IssuerJurisdiction1Choice
from . import OrganisationIdentification15Choice
from . import ReconciliationFlag2
from . import ReinvestedCashTypeAndAmount2
from . import SecuritiesLendingType3Choice
from . import TrueFalseIndicator

class CollateralData33(base_types._BaseFieldType):

	__slots__ = ["_CmpntTp", "_CshCollCcy", "_IssrJursdctn", "_Mtrty", "_NetXpsrCollstnInd", "_PricCcy", "_Qlty", "_RcncltnFlg", "_RinvstdCsh", "_Tp", "_TradRpstry"]
	@property
	def CmpntTp(self):
		return self._CmpntTp

	@CmpntTp.setter
	def CmpntTp(self, value):
		self._CmpntTp = value if value is not None else base_types.UninitialisedField(self, 'CmpntTp', CollateralType6Code, False)

	@CmpntTp.deleter
	def CmpntTp(self):
		del self._CmpntTp
		self._CmpntTp = base_types.UninitialisedField(self, 'CmpntTp', CollateralType6Code, False)

	@property
	def CshCollCcy(self):
		return self._CshCollCcy

	@CshCollCcy.setter
	def CshCollCcy(self, value):
		self._CshCollCcy = value if value is not None else base_types.UninitialisedField(self, 'CshCollCcy', ActiveOrHistoricCurrencyCode, False)

	@CshCollCcy.deleter
	def CshCollCcy(self):
		del self._CshCollCcy
		self._CshCollCcy = base_types.UninitialisedField(self, 'CshCollCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def IssrJursdctn(self):
		return self._IssrJursdctn

	@IssrJursdctn.setter
	def IssrJursdctn(self, value):
		self._IssrJursdctn = value if value is not None else base_types.UninitialisedField(self, 'IssrJursdctn', IssuerJurisdiction1Choice, False)

	@IssrJursdctn.deleter
	def IssrJursdctn(self):
		del self._IssrJursdctn
		self._IssrJursdctn = base_types.UninitialisedField(self, 'IssrJursdctn', IssuerJurisdiction1Choice, False)

	@property
	def Mtrty(self):
		return self._Mtrty

	@Mtrty.setter
	def Mtrty(self, value):
		self._Mtrty = value if value is not None else base_types.UninitialisedField(self, 'Mtrty', ContractTerm6Choice, False)

	@Mtrty.deleter
	def Mtrty(self):
		del self._Mtrty
		self._Mtrty = base_types.UninitialisedField(self, 'Mtrty', ContractTerm6Choice, False)

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if value is not None else base_types.UninitialisedField(self, 'NetXpsrCollstnInd', TrueFalseIndicator, False)

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = base_types.UninitialisedField(self, 'NetXpsrCollstnInd', TrueFalseIndicator, False)

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if value is not None else base_types.UninitialisedField(self, 'PricCcy', ActiveOrHistoricCurrencyCode, False)

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = base_types.UninitialisedField(self, 'PricCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if value is not None else base_types.UninitialisedField(self, 'Qlty', CollateralQualityType1Code, False)

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = base_types.UninitialisedField(self, 'Qlty', CollateralQualityType1Code, False)

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if value is not None else base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

	@property
	def RinvstdCsh(self):
		return self._RinvstdCsh

	@RinvstdCsh.setter
	def RinvstdCsh(self, value):
		self._RinvstdCsh = value if value is not None else base_types.UninitialisedField(self, 'RinvstdCsh', ReinvestedCashTypeAndAmount2, False)

	@RinvstdCsh.deleter
	def RinvstdCsh(self):
		del self._RinvstdCsh
		self._RinvstdCsh = base_types.UninitialisedField(self, 'RinvstdCsh', ReinvestedCashTypeAndAmount2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SecuritiesLendingType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SecuritiesLendingType3Choice, False)

	@property
	def TradRpstry(self):
		return self._TradRpstry

	@TradRpstry.setter
	def TradRpstry(self, value):
		self._TradRpstry = value if value is not None else base_types.UninitialisedField(self, 'TradRpstry', OrganisationIdentification15Choice, False)

	@TradRpstry.deleter
	def TradRpstry(self):
		del self._TradRpstry
		self._TradRpstry = base_types.UninitialisedField(self, 'TradRpstry', OrganisationIdentification15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpntTp', type=CollateralType6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCollCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrJursdctn', type=IssuerJurisdiction1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrty', type=ContractTerm6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlty', type=CollateralQualityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstdCsh', type=ReinvestedCashTypeAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SecuritiesLendingType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRpstry', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))