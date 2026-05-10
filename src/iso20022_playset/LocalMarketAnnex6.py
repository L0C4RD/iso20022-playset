from . import base_types
from .ProcessingCharacteristics10 import ProcessingCharacteristics10
from .CountryCode import CountryCode
from .ProcessingCharacteristics11 import ProcessingCharacteristics11
from .ProcessingCharacteristics9 import ProcessingCharacteristics9
from .OrderDesk1 import OrderDesk1
from .AdditionalInformation15 import AdditionalInformation15
from .CashAccount205 import CashAccount205

class LocalMarketAnnex6(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_RedPrcgChrtcs", "_AddtlInf", "_SwtchPrcgChrtcs", "_SbcptPrcgChrtcs", "_CshSttlmDtls", "_LclOrdrDsk"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def RedPrcgChrtcs(self):
		return self._RedPrcgChrtcs

	@RedPrcgChrtcs.setter
	def RedPrcgChrtcs(self, value):
		self._RedPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("RedPrcgChrtcs")

	@RedPrcgChrtcs.deleter
	def RedPrcgChrtcs(self):
		del self._RedPrcgChrtcs
		self._RedPrcgChrtcs = None

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
	def SwtchPrcgChrtcs(self):
		return self._SwtchPrcgChrtcs

	@SwtchPrcgChrtcs.setter
	def SwtchPrcgChrtcs(self, value):
		self._SwtchPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("SwtchPrcgChrtcs")

	@SwtchPrcgChrtcs.deleter
	def SwtchPrcgChrtcs(self):
		del self._SwtchPrcgChrtcs
		self._SwtchPrcgChrtcs = None

	@property
	def SbcptPrcgChrtcs(self):
		return self._SbcptPrcgChrtcs

	@SbcptPrcgChrtcs.setter
	def SbcptPrcgChrtcs(self, value):
		self._SbcptPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("SbcptPrcgChrtcs")

	@SbcptPrcgChrtcs.deleter
	def SbcptPrcgChrtcs(self):
		del self._SbcptPrcgChrtcs
		self._SbcptPrcgChrtcs = None

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if type(value) != base_types.auto else self.make_default("CshSttlmDtls")

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = None

	@property
	def LclOrdrDsk(self):
		return self._LclOrdrDsk

	@LclOrdrDsk.setter
	def LclOrdrDsk(self, value):
		self._LclOrdrDsk = value if type(value) != base_types.auto else self.make_default("LclOrdrDsk")

	@LclOrdrDsk.deleter
	def LclOrdrDsk(self):
		del self._LclOrdrDsk
		self._LclOrdrDsk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RedPrcgChrtcs', type=ProcessingCharacteristics10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SwtchPrcgChrtcs', type=ProcessingCharacteristics9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPrcgChrtcs', type=ProcessingCharacteristics11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=CashAccount205, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LclOrdrDsk', type=OrderDesk1, min=1, max=1, mutex_group=None, array=False),
	))

