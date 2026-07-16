# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtInstrument5
from . import Derivative3Choice
from . import ExternalEmissionAllowanceSubProductType1Code
from . import ExternalProductType1Code
from . import FinancialInstrumentContractType1Code
from . import ISINOct2015Identifier
from . import ISODate
from . import MICIdentifier
from . import Max350Text
from . import Max35Text
from . import NonEquityInstrumentReportingClassification1Code

class TransparencyDataReport21(base_types._BaseFieldType):

	__slots__ = ["_Bd", "_Deriv", "_DerivCtrctTp", "_EmssnAllwncTp", "_FinInstrmClssfctn", "_FullNm", "_Id", "_MtrtyDt", "_RptgDt", "_TechRcrdId", "_TradgVn", "_UndrlygInstrmAsstClss"]
	@property
	def Bd(self):
		return self._Bd

	@Bd.setter
	def Bd(self, value):
		self._Bd = value if value is not None else base_types.UninitialisedField(self, 'Bd', DebtInstrument5, False)

	@Bd.deleter
	def Bd(self):
		del self._Bd
		self._Bd = base_types.UninitialisedField(self, 'Bd', DebtInstrument5, False)

	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if value is not None else base_types.UninitialisedField(self, 'Deriv', Derivative3Choice, False)

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = base_types.UninitialisedField(self, 'Deriv', Derivative3Choice, False)

	@property
	def DerivCtrctTp(self):
		return self._DerivCtrctTp

	@DerivCtrctTp.setter
	def DerivCtrctTp(self, value):
		self._DerivCtrctTp = value if value is not None else base_types.UninitialisedField(self, 'DerivCtrctTp', FinancialInstrumentContractType1Code, False)

	@DerivCtrctTp.deleter
	def DerivCtrctTp(self):
		del self._DerivCtrctTp
		self._DerivCtrctTp = base_types.UninitialisedField(self, 'DerivCtrctTp', FinancialInstrumentContractType1Code, False)

	@property
	def EmssnAllwncTp(self):
		return self._EmssnAllwncTp

	@EmssnAllwncTp.setter
	def EmssnAllwncTp(self, value):
		self._EmssnAllwncTp = value if value is not None else base_types.UninitialisedField(self, 'EmssnAllwncTp', ExternalEmissionAllowanceSubProductType1Code, False)

	@EmssnAllwncTp.deleter
	def EmssnAllwncTp(self):
		del self._EmssnAllwncTp
		self._EmssnAllwncTp = base_types.UninitialisedField(self, 'EmssnAllwncTp', ExternalEmissionAllowanceSubProductType1Code, False)

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmClssfctn', NonEquityInstrumentReportingClassification1Code, False)

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = base_types.UninitialisedField(self, 'FinInstrmClssfctn', NonEquityInstrumentReportingClassification1Code, False)

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if value is not None else base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if value is not None else base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@property
	def UndrlygInstrmAsstClss(self):
		return self._UndrlygInstrmAsstClss

	@UndrlygInstrmAsstClss.setter
	def UndrlygInstrmAsstClss(self, value):
		self._UndrlygInstrmAsstClss = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrmAsstClss', ExternalProductType1Code, False)

	@UndrlygInstrmAsstClss.deleter
	def UndrlygInstrmAsstClss(self):
		del self._UndrlygInstrmAsstClss
		self._UndrlygInstrmAsstClss = base_types.UninitialisedField(self, 'UndrlygInstrmAsstClss', ExternalProductType1Code, False)

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