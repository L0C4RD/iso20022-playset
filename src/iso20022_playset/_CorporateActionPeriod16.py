# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Period6Choice

class CorporateActionPeriod16(base_types._BaseFieldType):

	__slots__ = ["_BookClsrPrd", "_ClmPrd", "_CmplsryPurchsPrd", "_CoDpstriesSspnsnPrd", "_DpstrySspnsnPrdForBookNtryTrf", "_DpstrySspnsnPrdForDpst", "_DpstrySspnsnPrdForDpstAtAgt", "_DpstrySspnsnPrdForPldg", "_DpstrySspnsnPrdForSgrtn", "_DpstrySspnsnPrdForWdrwlAtAgt", "_DpstrySspnsnPrdForWdrwlInNmneeNm", "_DpstrySspnsnPrdForWdrwlInStrtNm", "_FsclYrPrd", "_IntrstPrd", "_PricClctnPrd", "_SpltPrd"]
	@property
	def BookClsrPrd(self):
		return self._BookClsrPrd

	@BookClsrPrd.setter
	def BookClsrPrd(self, value):
		self._BookClsrPrd = value if value is not None else base_types.UninitialisedField(self, 'BookClsrPrd', Period6Choice, False)

	@BookClsrPrd.deleter
	def BookClsrPrd(self):
		del self._BookClsrPrd
		self._BookClsrPrd = base_types.UninitialisedField(self, 'BookClsrPrd', Period6Choice, False)

	@property
	def ClmPrd(self):
		return self._ClmPrd

	@ClmPrd.setter
	def ClmPrd(self, value):
		self._ClmPrd = value if value is not None else base_types.UninitialisedField(self, 'ClmPrd', Period6Choice, False)

	@ClmPrd.deleter
	def ClmPrd(self):
		del self._ClmPrd
		self._ClmPrd = base_types.UninitialisedField(self, 'ClmPrd', Period6Choice, False)

	@property
	def CmplsryPurchsPrd(self):
		return self._CmplsryPurchsPrd

	@CmplsryPurchsPrd.setter
	def CmplsryPurchsPrd(self, value):
		self._CmplsryPurchsPrd = value if value is not None else base_types.UninitialisedField(self, 'CmplsryPurchsPrd', Period6Choice, False)

	@CmplsryPurchsPrd.deleter
	def CmplsryPurchsPrd(self):
		del self._CmplsryPurchsPrd
		self._CmplsryPurchsPrd = base_types.UninitialisedField(self, 'CmplsryPurchsPrd', Period6Choice, False)

	@property
	def CoDpstriesSspnsnPrd(self):
		return self._CoDpstriesSspnsnPrd

	@CoDpstriesSspnsnPrd.setter
	def CoDpstriesSspnsnPrd(self, value):
		self._CoDpstriesSspnsnPrd = value if value is not None else base_types.UninitialisedField(self, 'CoDpstriesSspnsnPrd', Period6Choice, False)

	@CoDpstriesSspnsnPrd.deleter
	def CoDpstriesSspnsnPrd(self):
		del self._CoDpstriesSspnsnPrd
		self._CoDpstriesSspnsnPrd = base_types.UninitialisedField(self, 'CoDpstriesSspnsnPrd', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForBookNtryTrf(self):
		return self._DpstrySspnsnPrdForBookNtryTrf

	@DpstrySspnsnPrdForBookNtryTrf.setter
	def DpstrySspnsnPrdForBookNtryTrf(self, value):
		self._DpstrySspnsnPrdForBookNtryTrf = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForBookNtryTrf', Period6Choice, False)

	@DpstrySspnsnPrdForBookNtryTrf.deleter
	def DpstrySspnsnPrdForBookNtryTrf(self):
		del self._DpstrySspnsnPrdForBookNtryTrf
		self._DpstrySspnsnPrdForBookNtryTrf = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForBookNtryTrf', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForDpst(self):
		return self._DpstrySspnsnPrdForDpst

	@DpstrySspnsnPrdForDpst.setter
	def DpstrySspnsnPrdForDpst(self, value):
		self._DpstrySspnsnPrdForDpst = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForDpst', Period6Choice, False)

	@DpstrySspnsnPrdForDpst.deleter
	def DpstrySspnsnPrdForDpst(self):
		del self._DpstrySspnsnPrdForDpst
		self._DpstrySspnsnPrdForDpst = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForDpst', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForDpstAtAgt(self):
		return self._DpstrySspnsnPrdForDpstAtAgt

	@DpstrySspnsnPrdForDpstAtAgt.setter
	def DpstrySspnsnPrdForDpstAtAgt(self, value):
		self._DpstrySspnsnPrdForDpstAtAgt = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForDpstAtAgt', Period6Choice, False)

	@DpstrySspnsnPrdForDpstAtAgt.deleter
	def DpstrySspnsnPrdForDpstAtAgt(self):
		del self._DpstrySspnsnPrdForDpstAtAgt
		self._DpstrySspnsnPrdForDpstAtAgt = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForDpstAtAgt', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForPldg(self):
		return self._DpstrySspnsnPrdForPldg

	@DpstrySspnsnPrdForPldg.setter
	def DpstrySspnsnPrdForPldg(self, value):
		self._DpstrySspnsnPrdForPldg = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForPldg', Period6Choice, False)

	@DpstrySspnsnPrdForPldg.deleter
	def DpstrySspnsnPrdForPldg(self):
		del self._DpstrySspnsnPrdForPldg
		self._DpstrySspnsnPrdForPldg = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForPldg', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForSgrtn(self):
		return self._DpstrySspnsnPrdForSgrtn

	@DpstrySspnsnPrdForSgrtn.setter
	def DpstrySspnsnPrdForSgrtn(self, value):
		self._DpstrySspnsnPrdForSgrtn = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForSgrtn', Period6Choice, False)

	@DpstrySspnsnPrdForSgrtn.deleter
	def DpstrySspnsnPrdForSgrtn(self):
		del self._DpstrySspnsnPrdForSgrtn
		self._DpstrySspnsnPrdForSgrtn = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForSgrtn', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForWdrwlAtAgt(self):
		return self._DpstrySspnsnPrdForWdrwlAtAgt

	@DpstrySspnsnPrdForWdrwlAtAgt.setter
	def DpstrySspnsnPrdForWdrwlAtAgt(self, value):
		self._DpstrySspnsnPrdForWdrwlAtAgt = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlAtAgt', Period6Choice, False)

	@DpstrySspnsnPrdForWdrwlAtAgt.deleter
	def DpstrySspnsnPrdForWdrwlAtAgt(self):
		del self._DpstrySspnsnPrdForWdrwlAtAgt
		self._DpstrySspnsnPrdForWdrwlAtAgt = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlAtAgt', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self):
		return self._DpstrySspnsnPrdForWdrwlInNmneeNm

	@DpstrySspnsnPrdForWdrwlInNmneeNm.setter
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self, value):
		self._DpstrySspnsnPrdForWdrwlInNmneeNm = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlInNmneeNm', Period6Choice, False)

	@DpstrySspnsnPrdForWdrwlInNmneeNm.deleter
	def DpstrySspnsnPrdForWdrwlInNmneeNm(self):
		del self._DpstrySspnsnPrdForWdrwlInNmneeNm
		self._DpstrySspnsnPrdForWdrwlInNmneeNm = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlInNmneeNm', Period6Choice, False)

	@property
	def DpstrySspnsnPrdForWdrwlInStrtNm(self):
		return self._DpstrySspnsnPrdForWdrwlInStrtNm

	@DpstrySspnsnPrdForWdrwlInStrtNm.setter
	def DpstrySspnsnPrdForWdrwlInStrtNm(self, value):
		self._DpstrySspnsnPrdForWdrwlInStrtNm = value if value is not None else base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlInStrtNm', Period6Choice, False)

	@DpstrySspnsnPrdForWdrwlInStrtNm.deleter
	def DpstrySspnsnPrdForWdrwlInStrtNm(self):
		del self._DpstrySspnsnPrdForWdrwlInStrtNm
		self._DpstrySspnsnPrdForWdrwlInStrtNm = base_types.UninitialisedField(self, 'DpstrySspnsnPrdForWdrwlInStrtNm', Period6Choice, False)

	@property
	def FsclYrPrd(self):
		return self._FsclYrPrd

	@FsclYrPrd.setter
	def FsclYrPrd(self, value):
		self._FsclYrPrd = value if value is not None else base_types.UninitialisedField(self, 'FsclYrPrd', Period6Choice, False)

	@FsclYrPrd.deleter
	def FsclYrPrd(self):
		del self._FsclYrPrd
		self._FsclYrPrd = base_types.UninitialisedField(self, 'FsclYrPrd', Period6Choice, False)

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if value is not None else base_types.UninitialisedField(self, 'IntrstPrd', Period6Choice, False)

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = base_types.UninitialisedField(self, 'IntrstPrd', Period6Choice, False)

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', Period6Choice, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', Period6Choice, False)

	@property
	def SpltPrd(self):
		return self._SpltPrd

	@SpltPrd.setter
	def SpltPrd(self, value):
		self._SpltPrd = value if value is not None else base_types.UninitialisedField(self, 'SpltPrd', Period6Choice, False)

	@SpltPrd.deleter
	def SpltPrd(self):
		del self._SpltPrd
		self._SpltPrd = base_types.UninitialisedField(self, 'SpltPrd', Period6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookClsrPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplsryPurchsPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoDpstriesSspnsnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForBookNtryTrf', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForDpst', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForDpstAtAgt', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForPldg', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForSgrtn', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlAtAgt', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlInNmneeNm', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwlInStrtNm', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclYrPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
	))