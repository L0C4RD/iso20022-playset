# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import CFIOct2015Identifier
from . import CollateralQualityType1Code
from . import ISINOct2015Identifier
from . import ISODate
from . import PercentageRate
from . import QuantityNominalValue2Choice
from . import SecuritiesLendingType3Choice
from . import SecuritiesTransactionPrice19Choice
from . import SecurityIssuer4
from . import TrueFalseIndicator

class Security52(base_types._BaseFieldType):

	__slots__ = ["_AvlblForCollReuse", "_ClssfctnTp", "_ExclsvArrgmnt", "_HrcutOrMrgn", "_Id", "_Issr", "_MktVal", "_Mtrty", "_Qlty", "_QtyOrNmnlVal", "_Tp", "_UnitPric"]
	@property
	def AvlblForCollReuse(self):
		return self._AvlblForCollReuse

	@AvlblForCollReuse.setter
	def AvlblForCollReuse(self, value):
		self._AvlblForCollReuse = value if value is not None else base_types.UninitialisedField(self, 'AvlblForCollReuse', TrueFalseIndicator, False)

	@AvlblForCollReuse.deleter
	def AvlblForCollReuse(self):
		del self._AvlblForCollReuse
		self._AvlblForCollReuse = base_types.UninitialisedField(self, 'AvlblForCollReuse', TrueFalseIndicator, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', CFIOct2015Identifier, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', CFIOct2015Identifier, False)

	@property
	def ExclsvArrgmnt(self):
		return self._ExclsvArrgmnt

	@ExclsvArrgmnt.setter
	def ExclsvArrgmnt(self, value):
		self._ExclsvArrgmnt = value if value is not None else base_types.UninitialisedField(self, 'ExclsvArrgmnt', TrueFalseIndicator, False)

	@ExclsvArrgmnt.deleter
	def ExclsvArrgmnt(self):
		del self._ExclsvArrgmnt
		self._ExclsvArrgmnt = base_types.UninitialisedField(self, 'ExclsvArrgmnt', TrueFalseIndicator, False)

	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if value is not None else base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

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
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', SecurityIssuer4, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', SecurityIssuer4, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@property
	def Mtrty(self):
		return self._Mtrty

	@Mtrty.setter
	def Mtrty(self, value):
		self._Mtrty = value if value is not None else base_types.UninitialisedField(self, 'Mtrty', ISODate, False)

	@Mtrty.deleter
	def Mtrty(self):
		del self._Mtrty
		self._Mtrty = base_types.UninitialisedField(self, 'Mtrty', ISODate, False)

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
	def QtyOrNmnlVal(self):
		return self._QtyOrNmnlVal

	@QtyOrNmnlVal.setter
	def QtyOrNmnlVal(self, value):
		self._QtyOrNmnlVal = value if value is not None else base_types.UninitialisedField(self, 'QtyOrNmnlVal', QuantityNominalValue2Choice, False)

	@QtyOrNmnlVal.deleter
	def QtyOrNmnlVal(self):
		del self._QtyOrNmnlVal
		self._QtyOrNmnlVal = base_types.UninitialisedField(self, 'QtyOrNmnlVal', QuantityNominalValue2Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SecuritiesLendingType3Choice, True)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SecuritiesLendingType3Choice, True)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', SecuritiesTransactionPrice19Choice, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', SecuritiesTransactionPrice19Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblForCollReuse', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsvArrgmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrcutOrMrgn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=SecurityIssuer4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrty', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlty', type=CollateralQualityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyOrNmnlVal', type=QuantityNominalValue2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SecuritiesLendingType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnitPric', type=SecuritiesTransactionPrice19Choice, min=0, max=1, mutex_group=None, array=False),
	))