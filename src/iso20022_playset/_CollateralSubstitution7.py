# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashCollateral5
from . import CollateralSubstitutionSequence1Code
from . import CollateralSubstitutionType1Code
from . import Max140Text
from . import OtherCollateral11
from . import Reference17
from . import SecuritiesCollateral11

class CollateralSubstitution7(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnSeq", "_CollSbstitnTp", "_CshColl", "_LkdRefs", "_OthrColl", "_SbstitnRqrmnt", "_SctiesColl", "_StdSttlmInstrs"]
	@property
	def CollSbstitnSeq(self):
		return self._CollSbstitnSeq

	@CollSbstitnSeq.setter
	def CollSbstitnSeq(self, value):
		self._CollSbstitnSeq = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnSeq', CollateralSubstitutionSequence1Code, False)

	@CollSbstitnSeq.deleter
	def CollSbstitnSeq(self):
		del self._CollSbstitnSeq
		self._CollSbstitnSeq = base_types.UninitialisedField(self, 'CollSbstitnSeq', CollateralSubstitutionSequence1Code, False)

	@property
	def CollSbstitnTp(self):
		return self._CollSbstitnTp

	@CollSbstitnTp.setter
	def CollSbstitnTp(self, value):
		self._CollSbstitnTp = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnTp', CollateralSubstitutionType1Code, False)

	@CollSbstitnTp.deleter
	def CollSbstitnTp(self):
		del self._CollSbstitnTp
		self._CollSbstitnTp = base_types.UninitialisedField(self, 'CollSbstitnTp', CollateralSubstitutionType1Code, False)

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if value is not None else base_types.UninitialisedField(self, 'CshColl', CashCollateral5, True)

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = base_types.UninitialisedField(self, 'CshColl', CashCollateral5, True)

	@property
	def LkdRefs(self):
		return self._LkdRefs

	@LkdRefs.setter
	def LkdRefs(self, value):
		self._LkdRefs = value if value is not None else base_types.UninitialisedField(self, 'LkdRefs', Reference17, False)

	@LkdRefs.deleter
	def LkdRefs(self):
		del self._LkdRefs
		self._LkdRefs = base_types.UninitialisedField(self, 'LkdRefs', Reference17, False)

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if value is not None else base_types.UninitialisedField(self, 'OthrColl', OtherCollateral11, True)

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = base_types.UninitialisedField(self, 'OthrColl', OtherCollateral11, True)

	@property
	def SbstitnRqrmnt(self):
		return self._SbstitnRqrmnt

	@SbstitnRqrmnt.setter
	def SbstitnRqrmnt(self, value):
		self._SbstitnRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'SbstitnRqrmnt', ActiveCurrencyAndAmount, False)

	@SbstitnRqrmnt.deleter
	def SbstitnRqrmnt(self):
		del self._SbstitnRqrmnt
		self._SbstitnRqrmnt = base_types.UninitialisedField(self, 'SbstitnRqrmnt', ActiveCurrencyAndAmount, False)

	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if value is not None else base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral11, True)

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral11, True)

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnSeq', type=CollateralSubstitutionSequence1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnTp', type=CollateralSubstitutionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshColl', type=CashCollateral5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LkdRefs', type=Reference17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrColl', type=OtherCollateral11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbstitnRqrmnt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesColl', type=SecuritiesCollateral11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))