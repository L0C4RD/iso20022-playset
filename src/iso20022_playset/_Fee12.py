from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ChargeType10Choice import ChargeType10Choice
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._YesNoIndicator import YesNoIndicator

class Fee12(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_NewComrclAgrmtRefInd", "_RprdDscntAmt", "_RprdDscntRate", "_RprdReqdAmt", "_RprdReqdRate", "_RprdStdAmt", "_RprdStdRate", "_Tp"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != base_types.auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	@property
	def NewComrclAgrmtRefInd(self):
		return self._NewComrclAgrmtRefInd

	@NewComrclAgrmtRefInd.setter
	def NewComrclAgrmtRefInd(self, value):
		self._NewComrclAgrmtRefInd = value if type(value) != base_types.auto else self.make_default("NewComrclAgrmtRefInd")

	@NewComrclAgrmtRefInd.deleter
	def NewComrclAgrmtRefInd(self):
		del self._NewComrclAgrmtRefInd
		self._NewComrclAgrmtRefInd = None

	@property
	def RprdDscntAmt(self):
		return self._RprdDscntAmt

	@RprdDscntAmt.setter
	def RprdDscntAmt(self, value):
		self._RprdDscntAmt = value if type(value) != base_types.auto else self.make_default("RprdDscntAmt")

	@RprdDscntAmt.deleter
	def RprdDscntAmt(self):
		del self._RprdDscntAmt
		self._RprdDscntAmt = None

	@property
	def RprdDscntRate(self):
		return self._RprdDscntRate

	@RprdDscntRate.setter
	def RprdDscntRate(self, value):
		self._RprdDscntRate = value if type(value) != base_types.auto else self.make_default("RprdDscntRate")

	@RprdDscntRate.deleter
	def RprdDscntRate(self):
		del self._RprdDscntRate
		self._RprdDscntRate = None

	@property
	def RprdReqdAmt(self):
		return self._RprdReqdAmt

	@RprdReqdAmt.setter
	def RprdReqdAmt(self, value):
		self._RprdReqdAmt = value if type(value) != base_types.auto else self.make_default("RprdReqdAmt")

	@RprdReqdAmt.deleter
	def RprdReqdAmt(self):
		del self._RprdReqdAmt
		self._RprdReqdAmt = None

	@property
	def RprdReqdRate(self):
		return self._RprdReqdRate

	@RprdReqdRate.setter
	def RprdReqdRate(self, value):
		self._RprdReqdRate = value if type(value) != base_types.auto else self.make_default("RprdReqdRate")

	@RprdReqdRate.deleter
	def RprdReqdRate(self):
		del self._RprdReqdRate
		self._RprdReqdRate = None

	@property
	def RprdStdAmt(self):
		return self._RprdStdAmt

	@RprdStdAmt.setter
	def RprdStdAmt(self, value):
		self._RprdStdAmt = value if type(value) != base_types.auto else self.make_default("RprdStdAmt")

	@RprdStdAmt.deleter
	def RprdStdAmt(self):
		del self._RprdStdAmt
		self._RprdStdAmt = None

	@property
	def RprdStdRate(self):
		return self._RprdStdRate

	@RprdStdRate.setter
	def RprdStdRate(self, value):
		self._RprdStdRate = value if type(value) != base_types.auto else self.make_default("RprdStdRate")

	@RprdStdRate.deleter
	def RprdStdRate(self):
		del self._RprdStdRate
		self._RprdStdRate = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewComrclAgrmtRefInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdDscntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdDscntRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdReqdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdReqdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdStdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdStdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType10Choice, min=0, max=1, mutex_group=None, array=False),
	))

