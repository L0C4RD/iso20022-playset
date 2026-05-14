from . import base_types
from ._FundingSource5 import FundingSource5
from ._ISODateTime import ISODateTime
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max3Text import Max3Text
from ._Max500Text import Max500Text

class FundingService4(base_types._BaseFieldType):

	__slots__ = ["_BizPurp", "_ClmAssgnr", "_ClmCrdntls", "_Desc", "_DfrrdDtTm", "_FndgSrc", "_Nm", "_Prvdr", "_Ref", "_SvcPrcgTp"]
	@property
	def BizPurp(self):
		return self._BizPurp

	@BizPurp.setter
	def BizPurp(self, value):
		self._BizPurp = value if type(value) != base_types.auto else self.make_default("BizPurp")

	@BizPurp.deleter
	def BizPurp(self):
		del self._BizPurp
		self._BizPurp = None

	@property
	def ClmAssgnr(self):
		return self._ClmAssgnr

	@ClmAssgnr.setter
	def ClmAssgnr(self, value):
		self._ClmAssgnr = value if type(value) != base_types.auto else self.make_default("ClmAssgnr")

	@ClmAssgnr.deleter
	def ClmAssgnr(self):
		del self._ClmAssgnr
		self._ClmAssgnr = None

	@property
	def ClmCrdntls(self):
		return self._ClmCrdntls

	@ClmCrdntls.setter
	def ClmCrdntls(self, value):
		self._ClmCrdntls = value if type(value) != base_types.auto else self.make_default("ClmCrdntls")

	@ClmCrdntls.deleter
	def ClmCrdntls(self):
		del self._ClmCrdntls
		self._ClmCrdntls = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def DfrrdDtTm(self):
		return self._DfrrdDtTm

	@DfrrdDtTm.setter
	def DfrrdDtTm(self, value):
		self._DfrrdDtTm = value if type(value) != base_types.auto else self.make_default("DfrrdDtTm")

	@DfrrdDtTm.deleter
	def DfrrdDtTm(self):
		del self._DfrrdDtTm
		self._DfrrdDtTm = None

	@property
	def FndgSrc(self):
		return self._FndgSrc

	@FndgSrc.setter
	def FndgSrc(self, value):
		self._FndgSrc = value if type(value) != base_types.auto else self.make_default("FndgSrc")

	@FndgSrc.deleter
	def FndgSrc(self):
		del self._FndgSrc
		self._FndgSrc = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != base_types.auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def SvcPrcgTp(self):
		return self._SvcPrcgTp

	@SvcPrcgTp.setter
	def SvcPrcgTp(self, value):
		self._SvcPrcgTp = value if type(value) != base_types.auto else self.make_default("SvcPrcgTp")

	@SvcPrcgTp.deleter
	def SvcPrcgTp(self):
		del self._SvcPrcgTp
		self._SvcPrcgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizPurp', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmCrdntls', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndgSrc', type=FundingSource5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcPrcgTp', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
	))

