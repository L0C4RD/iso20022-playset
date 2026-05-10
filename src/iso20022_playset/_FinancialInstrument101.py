from . import base_types
from ._Account28 import Account28
from ._AdditionalReference10 import AdditionalReference10
from ._Max35Text import Max35Text
from ._YesNoIndicator import YesNoIndicator
from ._FinancialInstrument61Choice import FinancialInstrument61Choice
from ._FundSettlementParameters18 import FundSettlementParameters18
from ._AdditionalInformation15 import AdditionalInformation15

class FinancialInstrument101(base_types._BaseFieldType):

	__slots__ = ["_AsstsHeldInOwnNm", "_TrfRsltsInChngOfBnfclOwnr", "_SttlmPtiesDtls", "_CtrPtyRef", "_Instrm", "_Trfr", "_ClntRef", "_AddtlInf", "_TrfeeAcct", "_LineId"]
	@property
	def AsstsHeldInOwnNm(self):
		return self._AsstsHeldInOwnNm

	@AsstsHeldInOwnNm.setter
	def AsstsHeldInOwnNm(self, value):
		self._AsstsHeldInOwnNm = value if type(value) != base_types.auto else self.make_default("AsstsHeldInOwnNm")

	@AsstsHeldInOwnNm.deleter
	def AsstsHeldInOwnNm(self):
		del self._AsstsHeldInOwnNm
		self._AsstsHeldInOwnNm = None

	@property
	def TrfRsltsInChngOfBnfclOwnr(self):
		return self._TrfRsltsInChngOfBnfclOwnr

	@TrfRsltsInChngOfBnfclOwnr.setter
	def TrfRsltsInChngOfBnfclOwnr(self, value):
		self._TrfRsltsInChngOfBnfclOwnr = value if type(value) != base_types.auto else self.make_default("TrfRsltsInChngOfBnfclOwnr")

	@TrfRsltsInChngOfBnfclOwnr.deleter
	def TrfRsltsInChngOfBnfclOwnr(self):
		del self._TrfRsltsInChngOfBnfclOwnr
		self._TrfRsltsInChngOfBnfclOwnr = None

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if type(value) != base_types.auto else self.make_default("SttlmPtiesDtls")

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = None

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
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != base_types.auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if type(value) != base_types.auto else self.make_default("Trfr")

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def TrfeeAcct(self):
		return self._TrfeeAcct

	@TrfeeAcct.setter
	def TrfeeAcct(self, value):
		self._TrfeeAcct = value if type(value) != base_types.auto else self.make_default("TrfeeAcct")

	@TrfeeAcct.deleter
	def TrfeeAcct(self):
		del self._TrfeeAcct
		self._TrfeeAcct = None

	@property
	def LineId(self):
		return self._LineId

	@LineId.setter
	def LineId(self, value):
		self._LineId = value if type(value) != base_types.auto else self.make_default("LineId")

	@LineId.deleter
	def LineId(self):
		del self._LineId
		self._LineId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument61Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfeeAcct', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

