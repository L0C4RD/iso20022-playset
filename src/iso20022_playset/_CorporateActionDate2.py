# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat4Choice

class CorporateActionDate2(base_types._BaseFieldType):

	__slots__ = ["_CertfctnDdln", "_CoverXprtnDt", "_CrtApprvlDt", "_DdlnForTaxBrkdwnInstr", "_EarlyClsgDt", "_ElctnToCtrPtyDdln", "_EqulstnDt", "_ExDvddDt", "_FctvDt", "_GrntedPrtcptnDt", "_IndxFxgDt", "_LpsdDt", "_LtryDt", "_MrgnFxgDt", "_MtrtyDt", "_PrratnDt", "_PrtctDt", "_RcrdDt", "_RedDt", "_RegnDdln", "_RsltsPblctnDt", "_SpclExDt", "_TradgSspdDt", "_UcondlDt", "_WhlyUcondlDt"]
	@property
	def CertfctnDdln(self):
		return self._CertfctnDdln

	@CertfctnDdln.setter
	def CertfctnDdln(self, value):
		self._CertfctnDdln = value if value is not None else base_types.UninitialisedField(self, 'CertfctnDdln', DateFormat4Choice, False)

	@CertfctnDdln.deleter
	def CertfctnDdln(self):
		del self._CertfctnDdln
		self._CertfctnDdln = base_types.UninitialisedField(self, 'CertfctnDdln', DateFormat4Choice, False)

	@property
	def CoverXprtnDt(self):
		return self._CoverXprtnDt

	@CoverXprtnDt.setter
	def CoverXprtnDt(self, value):
		self._CoverXprtnDt = value if value is not None else base_types.UninitialisedField(self, 'CoverXprtnDt', DateFormat4Choice, False)

	@CoverXprtnDt.deleter
	def CoverXprtnDt(self):
		del self._CoverXprtnDt
		self._CoverXprtnDt = base_types.UninitialisedField(self, 'CoverXprtnDt', DateFormat4Choice, False)

	@property
	def CrtApprvlDt(self):
		return self._CrtApprvlDt

	@CrtApprvlDt.setter
	def CrtApprvlDt(self, value):
		self._CrtApprvlDt = value if value is not None else base_types.UninitialisedField(self, 'CrtApprvlDt', DateFormat4Choice, False)

	@CrtApprvlDt.deleter
	def CrtApprvlDt(self):
		del self._CrtApprvlDt
		self._CrtApprvlDt = base_types.UninitialisedField(self, 'CrtApprvlDt', DateFormat4Choice, False)

	@property
	def DdlnForTaxBrkdwnInstr(self):
		return self._DdlnForTaxBrkdwnInstr

	@DdlnForTaxBrkdwnInstr.setter
	def DdlnForTaxBrkdwnInstr(self, value):
		self._DdlnForTaxBrkdwnInstr = value if value is not None else base_types.UninitialisedField(self, 'DdlnForTaxBrkdwnInstr', DateFormat4Choice, False)

	@DdlnForTaxBrkdwnInstr.deleter
	def DdlnForTaxBrkdwnInstr(self):
		del self._DdlnForTaxBrkdwnInstr
		self._DdlnForTaxBrkdwnInstr = base_types.UninitialisedField(self, 'DdlnForTaxBrkdwnInstr', DateFormat4Choice, False)

	@property
	def EarlyClsgDt(self):
		return self._EarlyClsgDt

	@EarlyClsgDt.setter
	def EarlyClsgDt(self, value):
		self._EarlyClsgDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyClsgDt', DateFormat4Choice, False)

	@EarlyClsgDt.deleter
	def EarlyClsgDt(self):
		del self._EarlyClsgDt
		self._EarlyClsgDt = base_types.UninitialisedField(self, 'EarlyClsgDt', DateFormat4Choice, False)

	@property
	def ElctnToCtrPtyDdln(self):
		return self._ElctnToCtrPtyDdln

	@ElctnToCtrPtyDdln.setter
	def ElctnToCtrPtyDdln(self, value):
		self._ElctnToCtrPtyDdln = value if value is not None else base_types.UninitialisedField(self, 'ElctnToCtrPtyDdln', DateFormat4Choice, False)

	@ElctnToCtrPtyDdln.deleter
	def ElctnToCtrPtyDdln(self):
		del self._ElctnToCtrPtyDdln
		self._ElctnToCtrPtyDdln = base_types.UninitialisedField(self, 'ElctnToCtrPtyDdln', DateFormat4Choice, False)

	@property
	def EqulstnDt(self):
		return self._EqulstnDt

	@EqulstnDt.setter
	def EqulstnDt(self, value):
		self._EqulstnDt = value if value is not None else base_types.UninitialisedField(self, 'EqulstnDt', DateFormat4Choice, False)

	@EqulstnDt.deleter
	def EqulstnDt(self):
		del self._EqulstnDt
		self._EqulstnDt = base_types.UninitialisedField(self, 'EqulstnDt', DateFormat4Choice, False)

	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if value is not None else base_types.UninitialisedField(self, 'ExDvddDt', DateFormat4Choice, False)

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = base_types.UninitialisedField(self, 'ExDvddDt', DateFormat4Choice, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', DateFormat4Choice, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', DateFormat4Choice, False)

	@property
	def GrntedPrtcptnDt(self):
		return self._GrntedPrtcptnDt

	@GrntedPrtcptnDt.setter
	def GrntedPrtcptnDt(self, value):
		self._GrntedPrtcptnDt = value if value is not None else base_types.UninitialisedField(self, 'GrntedPrtcptnDt', DateFormat4Choice, False)

	@GrntedPrtcptnDt.deleter
	def GrntedPrtcptnDt(self):
		del self._GrntedPrtcptnDt
		self._GrntedPrtcptnDt = base_types.UninitialisedField(self, 'GrntedPrtcptnDt', DateFormat4Choice, False)

	@property
	def IndxFxgDt(self):
		return self._IndxFxgDt

	@IndxFxgDt.setter
	def IndxFxgDt(self, value):
		self._IndxFxgDt = value if value is not None else base_types.UninitialisedField(self, 'IndxFxgDt', DateFormat4Choice, False)

	@IndxFxgDt.deleter
	def IndxFxgDt(self):
		del self._IndxFxgDt
		self._IndxFxgDt = base_types.UninitialisedField(self, 'IndxFxgDt', DateFormat4Choice, False)

	@property
	def LpsdDt(self):
		return self._LpsdDt

	@LpsdDt.setter
	def LpsdDt(self, value):
		self._LpsdDt = value if value is not None else base_types.UninitialisedField(self, 'LpsdDt', DateFormat4Choice, False)

	@LpsdDt.deleter
	def LpsdDt(self):
		del self._LpsdDt
		self._LpsdDt = base_types.UninitialisedField(self, 'LpsdDt', DateFormat4Choice, False)

	@property
	def LtryDt(self):
		return self._LtryDt

	@LtryDt.setter
	def LtryDt(self, value):
		self._LtryDt = value if value is not None else base_types.UninitialisedField(self, 'LtryDt', DateFormat4Choice, False)

	@LtryDt.deleter
	def LtryDt(self):
		del self._LtryDt
		self._LtryDt = base_types.UninitialisedField(self, 'LtryDt', DateFormat4Choice, False)

	@property
	def MrgnFxgDt(self):
		return self._MrgnFxgDt

	@MrgnFxgDt.setter
	def MrgnFxgDt(self, value):
		self._MrgnFxgDt = value if value is not None else base_types.UninitialisedField(self, 'MrgnFxgDt', DateFormat4Choice, False)

	@MrgnFxgDt.deleter
	def MrgnFxgDt(self):
		del self._MrgnFxgDt
		self._MrgnFxgDt = base_types.UninitialisedField(self, 'MrgnFxgDt', DateFormat4Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', DateFormat4Choice, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', DateFormat4Choice, False)

	@property
	def PrratnDt(self):
		return self._PrratnDt

	@PrratnDt.setter
	def PrratnDt(self, value):
		self._PrratnDt = value if value is not None else base_types.UninitialisedField(self, 'PrratnDt', DateFormat4Choice, False)

	@PrratnDt.deleter
	def PrratnDt(self):
		del self._PrratnDt
		self._PrratnDt = base_types.UninitialisedField(self, 'PrratnDt', DateFormat4Choice, False)

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if value is not None else base_types.UninitialisedField(self, 'PrtctDt', DateFormat4Choice, False)

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = base_types.UninitialisedField(self, 'PrtctDt', DateFormat4Choice, False)

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if value is not None else base_types.UninitialisedField(self, 'RcrdDt', DateFormat4Choice, False)

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = base_types.UninitialisedField(self, 'RcrdDt', DateFormat4Choice, False)

	@property
	def RedDt(self):
		return self._RedDt

	@RedDt.setter
	def RedDt(self, value):
		self._RedDt = value if value is not None else base_types.UninitialisedField(self, 'RedDt', DateFormat4Choice, False)

	@RedDt.deleter
	def RedDt(self):
		del self._RedDt
		self._RedDt = base_types.UninitialisedField(self, 'RedDt', DateFormat4Choice, False)

	@property
	def RegnDdln(self):
		return self._RegnDdln

	@RegnDdln.setter
	def RegnDdln(self, value):
		self._RegnDdln = value if value is not None else base_types.UninitialisedField(self, 'RegnDdln', DateFormat4Choice, False)

	@RegnDdln.deleter
	def RegnDdln(self):
		del self._RegnDdln
		self._RegnDdln = base_types.UninitialisedField(self, 'RegnDdln', DateFormat4Choice, False)

	@property
	def RsltsPblctnDt(self):
		return self._RsltsPblctnDt

	@RsltsPblctnDt.setter
	def RsltsPblctnDt(self, value):
		self._RsltsPblctnDt = value if value is not None else base_types.UninitialisedField(self, 'RsltsPblctnDt', DateFormat4Choice, False)

	@RsltsPblctnDt.deleter
	def RsltsPblctnDt(self):
		del self._RsltsPblctnDt
		self._RsltsPblctnDt = base_types.UninitialisedField(self, 'RsltsPblctnDt', DateFormat4Choice, False)

	@property
	def SpclExDt(self):
		return self._SpclExDt

	@SpclExDt.setter
	def SpclExDt(self, value):
		self._SpclExDt = value if value is not None else base_types.UninitialisedField(self, 'SpclExDt', DateFormat4Choice, False)

	@SpclExDt.deleter
	def SpclExDt(self):
		del self._SpclExDt
		self._SpclExDt = base_types.UninitialisedField(self, 'SpclExDt', DateFormat4Choice, False)

	@property
	def TradgSspdDt(self):
		return self._TradgSspdDt

	@TradgSspdDt.setter
	def TradgSspdDt(self, value):
		self._TradgSspdDt = value if value is not None else base_types.UninitialisedField(self, 'TradgSspdDt', DateFormat4Choice, False)

	@TradgSspdDt.deleter
	def TradgSspdDt(self):
		del self._TradgSspdDt
		self._TradgSspdDt = base_types.UninitialisedField(self, 'TradgSspdDt', DateFormat4Choice, False)

	@property
	def UcondlDt(self):
		return self._UcondlDt

	@UcondlDt.setter
	def UcondlDt(self, value):
		self._UcondlDt = value if value is not None else base_types.UninitialisedField(self, 'UcondlDt', DateFormat4Choice, False)

	@UcondlDt.deleter
	def UcondlDt(self):
		del self._UcondlDt
		self._UcondlDt = base_types.UninitialisedField(self, 'UcondlDt', DateFormat4Choice, False)

	@property
	def WhlyUcondlDt(self):
		return self._WhlyUcondlDt

	@WhlyUcondlDt.setter
	def WhlyUcondlDt(self, value):
		self._WhlyUcondlDt = value if value is not None else base_types.UninitialisedField(self, 'WhlyUcondlDt', DateFormat4Choice, False)

	@WhlyUcondlDt.deleter
	def WhlyUcondlDt(self):
		del self._WhlyUcondlDt
		self._WhlyUcondlDt = base_types.UninitialisedField(self, 'WhlyUcondlDt', DateFormat4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertfctnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverXprtnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrtApprvlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdlnForTaxBrkdwnInstr', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyClsgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnToCtrPtyDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPrtcptnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFxgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LpsdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnFxgDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDdln', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltsPblctnDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclExDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSspdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcondlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlyUcondlDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))