# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading5Code
from . import DecimalNumber
from . import Max35NumericText
from . import Max35Text
from . import PlainCardData17
from . import TrueFalseIndicator
from . import Vehicle2

class Vehicle1(base_types._BaseFieldType):

	__slots__ = ["_AddtlVhclData", "_DrvrOrVhclCard", "_Hbmtr", "_MntncId", "_Odmtr", "_RefrHrs", "_RplcmntCar", "_TrlrHrs", "_TrlrNb", "_UnitNb", "_VhclNb", "_VhclTag", "_VhclTagNtryMd"]
	@property
	def AddtlVhclData(self):
		return self._AddtlVhclData

	@AddtlVhclData.setter
	def AddtlVhclData(self, value):
		self._AddtlVhclData = value if value is not None else base_types.UninitialisedField(self, 'AddtlVhclData', Vehicle2, True)

	@AddtlVhclData.deleter
	def AddtlVhclData(self):
		del self._AddtlVhclData
		self._AddtlVhclData = base_types.UninitialisedField(self, 'AddtlVhclData', Vehicle2, True)

	@property
	def DrvrOrVhclCard(self):
		return self._DrvrOrVhclCard

	@DrvrOrVhclCard.setter
	def DrvrOrVhclCard(self, value):
		self._DrvrOrVhclCard = value if value is not None else base_types.UninitialisedField(self, 'DrvrOrVhclCard', PlainCardData17, False)

	@DrvrOrVhclCard.deleter
	def DrvrOrVhclCard(self):
		del self._DrvrOrVhclCard
		self._DrvrOrVhclCard = base_types.UninitialisedField(self, 'DrvrOrVhclCard', PlainCardData17, False)

	@property
	def Hbmtr(self):
		return self._Hbmtr

	@Hbmtr.setter
	def Hbmtr(self, value):
		self._Hbmtr = value if value is not None else base_types.UninitialisedField(self, 'Hbmtr', DecimalNumber, False)

	@Hbmtr.deleter
	def Hbmtr(self):
		del self._Hbmtr
		self._Hbmtr = base_types.UninitialisedField(self, 'Hbmtr', DecimalNumber, False)

	@property
	def MntncId(self):
		return self._MntncId

	@MntncId.setter
	def MntncId(self, value):
		self._MntncId = value if value is not None else base_types.UninitialisedField(self, 'MntncId', Max35Text, False)

	@MntncId.deleter
	def MntncId(self):
		del self._MntncId
		self._MntncId = base_types.UninitialisedField(self, 'MntncId', Max35Text, False)

	@property
	def Odmtr(self):
		return self._Odmtr

	@Odmtr.setter
	def Odmtr(self, value):
		self._Odmtr = value if value is not None else base_types.UninitialisedField(self, 'Odmtr', DecimalNumber, False)

	@Odmtr.deleter
	def Odmtr(self):
		del self._Odmtr
		self._Odmtr = base_types.UninitialisedField(self, 'Odmtr', DecimalNumber, False)

	@property
	def RefrHrs(self):
		return self._RefrHrs

	@RefrHrs.setter
	def RefrHrs(self, value):
		self._RefrHrs = value if value is not None else base_types.UninitialisedField(self, 'RefrHrs', Max35Text, False)

	@RefrHrs.deleter
	def RefrHrs(self):
		del self._RefrHrs
		self._RefrHrs = base_types.UninitialisedField(self, 'RefrHrs', Max35Text, False)

	@property
	def RplcmntCar(self):
		return self._RplcmntCar

	@RplcmntCar.setter
	def RplcmntCar(self, value):
		self._RplcmntCar = value if value is not None else base_types.UninitialisedField(self, 'RplcmntCar', TrueFalseIndicator, False)

	@RplcmntCar.deleter
	def RplcmntCar(self):
		del self._RplcmntCar
		self._RplcmntCar = base_types.UninitialisedField(self, 'RplcmntCar', TrueFalseIndicator, False)

	@property
	def TrlrHrs(self):
		return self._TrlrHrs

	@TrlrHrs.setter
	def TrlrHrs(self, value):
		self._TrlrHrs = value if value is not None else base_types.UninitialisedField(self, 'TrlrHrs', Max35Text, False)

	@TrlrHrs.deleter
	def TrlrHrs(self):
		del self._TrlrHrs
		self._TrlrHrs = base_types.UninitialisedField(self, 'TrlrHrs', Max35Text, False)

	@property
	def TrlrNb(self):
		return self._TrlrNb

	@TrlrNb.setter
	def TrlrNb(self, value):
		self._TrlrNb = value if value is not None else base_types.UninitialisedField(self, 'TrlrNb', Max35NumericText, False)

	@TrlrNb.deleter
	def TrlrNb(self):
		del self._TrlrNb
		self._TrlrNb = base_types.UninitialisedField(self, 'TrlrNb', Max35NumericText, False)

	@property
	def UnitNb(self):
		return self._UnitNb

	@UnitNb.setter
	def UnitNb(self, value):
		self._UnitNb = value if value is not None else base_types.UninitialisedField(self, 'UnitNb', Max35NumericText, False)

	@UnitNb.deleter
	def UnitNb(self):
		del self._UnitNb
		self._UnitNb = base_types.UninitialisedField(self, 'UnitNb', Max35NumericText, False)

	@property
	def VhclNb(self):
		return self._VhclNb

	@VhclNb.setter
	def VhclNb(self, value):
		self._VhclNb = value if value is not None else base_types.UninitialisedField(self, 'VhclNb', Max35NumericText, False)

	@VhclNb.deleter
	def VhclNb(self):
		del self._VhclNb
		self._VhclNb = base_types.UninitialisedField(self, 'VhclNb', Max35NumericText, False)

	@property
	def VhclTag(self):
		return self._VhclTag

	@VhclTag.setter
	def VhclTag(self, value):
		self._VhclTag = value if value is not None else base_types.UninitialisedField(self, 'VhclTag', Max35Text, False)

	@VhclTag.deleter
	def VhclTag(self):
		del self._VhclTag
		self._VhclTag = base_types.UninitialisedField(self, 'VhclTag', Max35Text, False)

	@property
	def VhclTagNtryMd(self):
		return self._VhclTagNtryMd

	@VhclTagNtryMd.setter
	def VhclTagNtryMd(self, value):
		self._VhclTagNtryMd = value if value is not None else base_types.UninitialisedField(self, 'VhclTagNtryMd', CardDataReading5Code, False)

	@VhclTagNtryMd.deleter
	def VhclTagNtryMd(self):
		del self._VhclTagNtryMd
		self._VhclTagNtryMd = base_types.UninitialisedField(self, 'VhclTagNtryMd', CardDataReading5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlVhclData', type=Vehicle2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrvrOrVhclCard', type=PlainCardData17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hbmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Odmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefrHrs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RplcmntCar', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrHrs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclTag', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VhclTagNtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
	))