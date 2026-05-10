from . import base_types
from ._DateFormat30Choice import DateFormat30Choice
from ._DateFormat43Choice import DateFormat43Choice

class CorporateActionDate83(base_types._BaseFieldType):

	__slots__ = ["_AnncmntDt", "_CertfctnDdln", "_CrtApprvlDt", "_DdlnForTaxBrkdwnInstr", "_DdlnToSplt", "_EarlyClsgDt", "_EarlyThrdPtyDdln", "_ElctnToCtrPtyMktDdln", "_ElctnToCtrPtyRspnDdln", "_EqulstnDt", "_ExDvddDt", "_FctvDt", "_FilgDt", "_FrthrDtldAnncmntDt", "_FxgDt", "_GrntedPrtcptnDt", "_HrgDt", "_LeadPlntffDdln", "_LpsdDt", "_LtryDt", "_MktClmTrckgEndDt", "_MrgnFxgDt", "_MtgDt", "_NewMtrtyDt", "_OffclAnncmntPblctnDt", "_PmtDt", "_PrratnDt", "_RcrdDt", "_RegnDdln", "_RsltsPblctnDt", "_SpclExDt", "_ThrdPtyDdln", "_TradgSspdDt", "_UcondlDt", "_WhlyUcondlDt"]
	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if type(value) != base_types.auto else self.make_default("AnncmntDt")

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = None

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
	def EarlyThrdPtyDdln(self):
		return self._EarlyThrdPtyDdln

	@EarlyThrdPtyDdln.setter
	def EarlyThrdPtyDdln(self, value):
		self._EarlyThrdPtyDdln = value if type(value) != base_types.auto else self.make_default("EarlyThrdPtyDdln")

	@EarlyThrdPtyDdln.deleter
	def EarlyThrdPtyDdln(self):
		del self._EarlyThrdPtyDdln
		self._EarlyThrdPtyDdln = None

	@property
	def ElctnToCtrPtyMktDdln(self):
		return self._ElctnToCtrPtyMktDdln

	@ElctnToCtrPtyMktDdln.setter
	def ElctnToCtrPtyMktDdln(self, value):
		self._ElctnToCtrPtyMktDdln = value if type(value) != base_types.auto else self.make_default("ElctnToCtrPtyMktDdln")

	@ElctnToCtrPtyMktDdln.deleter
	def ElctnToCtrPtyMktDdln(self):
		del self._ElctnToCtrPtyMktDdln
		self._ElctnToCtrPtyMktDdln = None

	@property
	def ElctnToCtrPtyRspnDdln(self):
		return self._ElctnToCtrPtyRspnDdln

	@ElctnToCtrPtyRspnDdln.setter
	def ElctnToCtrPtyRspnDdln(self, value):
		self._ElctnToCtrPtyRspnDdln = value if type(value) != base_types.auto else self.make_default("ElctnToCtrPtyRspnDdln")

	@ElctnToCtrPtyRspnDdln.deleter
	def ElctnToCtrPtyRspnDdln(self):
		del self._ElctnToCtrPtyRspnDdln
		self._ElctnToCtrPtyRspnDdln = None

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
	def FilgDt(self):
		return self._FilgDt

	@FilgDt.setter
	def FilgDt(self, value):
		self._FilgDt = value if type(value) != base_types.auto else self.make_default("FilgDt")

	@FilgDt.deleter
	def FilgDt(self):
		del self._FilgDt
		self._FilgDt = None

	@property
	def FrthrDtldAnncmntDt(self):
		return self._FrthrDtldAnncmntDt

	@FrthrDtldAnncmntDt.setter
	def FrthrDtldAnncmntDt(self, value):
		self._FrthrDtldAnncmntDt = value if type(value) != base_types.auto else self.make_default("FrthrDtldAnncmntDt")

	@FrthrDtldAnncmntDt.deleter
	def FrthrDtldAnncmntDt(self):
		del self._FrthrDtldAnncmntDt
		self._FrthrDtldAnncmntDt = None

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if type(value) != base_types.auto else self.make_default("FxgDt")

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = None

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
	def HrgDt(self):
		return self._HrgDt

	@HrgDt.setter
	def HrgDt(self, value):
		self._HrgDt = value if type(value) != base_types.auto else self.make_default("HrgDt")

	@HrgDt.deleter
	def HrgDt(self):
		del self._HrgDt
		self._HrgDt = None

	@property
	def LeadPlntffDdln(self):
		return self._LeadPlntffDdln

	@LeadPlntffDdln.setter
	def LeadPlntffDdln(self, value):
		self._LeadPlntffDdln = value if type(value) != base_types.auto else self.make_default("LeadPlntffDdln")

	@LeadPlntffDdln.deleter
	def LeadPlntffDdln(self):
		del self._LeadPlntffDdln
		self._LeadPlntffDdln = None

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
	def MktClmTrckgEndDt(self):
		return self._MktClmTrckgEndDt

	@MktClmTrckgEndDt.setter
	def MktClmTrckgEndDt(self, value):
		self._MktClmTrckgEndDt = value if type(value) != base_types.auto else self.make_default("MktClmTrckgEndDt")

	@MktClmTrckgEndDt.deleter
	def MktClmTrckgEndDt(self):
		del self._MktClmTrckgEndDt
		self._MktClmTrckgEndDt = None

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
	def MtgDt(self):
		return self._MtgDt

	@MtgDt.setter
	def MtgDt(self, value):
		self._MtgDt = value if type(value) != base_types.auto else self.make_default("MtgDt")

	@MtgDt.deleter
	def MtgDt(self):
		del self._MtgDt
		self._MtgDt = None

	@property
	def NewMtrtyDt(self):
		return self._NewMtrtyDt

	@NewMtrtyDt.setter
	def NewMtrtyDt(self, value):
		self._NewMtrtyDt = value if type(value) != base_types.auto else self.make_default("NewMtrtyDt")

	@NewMtrtyDt.deleter
	def NewMtrtyDt(self):
		del self._NewMtrtyDt
		self._NewMtrtyDt = None

	@property
	def OffclAnncmntPblctnDt(self):
		return self._OffclAnncmntPblctnDt

	@OffclAnncmntPblctnDt.setter
	def OffclAnncmntPblctnDt(self, value):
		self._OffclAnncmntPblctnDt = value if type(value) != base_types.auto else self.make_default("OffclAnncmntPblctnDt")

	@OffclAnncmntPblctnDt.deleter
	def OffclAnncmntPblctnDt(self):
		del self._OffclAnncmntPblctnDt
		self._OffclAnncmntPblctnDt = None

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
	def ThrdPtyDdln(self):
		return self._ThrdPtyDdln

	@ThrdPtyDdln.setter
	def ThrdPtyDdln(self, value):
		self._ThrdPtyDdln = value if type(value) != base_types.auto else self.make_default("ThrdPtyDdln")

	@ThrdPtyDdln.deleter
	def ThrdPtyDdln(self):
		del self._ThrdPtyDdln
		self._ThrdPtyDdln = None

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
	def WhlyUcondlDt(self):
		return self._WhlyUcondlDt

	@WhlyUcondlDt.setter
	def WhlyUcondlDt(self, value):
		self._WhlyUcondlDt = value if type(value) != base_types.auto else self.make_default("WhlyUcondlDt")

	@WhlyUcondlDt.deleter
	def WhlyUcondlDt(self):
		del self._WhlyUcondlDt
		self._WhlyUcondlDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnncmntDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrtApprvlDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnForTaxBrkdwnInstr', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnToSplt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyClsgDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyThrdPtyDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyMktDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyRspnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FilgDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrthrDtldAnncmntDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPrtcptnDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrgDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LeadPlntffDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LpsdDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmTrckgEndDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnFxgDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewMtrtyDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclAnncmntPblctnDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltsPblctnDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclExDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSspdDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcondlDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlyUcondlDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
	))

