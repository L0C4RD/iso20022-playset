# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document8
from . import Max2000Text
from . import PlaceOrUnderConfirmationChoice1
from . import PresentationMedium1Choice

class Presentation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Doc", "_Mdm", "_PlcOfPresntnOrUdrConfChc"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if value is not None else base_types.UninitialisedField(self, 'Doc', Document8, True)

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = base_types.UninitialisedField(self, 'Doc', Document8, True)

	@property
	def Mdm(self):
		return self._Mdm

	@Mdm.setter
	def Mdm(self, value):
		self._Mdm = value if value is not None else base_types.UninitialisedField(self, 'Mdm', PresentationMedium1Choice, False)

	@Mdm.deleter
	def Mdm(self):
		del self._Mdm
		self._Mdm = base_types.UninitialisedField(self, 'Mdm', PresentationMedium1Choice, False)

	@property
	def PlcOfPresntnOrUdrConfChc(self):
		return self._PlcOfPresntnOrUdrConfChc

	@PlcOfPresntnOrUdrConfChc.setter
	def PlcOfPresntnOrUdrConfChc(self, value):
		self._PlcOfPresntnOrUdrConfChc = value if value is not None else base_types.UninitialisedField(self, 'PlcOfPresntnOrUdrConfChc', PlaceOrUnderConfirmationChoice1, False)

	@PlcOfPresntnOrUdrConfChc.deleter
	def PlcOfPresntnOrUdrConfChc(self):
		del self._PlcOfPresntnOrUdrConfChc
		self._PlcOfPresntnOrUdrConfChc = base_types.UninitialisedField(self, 'PlcOfPresntnOrUdrConfChc', PlaceOrUnderConfirmationChoice1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Doc', type=Document8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mdm', type=PresentationMedium1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfPresntnOrUdrConfChc', type=PlaceOrUnderConfirmationChoice1, min=0, max=1, mutex_group=None, array=False),
	))