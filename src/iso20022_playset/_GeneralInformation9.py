# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AgreementConditions1
from . import CalculationAgent1Choice
from . import ContactInformation1
from . import CountryCode
from . import ISOYear
from . import Max210Text
from . import Max35Text
from . import PartyIdentification242Choice
from . import Trading1MethodCode
from . import YesNoIndicator

class GeneralInformation9(base_types._BaseFieldType):

	__slots__ = ["_AgrmtDtls", "_BlckInd", "_BrkrId", "_BrkrsComssn", "_BrkrsRef", "_ClctnAgt", "_CtctInf", "_CtrPtyRef", "_DealgBrnchCtrPtySd", "_DealgBrnchTradgSd", "_DealgMtd", "_DefsYr", "_PmtClrCentr", "_RltdTradRef", "_SndrToRcvrInf"]
	@property
	def AgrmtDtls(self):
		return self._AgrmtDtls

	@AgrmtDtls.setter
	def AgrmtDtls(self, value):
		self._AgrmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AgrmtDtls', AgreementConditions1, False)

	@AgrmtDtls.deleter
	def AgrmtDtls(self):
		del self._AgrmtDtls
		self._AgrmtDtls = base_types.UninitialisedField(self, 'AgrmtDtls', AgreementConditions1, False)

	@property
	def BlckInd(self):
		return self._BlckInd

	@BlckInd.setter
	def BlckInd(self, value):
		self._BlckInd = value if value is not None else base_types.UninitialisedField(self, 'BlckInd', YesNoIndicator, False)

	@BlckInd.deleter
	def BlckInd(self):
		del self._BlckInd
		self._BlckInd = base_types.UninitialisedField(self, 'BlckInd', YesNoIndicator, False)

	@property
	def BrkrId(self):
		return self._BrkrId

	@BrkrId.setter
	def BrkrId(self, value):
		self._BrkrId = value if value is not None else base_types.UninitialisedField(self, 'BrkrId', PartyIdentification242Choice, False)

	@BrkrId.deleter
	def BrkrId(self):
		del self._BrkrId
		self._BrkrId = base_types.UninitialisedField(self, 'BrkrId', PartyIdentification242Choice, False)

	@property
	def BrkrsComssn(self):
		return self._BrkrsComssn

	@BrkrsComssn.setter
	def BrkrsComssn(self, value):
		self._BrkrsComssn = value if value is not None else base_types.UninitialisedField(self, 'BrkrsComssn', ActiveCurrencyAndAmount, False)

	@BrkrsComssn.deleter
	def BrkrsComssn(self):
		del self._BrkrsComssn
		self._BrkrsComssn = base_types.UninitialisedField(self, 'BrkrsComssn', ActiveCurrencyAndAmount, False)

	@property
	def BrkrsRef(self):
		return self._BrkrsRef

	@BrkrsRef.setter
	def BrkrsRef(self, value):
		self._BrkrsRef = value if value is not None else base_types.UninitialisedField(self, 'BrkrsRef', Max35Text, False)

	@BrkrsRef.deleter
	def BrkrsRef(self):
		del self._BrkrsRef
		self._BrkrsRef = base_types.UninitialisedField(self, 'BrkrsRef', Max35Text, False)

	@property
	def ClctnAgt(self):
		return self._ClctnAgt

	@ClctnAgt.setter
	def ClctnAgt(self, value):
		self._ClctnAgt = value if value is not None else base_types.UninitialisedField(self, 'ClctnAgt', CalculationAgent1Choice, False)

	@ClctnAgt.deleter
	def ClctnAgt(self):
		del self._ClctnAgt
		self._ClctnAgt = base_types.UninitialisedField(self, 'ClctnAgt', CalculationAgent1Choice, False)

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if value is not None else base_types.UninitialisedField(self, 'CtctInf', ContactInformation1, False)

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = base_types.UninitialisedField(self, 'CtctInf', ContactInformation1, False)

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRef', Max35Text, False)

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = base_types.UninitialisedField(self, 'CtrPtyRef', Max35Text, False)

	@property
	def DealgBrnchCtrPtySd(self):
		return self._DealgBrnchCtrPtySd

	@DealgBrnchCtrPtySd.setter
	def DealgBrnchCtrPtySd(self, value):
		self._DealgBrnchCtrPtySd = value if value is not None else base_types.UninitialisedField(self, 'DealgBrnchCtrPtySd', PartyIdentification242Choice, False)

	@DealgBrnchCtrPtySd.deleter
	def DealgBrnchCtrPtySd(self):
		del self._DealgBrnchCtrPtySd
		self._DealgBrnchCtrPtySd = base_types.UninitialisedField(self, 'DealgBrnchCtrPtySd', PartyIdentification242Choice, False)

	@property
	def DealgBrnchTradgSd(self):
		return self._DealgBrnchTradgSd

	@DealgBrnchTradgSd.setter
	def DealgBrnchTradgSd(self, value):
		self._DealgBrnchTradgSd = value if value is not None else base_types.UninitialisedField(self, 'DealgBrnchTradgSd', PartyIdentification242Choice, False)

	@DealgBrnchTradgSd.deleter
	def DealgBrnchTradgSd(self):
		del self._DealgBrnchTradgSd
		self._DealgBrnchTradgSd = base_types.UninitialisedField(self, 'DealgBrnchTradgSd', PartyIdentification242Choice, False)

	@property
	def DealgMtd(self):
		return self._DealgMtd

	@DealgMtd.setter
	def DealgMtd(self, value):
		self._DealgMtd = value if value is not None else base_types.UninitialisedField(self, 'DealgMtd', Trading1MethodCode, False)

	@DealgMtd.deleter
	def DealgMtd(self):
		del self._DealgMtd
		self._DealgMtd = base_types.UninitialisedField(self, 'DealgMtd', Trading1MethodCode, False)

	@property
	def DefsYr(self):
		return self._DefsYr

	@DefsYr.setter
	def DefsYr(self, value):
		self._DefsYr = value if value is not None else base_types.UninitialisedField(self, 'DefsYr', ISOYear, False)

	@DefsYr.deleter
	def DefsYr(self):
		del self._DefsYr
		self._DefsYr = base_types.UninitialisedField(self, 'DefsYr', ISOYear, False)

	@property
	def PmtClrCentr(self):
		return self._PmtClrCentr

	@PmtClrCentr.setter
	def PmtClrCentr(self, value):
		self._PmtClrCentr = value if value is not None else base_types.UninitialisedField(self, 'PmtClrCentr', CountryCode, False)

	@PmtClrCentr.deleter
	def PmtClrCentr(self):
		del self._PmtClrCentr
		self._PmtClrCentr = base_types.UninitialisedField(self, 'PmtClrCentr', CountryCode, False)

	@property
	def RltdTradRef(self):
		return self._RltdTradRef

	@RltdTradRef.setter
	def RltdTradRef(self, value):
		self._RltdTradRef = value if value is not None else base_types.UninitialisedField(self, 'RltdTradRef', Max35Text, False)

	@RltdTradRef.deleter
	def RltdTradRef(self):
		del self._RltdTradRef
		self._RltdTradRef = base_types.UninitialisedField(self, 'RltdTradRef', Max35Text, False)

	@property
	def SndrToRcvrInf(self):
		return self._SndrToRcvrInf

	@SndrToRcvrInf.setter
	def SndrToRcvrInf(self, value):
		self._SndrToRcvrInf = value if value is not None else base_types.UninitialisedField(self, 'SndrToRcvrInf', Max210Text, False)

	@SndrToRcvrInf.deleter
	def SndrToRcvrInf(self):
		del self._SndrToRcvrInf
		self._SndrToRcvrInf = base_types.UninitialisedField(self, 'SndrToRcvrInf', Max210Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtDtls', type=AgreementConditions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrsComssn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrsRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnAgt', type=CalculationAgent1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgBrnchCtrPtySd', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgBrnchTradgSd', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgMtd', type=Trading1MethodCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DefsYr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtClrCentr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTradRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrToRcvrInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))