# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd19DecimalAmount
from . import EmbeddedType1Code
from . import ExerciseDate1Choice
from . import ISODate
from . import OptionBarrierLevel1Choice
from . import OptionStyle6Code
from . import OptionType2Code
from . import Schedule4
from . import SecuritiesTransactionPrice17Choice

class OptionOrSwaption11(base_types._BaseFieldType):

	__slots__ = ["_BrrrLvls", "_CallAmt", "_ExrcDt", "_ExrcStyle", "_MbddTp", "_MtrtyDtOfUndrlyg", "_PrmAmt", "_PrmPmtDt", "_PutAmt", "_StrkPric", "_StrkPricSchdl", "_Tp"]
	@property
	def BrrrLvls(self):
		return self._BrrrLvls

	@BrrrLvls.setter
	def BrrrLvls(self, value):
		self._BrrrLvls = value if value is not None else base_types.UninitialisedField(self, 'BrrrLvls', OptionBarrierLevel1Choice, False)

	@BrrrLvls.deleter
	def BrrrLvls(self):
		del self._BrrrLvls
		self._BrrrLvls = base_types.UninitialisedField(self, 'BrrrLvls', OptionBarrierLevel1Choice, False)

	@property
	def CallAmt(self):
		return self._CallAmt

	@CallAmt.setter
	def CallAmt(self, value):
		self._CallAmt = value if value is not None else base_types.UninitialisedField(self, 'CallAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@CallAmt.deleter
	def CallAmt(self):
		del self._CallAmt
		self._CallAmt = base_types.UninitialisedField(self, 'CallAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@property
	def ExrcDt(self):
		return self._ExrcDt

	@ExrcDt.setter
	def ExrcDt(self, value):
		self._ExrcDt = value if value is not None else base_types.UninitialisedField(self, 'ExrcDt', ExerciseDate1Choice, False)

	@ExrcDt.deleter
	def ExrcDt(self):
		del self._ExrcDt
		self._ExrcDt = base_types.UninitialisedField(self, 'ExrcDt', ExerciseDate1Choice, False)

	@property
	def ExrcStyle(self):
		return self._ExrcStyle

	@ExrcStyle.setter
	def ExrcStyle(self, value):
		self._ExrcStyle = value if value is not None else base_types.UninitialisedField(self, 'ExrcStyle', OptionStyle6Code, True)

	@ExrcStyle.deleter
	def ExrcStyle(self):
		del self._ExrcStyle
		self._ExrcStyle = base_types.UninitialisedField(self, 'ExrcStyle', OptionStyle6Code, True)

	@property
	def MbddTp(self):
		return self._MbddTp

	@MbddTp.setter
	def MbddTp(self, value):
		self._MbddTp = value if value is not None else base_types.UninitialisedField(self, 'MbddTp', EmbeddedType1Code, False)

	@MbddTp.deleter
	def MbddTp(self):
		del self._MbddTp
		self._MbddTp = base_types.UninitialisedField(self, 'MbddTp', EmbeddedType1Code, False)

	@property
	def MtrtyDtOfUndrlyg(self):
		return self._MtrtyDtOfUndrlyg

	@MtrtyDtOfUndrlyg.setter
	def MtrtyDtOfUndrlyg(self, value):
		self._MtrtyDtOfUndrlyg = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDtOfUndrlyg', ISODate, False)

	@MtrtyDtOfUndrlyg.deleter
	def MtrtyDtOfUndrlyg(self):
		del self._MtrtyDtOfUndrlyg
		self._MtrtyDtOfUndrlyg = base_types.UninitialisedField(self, 'MtrtyDtOfUndrlyg', ISODate, False)

	@property
	def PrmAmt(self):
		return self._PrmAmt

	@PrmAmt.setter
	def PrmAmt(self, value):
		self._PrmAmt = value if value is not None else base_types.UninitialisedField(self, 'PrmAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@PrmAmt.deleter
	def PrmAmt(self):
		del self._PrmAmt
		self._PrmAmt = base_types.UninitialisedField(self, 'PrmAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@property
	def PrmPmtDt(self):
		return self._PrmPmtDt

	@PrmPmtDt.setter
	def PrmPmtDt(self, value):
		self._PrmPmtDt = value if value is not None else base_types.UninitialisedField(self, 'PrmPmtDt', ISODate, False)

	@PrmPmtDt.deleter
	def PrmPmtDt(self):
		del self._PrmPmtDt
		self._PrmPmtDt = base_types.UninitialisedField(self, 'PrmPmtDt', ISODate, False)

	@property
	def PutAmt(self):
		return self._PutAmt

	@PutAmt.setter
	def PutAmt(self, value):
		self._PutAmt = value if value is not None else base_types.UninitialisedField(self, 'PutAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@PutAmt.deleter
	def PutAmt(self):
		del self._PutAmt
		self._PutAmt = base_types.UninitialisedField(self, 'PutAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if value is not None else base_types.UninitialisedField(self, 'StrkPric', SecuritiesTransactionPrice17Choice, False)

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = base_types.UninitialisedField(self, 'StrkPric', SecuritiesTransactionPrice17Choice, False)

	@property
	def StrkPricSchdl(self):
		return self._StrkPricSchdl

	@StrkPricSchdl.setter
	def StrkPricSchdl(self, value):
		self._StrkPricSchdl = value if value is not None else base_types.UninitialisedField(self, 'StrkPricSchdl', Schedule4, True)

	@StrkPricSchdl.deleter
	def StrkPricSchdl(self):
		del self._StrkPricSchdl
		self._StrkPricSchdl = base_types.UninitialisedField(self, 'StrkPricSchdl', Schedule4, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', OptionType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', OptionType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrrrLvls', type=OptionBarrierLevel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcDt', type=ExerciseDate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcStyle', type=OptionStyle6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MbddTp', type=EmbeddedType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDtOfUndrlyg', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPricSchdl', type=Schedule4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=OptionType2Code, min=0, max=1, mutex_group=None, array=False),
	))