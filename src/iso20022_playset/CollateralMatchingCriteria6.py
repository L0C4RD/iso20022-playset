import base_types
import SecurityCommodityCash4
import CompareDate3
import CompareSecurityIdentification4
import CompareTrueFalseIndicator3

class CollateralMatchingCriteria6(base_types._BaseFieldType):

	__slots__ = ["_CollValDt", "_NetXpsrCollstnInd", "_BsktIdr", "_UncollsdFlg", "_AsstTp"]
	@property
	def CollValDt(self):
		return self._CollValDt

	@CollValDt.setter
	def CollValDt(self, value):
		self._CollValDt = value if type(value) != auto else self.make_default("CollValDt")

	@CollValDt.deleter
	def CollValDt(self):
		del self._CollValDt
		self._CollValDt = None

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
	def BsktIdr(self):
		return self._BsktIdr

	@BsktIdr.setter
	def BsktIdr(self, value):
		self._BsktIdr = value if type(value) != auto else self.make_default("BsktIdr")

	@BsktIdr.deleter
	def BsktIdr(self):
		del self._BsktIdr
		self._BsktIdr = None

	@property
	def UncollsdFlg(self):
		return self._UncollsdFlg

	@UncollsdFlg.setter
	def UncollsdFlg(self, value):
		self._UncollsdFlg = value if type(value) != auto else self.make_default("UncollsdFlg")

	@UncollsdFlg.deleter
	def UncollsdFlg(self):
		del self._UncollsdFlg
		self._UncollsdFlg = None

	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollValDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdr', type=CompareSecurityIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UncollsdFlg', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstTp', type=SecurityCommodityCash4, min=0, max=1, mutex_group=None, array=False),
	))

