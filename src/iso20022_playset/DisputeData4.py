from . import base_types
from .DisputeReference1 import DisputeReference1
from .Exact1NumericText import Exact1NumericText
from .AdditionalData1 import AdditionalData1
from .TrueFalseIndicator import TrueFalseIndicator
from .Max35Text import Max35Text

class DisputeData4(base_types._BaseFieldType):

	__slots__ = ["_Prtl", "_Ref", "_ChrgbckElgblty", "_Cond", "_Sts", "_DcmnttnSts", "_AddtlData", "_Cycl", "_RjctRsn"]
	@property
	def Prtl(self):
		return self._Prtl

	@Prtl.setter
	def Prtl(self, value):
		self._Prtl = value if type(value) != base_types.auto else self.make_default("Prtl")

	@Prtl.deleter
	def Prtl(self):
		del self._Prtl
		self._Prtl = None

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
	def ChrgbckElgblty(self):
		return self._ChrgbckElgblty

	@ChrgbckElgblty.setter
	def ChrgbckElgblty(self, value):
		self._ChrgbckElgblty = value if type(value) != base_types.auto else self.make_default("ChrgbckElgblty")

	@ChrgbckElgblty.deleter
	def ChrgbckElgblty(self):
		del self._ChrgbckElgblty
		self._ChrgbckElgblty = None

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != base_types.auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def DcmnttnSts(self):
		return self._DcmnttnSts

	@DcmnttnSts.setter
	def DcmnttnSts(self, value):
		self._DcmnttnSts = value if type(value) != base_types.auto else self.make_default("DcmnttnSts")

	@DcmnttnSts.deleter
	def DcmnttnSts(self):
		del self._DcmnttnSts
		self._DcmnttnSts = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def Cycl(self):
		return self._Cycl

	@Cycl.setter
	def Cycl(self, value):
		self._Cycl = value if type(value) != base_types.auto else self.make_default("Cycl")

	@Cycl.deleter
	def Cycl(self):
		del self._Cycl
		self._Cycl = None

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if type(value) != base_types.auto else self.make_default("RjctRsn")

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=DisputeReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgbckElgblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmnttnSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

