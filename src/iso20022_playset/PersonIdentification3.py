import base_types
import Max35Text
import DateAndPlaceOfBirth
import GenericIdentification4

class PersonIdentification3(base_types._BaseFieldType):

	__slots__ = ["_AlnRegnNb", "_SclSctyNb", "_TaxIdNb", "_IdntyCardNb", "_PsptNb", "_OthrId", "_MplyrIdNb", "_CstmrNb", "_DrvrsLicNb", "_Issr", "_DtAndPlcOfBirth"]
	@property
	def AlnRegnNb(self):
		return self._AlnRegnNb

	@AlnRegnNb.setter
	def AlnRegnNb(self, value):
		self._AlnRegnNb = value if type(value) != auto else self.make_default("AlnRegnNb")

	@AlnRegnNb.deleter
	def AlnRegnNb(self):
		del self._AlnRegnNb
		self._AlnRegnNb = None

	@property
	def SclSctyNb(self):
		return self._SclSctyNb

	@SclSctyNb.setter
	def SclSctyNb(self, value):
		self._SclSctyNb = value if type(value) != auto else self.make_default("SclSctyNb")

	@SclSctyNb.deleter
	def SclSctyNb(self):
		del self._SclSctyNb
		self._SclSctyNb = None

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if type(value) != auto else self.make_default("TaxIdNb")

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = None

	@property
	def IdntyCardNb(self):
		return self._IdntyCardNb

	@IdntyCardNb.setter
	def IdntyCardNb(self, value):
		self._IdntyCardNb = value if type(value) != auto else self.make_default("IdntyCardNb")

	@IdntyCardNb.deleter
	def IdntyCardNb(self):
		del self._IdntyCardNb
		self._IdntyCardNb = None

	@property
	def PsptNb(self):
		return self._PsptNb

	@PsptNb.setter
	def PsptNb(self, value):
		self._PsptNb = value if type(value) != auto else self.make_default("PsptNb")

	@PsptNb.deleter
	def PsptNb(self):
		del self._PsptNb
		self._PsptNb = None

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if type(value) != auto else self.make_default("OthrId")

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = None

	@property
	def MplyrIdNb(self):
		return self._MplyrIdNb

	@MplyrIdNb.setter
	def MplyrIdNb(self, value):
		self._MplyrIdNb = value if type(value) != auto else self.make_default("MplyrIdNb")

	@MplyrIdNb.deleter
	def MplyrIdNb(self):
		del self._MplyrIdNb
		self._MplyrIdNb = None

	@property
	def CstmrNb(self):
		return self._CstmrNb

	@CstmrNb.setter
	def CstmrNb(self, value):
		self._CstmrNb = value if type(value) != auto else self.make_default("CstmrNb")

	@CstmrNb.deleter
	def CstmrNb(self):
		del self._CstmrNb
		self._CstmrNb = None

	@property
	def DrvrsLicNb(self):
		return self._DrvrsLicNb

	@DrvrsLicNb.setter
	def DrvrsLicNb(self, value):
		self._DrvrsLicNb = value if type(value) != auto else self.make_default("DrvrsLicNb")

	@DrvrsLicNb.deleter
	def DrvrsLicNb(self):
		del self._DrvrsLicNb
		self._DrvrsLicNb = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if type(value) != auto else self.make_default("DtAndPlcOfBirth")

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AlnRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdntyCardNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PsptNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MplyrIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CstmrNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrvrsLicNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth, min=0, max=1, mutex_group=1, array=False),
	))

