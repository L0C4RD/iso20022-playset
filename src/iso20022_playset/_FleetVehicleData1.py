# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import CardDataReading5Code
from . import DecimalNumber
from . import Max10Text
from . import Max35NumericText
from . import Max35Text
from . import OnBoardDiagnostics1
from . import TrueFalseIndicator
from . import Vehicle2

class FleetVehicleData1(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_FleetNb", "_Hbmtr", "_IdNb", "_MntncId", "_Nb", "_NtlData", "_Odmtr", "_OnBrdDgnstcs", "_PrvtData", "_Rplcmnt", "_SubFleetNb", "_Tag", "_TagNtryMd", "_TrlrNb", "_UnitNb"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', Vehicle2, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', Vehicle2, True)

	@property
	def FleetNb(self):
		return self._FleetNb

	@FleetNb.setter
	def FleetNb(self, value):
		self._FleetNb = value if value is not None else base_types.UninitialisedField(self, 'FleetNb', Max10Text, False)

	@FleetNb.deleter
	def FleetNb(self):
		del self._FleetNb
		self._FleetNb = base_types.UninitialisedField(self, 'FleetNb', Max10Text, False)

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
	def IdNb(self):
		return self._IdNb

	@IdNb.setter
	def IdNb(self, value):
		self._IdNb = value if value is not None else base_types.UninitialisedField(self, 'IdNb', Max35NumericText, False)

	@IdNb.deleter
	def IdNb(self):
		del self._IdNb
		self._IdNb = base_types.UninitialisedField(self, 'IdNb', Max35NumericText, False)

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
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35NumericText, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35NumericText, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

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
	def OnBrdDgnstcs(self):
		return self._OnBrdDgnstcs

	@OnBrdDgnstcs.setter
	def OnBrdDgnstcs(self, value):
		self._OnBrdDgnstcs = value if value is not None else base_types.UninitialisedField(self, 'OnBrdDgnstcs', OnBoardDiagnostics1, False)

	@OnBrdDgnstcs.deleter
	def OnBrdDgnstcs(self):
		del self._OnBrdDgnstcs
		self._OnBrdDgnstcs = base_types.UninitialisedField(self, 'OnBrdDgnstcs', OnBoardDiagnostics1, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def Rplcmnt(self):
		return self._Rplcmnt

	@Rplcmnt.setter
	def Rplcmnt(self, value):
		self._Rplcmnt = value if value is not None else base_types.UninitialisedField(self, 'Rplcmnt', TrueFalseIndicator, False)

	@Rplcmnt.deleter
	def Rplcmnt(self):
		del self._Rplcmnt
		self._Rplcmnt = base_types.UninitialisedField(self, 'Rplcmnt', TrueFalseIndicator, False)

	@property
	def SubFleetNb(self):
		return self._SubFleetNb

	@SubFleetNb.setter
	def SubFleetNb(self, value):
		self._SubFleetNb = value if value is not None else base_types.UninitialisedField(self, 'SubFleetNb', Max35Text, False)

	@SubFleetNb.deleter
	def SubFleetNb(self):
		del self._SubFleetNb
		self._SubFleetNb = base_types.UninitialisedField(self, 'SubFleetNb', Max35Text, False)

	@property
	def Tag(self):
		return self._Tag

	@Tag.setter
	def Tag(self, value):
		self._Tag = value if value is not None else base_types.UninitialisedField(self, 'Tag', Max35Text, False)

	@Tag.deleter
	def Tag(self):
		del self._Tag
		self._Tag = base_types.UninitialisedField(self, 'Tag', Max35Text, False)

	@property
	def TagNtryMd(self):
		return self._TagNtryMd

	@TagNtryMd.setter
	def TagNtryMd(self, value):
		self._TagNtryMd = value if value is not None else base_types.UninitialisedField(self, 'TagNtryMd', CardDataReading5Code, False)

	@TagNtryMd.deleter
	def TagNtryMd(self):
		del self._TagNtryMd
		self._TagNtryMd = base_types.UninitialisedField(self, 'TagNtryMd', CardDataReading5Code, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=Vehicle2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FleetNb', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hbmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Odmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnBrdDgnstcs', type=OnBoardDiagnostics1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rplcmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubFleetNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tag', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TagNtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))