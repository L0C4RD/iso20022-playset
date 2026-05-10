from . import base_types
from .CashAssetType1Choice import CashAssetType1Choice
from .ActiveCurrencyCode import ActiveCurrencyCode
from .AdditionalInformation15 import AdditionalInformation15

class CashAsset2(base_types._BaseFieldType):

	__slots__ = ["_HldgCcy", "_CshAsstTp", "_AddtlInf"]
	@property
	def HldgCcy(self):
		return self._HldgCcy

	@HldgCcy.setter
	def HldgCcy(self, value):
		self._HldgCcy = value if type(value) != base_types.auto else self.make_default("HldgCcy")

	@HldgCcy.deleter
	def HldgCcy(self):
		del self._HldgCcy
		self._HldgCcy = None

	@property
	def CshAsstTp(self):
		return self._CshAsstTp

	@CshAsstTp.setter
	def CshAsstTp(self, value):
		self._CshAsstTp = value if type(value) != base_types.auto else self.make_default("CshAsstTp")

	@CshAsstTp.deleter
	def CshAsstTp(self):
		del self._CshAsstTp
		self._CshAsstTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldgCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAsstTp', type=CashAssetType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
	))

