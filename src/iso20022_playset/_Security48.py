# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection2
from . import CompareCFIIdentifier3
from . import CompareCollateralQualityType3
from . import CompareCountryCode3
from . import CompareDate3
from . import CompareDecimalNumber3
from . import CompareISINIdentifier4
from . import CompareOrganisationIdentification6
from . import ComparePercentageRate3
from . import CompareSecuritiesLendingType3
from . import CompareTrueFalseIndicator3
from . import CompareUnitPrice6

class Security48(base_types._BaseFieldType):

	__slots__ = ["_AvlblForCollReuse", "_ClssfctnTp", "_ExclsvArrgmnt", "_HrcutOrMrgn", "_Id", "_IssrCtry", "_IssrId", "_MktVal", "_Mtrty", "_NmnlVal", "_Qlty", "_Qty", "_Tp", "_UnitPric"]
	@property
	def AvlblForCollReuse(self):
		return self._AvlblForCollReuse

	@AvlblForCollReuse.setter
	def AvlblForCollReuse(self, value):
		self._AvlblForCollReuse = value if value is not None else base_types.UninitialisedField(self, 'AvlblForCollReuse', CompareTrueFalseIndicator3, False)

	@AvlblForCollReuse.deleter
	def AvlblForCollReuse(self):
		del self._AvlblForCollReuse
		self._AvlblForCollReuse = base_types.UninitialisedField(self, 'AvlblForCollReuse', CompareTrueFalseIndicator3, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', CompareCFIIdentifier3, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', CompareCFIIdentifier3, False)

	@property
	def ExclsvArrgmnt(self):
		return self._ExclsvArrgmnt

	@ExclsvArrgmnt.setter
	def ExclsvArrgmnt(self, value):
		self._ExclsvArrgmnt = value if value is not None else base_types.UninitialisedField(self, 'ExclsvArrgmnt', CompareTrueFalseIndicator3, False)

	@ExclsvArrgmnt.deleter
	def ExclsvArrgmnt(self):
		del self._ExclsvArrgmnt
		self._ExclsvArrgmnt = base_types.UninitialisedField(self, 'ExclsvArrgmnt', CompareTrueFalseIndicator3, False)

	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if value is not None else base_types.UninitialisedField(self, 'HrcutOrMrgn', ComparePercentageRate3, False)

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = base_types.UninitialisedField(self, 'HrcutOrMrgn', ComparePercentageRate3, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', CompareISINIdentifier4, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', CompareISINIdentifier4, False)

	@property
	def IssrCtry(self):
		return self._IssrCtry

	@IssrCtry.setter
	def IssrCtry(self, value):
		self._IssrCtry = value if value is not None else base_types.UninitialisedField(self, 'IssrCtry', CompareCountryCode3, False)

	@IssrCtry.deleter
	def IssrCtry(self):
		del self._IssrCtry
		self._IssrCtry = base_types.UninitialisedField(self, 'IssrCtry', CompareCountryCode3, False)

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if value is not None else base_types.UninitialisedField(self, 'IssrId', CompareOrganisationIdentification6, False)

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = base_types.UninitialisedField(self, 'IssrId', CompareOrganisationIdentification6, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', CompareAmountAndDirection2, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', CompareAmountAndDirection2, False)

	@property
	def Mtrty(self):
		return self._Mtrty

	@Mtrty.setter
	def Mtrty(self, value):
		self._Mtrty = value if value is not None else base_types.UninitialisedField(self, 'Mtrty', CompareDate3, False)

	@Mtrty.deleter
	def Mtrty(self):
		del self._Mtrty
		self._Mtrty = base_types.UninitialisedField(self, 'Mtrty', CompareDate3, False)

	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if value is not None else base_types.UninitialisedField(self, 'NmnlVal', CompareAmountAndDirection2, False)

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = base_types.UninitialisedField(self, 'NmnlVal', CompareAmountAndDirection2, False)

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if value is not None else base_types.UninitialisedField(self, 'Qlty', CompareCollateralQualityType3, False)

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = base_types.UninitialisedField(self, 'Qlty', CompareCollateralQualityType3, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', CompareDecimalNumber3, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', CompareDecimalNumber3, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CompareSecuritiesLendingType3, True)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CompareSecuritiesLendingType3, True)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', CompareUnitPrice6, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', CompareUnitPrice6, False)

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