from . import base_types
import Vehicle2
import Max10Text
import OnBoardDiagnostics1
import Max35Text
import Max35NumericText
import TrueFalseIndicator
import DecimalNumber
import CardDataReading5Code

class Vehicle6(base_types._BaseFieldType):

	__slots__ = ["_FleetNb", "_TagNtryMd", "_SubFleetNb", "_Tag", "_MntncId", "_UnitNb", "_IdNb", "_Rplcmnt", "_Nb", "_TrlrNb", "_OnBrdDgnstcs", "_Hbmtr", "_AddtlData", "_Odmtr"]
	@property
	def FleetNb(self):
		return self._FleetNb

	@FleetNb.setter
	def FleetNb(self, value):
		self._FleetNb = value if type(value) != auto else self.make_default("FleetNb")

	@FleetNb.deleter
	def FleetNb(self):
		del self._FleetNb
		self._FleetNb = None

	@property
	def TagNtryMd(self):
		return self._TagNtryMd

	@TagNtryMd.setter
	def TagNtryMd(self, value):
		self._TagNtryMd = value if type(value) != auto else self.make_default("TagNtryMd")

	@TagNtryMd.deleter
	def TagNtryMd(self):
		del self._TagNtryMd
		self._TagNtryMd = None

	@property
	def SubFleetNb(self):
		return self._SubFleetNb

	@SubFleetNb.setter
	def SubFleetNb(self, value):
		self._SubFleetNb = value if type(value) != auto else self.make_default("SubFleetNb")

	@SubFleetNb.deleter
	def SubFleetNb(self):
		del self._SubFleetNb
		self._SubFleetNb = None

	@property
	def Tag(self):
		return self._Tag

	@Tag.setter
	def Tag(self, value):
		self._Tag = value if type(value) != auto else self.make_default("Tag")

	@Tag.deleter
	def Tag(self):
		del self._Tag
		self._Tag = None

	@property
	def MntncId(self):
		return self._MntncId

	@MntncId.setter
	def MntncId(self, value):
		self._MntncId = value if type(value) != auto else self.make_default("MntncId")

	@MntncId.deleter
	def MntncId(self):
		del self._MntncId
		self._MntncId = None

	@property
	def UnitNb(self):
		return self._UnitNb

	@UnitNb.setter
	def UnitNb(self, value):
		self._UnitNb = value if type(value) != auto else self.make_default("UnitNb")

	@UnitNb.deleter
	def UnitNb(self):
		del self._UnitNb
		self._UnitNb = None

	@property
	def IdNb(self):
		return self._IdNb

	@IdNb.setter
	def IdNb(self, value):
		self._IdNb = value if type(value) != auto else self.make_default("IdNb")

	@IdNb.deleter
	def IdNb(self):
		del self._IdNb
		self._IdNb = None

	@property
	def Rplcmnt(self):
		return self._Rplcmnt

	@Rplcmnt.setter
	def Rplcmnt(self, value):
		self._Rplcmnt = value if type(value) != auto else self.make_default("Rplcmnt")

	@Rplcmnt.deleter
	def Rplcmnt(self):
		del self._Rplcmnt
		self._Rplcmnt = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def TrlrNb(self):
		return self._TrlrNb

	@TrlrNb.setter
	def TrlrNb(self, value):
		self._TrlrNb = value if type(value) != auto else self.make_default("TrlrNb")

	@TrlrNb.deleter
	def TrlrNb(self):
		del self._TrlrNb
		self._TrlrNb = None

	@property
	def OnBrdDgnstcs(self):
		return self._OnBrdDgnstcs

	@OnBrdDgnstcs.setter
	def OnBrdDgnstcs(self, value):
		self._OnBrdDgnstcs = value if type(value) != auto else self.make_default("OnBrdDgnstcs")

	@OnBrdDgnstcs.deleter
	def OnBrdDgnstcs(self):
		del self._OnBrdDgnstcs
		self._OnBrdDgnstcs = None

	@property
	def Hbmtr(self):
		return self._Hbmtr

	@Hbmtr.setter
	def Hbmtr(self, value):
		self._Hbmtr = value if type(value) != auto else self.make_default("Hbmtr")

	@Hbmtr.deleter
	def Hbmtr(self):
		del self._Hbmtr
		self._Hbmtr = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def Odmtr(self):
		return self._Odmtr

	@Odmtr.setter
	def Odmtr(self, value):
		self._Odmtr = value if type(value) != auto else self.make_default("Odmtr")

	@Odmtr.deleter
	def Odmtr(self):
		del self._Odmtr
		self._Odmtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FleetNb', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TagNtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubFleetNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tag', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rplcmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnBrdDgnstcs', type=OnBoardDiagnostics1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hbmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=Vehicle2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Odmtr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

