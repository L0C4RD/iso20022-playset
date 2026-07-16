# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account28
from . import AdditionalInformation15
from . import AdditionalReference10
from . import FinancialInstrument61Choice
from . import FundSettlementParameters18
from . import Max35Text
from . import YesNoIndicator

class FinancialInstrument101(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AsstsHeldInOwnNm", "_ClntRef", "_CtrPtyRef", "_Instrm", "_LineId", "_SttlmPtiesDtls", "_TrfRsltsInChngOfBnfclOwnr", "_TrfeeAcct", "_Trfr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def AsstsHeldInOwnNm(self):
		return self._AsstsHeldInOwnNm

	@AsstsHeldInOwnNm.setter
	def AsstsHeldInOwnNm(self, value):
		self._AsstsHeldInOwnNm = value if value is not None else base_types.UninitialisedField(self, 'AsstsHeldInOwnNm', YesNoIndicator, False)

	@AsstsHeldInOwnNm.deleter
	def AsstsHeldInOwnNm(self):
		del self._AsstsHeldInOwnNm
		self._AsstsHeldInOwnNm = base_types.UninitialisedField(self, 'AsstsHeldInOwnNm', YesNoIndicator, False)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', FinancialInstrument61Choice, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', FinancialInstrument61Choice, False)

	@property
	def LineId(self):
		return self._LineId

	@LineId.setter
	def LineId(self, value):
		self._LineId = value if value is not None else base_types.UninitialisedField(self, 'LineId', Max35Text, False)

	@LineId.deleter
	def LineId(self):
		del self._LineId
		self._LineId = base_types.UninitialisedField(self, 'LineId', Max35Text, False)

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters18, False)

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters18, False)

	@property
	def TrfRsltsInChngOfBnfclOwnr(self):
		return self._TrfRsltsInChngOfBnfclOwnr

	@TrfRsltsInChngOfBnfclOwnr.setter
	def TrfRsltsInChngOfBnfclOwnr(self, value):
		self._TrfRsltsInChngOfBnfclOwnr = value if value is not None else base_types.UninitialisedField(self, 'TrfRsltsInChngOfBnfclOwnr', YesNoIndicator, False)

	@TrfRsltsInChngOfBnfclOwnr.deleter
	def TrfRsltsInChngOfBnfclOwnr(self):
		del self._TrfRsltsInChngOfBnfclOwnr
		self._TrfRsltsInChngOfBnfclOwnr = base_types.UninitialisedField(self, 'TrfRsltsInChngOfBnfclOwnr', YesNoIndicator, False)

	@property
	def TrfeeAcct(self):
		return self._TrfeeAcct

	@TrfeeAcct.setter
	def TrfeeAcct(self, value):
		self._TrfeeAcct = value if value is not None else base_types.UninitialisedField(self, 'TrfeeAcct', Account28, False)

	@TrfeeAcct.deleter
	def TrfeeAcct(self):
		del self._TrfeeAcct
		self._TrfeeAcct = base_types.UninitialisedField(self, 'TrfeeAcct', Account28, False)

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if value is not None else base_types.UninitialisedField(self, 'Trfr', Account28, False)

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = base_types.UninitialisedField(self, 'Trfr', Account28, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument61Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfeeAcct', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=Account28, min=0, max=1, mutex_group=None, array=False),
	))