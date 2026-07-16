# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import CashAccount205
from . import CountryCode
from . import OrderDesk1
from . import ProcessingCharacteristics10
from . import ProcessingCharacteristics11
from . import ProcessingCharacteristics9

class LocalMarketAnnex6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CshSttlmDtls", "_Ctry", "_LclOrdrDsk", "_RedPrcgChrtcs", "_SbcptPrcgChrtcs", "_SwtchPrcgChrtcs"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDtls', CashAccount205, True)

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = base_types.UninitialisedField(self, 'CshSttlmDtls', CashAccount205, True)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, True)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, True)

	@property
	def LclOrdrDsk(self):
		return self._LclOrdrDsk

	@LclOrdrDsk.setter
	def LclOrdrDsk(self, value):
		self._LclOrdrDsk = value if value is not None else base_types.UninitialisedField(self, 'LclOrdrDsk', OrderDesk1, False)

	@LclOrdrDsk.deleter
	def LclOrdrDsk(self):
		del self._LclOrdrDsk
		self._LclOrdrDsk = base_types.UninitialisedField(self, 'LclOrdrDsk', OrderDesk1, False)

	@property
	def RedPrcgChrtcs(self):
		return self._RedPrcgChrtcs

	@RedPrcgChrtcs.setter
	def RedPrcgChrtcs(self, value):
		self._RedPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'RedPrcgChrtcs', ProcessingCharacteristics10, False)

	@RedPrcgChrtcs.deleter
	def RedPrcgChrtcs(self):
		del self._RedPrcgChrtcs
		self._RedPrcgChrtcs = base_types.UninitialisedField(self, 'RedPrcgChrtcs', ProcessingCharacteristics10, False)

	@property
	def SbcptPrcgChrtcs(self):
		return self._SbcptPrcgChrtcs

	@SbcptPrcgChrtcs.setter
	def SbcptPrcgChrtcs(self, value):
		self._SbcptPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SbcptPrcgChrtcs', ProcessingCharacteristics11, False)

	@SbcptPrcgChrtcs.deleter
	def SbcptPrcgChrtcs(self):
		del self._SbcptPrcgChrtcs
		self._SbcptPrcgChrtcs = base_types.UninitialisedField(self, 'SbcptPrcgChrtcs', ProcessingCharacteristics11, False)

	@property
	def SwtchPrcgChrtcs(self):
		return self._SwtchPrcgChrtcs

	@SwtchPrcgChrtcs.setter
	def SwtchPrcgChrtcs(self, value):
		self._SwtchPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SwtchPrcgChrtcs', ProcessingCharacteristics9, False)

	@SwtchPrcgChrtcs.deleter
	def SwtchPrcgChrtcs(self):
		del self._SwtchPrcgChrtcs
		self._SwtchPrcgChrtcs = base_types.UninitialisedField(self, 'SwtchPrcgChrtcs', ProcessingCharacteristics9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshSttlmDtls', type=CashAccount205, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LclOrdrDsk', type=OrderDesk1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPrcgChrtcs', type=ProcessingCharacteristics10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPrcgChrtcs', type=ProcessingCharacteristics11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchPrcgChrtcs', type=ProcessingCharacteristics9, min=0, max=1, mutex_group=None, array=False),
	))