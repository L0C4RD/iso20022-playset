# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DebtInstrument5 import DebtInstrument5
from ._Derivative3Choice import Derivative3Choice
from ._ExternalEmissionAllowanceSubProductType1Code import ExternalEmissionAllowanceSubProductType1Code
from ._ExternalProductType1Code import ExternalProductType1Code
from ._FinancialInstrumentContractType1Code import FinancialInstrumentContractType1Code
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._ISODate import ISODate
from ._MICIdentifier import MICIdentifier
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._NonEquityInstrumentReportingClassification1Code import NonEquityInstrumentReportingClassification1Code

class TransparencyDataReport21(base_types._BaseFieldType):

	__slots__ = ["_Bd", "_Deriv", "_DerivCtrctTp", "_EmssnAllwncTp", "_FinInstrmClssfctn", "_FullNm", "_Id", "_MtrtyDt", "_RptgDt", "_TechRcrdId", "_TradgVn", "_UndrlygInstrmAsstClss"]
	@property
	def Bd(self):
		return self._Bd

	@Bd.setter
	def Bd(self, value):
		self._Bd = value if type(value) != base_types.auto else self.make_default("Bd")

	@Bd.deleter
	def Bd(self):
		del self._Bd
		self._Bd = None

	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if type(value) != base_types.auto else self.make_default("Deriv")

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = None

	@property
	def DerivCtrctTp(self):
		return self._DerivCtrctTp

	@DerivCtrctTp.setter
	def DerivCtrctTp(self, value):
		self._DerivCtrctTp = value if type(value) != base_types.auto else self.make_default("DerivCtrctTp")

	@DerivCtrctTp.deleter
	def DerivCtrctTp(self):
		del self._DerivCtrctTp
		self._DerivCtrctTp = None

	@property
	def EmssnAllwncTp(self):
		return self._EmssnAllwncTp

	@EmssnAllwncTp.setter
	def EmssnAllwncTp(self, value):
		self._EmssnAllwncTp = value if type(value) != base_types.auto else self.make_default("EmssnAllwncTp")

	@EmssnAllwncTp.deleter
	def EmssnAllwncTp(self):
		del self._EmssnAllwncTp
		self._EmssnAllwncTp = None

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if type(value) != base_types.auto else self.make_default("FinInstrmClssfctn")

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = None

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != base_types.auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != base_types.auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != base_types.auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def UndrlygInstrmAsstClss(self):
		return self._UndrlygInstrmAsstClss

	@UndrlygInstrmAsstClss.setter
	def UndrlygInstrmAsstClss(self, value):
		self._UndrlygInstrmAsstClss = value if type(value) != base_types.auto else self.make_default("UndrlygInstrmAsstClss")

	@UndrlygInstrmAsstClss.deleter
	def UndrlygInstrmAsstClss(self):
		del self._UndrlygInstrmAsstClss
		self._UndrlygInstrmAsstClss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bd', type=DebtInstrument5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Deriv', type=Derivative3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivCtrctTp', type=FinancialInstrumentContractType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmssnAllwncTp', type=ExternalEmissionAllowanceSubProductType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=NonEquityInstrumentReportingClassification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrmAsstClss', type=ExternalProductType1Code, min=0, max=1, mutex_group=None, array=False),
	))