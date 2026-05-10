from . import base_types
from .Period6Choice import Period6Choice

class CorporateActionPeriod16(base_types._BaseFieldType):

	__slots__ = ["_DpstrySspnsnPrdForWdrwlInStrtNm", "_DpstrySspnsnPrdForPldg", "_DpstrySspnsnPrdForWdrwlAtAgt", "_BookClsrPrd", "_PricClctnPrd", "_DpstrySspnsnPrdForBookNtryTrf", "_DpstrySspnsnPrdForWdrwlInNmneeNm", "_DpstrySspnsnPrdForSgrtn", "_SpltPrd", "_IntrstPrd", "_ClmPrd", "_CoDpstriesSspnsnPrd", "_DpstrySspnsnPrdForDpst", "_FsclYrPrd", "_CmplsryPurchsPrd", "_DpstrySspnsnPrdForDpstAtAgt"]
	@property
	def DpstrySspnsnPrdForWdrwlInStrtNm(self):
		return self._DpstrySspnsnPrdForWdrwlInStrtNm

	@DpstrySspnsnPrdForWdrwlInStrtNm.setter
	def DpstrySspnsnPrdForWdrwlInStrtNm(self, value):
		self._DpstrySspnsnPrdForWdrwlInStrtNm = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForWdrwlInStrtNm")

	@DpstrySspnsnPrdForWdrwlInStrtNm.deleter
	def DpstrySspnsnPrdForWdrwlInStrtNm(self):
		del self._DpstrySspnsnPrdForWdrwlInStrtNm
		self._DpstrySspnsnPrdForWdrwlInStrtNm = None

	@property
	def DpstrySspnsnPrdForPldg(self):
		return self._DpstrySspnsnPrdForPldg

	@DpstrySspnsnPrdForPldg.setter
	def DpstrySspnsnPrdForPldg(self, value):
		self._DpstrySspnsnPrdForPldg = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForPldg")

	@DpstrySspnsnPrdForPldg.deleter
	def DpstrySspnsnPrdForPldg(self):
		del self._DpstrySspnsnPrdForPldg
		self._DpstrySspnsnPrdForPldg = None

	@property
	def DpstrySspnsnPrdForWdrwlAtAgt(self):
		return self._DpstrySspnsnPrdForWdrwlAtAgt

	@DpstrySspnsnPrdForWdrwlAtAgt.setter
	def DpstrySspnsnPrdForWdrwlAtAgt(self, value):
		self._DpstrySspnsnPrdForWdrwlAtAgt = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForWdrwlAtAgt")

	@DpstrySspnsnPrdForWdrwlAtAgt.deleter
	def DpstrySspnsnPrdForWdrwlAtAgt(self):
		del self._DpstrySspnsnPrdForWdrwlAtAgt
		self._DpstrySspnsnPrdForWdrwlAtAgt = None

	@property
	def BookClsrPrd(self):
		return self._BookClsrPrd

	@BookClsrPrd.setter
	def BookClsrPrd(self, value):
		self._BookClsrPrd = value if type(value) != auto else self.make_default("BookClsrPrd")

	@BookClsrPrd.deleter
	def BookClsrPrd(self):
		del self._BookClsrPrd
		self._BookClsrPrd = None

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if type(value) != auto else self.make_default("PricClctnPrd")

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = None

	@property
	def DpstrySspnsnPrdForBookNtryTrf(self):
		return self._DpstrySspnsnPrdForBookNtryTrf

	@DpstrySspnsnPrdForBookNtryTrf.setter
	def DpstrySspnsnPrdForBookNtryTrf(self, value):
		self._DpstrySspnsnPrdForBookNtryTrf = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForBookNtryTrf")

	@DpstrySspnsnPrdForBookNtryTrf.deleter
	def DpstrySspnsnPrdForBookNtryTrf(self):
		del self._DpstrySspnsnPrdForBookNtryTrf
		self._DpstrySspnsnPrdForBookNtryTrf = None

	@property
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self):
		return self._DpstrySspnsnPrdForWdrwlInNmneeNm

	@DpstrySspnsnPrdForWdrwlInNmneeNm.setter
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self, value):
		self._DpstrySspnsnPrdForWdrwlInNmneeNm = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForWdrwlInNmneeNm")

	@DpstrySspnsnPrdForWdrwlInNmneeNm.deleter
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self):
		del self._DpstrySspnsnPrdForWdrwlInNmneeNm
		self._DpstrySspnsnPrdForWdrwlInNmneeNm = None

	@property
	def DpstrySspnsnPrdForSgrtn(self):
		return self._DpstrySspnsnPrdForSgrtn

	@DpstrySspnsnPrdForSgrtn.setter
	def DpstrySspnsnPrdForSgrtn(self, value):
		self._DpstrySspnsnPrdForSgrtn = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForSgrtn")

	@DpstrySspnsnPrdForSgrtn.deleter
	def DpstrySspnsnPrdForSgrtn(self):
		del self._DpstrySspnsnPrdForSgrtn
		self._DpstrySspnsnPrdForSgrtn = None

	@property
	def SpltPrd(self):
		return self._SpltPrd

	@SpltPrd.setter
	def SpltPrd(self, value):
		self._SpltPrd = value if type(value) != auto else self.make_default("SpltPrd")

	@SpltPrd.deleter
	def SpltPrd(self):
		del self._SpltPrd
		self._SpltPrd = None

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if type(value) != auto else self.make_default("IntrstPrd")

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = None

	@property
	def ClmPrd(self):
		return self._ClmPrd

	@ClmPrd.setter
	def ClmPrd(self, value):
		self._ClmPrd = value if type(value) != auto else self.make_default("ClmPrd")

	@ClmPrd.deleter
	def ClmPrd(self):
		del self._ClmPrd
		self._ClmPrd = None

	@property
	def CoDpstriesSspnsnPrd(self):
		return self._CoDpstriesSspnsnPrd

	@CoDpstriesSspnsnPrd.setter
	def CoDpstriesSspnsnPrd(self, value):
		self._CoDpstriesSspnsnPrd = value if type(value) != auto else self.make_default("CoDpstriesSspnsnPrd")

	@CoDpstriesSspnsnPrd.deleter
	def CoDpstriesSspnsnPrd(self):
		del self._CoDpstriesSspnsnPrd
		self._CoDpstriesSspnsnPrd = None

	@property
	def DpstrySspnsnPrdForDpst(self):
		return self._DpstrySspnsnPrdForDpst

	@DpstrySspnsnPrdForDpst.setter
	def DpstrySspnsnPrdForDpst(self, value):
		self._DpstrySspnsnPrdForDpst = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForDpst")

	@DpstrySspnsnPrdForDpst.deleter
	def DpstrySspnsnPrdForDpst(self):
		del self._DpstrySspnsnPrdForDpst
		self._DpstrySspnsnPrdForDpst = None

	@property
	def FsclYrPrd(self):
		return self._FsclYrPrd

	@FsclYrPrd.setter
	def FsclYrPrd(self, value):
		self._FsclYrPrd = value if type(value) != auto else self.make_default("FsclYrPrd")

	@FsclYrPrd.deleter
	def FsclYrPrd(self):
		del self._FsclYrPrd
		self._FsclYrPrd = None

	@property
	def CmplsryPurchsPrd(self):
		return self._CmplsryPurchsPrd

	@CmplsryPurchsPrd.setter
	def CmplsryPurchsPrd(self, value):
		self._CmplsryPurchsPrd = value if type(value) != auto else self.make_default("CmplsryPurchsPrd")

	@CmplsryPurchsPrd.deleter
	def CmplsryPurchsPrd(self):
		del self._CmplsryPurchsPrd
		self._CmplsryPurchsPrd = None

	@property
	def DpstrySspnsnPrdForDpstAtAgt(self):
		return self._DpstrySspnsnPrdForDpstAtAgt

	@DpstrySspnsnPrdForDpstAtAgt.setter
	def DpstrySspnsnPrdForDpstAtAgt(self, value):
		self._DpstrySspnsnPrdForDpstAtAgt = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForDpstAtAgt")

	@DpstrySspnsnPrdForDpstAtAgt.deleter
	def DpstrySspnsnPrdForDpstAtAgt(self):
		del self._DpstrySspnsnPrdForDpstAtAgt
		self._DpstrySspnsnPrdForDpstAtAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlInStrtNm', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForPldg', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlAtAgt', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookClsrPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForBookNtryTrf', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlInNmneeNm', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForSgrtn', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoDpstriesSspnsnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForDpst', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclYrPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplsryPurchsPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForDpstAtAgt', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
	))

