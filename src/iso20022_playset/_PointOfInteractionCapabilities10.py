# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaType1Code
from . import ATMMediaType4Code
from . import CardDataReading4Code
from . import CardholderVerificationCapability3Code
from . import DisplayCapabilities5
from . import Max256Text
from . import Number
from . import TrueFalseIndicator

class PointOfInteractionCapabilities10(base_types._BaseFieldType):

	__slots__ = ["_ApprvlCdLngth", "_Authntcn", "_CardCaptrCpbl", "_CardRdData", "_CardWrtData", "_DpstdMdia", "_IntractvTxs", "_MsgCpblties", "_MxScrptLngth", "_PINLngthCpblties", "_RctPrtg", "_WdrwlMdia"]
	@property
	def ApprvlCdLngth(self):
		return self._ApprvlCdLngth

	@ApprvlCdLngth.setter
	def ApprvlCdLngth(self, value):
		self._ApprvlCdLngth = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCdLngth', Number, False)

	@ApprvlCdLngth.deleter
	def ApprvlCdLngth(self):
		del self._ApprvlCdLngth
		self._ApprvlCdLngth = base_types.UninitialisedField(self, 'ApprvlCdLngth', Number, False)

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if value is not None else base_types.UninitialisedField(self, 'Authntcn', CardholderVerificationCapability3Code, True)

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = base_types.UninitialisedField(self, 'Authntcn', CardholderVerificationCapability3Code, True)

	@property
	def CardCaptrCpbl(self):
		return self._CardCaptrCpbl

	@CardCaptrCpbl.setter
	def CardCaptrCpbl(self, value):
		self._CardCaptrCpbl = value if value is not None else base_types.UninitialisedField(self, 'CardCaptrCpbl', TrueFalseIndicator, False)

	@CardCaptrCpbl.deleter
	def CardCaptrCpbl(self):
		del self._CardCaptrCpbl
		self._CardCaptrCpbl = base_types.UninitialisedField(self, 'CardCaptrCpbl', TrueFalseIndicator, False)

	@property
	def CardRdData(self):
		return self._CardRdData

	@CardRdData.setter
	def CardRdData(self, value):
		self._CardRdData = value if value is not None else base_types.UninitialisedField(self, 'CardRdData', CardDataReading4Code, True)

	@CardRdData.deleter
	def CardRdData(self):
		del self._CardRdData
		self._CardRdData = base_types.UninitialisedField(self, 'CardRdData', CardDataReading4Code, True)

	@property
	def CardWrtData(self):
		return self._CardWrtData

	@CardWrtData.setter
	def CardWrtData(self, value):
		self._CardWrtData = value if value is not None else base_types.UninitialisedField(self, 'CardWrtData', CardDataReading4Code, True)

	@CardWrtData.deleter
	def CardWrtData(self):
		del self._CardWrtData
		self._CardWrtData = base_types.UninitialisedField(self, 'CardWrtData', CardDataReading4Code, True)

	@property
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if value is not None else base_types.UninitialisedField(self, 'DpstdMdia', ATMMediaType4Code, True)

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = base_types.UninitialisedField(self, 'DpstdMdia', ATMMediaType4Code, True)

	@property
	def IntractvTxs(self):
		return self._IntractvTxs

	@IntractvTxs.setter
	def IntractvTxs(self, value):
		self._IntractvTxs = value if value is not None else base_types.UninitialisedField(self, 'IntractvTxs', Max256Text, True)

	@IntractvTxs.deleter
	def IntractvTxs(self):
		del self._IntractvTxs
		self._IntractvTxs = base_types.UninitialisedField(self, 'IntractvTxs', Max256Text, True)

	@property
	def MsgCpblties(self):
		return self._MsgCpblties

	@MsgCpblties.setter
	def MsgCpblties(self, value):
		self._MsgCpblties = value if value is not None else base_types.UninitialisedField(self, 'MsgCpblties', DisplayCapabilities5, True)

	@MsgCpblties.deleter
	def MsgCpblties(self):
		del self._MsgCpblties
		self._MsgCpblties = base_types.UninitialisedField(self, 'MsgCpblties', DisplayCapabilities5, True)

	@property
	def MxScrptLngth(self):
		return self._MxScrptLngth

	@MxScrptLngth.setter
	def MxScrptLngth(self, value):
		self._MxScrptLngth = value if value is not None else base_types.UninitialisedField(self, 'MxScrptLngth', Number, False)

	@MxScrptLngth.deleter
	def MxScrptLngth(self):
		del self._MxScrptLngth
		self._MxScrptLngth = base_types.UninitialisedField(self, 'MxScrptLngth', Number, False)

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if value is not None else base_types.UninitialisedField(self, 'PINLngthCpblties', Number, False)

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = base_types.UninitialisedField(self, 'PINLngthCpblties', Number, False)

	@property
	def RctPrtg(self):
		return self._RctPrtg

	@RctPrtg.setter
	def RctPrtg(self, value):
		self._RctPrtg = value if value is not None else base_types.UninitialisedField(self, 'RctPrtg', TrueFalseIndicator, False)

	@RctPrtg.deleter
	def RctPrtg(self):
		del self._RctPrtg
		self._RctPrtg = base_types.UninitialisedField(self, 'RctPrtg', TrueFalseIndicator, False)

	@property
	def WdrwlMdia(self):
		return self._WdrwlMdia

	@WdrwlMdia.setter
	def WdrwlMdia(self, value):
		self._WdrwlMdia = value if value is not None else base_types.UninitialisedField(self, 'WdrwlMdia', ATMMediaType1Code, True)

	@WdrwlMdia.deleter
	def WdrwlMdia(self):
		del self._WdrwlMdia
		self._WdrwlMdia = base_types.UninitialisedField(self, 'WdrwlMdia', ATMMediaType1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlCdLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=CardholderVerificationCapability3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardCaptrCpbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardRdData', type=CardDataReading4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardWrtData', type=CardDataReading4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DpstdMdia', type=ATMMediaType4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntractvTxs', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgCpblties', type=DisplayCapabilities5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MxScrptLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINLngthCpblties', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlMdia', type=ATMMediaType1Code, min=0, max=None, mutex_group=None, array=True),
	))