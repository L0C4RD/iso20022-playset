import base_types
import Max35Text
import AdditionalInformation15
import TargetMarket1Choice

class OtherInvestmentNeed1(base_types._BaseFieldType):

	__slots__ = ["_Trgt", "_AddtlInf", "_ClntObjctvsAndNeedsTp"]
	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ClntObjctvsAndNeedsTp(self):
		return self._ClntObjctvsAndNeedsTp

	@ClntObjctvsAndNeedsTp.setter
	def ClntObjctvsAndNeedsTp(self, value):
		self._ClntObjctvsAndNeedsTp = value if type(value) != auto else self.make_default("ClntObjctvsAndNeedsTp")

	@ClntObjctvsAndNeedsTp.deleter
	def ClntObjctvsAndNeedsTp(self):
		del self._ClntObjctvsAndNeedsTp
		self._ClntObjctvsAndNeedsTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trgt', type=TargetMarket1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntObjctvsAndNeedsTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

