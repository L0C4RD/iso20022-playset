from . import base_types
from .PresentationMedium1Choice import PresentationMedium1Choice
from .PlaceOrUnderConfirmationChoice1 import PlaceOrUnderConfirmationChoice1
from .Max2000Text import Max2000Text
from .Document8 import Document8

class Presentation1(base_types._BaseFieldType):

	__slots__ = ["_PlcOfPresntnOrUdrConfChc", "_Mdm", "_AddtlInf", "_Doc"]
	@property
	def PlcOfPresntnOrUdrConfChc(self):
		return self._PlcOfPresntnOrUdrConfChc

	@PlcOfPresntnOrUdrConfChc.setter
	def PlcOfPresntnOrUdrConfChc(self, value):
		self._PlcOfPresntnOrUdrConfChc = value if type(value) != base_types.auto else self.make_default("PlcOfPresntnOrUdrConfChc")

	@PlcOfPresntnOrUdrConfChc.deleter
	def PlcOfPresntnOrUdrConfChc(self):
		del self._PlcOfPresntnOrUdrConfChc
		self._PlcOfPresntnOrUdrConfChc = None

	@property
	def Mdm(self):
		return self._Mdm

	@Mdm.setter
	def Mdm(self, value):
		self._Mdm = value if type(value) != base_types.auto else self.make_default("Mdm")

	@Mdm.deleter
	def Mdm(self):
		del self._Mdm
		self._Mdm = None

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
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if type(value) != base_types.auto else self.make_default("Doc")

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfPresntnOrUdrConfChc', type=PlaceOrUnderConfirmationChoice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdm', type=PresentationMedium1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Doc', type=Document8, min=0, max=None, mutex_group=None, array=True),
	))

