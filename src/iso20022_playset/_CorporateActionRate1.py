# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndRateFormat3Choice
from . import RateAndAmountFormat1Choice
from . import RateFormat1Choice

class CorporateActionRate1(base_types._BaseFieldType):

	__slots__ = ["_BidIntrvl", "_Chrgs", "_Intrst", "_PctgSght", "_RinvstmtDscntToMkt", "_RltdIndx", "_Sprd"]
	@property
	def BidIntrvl(self):
		return self._BidIntrvl

	@BidIntrvl.setter
	def BidIntrvl(self, value):
		self._BidIntrvl = value if value is not None else base_types.UninitialisedField(self, 'BidIntrvl', AmountAndRateFormat3Choice, False)

	@BidIntrvl.deleter
	def BidIntrvl(self):
		del self._BidIntrvl
		self._BidIntrvl = base_types.UninitialisedField(self, 'BidIntrvl', AmountAndRateFormat3Choice, False)

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', RateAndAmountFormat1Choice, False)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', RateAndAmountFormat1Choice, False)

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if value is not None else base_types.UninitialisedField(self, 'Intrst', RateAndAmountFormat1Choice, False)

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = base_types.UninitialisedField(self, 'Intrst', RateAndAmountFormat1Choice, False)

	@property
	def PctgSght(self):
		return self._PctgSght

	@PctgSght.setter
	def PctgSght(self, value):
		self._PctgSght = value if value is not None else base_types.UninitialisedField(self, 'PctgSght', RateFormat1Choice, False)

	@PctgSght.deleter
	def PctgSght(self):
		del self._PctgSght
		self._PctgSght = base_types.UninitialisedField(self, 'PctgSght', RateFormat1Choice, False)

	@property
	def RinvstmtDscntToMkt(self):
		return self._RinvstmtDscntToMkt

	@RinvstmtDscntToMkt.setter
	def RinvstmtDscntToMkt(self, value):
		self._RinvstmtDscntToMkt = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtDscntToMkt', RateFormat1Choice, False)

	@RinvstmtDscntToMkt.deleter
	def RinvstmtDscntToMkt(self):
		del self._RinvstmtDscntToMkt
		self._RinvstmtDscntToMkt = base_types.UninitialisedField(self, 'RinvstmtDscntToMkt', RateFormat1Choice, False)

	@property
	def RltdIndx(self):
		return self._RltdIndx

	@RltdIndx.setter
	def RltdIndx(self, value):
		self._RltdIndx = value if value is not None else base_types.UninitialisedField(self, 'RltdIndx', RateFormat1Choice, False)

	@RltdIndx.deleter
	def RltdIndx(self):
		del self._RltdIndx
		self._RltdIndx = base_types.UninitialisedField(self, 'RltdIndx', RateFormat1Choice, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', RateFormat1Choice, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', RateFormat1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BidIntrvl', type=AmountAndRateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgSght', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtDscntToMkt', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdIndx', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
	))