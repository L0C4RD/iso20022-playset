# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType14
from . import Max35Text

class ATMEquipment3(base_types._BaseFieldType):

	__slots__ = ["_FrmwrId", "_FrmwrPrvdr", "_FrmwrVrsn", "_Manfctr", "_Mdl", "_SgndSrlNb", "_SrlNb", "_Vrsn"]
	@property
	def FrmwrId(self):
		return self._FrmwrId

	@FrmwrId.setter
	def FrmwrId(self, value):
		self._FrmwrId = value if value is not None else base_types.UninitialisedField(self, 'FrmwrId', Max35Text, False)

	@FrmwrId.deleter
	def FrmwrId(self):
		del self._FrmwrId
		self._FrmwrId = base_types.UninitialisedField(self, 'FrmwrId', Max35Text, False)

	@property
	def FrmwrPrvdr(self):
		return self._FrmwrPrvdr

	@FrmwrPrvdr.setter
	def FrmwrPrvdr(self, value):
		self._FrmwrPrvdr = value if value is not None else base_types.UninitialisedField(self, 'FrmwrPrvdr', Max35Text, False)

	@FrmwrPrvdr.deleter
	def FrmwrPrvdr(self):
		del self._FrmwrPrvdr
		self._FrmwrPrvdr = base_types.UninitialisedField(self, 'FrmwrPrvdr', Max35Text, False)

	@property
	def FrmwrVrsn(self):
		return self._FrmwrVrsn

	@FrmwrVrsn.setter
	def FrmwrVrsn(self, value):
		self._FrmwrVrsn = value if value is not None else base_types.UninitialisedField(self, 'FrmwrVrsn', Max35Text, False)

	@FrmwrVrsn.deleter
	def FrmwrVrsn(self):
		del self._FrmwrVrsn
		self._FrmwrVrsn = base_types.UninitialisedField(self, 'FrmwrVrsn', Max35Text, False)

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
	def SgndSrlNb(self):
		return self._SgndSrlNb

	@SgndSrlNb.setter
	def SgndSrlNb(self, value):
		self._SgndSrlNb = value if value is not None else base_types.UninitialisedField(self, 'SgndSrlNb', ContentInformationType14, False)

	@SgndSrlNb.deleter
	def SgndSrlNb(self):
		del self._SgndSrlNb
		self._SgndSrlNb = base_types.UninitialisedField(self, 'SgndSrlNb', ContentInformationType14, False)

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
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max35Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrmwrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmwrPrvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmwrVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Manfctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndSrlNb', type=ContentInformationType14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))