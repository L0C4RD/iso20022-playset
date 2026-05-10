import base_types
import OptionBarrierLevel1Choice
import ActiveOrHistoricCurrencyAnd19DecimalAmount
import OptionType2Code
import ExerciseDate1Choice
import ISODate
import OptionStyle6Code
import EmbeddedType1Code
import Schedule4
import SecuritiesTransactionPrice17Choice

class OptionOrSwaption11(base_types._BaseFieldType):

	__slots__ = ["_ExrcStyle", "_MbddTp", "_PutAmt", "_PrmAmt", "_Tp", "_ExrcDt", "_CallAmt", "_MtrtyDtOfUndrlyg", "_BrrrLvls", "_StrkPric", "_StrkPricSchdl", "_PrmPmtDt"]
	@property
	def ExrcStyle(self):
		return self._ExrcStyle

	@ExrcStyle.setter
	def ExrcStyle(self, value):
		self._ExrcStyle = value if type(value) != auto else self.make_default("ExrcStyle")

	@ExrcStyle.deleter
	def ExrcStyle(self):
		del self._ExrcStyle
		self._ExrcStyle = None

	@property
	def MbddTp(self):
		return self._MbddTp

	@MbddTp.setter
	def MbddTp(self, value):
		self._MbddTp = value if type(value) != auto else self.make_default("MbddTp")

	@MbddTp.deleter
	def MbddTp(self):
		del self._MbddTp
		self._MbddTp = None

	@property
	def PutAmt(self):
		return self._PutAmt

	@PutAmt.setter
	def PutAmt(self, value):
		self._PutAmt = value if type(value) != auto else self.make_default("PutAmt")

	@PutAmt.deleter
	def PutAmt(self):
		del self._PutAmt
		self._PutAmt = None

	@property
	def PrmAmt(self):
		return self._PrmAmt

	@PrmAmt.setter
	def PrmAmt(self, value):
		self._PrmAmt = value if type(value) != auto else self.make_default("PrmAmt")

	@PrmAmt.deleter
	def PrmAmt(self):
		del self._PrmAmt
		self._PrmAmt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def ExrcDt(self):
		return self._ExrcDt

	@ExrcDt.setter
	def ExrcDt(self, value):
		self._ExrcDt = value if type(value) != auto else self.make_default("ExrcDt")

	@ExrcDt.deleter
	def ExrcDt(self):
		del self._ExrcDt
		self._ExrcDt = None

	@property
	def CallAmt(self):
		return self._CallAmt

	@CallAmt.setter
	def CallAmt(self, value):
		self._CallAmt = value if type(value) != auto else self.make_default("CallAmt")

	@CallAmt.deleter
	def CallAmt(self):
		del self._CallAmt
		self._CallAmt = None

	@property
	def MtrtyDtOfUndrlyg(self):
		return self._MtrtyDtOfUndrlyg

	@MtrtyDtOfUndrlyg.setter
	def MtrtyDtOfUndrlyg(self, value):
		self._MtrtyDtOfUndrlyg = value if type(value) != auto else self.make_default("MtrtyDtOfUndrlyg")

	@MtrtyDtOfUndrlyg.deleter
	def MtrtyDtOfUndrlyg(self):
		del self._MtrtyDtOfUndrlyg
		self._MtrtyDtOfUndrlyg = None

	@property
	def BrrrLvls(self):
		return self._BrrrLvls

	@BrrrLvls.setter
	def BrrrLvls(self, value):
		self._BrrrLvls = value if type(value) != auto else self.make_default("BrrrLvls")

	@BrrrLvls.deleter
	def BrrrLvls(self):
		del self._BrrrLvls
		self._BrrrLvls = None

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if type(value) != auto else self.make_default("StrkPric")

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = None

	@property
	def StrkPricSchdl(self):
		return self._StrkPricSchdl

	@StrkPricSchdl.setter
	def StrkPricSchdl(self, value):
		self._StrkPricSchdl = value if type(value) != auto else self.make_default("StrkPricSchdl")

	@StrkPricSchdl.deleter
	def StrkPricSchdl(self):
		del self._StrkPricSchdl
		self._StrkPricSchdl = None

	@property
	def PrmPmtDt(self):
		return self._PrmPmtDt

	@PrmPmtDt.setter
	def PrmPmtDt(self, value):
		self._PrmPmtDt = value if type(value) != auto else self.make_default("PrmPmtDt")

	@PrmPmtDt.deleter
	def PrmPmtDt(self):
		del self._PrmPmtDt
		self._PrmPmtDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExrcStyle', type=OptionStyle6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MbddTp', type=EmbeddedType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=OptionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcDt', type=ExerciseDate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDtOfUndrlyg', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrrLvls', type=OptionBarrierLevel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPricSchdl', type=Schedule4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrmPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

