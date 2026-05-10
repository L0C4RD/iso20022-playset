from . import base_types
from ._RateAndAmountFormat1Choice import RateAndAmountFormat1Choice
from ._RateFormat1Choice import RateFormat1Choice
from ._AmountAndRateFormat3Choice import AmountAndRateFormat3Choice

class CorporateActionRate1(base_types._BaseFieldType):

	__slots__ = ["_RltdIndx", "_Chrgs", "_Intrst", "_Sprd", "_RinvstmtDscntToMkt", "_BidIntrvl", "_PctgSght"]
	@property
	def RltdIndx(self):
		return self._RltdIndx

	@RltdIndx.setter
	def RltdIndx(self, value):
		self._RltdIndx = value if type(value) != base_types.auto else self.make_default("RltdIndx")

	@RltdIndx.deleter
	def RltdIndx(self):
		del self._RltdIndx
		self._RltdIndx = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != base_types.auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def RinvstmtDscntToMkt(self):
		return self._RinvstmtDscntToMkt

	@RinvstmtDscntToMkt.setter
	def RinvstmtDscntToMkt(self, value):
		self._RinvstmtDscntToMkt = value if type(value) != base_types.auto else self.make_default("RinvstmtDscntToMkt")

	@RinvstmtDscntToMkt.deleter
	def RinvstmtDscntToMkt(self):
		del self._RinvstmtDscntToMkt
		self._RinvstmtDscntToMkt = None

	@property
	def BidIntrvl(self):
		return self._BidIntrvl

	@BidIntrvl.setter
	def BidIntrvl(self, value):
		self._BidIntrvl = value if type(value) != base_types.auto else self.make_default("BidIntrvl")

	@BidIntrvl.deleter
	def BidIntrvl(self):
		del self._BidIntrvl
		self._BidIntrvl = None

	@property
	def PctgSght(self):
		return self._PctgSght

	@PctgSght.setter
	def PctgSght(self, value):
		self._PctgSght = value if type(value) != base_types.auto else self.make_default("PctgSght")

	@PctgSght.deleter
	def PctgSght(self):
		del self._PctgSght
		self._PctgSght = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdIndx', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtDscntToMkt', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BidIntrvl', type=AmountAndRateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgSght', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
	))

