# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RateAndAmountFormat57Choice
from . import RateAndAmountFormat58Choice
from . import RateAndAmountFormat59Choice
from . import RateFormat12Choice
from . import RateFormat24Choice
from . import RateFormat25Choice

class CorporateActionRate122(base_types._BaseFieldType):

	__slots__ = ["_BidIntrvl", "_DclrdRate", "_IndxFctr", "_IntrstRate", "_IntrstShrtfll", "_NxtFctr", "_PctgSght", "_PrvsFctr", "_RealsdLoss", "_RinvstmtDscntRateToMkt", "_RltdIndx", "_Sprd"]
	@property
	def BidIntrvl(self):
		return self._BidIntrvl

	@BidIntrvl.setter
	def BidIntrvl(self, value):
		self._BidIntrvl = value if value is not None else base_types.UninitialisedField(self, 'BidIntrvl', RateAndAmountFormat58Choice, False)

	@BidIntrvl.deleter
	def BidIntrvl(self):
		del self._BidIntrvl
		self._BidIntrvl = base_types.UninitialisedField(self, 'BidIntrvl', RateAndAmountFormat58Choice, False)

	@property
	def DclrdRate(self):
		return self._DclrdRate

	@DclrdRate.setter
	def DclrdRate(self, value):
		self._DclrdRate = value if value is not None else base_types.UninitialisedField(self, 'DclrdRate', RateAndAmountFormat59Choice, False)

	@DclrdRate.deleter
	def DclrdRate(self):
		del self._DclrdRate
		self._DclrdRate = base_types.UninitialisedField(self, 'DclrdRate', RateAndAmountFormat59Choice, False)

	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if value is not None else base_types.UninitialisedField(self, 'IndxFctr', RateAndAmountFormat57Choice, False)

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = base_types.UninitialisedField(self, 'IndxFctr', RateAndAmountFormat57Choice, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', RateAndAmountFormat57Choice, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', RateAndAmountFormat57Choice, False)

	@property
	def IntrstShrtfll(self):
		return self._IntrstShrtfll

	@IntrstShrtfll.setter
	def IntrstShrtfll(self, value):
		self._IntrstShrtfll = value if value is not None else base_types.UninitialisedField(self, 'IntrstShrtfll', RateAndAmountFormat59Choice, False)

	@IntrstShrtfll.deleter
	def IntrstShrtfll(self):
		del self._IntrstShrtfll
		self._IntrstShrtfll = base_types.UninitialisedField(self, 'IntrstShrtfll', RateAndAmountFormat59Choice, False)

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if value is not None else base_types.UninitialisedField(self, 'NxtFctr', RateFormat12Choice, False)

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = base_types.UninitialisedField(self, 'NxtFctr', RateFormat12Choice, False)

	@property
	def PctgSght(self):
		return self._PctgSght

	@PctgSght.setter
	def PctgSght(self, value):
		self._PctgSght = value if value is not None else base_types.UninitialisedField(self, 'PctgSght', RateFormat25Choice, False)

	@PctgSght.deleter
	def PctgSght(self):
		del self._PctgSght
		self._PctgSght = base_types.UninitialisedField(self, 'PctgSght', RateFormat25Choice, False)

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if value is not None else base_types.UninitialisedField(self, 'PrvsFctr', RateFormat12Choice, False)

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = base_types.UninitialisedField(self, 'PrvsFctr', RateFormat12Choice, False)

	@property
	def RealsdLoss(self):
		return self._RealsdLoss

	@RealsdLoss.setter
	def RealsdLoss(self, value):
		self._RealsdLoss = value if value is not None else base_types.UninitialisedField(self, 'RealsdLoss', RateAndAmountFormat59Choice, False)

	@RealsdLoss.deleter
	def RealsdLoss(self):
		del self._RealsdLoss
		self._RealsdLoss = base_types.UninitialisedField(self, 'RealsdLoss', RateAndAmountFormat59Choice, False)

	@property
	def RinvstmtDscntRateToMkt(self):
		return self._RinvstmtDscntRateToMkt

	@RinvstmtDscntRateToMkt.setter
	def RinvstmtDscntRateToMkt(self, value):
		self._RinvstmtDscntRateToMkt = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtDscntRateToMkt', RateFormat24Choice, False)

	@RinvstmtDscntRateToMkt.deleter
	def RinvstmtDscntRateToMkt(self):
		del self._RinvstmtDscntRateToMkt
		self._RinvstmtDscntRateToMkt = base_types.UninitialisedField(self, 'RinvstmtDscntRateToMkt', RateFormat24Choice, False)

	@property
	def RltdIndx(self):
		return self._RltdIndx

	@RltdIndx.setter
	def RltdIndx(self, value):
		self._RltdIndx = value if value is not None else base_types.UninitialisedField(self, 'RltdIndx', RateFormat24Choice, False)

	@RltdIndx.deleter
	def RltdIndx(self):
		del self._RltdIndx
		self._RltdIndx = base_types.UninitialisedField(self, 'RltdIndx', RateFormat24Choice, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', RateFormat24Choice, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', RateFormat24Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BidIntrvl', type=RateAndAmountFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrdRate', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFctr', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstShrtfll', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgSght', type=RateFormat25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RealsdLoss', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtDscntRateToMkt', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdIndx', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
	))