from . import base_types
from .PartyIdentification242Choice import PartyIdentification242Choice
from .ISOYear import ISOYear
from .CalculationAgent1Choice import CalculationAgent1Choice
from .CountryCode import CountryCode
from .ContactInformation1 import ContactInformation1
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .AgreementConditions1 import AgreementConditions1
from .Max35Text import Max35Text
from .Max210Text import Max210Text
from .YesNoIndicator import YesNoIndicator
from .Trading1MethodCode import Trading1MethodCode

class GeneralInformation9(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyRef", "_CtctInf", "_DealgBrnchCtrPtySd", "_DefsYr", "_DealgBrnchTradgSd", "_PmtClrCentr", "_AgrmtDtls", "_DealgMtd", "_SndrToRcvrInf", "_ClctnAgt", "_BrkrsRef", "_BrkrId", "_BlckInd", "_BrkrsComssn", "_RltdTradRef"]
	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != base_types.auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if type(value) != base_types.auto else self.make_default("CtctInf")

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = None

	@property
	def DealgBrnchCtrPtySd(self):
		return self._DealgBrnchCtrPtySd

	@DealgBrnchCtrPtySd.setter
	def DealgBrnchCtrPtySd(self, value):
		self._DealgBrnchCtrPtySd = value if type(value) != base_types.auto else self.make_default("DealgBrnchCtrPtySd")

	@DealgBrnchCtrPtySd.deleter
	def DealgBrnchCtrPtySd(self):
		del self._DealgBrnchCtrPtySd
		self._DealgBrnchCtrPtySd = None

	@property
	def DefsYr(self):
		return self._DefsYr

	@DefsYr.setter
	def DefsYr(self, value):
		self._DefsYr = value if type(value) != base_types.auto else self.make_default("DefsYr")

	@DefsYr.deleter
	def DefsYr(self):
		del self._DefsYr
		self._DefsYr = None

	@property
	def DealgBrnchTradgSd(self):
		return self._DealgBrnchTradgSd

	@DealgBrnchTradgSd.setter
	def DealgBrnchTradgSd(self, value):
		self._DealgBrnchTradgSd = value if type(value) != base_types.auto else self.make_default("DealgBrnchTradgSd")

	@DealgBrnchTradgSd.deleter
	def DealgBrnchTradgSd(self):
		del self._DealgBrnchTradgSd
		self._DealgBrnchTradgSd = None

	@property
	def PmtClrCentr(self):
		return self._PmtClrCentr

	@PmtClrCentr.setter
	def PmtClrCentr(self, value):
		self._PmtClrCentr = value if type(value) != base_types.auto else self.make_default("PmtClrCentr")

	@PmtClrCentr.deleter
	def PmtClrCentr(self):
		del self._PmtClrCentr
		self._PmtClrCentr = None

	@property
	def AgrmtDtls(self):
		return self._AgrmtDtls

	@AgrmtDtls.setter
	def AgrmtDtls(self, value):
		self._AgrmtDtls = value if type(value) != base_types.auto else self.make_default("AgrmtDtls")

	@AgrmtDtls.deleter
	def AgrmtDtls(self):
		del self._AgrmtDtls
		self._AgrmtDtls = None

	@property
	def DealgMtd(self):
		return self._DealgMtd

	@DealgMtd.setter
	def DealgMtd(self, value):
		self._DealgMtd = value if type(value) != base_types.auto else self.make_default("DealgMtd")

	@DealgMtd.deleter
	def DealgMtd(self):
		del self._DealgMtd
		self._DealgMtd = None

	@property
	def SndrToRcvrInf(self):
		return self._SndrToRcvrInf

	@SndrToRcvrInf.setter
	def SndrToRcvrInf(self, value):
		self._SndrToRcvrInf = value if type(value) != base_types.auto else self.make_default("SndrToRcvrInf")

	@SndrToRcvrInf.deleter
	def SndrToRcvrInf(self):
		del self._SndrToRcvrInf
		self._SndrToRcvrInf = None

	@property
	def ClctnAgt(self):
		return self._ClctnAgt

	@ClctnAgt.setter
	def ClctnAgt(self, value):
		self._ClctnAgt = value if type(value) != base_types.auto else self.make_default("ClctnAgt")

	@ClctnAgt.deleter
	def ClctnAgt(self):
		del self._ClctnAgt
		self._ClctnAgt = None

	@property
	def BrkrsRef(self):
		return self._BrkrsRef

	@BrkrsRef.setter
	def BrkrsRef(self, value):
		self._BrkrsRef = value if type(value) != base_types.auto else self.make_default("BrkrsRef")

	@BrkrsRef.deleter
	def BrkrsRef(self):
		del self._BrkrsRef
		self._BrkrsRef = None

	@property
	def BrkrId(self):
		return self._BrkrId

	@BrkrId.setter
	def BrkrId(self, value):
		self._BrkrId = value if type(value) != base_types.auto else self.make_default("BrkrId")

	@BrkrId.deleter
	def BrkrId(self):
		del self._BrkrId
		self._BrkrId = None

	@property
	def BlckInd(self):
		return self._BlckInd

	@BlckInd.setter
	def BlckInd(self, value):
		self._BlckInd = value if type(value) != base_types.auto else self.make_default("BlckInd")

	@BlckInd.deleter
	def BlckInd(self):
		del self._BlckInd
		self._BlckInd = None

	@property
	def BrkrsComssn(self):
		return self._BrkrsComssn

	@BrkrsComssn.setter
	def BrkrsComssn(self, value):
		self._BrkrsComssn = value if type(value) != base_types.auto else self.make_default("BrkrsComssn")

	@BrkrsComssn.deleter
	def BrkrsComssn(self):
		del self._BrkrsComssn
		self._BrkrsComssn = None

	@property
	def RltdTradRef(self):
		return self._RltdTradRef

	@RltdTradRef.setter
	def RltdTradRef(self, value):
		self._RltdTradRef = value if type(value) != base_types.auto else self.make_default("RltdTradRef")

	@RltdTradRef.deleter
	def RltdTradRef(self):
		del self._RltdTradRef
		self._RltdTradRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgBrnchCtrPtySd', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DefsYr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgBrnchTradgSd', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtClrCentr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtDtls', type=AgreementConditions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgMtd', type=Trading1MethodCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrToRcvrInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnAgt', type=CalculationAgent1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrsRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrsComssn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTradRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

