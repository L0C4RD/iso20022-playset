# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassetteCounters6
from . import ATMCassetteStatus1Code
from . import ATMCassetteType1Code
from . import ATMMediaType4Code
from . import ATMNoteType1Code
from . import Max35Text

class ATMCassette3(base_types._BaseFieldType):

	__slots__ = ["_CssttSts", "_LogclId", "_MdiaCntrs", "_MdiaTp", "_PhysId", "_SrlNb", "_SubTp", "_Tp"]
	@property
	def CssttSts(self):
		return self._CssttSts

	@CssttSts.setter
	def CssttSts(self, value):
		self._CssttSts = value if value is not None else base_types.UninitialisedField(self, 'CssttSts', ATMCassetteStatus1Code, False)

	@CssttSts.deleter
	def CssttSts(self):
		del self._CssttSts
		self._CssttSts = base_types.UninitialisedField(self, 'CssttSts', ATMCassetteStatus1Code, False)

	@property
	def LogclId(self):
		return self._LogclId

	@LogclId.setter
	def LogclId(self, value):
		self._LogclId = value if value is not None else base_types.UninitialisedField(self, 'LogclId', Max35Text, False)

	@LogclId.deleter
	def LogclId(self):
		del self._LogclId
		self._LogclId = base_types.UninitialisedField(self, 'LogclId', Max35Text, False)

	@property
	def MdiaCntrs(self):
		return self._MdiaCntrs

	@MdiaCntrs.setter
	def MdiaCntrs(self, value):
		self._MdiaCntrs = value if value is not None else base_types.UninitialisedField(self, 'MdiaCntrs', ATMCassetteCounters6, True)

	@MdiaCntrs.deleter
	def MdiaCntrs(self):
		del self._MdiaCntrs
		self._MdiaCntrs = base_types.UninitialisedField(self, 'MdiaCntrs', ATMCassetteCounters6, True)

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if value is not None else base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@property
	def PhysId(self):
		return self._PhysId

	@PhysId.setter
	def PhysId(self, value):
		self._PhysId = value if value is not None else base_types.UninitialisedField(self, 'PhysId', Max35Text, False)

	@PhysId.deleter
	def PhysId(self):
		del self._PhysId
		self._PhysId = base_types.UninitialisedField(self, 'PhysId', Max35Text, False)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', ATMNoteType1Code, True)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', ATMNoteType1Code, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ATMCassetteType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ATMCassetteType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CssttSts', type=ATMCassetteStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LogclId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaCntrs', type=ATMCassetteCounters6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=ATMNoteType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ATMCassetteType1Code, min=1, max=1, mutex_group=None, array=False),
	))