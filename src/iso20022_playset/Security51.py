import base_types
import AmountAndDirection53
import SecuritiesTransactionPrice19Choice
import CollateralQualityType1Code
import TrueFalseIndicator
import SecuritiesLendingType3Choice
import CFIOct2015Identifier
import SecurityIssuer4
import ISODate
import ISINOct2015Identifier
import QuantityNominalValue2Choice

class Security51(base_types._BaseFieldType):

	__slots__ = ["_AvlblForCollReuse", "_Id", "_ExclsvArrgmnt", "_ClssfctnTp", "_Issr", "_Qlty", "_UnitPric", "_QtyOrNmnlVal", "_Tp", "_Mtrty", "_MktVal"]
	@property
	def AvlblForCollReuse(self):
		return self._AvlblForCollReuse

	@AvlblForCollReuse.setter
	def AvlblForCollReuse(self, value):
		self._AvlblForCollReuse = value if type(value) != auto else self.make_default("AvlblForCollReuse")

	@AvlblForCollReuse.deleter
	def AvlblForCollReuse(self):
		del self._AvlblForCollReuse
		self._AvlblForCollReuse = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ExclsvArrgmnt(self):
		return self._ExclsvArrgmnt

	@ExclsvArrgmnt.setter
	def ExclsvArrgmnt(self, value):
		self._ExclsvArrgmnt = value if type(value) != auto else self.make_default("ExclsvArrgmnt")

	@ExclsvArrgmnt.deleter
	def ExclsvArrgmnt(self):
		del self._ExclsvArrgmnt
		self._ExclsvArrgmnt = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def QtyOrNmnlVal(self):
		return self._QtyOrNmnlVal

	@QtyOrNmnlVal.setter
	def QtyOrNmnlVal(self, value):
		self._QtyOrNmnlVal = value if type(value) != auto else self.make_default("QtyOrNmnlVal")

	@QtyOrNmnlVal.deleter
	def QtyOrNmnlVal(self):
		del self._QtyOrNmnlVal
		self._QtyOrNmnlVal = None

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
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblForCollReuse', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsvArrgmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=SecurityIssuer4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlty', type=CollateralQualityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=SecuritiesTransactionPrice19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyOrNmnlVal', type=QuantityNominalValue2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SecuritiesLendingType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mtrty', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
	))

