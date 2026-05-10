from . import base_types
from ._CompareUnitPrice6 import CompareUnitPrice6
from ._CompareTrueFalseIndicator3 import CompareTrueFalseIndicator3
from ._CompareISINIdentifier4 import CompareISINIdentifier4
from ._ComparePercentageRate3 import ComparePercentageRate3
from ._CompareAmountAndDirection2 import CompareAmountAndDirection2
from ._CompareCollateralQualityType3 import CompareCollateralQualityType3
from ._CompareDecimalNumber3 import CompareDecimalNumber3
from ._CompareCountryCode3 import CompareCountryCode3
from ._CompareCFIIdentifier3 import CompareCFIIdentifier3
from ._CompareSecuritiesLendingType3 import CompareSecuritiesLendingType3
from ._CompareOrganisationIdentification6 import CompareOrganisationIdentification6
from ._CompareDate3 import CompareDate3

class Security48(base_types._BaseFieldType):

	__slots__ = ["_UnitPric", "_IssrCtry", "_AvlblForCollReuse", "_Tp", "_IssrId", "_HrcutOrMrgn", "_NmnlVal", "_Qlty", "_Mtrty", "_Id", "_ClssfctnTp", "_Qty", "_MktVal", "_ExclsvArrgmnt"]
	@property
	def AvlblForCollReuse(self):
		return self._AvlblForCollReuse

	@AvlblForCollReuse.setter
	def AvlblForCollReuse(self, value):
		self._AvlblForCollReuse = value if type(value) != base_types.auto else self.make_default("AvlblForCollReuse")

	@AvlblForCollReuse.deleter
	def AvlblForCollReuse(self):
		del self._AvlblForCollReuse
		self._AvlblForCollReuse = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def ExclsvArrgmnt(self):
		return self._ExclsvArrgmnt

	@ExclsvArrgmnt.setter
	def ExclsvArrgmnt(self, value):
		self._ExclsvArrgmnt = value if type(value) != base_types.auto else self.make_default("ExclsvArrgmnt")

	@ExclsvArrgmnt.deleter
	def ExclsvArrgmnt(self):
		del self._ExclsvArrgmnt
		self._ExclsvArrgmnt = None

	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if type(value) != base_types.auto else self.make_default("HrcutOrMrgn")

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = None

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
	def IssrCtry(self):
		return self._IssrCtry

	@IssrCtry.setter
	def IssrCtry(self, value):
		self._IssrCtry = value if type(value) != base_types.auto else self.make_default("IssrCtry")

	@IssrCtry.deleter
	def IssrCtry(self):
		del self._IssrCtry
		self._IssrCtry = None

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if type(value) != base_types.auto else self.make_default("IssrId")

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def Mtrty(self):
		return self._Mtrty

	@Mtrty.setter
	def Mtrty(self, value):
		self._Mtrty = value if type(value) != base_types.auto else self.make_default("Mtrty")

	@Mtrty.deleter
	def Mtrty(self):
		del self._Mtrty
		self._Mtrty = None

	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if type(value) != base_types.auto else self.make_default("NmnlVal")

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = None

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if type(value) != base_types.auto else self.make_default("Qlty")

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

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

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblForCollReuse', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=CompareCFIIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsvArrgmnt', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrcutOrMrgn', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=CompareISINIdentifier4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCtry', type=CompareCountryCode3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrId', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrty', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmnlVal', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlty', type=CompareCollateralQualityType3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CompareSecuritiesLendingType3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnitPric', type=CompareUnitPrice6, min=0, max=1, mutex_group=None, array=False),
	))

