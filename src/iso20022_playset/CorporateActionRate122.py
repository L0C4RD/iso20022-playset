import base_types
import RateFormat25Choice
import RateAndAmountFormat59Choice
import RateFormat24Choice
import RateAndAmountFormat58Choice
import RateAndAmountFormat57Choice
import RateFormat12Choice

class CorporateActionRate122(base_types._BaseFieldType):

	__slots__ = ["_IndxFctr", "_NxtFctr", "_RinvstmtDscntRateToMkt", "_PrvsFctr", "_IntrstShrtfll", "_DclrdRate", "_IntrstRate", "_RltdIndx", "_Sprd", "_RealsdLoss", "_PctgSght", "_BidIntrvl"]
	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if type(value) != auto else self.make_default("IndxFctr")

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = None

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if type(value) != auto else self.make_default("NxtFctr")

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = None

	@property
	def RinvstmtDscntRateToMkt(self):
		return self._RinvstmtDscntRateToMkt

	@RinvstmtDscntRateToMkt.setter
	def RinvstmtDscntRateToMkt(self, value):
		self._RinvstmtDscntRateToMkt = value if type(value) != auto else self.make_default("RinvstmtDscntRateToMkt")

	@RinvstmtDscntRateToMkt.deleter
	def RinvstmtDscntRateToMkt(self):
		del self._RinvstmtDscntRateToMkt
		self._RinvstmtDscntRateToMkt = None

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if type(value) != auto else self.make_default("PrvsFctr")

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = None

	@property
	def IntrstShrtfll(self):
		return self._IntrstShrtfll

	@IntrstShrtfll.setter
	def IntrstShrtfll(self, value):
		self._IntrstShrtfll = value if type(value) != auto else self.make_default("IntrstShrtfll")

	@IntrstShrtfll.deleter
	def IntrstShrtfll(self):
		del self._IntrstShrtfll
		self._IntrstShrtfll = None

	@property
	def DclrdRate(self):
		return self._DclrdRate

	@DclrdRate.setter
	def DclrdRate(self, value):
		self._DclrdRate = value if type(value) != auto else self.make_default("DclrdRate")

	@DclrdRate.deleter
	def DclrdRate(self):
		del self._DclrdRate
		self._DclrdRate = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def RltdIndx(self):
		return self._RltdIndx

	@RltdIndx.setter
	def RltdIndx(self, value):
		self._RltdIndx = value if type(value) != auto else self.make_default("RltdIndx")

	@RltdIndx.deleter
	def RltdIndx(self):
		del self._RltdIndx
		self._RltdIndx = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def RealsdLoss(self):
		return self._RealsdLoss

	@RealsdLoss.setter
	def RealsdLoss(self, value):
		self._RealsdLoss = value if type(value) != auto else self.make_default("RealsdLoss")

	@RealsdLoss.deleter
	def RealsdLoss(self):
		del self._RealsdLoss
		self._RealsdLoss = None

	@property
	def PctgSght(self):
		return self._PctgSght

	@PctgSght.setter
	def PctgSght(self, value):
		self._PctgSght = value if type(value) != auto else self.make_default("PctgSght")

	@PctgSght.deleter
	def PctgSght(self):
		del self._PctgSght
		self._PctgSght = None

	@property
	def BidIntrvl(self):
		return self._BidIntrvl

	@BidIntrvl.setter
	def BidIntrvl(self, value):
		self._BidIntrvl = value if type(value) != auto else self.make_default("BidIntrvl")

	@BidIntrvl.deleter
	def BidIntrvl(self):
		del self._BidIntrvl
		self._BidIntrvl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndxFctr', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtDscntRateToMkt', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstShrtfll', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrdRate', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdIndx', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RealsdLoss', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgSght', type=RateFormat25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BidIntrvl', type=RateAndAmountFormat58Choice, min=0, max=1, mutex_group=None, array=False),
	))

