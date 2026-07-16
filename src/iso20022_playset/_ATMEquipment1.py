# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMConfigurationParameter1
from . import Max35Text

class ATMEquipment1(base_types._BaseFieldType):

	__slots__ = ["_ApplNm", "_ApplPrvdr", "_ApplVrsn", "_ApprvlNb", "_CfgtnParam", "_Manfctr", "_Mdl", "_SrlNb"]
	@property
	def ApplNm(self):
		return self._ApplNm

	@ApplNm.setter
	def ApplNm(self, value):
		self._ApplNm = value if value is not None else base_types.UninitialisedField(self, 'ApplNm', Max35Text, False)

	@ApplNm.deleter
	def ApplNm(self):
		del self._ApplNm
		self._ApplNm = base_types.UninitialisedField(self, 'ApplNm', Max35Text, False)

	@property
	def ApplPrvdr(self):
		return self._ApplPrvdr

	@ApplPrvdr.setter
	def ApplPrvdr(self, value):
		self._ApplPrvdr = value if value is not None else base_types.UninitialisedField(self, 'ApplPrvdr', Max35Text, False)

	@ApplPrvdr.deleter
	def ApplPrvdr(self):
		del self._ApplPrvdr
		self._ApplPrvdr = base_types.UninitialisedField(self, 'ApplPrvdr', Max35Text, False)

	@property
	def ApplVrsn(self):
		return self._ApplVrsn

	@ApplVrsn.setter
	def ApplVrsn(self, value):
		self._ApplVrsn = value if value is not None else base_types.UninitialisedField(self, 'ApplVrsn', Max35Text, False)

	@ApplVrsn.deleter
	def ApplVrsn(self):
		del self._ApplVrsn
		self._ApplVrsn = base_types.UninitialisedField(self, 'ApplVrsn', Max35Text, False)

	@property
	def ApprvlNb(self):
		return self._ApprvlNb

	@ApprvlNb.setter
	def ApprvlNb(self, value):
		self._ApprvlNb = value if value is not None else base_types.UninitialisedField(self, 'ApprvlNb', Max35Text, False)

	@ApprvlNb.deleter
	def ApprvlNb(self):
		del self._ApprvlNb
		self._ApprvlNb = base_types.UninitialisedField(self, 'ApprvlNb', Max35Text, False)

	@property
	def CfgtnParam(self):
		return self._CfgtnParam

	@CfgtnParam.setter
	def CfgtnParam(self, value):
		self._CfgtnParam = value if value is not None else base_types.UninitialisedField(self, 'CfgtnParam', ATMConfigurationParameter1, True)

	@CfgtnParam.deleter
	def CfgtnParam(self):
		del self._CfgtnParam
		self._CfgtnParam = base_types.UninitialisedField(self, 'CfgtnParam', ATMConfigurationParameter1, True)

	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if value is not None else base_types.UninitialisedField(self, 'Manfctr', Max35Text, False)

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = base_types.UninitialisedField(self, 'Manfctr', Max35Text, False)

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if value is not None else base_types.UninitialisedField(self, 'Mdl', Max35Text, False)

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = base_types.UninitialisedField(self, 'Mdl', Max35Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplPrvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CfgtnParam', type=ATMConfigurationParameter1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Manfctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))