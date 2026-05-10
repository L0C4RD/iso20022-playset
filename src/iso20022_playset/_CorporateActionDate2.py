from . import base_types
from ._DateFormat4Choice import DateFormat4Choice

class CorporateActionDate2(base_types._BaseFieldType):

	__slots__ = ["_RegnDdln", "_CrtApprvlDt", "_LpsdDt", "_UcondlDt", "_DdlnForTaxBrkdwnInstr", "_RsltsPblctnDt", "_GrntedPrtcptnDt", "_TradgSspdDt", "_MtrtyDt", "_CoverXprtnDt", "_PrratnDt", "_WhlyUcondlDt", "_ElctnToCtrPtyDdln", "_RedDt", "_LtryDt", "_ExDvddDt", "_IndxFxgDt", "_EarlyClsgDt", "_EqulstnDt", "_RcrdDt", "_SpclExDt", "_CertfctnDdln", "_FctvDt", "_MrgnFxgDt", "_PrtctDt"]
	@property
	def RegnDdln(self):
		return self._RegnDdln

	@RegnDdln.setter
	def RegnDdln(self, value):
		self._RegnDdln = value if type(value) != base_types.auto else self.make_default("RegnDdln")

	@RegnDdln.deleter
	def RegnDdln(self):
		del self._RegnDdln
		self._RegnDdln = None

	@property
	def CrtApprvlDt(self):
		return self._CrtApprvlDt

	@CrtApprvlDt.setter
	def CrtApprvlDt(self, value):
		self._CrtApprvlDt = value if type(value) != base_types.auto else self.make_default("CrtApprvlDt")

	@CrtApprvlDt.deleter
	def CrtApprvlDt(self):
		del self._CrtApprvlDt
		self._CrtApprvlDt = None

	@property
	def LpsdDt(self):
		return self._LpsdDt

	@LpsdDt.setter
	def LpsdDt(self, value):
		self._LpsdDt = value if type(value) != base_types.auto else self.make_default("LpsdDt")

	@LpsdDt.deleter
	def LpsdDt(self):
		del self._LpsdDt
		self._LpsdDt = None

	@property
	def UcondlDt(self):
		return self._UcondlDt

	@UcondlDt.setter
	def UcondlDt(self, value):
		self._UcondlDt = value if type(value) != base_types.auto else self.make_default("UcondlDt")

	@UcondlDt.deleter
	def UcondlDt(self):
		del self._UcondlDt
		self._UcondlDt = None

	@property
	def DdlnForTaxBrkdwnInstr(self):
		return self._DdlnForTaxBrkdwnInstr

	@DdlnForTaxBrkdwnInstr.setter
	def DdlnForTaxBrkdwnInstr(self, value):
		self._DdlnForTaxBrkdwnInstr = value if type(value) != base_types.auto else self.make_default("DdlnForTaxBrkdwnInstr")

	@DdlnForTaxBrkdwnInstr.deleter
	def DdlnForTaxBrkdwnInstr(self):
		del self._DdlnForTaxBrkdwnInstr
		self._DdlnForTaxBrkdwnInstr = None

	@property
	def RsltsPblctnDt(self):
		return self._RsltsPblctnDt

	@RsltsPblctnDt.setter
	def RsltsPblctnDt(self, value):
		self._RsltsPblctnDt = value if type(value) != base_types.auto else self.make_default("RsltsPblctnDt")

	@RsltsPblctnDt.deleter
	def RsltsPblctnDt(self):
		del self._RsltsPblctnDt
		self._RsltsPblctnDt = None

	@property
	def GrntedPrtcptnDt(self):
		return self._GrntedPrtcptnDt

	@GrntedPrtcptnDt.setter
	def GrntedPrtcptnDt(self, value):
		self._GrntedPrtcptnDt = value if type(value) != base_types.auto else self.make_default("GrntedPrtcptnDt")

	@GrntedPrtcptnDt.deleter
	def GrntedPrtcptnDt(self):
		del self._GrntedPrtcptnDt
		self._GrntedPrtcptnDt = None

	@property
	def TradgSspdDt(self):
		return self._TradgSspdDt

	@TradgSspdDt.setter
	def TradgSspdDt(self, value):
		self._TradgSspdDt = value if type(value) != base_types.auto else self.make_default("TradgSspdDt")

	@TradgSspdDt.deleter
	def TradgSspdDt(self):
		del self._TradgSspdDt
		self._TradgSspdDt = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def CoverXprtnDt(self):
		return self._CoverXprtnDt

	@CoverXprtnDt.setter
	def CoverXprtnDt(self, value):
		self._CoverXprtnDt = value if type(value) != base_types.auto else self.make_default("CoverXprtnDt")

	@CoverXprtnDt.deleter
	def CoverXprtnDt(self):
		del self._CoverXprtnDt
		self._CoverXprtnDt = None

	@property
	def PrratnDt(self):
		return self._PrratnDt

	@PrratnDt.setter
	def PrratnDt(self, value):
		self._PrratnDt = value if type(value) != base_types.auto else self.make_default("PrratnDt")

	@PrratnDt.deleter
	def PrratnDt(self):
		del self._PrratnDt
		self._PrratnDt = None

	@property
	def WhlyUcondlDt(self):
		return self._WhlyUcondlDt

	@WhlyUcondlDt.setter
	def WhlyUcondlDt(self, value):
		self._WhlyUcondlDt = value if type(value) != base_types.auto else self.make_default("WhlyUcondlDt")

	@WhlyUcondlDt.deleter
	def WhlyUcondlDt(self):
		del self._WhlyUcondlDt
		self._WhlyUcondlDt = None

	@property
	def ElctnToCtrPtyDdln(self):
		return self._ElctnToCtrPtyDdln

	@ElctnToCtrPtyDdln.setter
	def ElctnToCtrPtyDdln(self, value):
		self._ElctnToCtrPtyDdln = value if type(value) != base_types.auto else self.make_default("ElctnToCtrPtyDdln")

	@ElctnToCtrPtyDdln.deleter
	def ElctnToCtrPtyDdln(self):
		del self._ElctnToCtrPtyDdln
		self._ElctnToCtrPtyDdln = None

	@property
	def RedDt(self):
		return self._RedDt

	@RedDt.setter
	def RedDt(self, value):
		self._RedDt = value if type(value) != base_types.auto else self.make_default("RedDt")

	@RedDt.deleter
	def RedDt(self):
		del self._RedDt
		self._RedDt = None

	@property
	def LtryDt(self):
		return self._LtryDt

	@LtryDt.setter
	def LtryDt(self, value):
		self._LtryDt = value if type(value) != base_types.auto else self.make_default("LtryDt")

	@LtryDt.deleter
	def LtryDt(self):
		del self._LtryDt
		self._LtryDt = None

	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if type(value) != base_types.auto else self.make_default("ExDvddDt")

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = None

	@property
	def IndxFxgDt(self):
		return self._IndxFxgDt

	@IndxFxgDt.setter
	def IndxFxgDt(self, value):
		self._IndxFxgDt = value if type(value) != base_types.auto else self.make_default("IndxFxgDt")

	@IndxFxgDt.deleter
	def IndxFxgDt(self):
		del self._IndxFxgDt
		self._IndxFxgDt = None

	@property
	def EarlyClsgDt(self):
		return self._EarlyClsgDt

	@EarlyClsgDt.setter
	def EarlyClsgDt(self, value):
		self._EarlyClsgDt = value if type(value) != base_types.auto else self.make_default("EarlyClsgDt")

	@EarlyClsgDt.deleter
	def EarlyClsgDt(self):
		del self._EarlyClsgDt
		self._EarlyClsgDt = None

	@property
	def EqulstnDt(self):
		return self._EqulstnDt

	@EqulstnDt.setter
	def EqulstnDt(self, value):
		self._EqulstnDt = value if type(value) != base_types.auto else self.make_default("EqulstnDt")

	@EqulstnDt.deleter
	def EqulstnDt(self):
		del self._EqulstnDt
		self._EqulstnDt = None

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if type(value) != base_types.auto else self.make_default("RcrdDt")

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = None

	@property
	def SpclExDt(self):
		return self._SpclExDt

	@SpclExDt.setter
	def SpclExDt(self, value):
		self._SpclExDt = value if type(value) != base_types.auto else self.make_default("SpclExDt")

	@SpclExDt.deleter
	def SpclExDt(self):
		del self._SpclExDt
		self._SpclExDt = None

	@property
	def CertfctnDdln(self):
		return self._CertfctnDdln

	@CertfctnDdln.setter
	def CertfctnDdln(self, value):
		self._CertfctnDdln = value if type(value) != base_types.auto else self.make_default("CertfctnDdln")

	@CertfctnDdln.deleter
	def CertfctnDdln(self):
		del self._CertfctnDdln
		self._CertfctnDdln = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != base_types.auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def MrgnFxgDt(self):
		return self._MrgnFxgDt

	@MrgnFxgDt.setter
	def MrgnFxgDt(self, value):
		self._MrgnFxgDt = value if type(value) != base_types.auto else self.make_default("MrgnFxgDt")

	@MrgnFxgDt.deleter
	def MrgnFxgDt(self):
		del self._MrgnFxgDt
		self._MrgnFxgDt = None

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if type(value) != base_types.auto else self.make_default("PrtctDt")

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrtApprvlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LpsdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcondlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnForTaxBrkdwnInstr', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltsPblctnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPrtcptnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSspdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverXprtnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlyUcondlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFxgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyClsgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclExDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnFxgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))

