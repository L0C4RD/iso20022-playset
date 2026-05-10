from . import base_types
from ._DateFormat4Choice import DateFormat4Choice

class CorporateActionDate4(base_types._BaseFieldType):

	__slots__ = ["_SbcptCostDbtDt", "_XpryDt", "_CnsntXprtnDt", "_DdlnToSplt", "_EarlstPmtDt", "_RspnDdln", "_PmtDt", "_CnsntRcrdDt", "_CpnClpngDt", "_QtnSetngDt", "_MktDdln"]
	@property
	def SbcptCostDbtDt(self):
		return self._SbcptCostDbtDt

	@SbcptCostDbtDt.setter
	def SbcptCostDbtDt(self, value):
		self._SbcptCostDbtDt = value if type(value) != base_types.auto else self.make_default("SbcptCostDbtDt")

	@SbcptCostDbtDt.deleter
	def SbcptCostDbtDt(self):
		del self._SbcptCostDbtDt
		self._SbcptCostDbtDt = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def CnsntXprtnDt(self):
		return self._CnsntXprtnDt

	@CnsntXprtnDt.setter
	def CnsntXprtnDt(self, value):
		self._CnsntXprtnDt = value if type(value) != base_types.auto else self.make_default("CnsntXprtnDt")

	@CnsntXprtnDt.deleter
	def CnsntXprtnDt(self):
		del self._CnsntXprtnDt
		self._CnsntXprtnDt = None

	@property
	def DdlnToSplt(self):
		return self._DdlnToSplt

	@DdlnToSplt.setter
	def DdlnToSplt(self, value):
		self._DdlnToSplt = value if type(value) != base_types.auto else self.make_default("DdlnToSplt")

	@DdlnToSplt.deleter
	def DdlnToSplt(self):
		del self._DdlnToSplt
		self._DdlnToSplt = None

	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if type(value) != base_types.auto else self.make_default("EarlstPmtDt")

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = None

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if type(value) != base_types.auto else self.make_default("RspnDdln")

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = None

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def CnsntRcrdDt(self):
		return self._CnsntRcrdDt

	@CnsntRcrdDt.setter
	def CnsntRcrdDt(self, value):
		self._CnsntRcrdDt = value if type(value) != base_types.auto else self.make_default("CnsntRcrdDt")

	@CnsntRcrdDt.deleter
	def CnsntRcrdDt(self):
		del self._CnsntRcrdDt
		self._CnsntRcrdDt = None

	@property
	def CpnClpngDt(self):
		return self._CpnClpngDt

	@CpnClpngDt.setter
	def CpnClpngDt(self, value):
		self._CpnClpngDt = value if type(value) != base_types.auto else self.make_default("CpnClpngDt")

	@CpnClpngDt.deleter
	def CpnClpngDt(self):
		del self._CpnClpngDt
		self._CpnClpngDt = None

	@property
	def QtnSetngDt(self):
		return self._QtnSetngDt

	@QtnSetngDt.setter
	def QtnSetngDt(self, value):
		self._QtnSetngDt = value if type(value) != base_types.auto else self.make_default("QtnSetngDt")

	@QtnSetngDt.deleter
	def QtnSetngDt(self):
		del self._QtnSetngDt
		self._QtnSetngDt = None

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if type(value) != base_types.auto else self.make_default("MktDdln")

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SbcptCostDbtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntXprtnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnToSplt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntRcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnClpngDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnSetngDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))

