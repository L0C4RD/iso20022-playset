# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat4Choice

class CorporateActionDate4(base_types._BaseFieldType):

	__slots__ = ["_CnsntRcrdDt", "_CnsntXprtnDt", "_CpnClpngDt", "_DdlnToSplt", "_EarlstPmtDt", "_MktDdln", "_PmtDt", "_QtnSetngDt", "_RspnDdln", "_SbcptCostDbtDt", "_XpryDt"]
	@property
	def CnsntRcrdDt(self):
		return self._CnsntRcrdDt

	@CnsntRcrdDt.setter
	def CnsntRcrdDt(self, value):
		self._CnsntRcrdDt = value if value is not None else base_types.UninitialisedField(self, 'CnsntRcrdDt', DateFormat4Choice, False)

	@CnsntRcrdDt.deleter
	def CnsntRcrdDt(self):
		del self._CnsntRcrdDt
		self._CnsntRcrdDt = base_types.UninitialisedField(self, 'CnsntRcrdDt', DateFormat4Choice, False)

	@property
	def CnsntXprtnDt(self):
		return self._CnsntXprtnDt

	@CnsntXprtnDt.setter
	def CnsntXprtnDt(self, value):
		self._CnsntXprtnDt = value if value is not None else base_types.UninitialisedField(self, 'CnsntXprtnDt', DateFormat4Choice, False)

	@CnsntXprtnDt.deleter
	def CnsntXprtnDt(self):
		del self._CnsntXprtnDt
		self._CnsntXprtnDt = base_types.UninitialisedField(self, 'CnsntXprtnDt', DateFormat4Choice, False)

	@property
	def CpnClpngDt(self):
		return self._CpnClpngDt

	@CpnClpngDt.setter
	def CpnClpngDt(self, value):
		self._CpnClpngDt = value if value is not None else base_types.UninitialisedField(self, 'CpnClpngDt', DateFormat4Choice, False)

	@CpnClpngDt.deleter
	def CpnClpngDt(self):
		del self._CpnClpngDt
		self._CpnClpngDt = base_types.UninitialisedField(self, 'CpnClpngDt', DateFormat4Choice, False)

	@property
	def DdlnToSplt(self):
		return self._DdlnToSplt

	@DdlnToSplt.setter
	def DdlnToSplt(self, value):
		self._DdlnToSplt = value if value is not None else base_types.UninitialisedField(self, 'DdlnToSplt', DateFormat4Choice, False)

	@DdlnToSplt.deleter
	def DdlnToSplt(self):
		del self._DdlnToSplt
		self._DdlnToSplt = base_types.UninitialisedField(self, 'DdlnToSplt', DateFormat4Choice, False)

	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat4Choice, False)

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat4Choice, False)

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if value is not None else base_types.UninitialisedField(self, 'MktDdln', DateFormat4Choice, False)

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = base_types.UninitialisedField(self, 'MktDdln', DateFormat4Choice, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat4Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat4Choice, False)

	@property
	def QtnSetngDt(self):
		return self._QtnSetngDt

	@QtnSetngDt.setter
	def QtnSetngDt(self, value):
		self._QtnSetngDt = value if value is not None else base_types.UninitialisedField(self, 'QtnSetngDt', DateFormat4Choice, False)

	@QtnSetngDt.deleter
	def QtnSetngDt(self):
		del self._QtnSetngDt
		self._QtnSetngDt = base_types.UninitialisedField(self, 'QtnSetngDt', DateFormat4Choice, False)

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if value is not None else base_types.UninitialisedField(self, 'RspnDdln', DateFormat4Choice, False)

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = base_types.UninitialisedField(self, 'RspnDdln', DateFormat4Choice, False)

	@property
	def SbcptCostDbtDt(self):
		return self._SbcptCostDbtDt

	@SbcptCostDbtDt.setter
	def SbcptCostDbtDt(self, value):
		self._SbcptCostDbtDt = value if value is not None else base_types.UninitialisedField(self, 'SbcptCostDbtDt', DateFormat4Choice, False)

	@SbcptCostDbtDt.deleter
	def SbcptCostDbtDt(self):
		del self._SbcptCostDbtDt
		self._SbcptCostDbtDt = base_types.UninitialisedField(self, 'SbcptCostDbtDt', DateFormat4Choice, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', DateFormat4Choice, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', DateFormat4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsntRcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntXprtnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnClpngDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnToSplt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnSetngDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptCostDbtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))