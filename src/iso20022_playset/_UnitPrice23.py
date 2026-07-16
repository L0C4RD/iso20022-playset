# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveOrHistoricCurrencyAndAmount
from . import Number
from . import PriceMethod1Code
from . import PriceValue1
from . import TaxableIncomePerShareCalculated2Choice
from . import TypeOfPrice46Choice

class UnitPrice23(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstNAV", "_NbOfDaysAcrd", "_PricMtd", "_TaxblIncmPerShr", "_TaxblIncmPerShrClctd", "_Tp", "_Val"]
	@property
	def AcrdIntrstNAV(self):
		return self._AcrdIntrstNAV

	@AcrdIntrstNAV.setter
	def AcrdIntrstNAV(self, value):
		self._AcrdIntrstNAV = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@AcrdIntrstNAV.deleter
	def AcrdIntrstNAV(self):
		del self._AcrdIntrstNAV
		self._AcrdIntrstNAV = base_types.UninitialisedField(self, 'AcrdIntrstNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if value is not None else base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@property
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShr', ActiveCurrencyAnd13DecimalAmount, False)

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = base_types.UninitialisedField(self, 'TaxblIncmPerShr', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Choice, False)

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice46Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice46Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceValue1, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceValue1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShr', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculated2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceValue1, min=1, max=1, mutex_group=None, array=False),
	))