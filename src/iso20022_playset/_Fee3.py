# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ChargeType5Choice
from . import Max35Text
from . import PercentageRate
from . import YesNoIndicator

class Fee3(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_NewComrclAgrmtRefInd", "_RprdDscntAmt", "_RprdDscntRate", "_RprdReqdAmt", "_RprdReqdRate", "_RprdStdAmt", "_RprdStdRate", "_Tp"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@property
	def NewComrclAgrmtRefInd(self):
		return self._NewComrclAgrmtRefInd

	@NewComrclAgrmtRefInd.setter
	def NewComrclAgrmtRefInd(self, value):
		self._NewComrclAgrmtRefInd = value if value is not None else base_types.UninitialisedField(self, 'NewComrclAgrmtRefInd', YesNoIndicator, False)

	@NewComrclAgrmtRefInd.deleter
	def NewComrclAgrmtRefInd(self):
		del self._NewComrclAgrmtRefInd
		self._NewComrclAgrmtRefInd = base_types.UninitialisedField(self, 'NewComrclAgrmtRefInd', YesNoIndicator, False)

	@property
	def RprdDscntAmt(self):
		return self._RprdDscntAmt

	@RprdDscntAmt.setter
	def RprdDscntAmt(self, value):
		self._RprdDscntAmt = value if value is not None else base_types.UninitialisedField(self, 'RprdDscntAmt', ActiveCurrencyAndAmount, False)

	@RprdDscntAmt.deleter
	def RprdDscntAmt(self):
		del self._RprdDscntAmt
		self._RprdDscntAmt = base_types.UninitialisedField(self, 'RprdDscntAmt', ActiveCurrencyAndAmount, False)

	@property
	def RprdDscntRate(self):
		return self._RprdDscntRate

	@RprdDscntRate.setter
	def RprdDscntRate(self, value):
		self._RprdDscntRate = value if value is not None else base_types.UninitialisedField(self, 'RprdDscntRate', PercentageRate, False)

	@RprdDscntRate.deleter
	def RprdDscntRate(self):
		del self._RprdDscntRate
		self._RprdDscntRate = base_types.UninitialisedField(self, 'RprdDscntRate', PercentageRate, False)

	@property
	def RprdReqdAmt(self):
		return self._RprdReqdAmt

	@RprdReqdAmt.setter
	def RprdReqdAmt(self, value):
		self._RprdReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'RprdReqdAmt', ActiveCurrencyAndAmount, False)

	@RprdReqdAmt.deleter
	def RprdReqdAmt(self):
		del self._RprdReqdAmt
		self._RprdReqdAmt = base_types.UninitialisedField(self, 'RprdReqdAmt', ActiveCurrencyAndAmount, False)

	@property
	def RprdReqdRate(self):
		return self._RprdReqdRate

	@RprdReqdRate.setter
	def RprdReqdRate(self, value):
		self._RprdReqdRate = value if value is not None else base_types.UninitialisedField(self, 'RprdReqdRate', PercentageRate, False)

	@RprdReqdRate.deleter
	def RprdReqdRate(self):
		del self._RprdReqdRate
		self._RprdReqdRate = base_types.UninitialisedField(self, 'RprdReqdRate', PercentageRate, False)

	@property
	def RprdStdAmt(self):
		return self._RprdStdAmt

	@RprdStdAmt.setter
	def RprdStdAmt(self, value):
		self._RprdStdAmt = value if value is not None else base_types.UninitialisedField(self, 'RprdStdAmt', ActiveCurrencyAndAmount, False)

	@RprdStdAmt.deleter
	def RprdStdAmt(self):
		del self._RprdStdAmt
		self._RprdStdAmt = base_types.UninitialisedField(self, 'RprdStdAmt', ActiveCurrencyAndAmount, False)

	@property
	def RprdStdRate(self):
		return self._RprdStdRate

	@RprdStdRate.setter
	def RprdStdRate(self, value):
		self._RprdStdRate = value if value is not None else base_types.UninitialisedField(self, 'RprdStdRate', PercentageRate, False)

	@RprdStdRate.deleter
	def RprdStdRate(self):
		del self._RprdStdRate
		self._RprdStdRate = base_types.UninitialisedField(self, 'RprdStdRate', PercentageRate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType5Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewComrclAgrmtRefInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdDscntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdDscntRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdReqdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdReqdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdStdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdStdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType5Choice, min=0, max=1, mutex_group=None, array=False),
	))