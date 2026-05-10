from . import base_types
import Number
import Frequency20Choice
import UnitsOrAmount1Choice
import YesNoIndicator
import InvestmentFundPlanType1Choice
import AdditionalInformation15

class InvestmentPlanCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_AddtlSbcpt", "_Frqcy", "_AddtlInf", "_PlanTp", "_AddtlSbcptFctn", "_PlanConttn", "_TtlNbOfInstlmts", "_Qty"]
	@property
	def AddtlSbcpt(self):
		return self._AddtlSbcpt

	@AddtlSbcpt.setter
	def AddtlSbcpt(self, value):
		self._AddtlSbcpt = value if type(value) != auto else self.make_default("AddtlSbcpt")

	@AddtlSbcpt.deleter
	def AddtlSbcpt(self):
		del self._AddtlSbcpt
		self._AddtlSbcpt = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def PlanTp(self):
		return self._PlanTp

	@PlanTp.setter
	def PlanTp(self, value):
		self._PlanTp = value if type(value) != auto else self.make_default("PlanTp")

	@PlanTp.deleter
	def PlanTp(self):
		del self._PlanTp
		self._PlanTp = None

	@property
	def AddtlSbcptFctn(self):
		return self._AddtlSbcptFctn

	@AddtlSbcptFctn.setter
	def AddtlSbcptFctn(self, value):
		self._AddtlSbcptFctn = value if type(value) != auto else self.make_default("AddtlSbcptFctn")

	@AddtlSbcptFctn.deleter
	def AddtlSbcptFctn(self):
		del self._AddtlSbcptFctn
		self._AddtlSbcptFctn = None

	@property
	def PlanConttn(self):
		return self._PlanConttn

	@PlanConttn.setter
	def PlanConttn(self, value):
		self._PlanConttn = value if type(value) != auto else self.make_default("PlanConttn")

	@PlanConttn.deleter
	def PlanConttn(self):
		del self._PlanConttn
		self._PlanConttn = None

	@property
	def TtlNbOfInstlmts(self):
		return self._TtlNbOfInstlmts

	@TtlNbOfInstlmts.setter
	def TtlNbOfInstlmts(self, value):
		self._TtlNbOfInstlmts = value if type(value) != auto else self.make_default("TtlNbOfInstlmts")

	@TtlNbOfInstlmts.deleter
	def TtlNbOfInstlmts(self):
		del self._TtlNbOfInstlmts
		self._TtlNbOfInstlmts = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSbcpt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanTp', type=InvestmentFundPlanType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSbcptFctn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanConttn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfInstlmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitsOrAmount1Choice, min=0, max=1, mutex_group=None, array=False),
	))

