from . import base_types
from ._Reference17 import Reference17
from ._CollateralSubstitutionType1Code import CollateralSubstitutionType1Code
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._OtherCollateral11 import OtherCollateral11
from ._CashCollateral5 import CashCollateral5
from ._SecuritiesCollateral11 import SecuritiesCollateral11
from ._CollateralSubstitutionSequence1Code import CollateralSubstitutionSequence1Code
from ._Max140Text import Max140Text

class CollateralSubstitution7(base_types._BaseFieldType):

	__slots__ = ["_LkdRefs", "_CollSbstitnSeq", "_OthrColl", "_StdSttlmInstrs", "_SbstitnRqrmnt", "_CshColl", "_SctiesColl", "_CollSbstitnTp"]
	@property
	def CollSbstitnSeq(self):
		return self._CollSbstitnSeq

	@CollSbstitnSeq.setter
	def CollSbstitnSeq(self, value):
		self._CollSbstitnSeq = value if type(value) != base_types.auto else self.make_default("CollSbstitnSeq")

	@CollSbstitnSeq.deleter
	def CollSbstitnSeq(self):
		del self._CollSbstitnSeq
		self._CollSbstitnSeq = None

	@property
	def CollSbstitnTp(self):
		return self._CollSbstitnTp

	@CollSbstitnTp.setter
	def CollSbstitnTp(self, value):
		self._CollSbstitnTp = value if type(value) != base_types.auto else self.make_default("CollSbstitnTp")

	@CollSbstitnTp.deleter
	def CollSbstitnTp(self):
		del self._CollSbstitnTp
		self._CollSbstitnTp = None

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if type(value) != base_types.auto else self.make_default("CshColl")

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = None

	@property
	def LkdRefs(self):
		return self._LkdRefs

	@LkdRefs.setter
	def LkdRefs(self, value):
		self._LkdRefs = value if type(value) != base_types.auto else self.make_default("LkdRefs")

	@LkdRefs.deleter
	def LkdRefs(self):
		del self._LkdRefs
		self._LkdRefs = None

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if type(value) != base_types.auto else self.make_default("OthrColl")

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = None

	@property
	def SbstitnRqrmnt(self):
		return self._SbstitnRqrmnt

	@SbstitnRqrmnt.setter
	def SbstitnRqrmnt(self, value):
		self._SbstitnRqrmnt = value if type(value) != base_types.auto else self.make_default("SbstitnRqrmnt")

	@SbstitnRqrmnt.deleter
	def SbstitnRqrmnt(self):
		del self._SbstitnRqrmnt
		self._SbstitnRqrmnt = None

	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if type(value) != base_types.auto else self.make_default("SctiesColl")

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = None

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if type(value) != base_types.auto else self.make_default("StdSttlmInstrs")

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = None

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

