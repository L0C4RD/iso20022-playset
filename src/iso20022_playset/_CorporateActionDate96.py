# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat41Choice
from . import DateFormat49Choice

class CorporateActionDate96(base_types._BaseFieldType):

	__slots__ = ["_AnncmntDt", "_CertfctnDdln", "_CrtApprvlDt", "_DdlnForTaxBrkdwnInstr", "_DdlnToSplt", "_EarlyClsgDt", "_EarlyThrdPtyDdln", "_ElctnToCtrPtyMktDdln", "_ElctnToCtrPtyRspnDdln", "_EqulstnDt", "_ExDvddDt", "_FctvDt", "_FilgDt", "_FrthrDtldAnncmntDt", "_FxgDt", "_GrntedPrtcptnDt", "_HrgDt", "_LeadPlntffDdln", "_LpsdDt", "_LtryDt", "_MktClmTrckgEndDt", "_MrgnFxgDt", "_MtgDt", "_NewMtrtyDt", "_OffclAnncmntPblctnDt", "_PmtDt", "_PrratnDt", "_RcrdDt", "_RegnDdln", "_RsltsPblctnDt", "_SpclExDt", "_ThrdPtyDdln", "_TradgSspdDt", "_UcondlDt", "_WhlyUcondlDt"]
	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if value is not None else base_types.UninitialisedField(self, 'AnncmntDt', DateFormat49Choice, False)

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = base_types.UninitialisedField(self, 'AnncmntDt', DateFormat49Choice, False)

	@property
	def CertfctnDdln(self):
		return self._CertfctnDdln

	@CertfctnDdln.setter
	def CertfctnDdln(self, value):
		self._CertfctnDdln = value if value is not None else base_types.UninitialisedField(self, 'CertfctnDdln', DateFormat49Choice, False)

	@CertfctnDdln.deleter
	def CertfctnDdln(self):
		del self._CertfctnDdln
		self._CertfctnDdln = base_types.UninitialisedField(self, 'CertfctnDdln', DateFormat49Choice, False)

	@property
	def CrtApprvlDt(self):
		return self._CrtApprvlDt

	@CrtApprvlDt.setter
	def CrtApprvlDt(self, value):
		self._CrtApprvlDt = value if value is not None else base_types.UninitialisedField(self, 'CrtApprvlDt', DateFormat41Choice, False)

	@CrtApprvlDt.deleter
	def CrtApprvlDt(self):
		del self._CrtApprvlDt
		self._CrtApprvlDt = base_types.UninitialisedField(self, 'CrtApprvlDt', DateFormat41Choice, False)

	@property
	def DdlnForTaxBrkdwnInstr(self):
		return self._DdlnForTaxBrkdwnInstr

	@DdlnForTaxBrkdwnInstr.setter
	def DdlnForTaxBrkdwnInstr(self, value):
		self._DdlnForTaxBrkdwnInstr = value if value is not None else base_types.UninitialisedField(self, 'DdlnForTaxBrkdwnInstr', DateFormat49Choice, False)

	@DdlnForTaxBrkdwnInstr.deleter
	def DdlnForTaxBrkdwnInstr(self):
		del self._DdlnForTaxBrkdwnInstr
		self._DdlnForTaxBrkdwnInstr = base_types.UninitialisedField(self, 'DdlnForTaxBrkdwnInstr', DateFormat49Choice, False)

	@property
	def DdlnToSplt(self):
		return self._DdlnToSplt

	@DdlnToSplt.setter
	def DdlnToSplt(self, value):
		self._DdlnToSplt = value if value is not None else base_types.UninitialisedField(self, 'DdlnToSplt', DateFormat49Choice, False)

	@DdlnToSplt.deleter
	def DdlnToSplt(self):
		del self._DdlnToSplt
		self._DdlnToSplt = base_types.UninitialisedField(self, 'DdlnToSplt', DateFormat49Choice, False)

	@property
	def EarlyClsgDt(self):
		return self._EarlyClsgDt

	@EarlyClsgDt.setter
	def EarlyClsgDt(self, value):
		self._EarlyClsgDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyClsgDt', DateFormat49Choice, False)

	@EarlyClsgDt.deleter
	def EarlyClsgDt(self):
		del self._EarlyClsgDt
		self._EarlyClsgDt = base_types.UninitialisedField(self, 'EarlyClsgDt', DateFormat49Choice, False)

	@property
	def EarlyThrdPtyDdln(self):
		return self._EarlyThrdPtyDdln

	@EarlyThrdPtyDdln.setter
	def EarlyThrdPtyDdln(self, value):
		self._EarlyThrdPtyDdln = value if value is not None else base_types.UninitialisedField(self, 'EarlyThrdPtyDdln', DateFormat49Choice, False)

	@EarlyThrdPtyDdln.deleter
	def EarlyThrdPtyDdln(self):
		del self._EarlyThrdPtyDdln
		self._EarlyThrdPtyDdln = base_types.UninitialisedField(self, 'EarlyThrdPtyDdln', DateFormat49Choice, False)

	@property
	def ElctnToCtrPtyMktDdln(self):
		return self._ElctnToCtrPtyMktDdln

	@ElctnToCtrPtyMktDdln.setter
	def ElctnToCtrPtyMktDdln(self, value):
		self._ElctnToCtrPtyMktDdln = value if value is not None else base_types.UninitialisedField(self, 'ElctnToCtrPtyMktDdln', DateFormat49Choice, False)

	@ElctnToCtrPtyMktDdln.deleter
	def ElctnToCtrPtyMktDdln(self):
		del self._ElctnToCtrPtyMktDdln
		self._ElctnToCtrPtyMktDdln = base_types.UninitialisedField(self, 'ElctnToCtrPtyMktDdln', DateFormat49Choice, False)

	@property
	def ElctnToCtrPtyRspnDdln(self):
		return self._ElctnToCtrPtyRspnDdln

	@ElctnToCtrPtyRspnDdln.setter
	def ElctnToCtrPtyRspnDdln(self, value):
		self._ElctnToCtrPtyRspnDdln = value if value is not None else base_types.UninitialisedField(self, 'ElctnToCtrPtyRspnDdln', DateFormat49Choice, False)

	@ElctnToCtrPtyRspnDdln.deleter
	def ElctnToCtrPtyRspnDdln(self):
		del self._ElctnToCtrPtyRspnDdln
		self._ElctnToCtrPtyRspnDdln = base_types.UninitialisedField(self, 'ElctnToCtrPtyRspnDdln', DateFormat49Choice, False)

	@property
	def EqulstnDt(self):
		return self._EqulstnDt

	@EqulstnDt.setter
	def EqulstnDt(self, value):
		self._EqulstnDt = value if value is not None else base_types.UninitialisedField(self, 'EqulstnDt', DateFormat41Choice, False)

	@EqulstnDt.deleter
	def EqulstnDt(self):
		del self._EqulstnDt
		self._EqulstnDt = base_types.UninitialisedField(self, 'EqulstnDt', DateFormat41Choice, False)

	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if value is not None else base_types.UninitialisedField(self, 'ExDvddDt', DateFormat41Choice, False)

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = base_types.UninitialisedField(self, 'ExDvddDt', DateFormat41Choice, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', DateFormat41Choice, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', DateFormat41Choice, False)

	@property
	def FilgDt(self):
		return self._FilgDt

	@FilgDt.setter
	def FilgDt(self, value):
		self._FilgDt = value if value is not None else base_types.UninitialisedField(self, 'FilgDt', DateFormat41Choice, False)

	@FilgDt.deleter
	def FilgDt(self):
		del self._FilgDt
		self._FilgDt = base_types.UninitialisedField(self, 'FilgDt', DateFormat41Choice, False)

	@property
	def FrthrDtldAnncmntDt(self):
		return self._FrthrDtldAnncmntDt

	@FrthrDtldAnncmntDt.setter
	def FrthrDtldAnncmntDt(self, value):
		self._FrthrDtldAnncmntDt = value if value is not None else base_types.UninitialisedField(self, 'FrthrDtldAnncmntDt', DateFormat49Choice, False)

	@FrthrDtldAnncmntDt.deleter
	def FrthrDtldAnncmntDt(self):
		del self._FrthrDtldAnncmntDt
		self._FrthrDtldAnncmntDt = base_types.UninitialisedField(self, 'FrthrDtldAnncmntDt', DateFormat49Choice, False)

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if value is not None else base_types.UninitialisedField(self, 'FxgDt', DateFormat49Choice, False)

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = base_types.UninitialisedField(self, 'FxgDt', DateFormat49Choice, False)

	@property
	def GrntedPrtcptnDt(self):
		return self._GrntedPrtcptnDt

	@GrntedPrtcptnDt.setter
	def GrntedPrtcptnDt(self, value):
		self._GrntedPrtcptnDt = value if value is not None else base_types.UninitialisedField(self, 'GrntedPrtcptnDt', DateFormat41Choice, False)

	@GrntedPrtcptnDt.deleter
	def GrntedPrtcptnDt(self):
		del self._GrntedPrtcptnDt
		self._GrntedPrtcptnDt = base_types.UninitialisedField(self, 'GrntedPrtcptnDt', DateFormat41Choice, False)

	@property
	def HrgDt(self):
		return self._HrgDt

	@HrgDt.setter
	def HrgDt(self, value):
		self._HrgDt = value if value is not None else base_types.UninitialisedField(self, 'HrgDt', DateFormat41Choice, False)

	@HrgDt.deleter
	def HrgDt(self):
		del self._HrgDt
		self._HrgDt = base_types.UninitialisedField(self, 'HrgDt', DateFormat41Choice, False)

	@property
	def LeadPlntffDdln(self):
		return self._LeadPlntffDdln

	@LeadPlntffDdln.setter
	def LeadPlntffDdln(self, value):
		self._LeadPlntffDdln = value if value is not None else base_types.UninitialisedField(self, 'LeadPlntffDdln', DateFormat49Choice, False)

	@LeadPlntffDdln.deleter
	def LeadPlntffDdln(self):
		del self._LeadPlntffDdln
		self._LeadPlntffDdln = base_types.UninitialisedField(self, 'LeadPlntffDdln', DateFormat49Choice, False)

	@property
	def LpsdDt(self):
		return self._LpsdDt

	@LpsdDt.setter
	def LpsdDt(self, value):
		self._LpsdDt = value if value is not None else base_types.UninitialisedField(self, 'LpsdDt', DateFormat41Choice, False)

	@LpsdDt.deleter
	def LpsdDt(self):
		del self._LpsdDt
		self._LpsdDt = base_types.UninitialisedField(self, 'LpsdDt', DateFormat41Choice, False)

	@property
	def LtryDt(self):
		return self._LtryDt

	@LtryDt.setter
	def LtryDt(self, value):
		self._LtryDt = value if value is not None else base_types.UninitialisedField(self, 'LtryDt', DateFormat41Choice, False)

	@LtryDt.deleter
	def LtryDt(self):
		del self._LtryDt
		self._LtryDt = base_types.UninitialisedField(self, 'LtryDt', DateFormat41Choice, False)

	@property
	def MktClmTrckgEndDt(self):
		return self._MktClmTrckgEndDt

	@MktClmTrckgEndDt.setter
	def MktClmTrckgEndDt(self, value):
		self._MktClmTrckgEndDt = value if value is not None else base_types.UninitialisedField(self, 'MktClmTrckgEndDt', DateFormat41Choice, False)

	@MktClmTrckgEndDt.deleter
	def MktClmTrckgEndDt(self):
		del self._MktClmTrckgEndDt
		self._MktClmTrckgEndDt = base_types.UninitialisedField(self, 'MktClmTrckgEndDt', DateFormat41Choice, False)

	@property
	def MrgnFxgDt(self):
		return self._MrgnFxgDt

	@MrgnFxgDt.setter
	def MrgnFxgDt(self, value):
		self._MrgnFxgDt = value if value is not None else base_types.UninitialisedField(self, 'MrgnFxgDt', DateFormat41Choice, False)

	@MrgnFxgDt.deleter
	def MrgnFxgDt(self):
		del self._MrgnFxgDt
		self._MrgnFxgDt = base_types.UninitialisedField(self, 'MrgnFxgDt', DateFormat41Choice, False)

	@property
	def MtgDt(self):
		return self._MtgDt

	@MtgDt.setter
	def MtgDt(self, value):
		self._MtgDt = value if value is not None else base_types.UninitialisedField(self, 'MtgDt', DateFormat49Choice, False)

	@MtgDt.deleter
	def MtgDt(self):
		del self._MtgDt
		self._MtgDt = base_types.UninitialisedField(self, 'MtgDt', DateFormat49Choice, False)

	@property
	def NewMtrtyDt(self):
		return self._NewMtrtyDt

	@NewMtrtyDt.setter
	def NewMtrtyDt(self, value):
		self._NewMtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'NewMtrtyDt', DateFormat41Choice, False)

	@NewMtrtyDt.deleter
	def NewMtrtyDt(self):
		del self._NewMtrtyDt
		self._NewMtrtyDt = base_types.UninitialisedField(self, 'NewMtrtyDt', DateFormat41Choice, False)

	@property
	def OffclAnncmntPblctnDt(self):
		return self._OffclAnncmntPblctnDt

	@OffclAnncmntPblctnDt.setter
	def OffclAnncmntPblctnDt(self, value):
		self._OffclAnncmntPblctnDt = value if value is not None else base_types.UninitialisedField(self, 'OffclAnncmntPblctnDt', DateFormat49Choice, False)

	@OffclAnncmntPblctnDt.deleter
	def OffclAnncmntPblctnDt(self):
		del self._OffclAnncmntPblctnDt
		self._OffclAnncmntPblctnDt = base_types.UninitialisedField(self, 'OffclAnncmntPblctnDt', DateFormat49Choice, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat41Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat41Choice, False)

	@property
	def PrratnDt(self):
		return self._PrratnDt

	@PrratnDt.setter
	def PrratnDt(self, value):
		self._PrratnDt = value if value is not None else base_types.UninitialisedField(self, 'PrratnDt', DateFormat41Choice, False)

	@PrratnDt.deleter
	def PrratnDt(self):
		del self._PrratnDt
		self._PrratnDt = base_types.UninitialisedField(self, 'PrratnDt', DateFormat41Choice, False)

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if value is not None else base_types.UninitialisedField(self, 'RcrdDt', DateFormat41Choice, False)

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = base_types.UninitialisedField(self, 'RcrdDt', DateFormat41Choice, False)

	@property
	def RegnDdln(self):
		return self._RegnDdln

	@RegnDdln.setter
	def RegnDdln(self, value):
		self._RegnDdln = value if value is not None else base_types.UninitialisedField(self, 'RegnDdln', DateFormat49Choice, False)

	@RegnDdln.deleter
	def RegnDdln(self):
		del self._RegnDdln
		self._RegnDdln = base_types.UninitialisedField(self, 'RegnDdln', DateFormat49Choice, False)

	@property
	def RsltsPblctnDt(self):
		return self._RsltsPblctnDt

	@RsltsPblctnDt.setter
	def RsltsPblctnDt(self, value):
		self._RsltsPblctnDt = value if value is not None else base_types.UninitialisedField(self, 'RsltsPblctnDt', DateFormat49Choice, False)

	@RsltsPblctnDt.deleter
	def RsltsPblctnDt(self):
		del self._RsltsPblctnDt
		self._RsltsPblctnDt = base_types.UninitialisedField(self, 'RsltsPblctnDt', DateFormat49Choice, False)

	@property
	def SpclExDt(self):
		return self._SpclExDt

	@SpclExDt.setter
	def SpclExDt(self, value):
		self._SpclExDt = value if value is not None else base_types.UninitialisedField(self, 'SpclExDt', DateFormat41Choice, False)

	@SpclExDt.deleter
	def SpclExDt(self):
		del self._SpclExDt
		self._SpclExDt = base_types.UninitialisedField(self, 'SpclExDt', DateFormat41Choice, False)

	@property
	def ThrdPtyDdln(self):
		return self._ThrdPtyDdln

	@ThrdPtyDdln.setter
	def ThrdPtyDdln(self, value):
		self._ThrdPtyDdln = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyDdln', DateFormat49Choice, False)

	@ThrdPtyDdln.deleter
	def ThrdPtyDdln(self):
		del self._ThrdPtyDdln
		self._ThrdPtyDdln = base_types.UninitialisedField(self, 'ThrdPtyDdln', DateFormat49Choice, False)

	@property
	def TradgSspdDt(self):
		return self._TradgSspdDt

	@TradgSspdDt.setter
	def TradgSspdDt(self, value):
		self._TradgSspdDt = value if value is not None else base_types.UninitialisedField(self, 'TradgSspdDt', DateFormat49Choice, False)

	@TradgSspdDt.deleter
	def TradgSspdDt(self):
		del self._TradgSspdDt
		self._TradgSspdDt = base_types.UninitialisedField(self, 'TradgSspdDt', DateFormat49Choice, False)

	@property
	def UcondlDt(self):
		return self._UcondlDt

	@UcondlDt.setter
	def UcondlDt(self, value):
		self._UcondlDt = value if value is not None else base_types.UninitialisedField(self, 'UcondlDt', DateFormat41Choice, False)

	@UcondlDt.deleter
	def UcondlDt(self):
		del self._UcondlDt
		self._UcondlDt = base_types.UninitialisedField(self, 'UcondlDt', DateFormat41Choice, False)

	@property
	def WhlyUcondlDt(self):
		return self._WhlyUcondlDt

	@WhlyUcondlDt.setter
	def WhlyUcondlDt(self, value):
		self._WhlyUcondlDt = value if value is not None else base_types.UninitialisedField(self, 'WhlyUcondlDt', DateFormat41Choice, False)

	@WhlyUcondlDt.deleter
	def WhlyUcondlDt(self):
		del self._WhlyUcondlDt
		self._WhlyUcondlDt = base_types.UninitialisedField(self, 'WhlyUcondlDt', DateFormat41Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnncmntDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrtApprvlDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnForTaxBrkdwnInstr', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnToSplt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyClsgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyThrdPtyDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyMktDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyRspnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FilgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrthrDtldAnncmntDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPrtcptnDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LeadPlntffDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LpsdDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmTrckgEndDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnFxgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewMtrtyDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclAnncmntPblctnDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltsPblctnDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclExDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSspdDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcondlDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlyUcondlDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
	))