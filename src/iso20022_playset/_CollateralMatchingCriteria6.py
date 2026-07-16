# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareDate3
from . import CompareSecurityIdentification4
from . import CompareTrueFalseIndicator3
from . import SecurityCommodityCash4

class CollateralMatchingCriteria6(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_BsktIdr", "_CollValDt", "_NetXpsrCollstnInd", "_UncollsdFlg"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if value is not None else base_types.UninitialisedField(self, 'AsstTp', SecurityCommodityCash4, False)

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = base_types.UninitialisedField(self, 'AsstTp', SecurityCommodityCash4, False)

	@property
	def BsktIdr(self):
		return self._BsktIdr

	@BsktIdr.setter
	def BsktIdr(self, value):
		self._BsktIdr = value if value is not None else base_types.UninitialisedField(self, 'BsktIdr', CompareSecurityIdentification4, False)

	@BsktIdr.deleter
	def BsktIdr(self):
		del self._BsktIdr
		self._BsktIdr = base_types.UninitialisedField(self, 'BsktIdr', CompareSecurityIdentification4, False)

	@property
	def CollValDt(self):
		return self._CollValDt

	@CollValDt.setter
	def CollValDt(self, value):
		self._CollValDt = value if value is not None else base_types.UninitialisedField(self, 'CollValDt', CompareDate3, False)

	@CollValDt.deleter
	def CollValDt(self):
		del self._CollValDt
		self._CollValDt = base_types.UninitialisedField(self, 'CollValDt', CompareDate3, False)

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if value is not None else base_types.UninitialisedField(self, 'NetXpsrCollstnInd', CompareTrueFalseIndicator3, False)

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = base_types.UninitialisedField(self, 'NetXpsrCollstnInd', CompareTrueFalseIndicator3, False)

	@property
	def UncollsdFlg(self):
		return self._UncollsdFlg

	@UncollsdFlg.setter
	def UncollsdFlg(self, value):
		self._UncollsdFlg = value if value is not None else base_types.UninitialisedField(self, 'UncollsdFlg', CompareTrueFalseIndicator3, False)

	@UncollsdFlg.deleter
	def UncollsdFlg(self):
		del self._UncollsdFlg
		self._UncollsdFlg = base_types.UninitialisedField(self, 'UncollsdFlg', CompareTrueFalseIndicator3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=SecurityCommodityCash4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdr', type=CompareSecurityIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollValDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UncollsdFlg', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
	))