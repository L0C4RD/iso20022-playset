from . import base_types
from ._DistributionStrategy1Choice import DistributionStrategy1Choice
from ._AdditionalInformation15 import AdditionalInformation15
from ._Max35Text import Max35Text

class OtherDistributionStrategy1(base_types._BaseFieldType):

	__slots__ = ["_DstrbtnStrtgyTp", "_Trgt", "_AddtlInf"]
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
	def DstrbtnStrtgyTp(self):
		return self._DstrbtnStrtgyTp

	@DstrbtnStrtgyTp.setter
	def DstrbtnStrtgyTp(self, value):
		self._DstrbtnStrtgyTp = value if type(value) != base_types.auto else self.make_default("DstrbtnStrtgyTp")

	@DstrbtnStrtgyTp.deleter
	def DstrbtnStrtgyTp(self):
		del self._DstrbtnStrtgyTp
		self._DstrbtnStrtgyTp = None

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != base_types.auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnStrtgyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
	))

