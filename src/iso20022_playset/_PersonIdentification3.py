# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndPlaceOfBirth
from . import GenericIdentification4
from . import Max35Text

class PersonIdentification3(base_types._BaseFieldType):

	__slots__ = ["_AlnRegnNb", "_CstmrNb", "_DrvrsLicNb", "_DtAndPlcOfBirth", "_IdntyCardNb", "_Issr", "_MplyrIdNb", "_OthrId", "_PsptNb", "_SclSctyNb", "_TaxIdNb"]
	@property
	def AlnRegnNb(self):
		return self._AlnRegnNb

	@AlnRegnNb.setter
	def AlnRegnNb(self, value):
		self._AlnRegnNb = value if value is not None else base_types.UninitialisedField(self, 'AlnRegnNb', Max35Text, False)

	@AlnRegnNb.deleter
	def AlnRegnNb(self):
		del self._AlnRegnNb
		self._AlnRegnNb = base_types.UninitialisedField(self, 'AlnRegnNb', Max35Text, False)

	@property
	def CstmrNb(self):
		return self._CstmrNb

	@CstmrNb.setter
	def CstmrNb(self, value):
		self._CstmrNb = value if value is not None else base_types.UninitialisedField(self, 'CstmrNb', Max35Text, False)

	@CstmrNb.deleter
	def CstmrNb(self):
		del self._CstmrNb
		self._CstmrNb = base_types.UninitialisedField(self, 'CstmrNb', Max35Text, False)

	@property
	def DrvrsLicNb(self):
		return self._DrvrsLicNb

	@DrvrsLicNb.setter
	def DrvrsLicNb(self, value):
		self._DrvrsLicNb = value if value is not None else base_types.UninitialisedField(self, 'DrvrsLicNb', Max35Text, False)

	@DrvrsLicNb.deleter
	def DrvrsLicNb(self):
		del self._DrvrsLicNb
		self._DrvrsLicNb = base_types.UninitialisedField(self, 'DrvrsLicNb', Max35Text, False)

	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth, False)

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth, False)

	@property
	def IdntyCardNb(self):
		return self._IdntyCardNb

	@IdntyCardNb.setter
	def IdntyCardNb(self, value):
		self._IdntyCardNb = value if value is not None else base_types.UninitialisedField(self, 'IdntyCardNb', Max35Text, False)

	@IdntyCardNb.deleter
	def IdntyCardNb(self):
		del self._IdntyCardNb
		self._IdntyCardNb = base_types.UninitialisedField(self, 'IdntyCardNb', Max35Text, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	@property
	def MplyrIdNb(self):
		return self._MplyrIdNb

	@MplyrIdNb.setter
	def MplyrIdNb(self, value):
		self._MplyrIdNb = value if value is not None else base_types.UninitialisedField(self, 'MplyrIdNb', Max35Text, False)

	@MplyrIdNb.deleter
	def MplyrIdNb(self):
		del self._MplyrIdNb
		self._MplyrIdNb = base_types.UninitialisedField(self, 'MplyrIdNb', Max35Text, False)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', GenericIdentification4, False)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', GenericIdentification4, False)

	@property
	def PsptNb(self):
		return self._PsptNb

	@PsptNb.setter
	def PsptNb(self, value):
		self._PsptNb = value if value is not None else base_types.UninitialisedField(self, 'PsptNb', Max35Text, False)

	@PsptNb.deleter
	def PsptNb(self):
		del self._PsptNb
		self._PsptNb = base_types.UninitialisedField(self, 'PsptNb', Max35Text, False)

	@property
	def SclSctyNb(self):
		return self._SclSctyNb

	@SclSctyNb.setter
	def SclSctyNb(self, value):
		self._SclSctyNb = value if value is not None else base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	@SclSctyNb.deleter
	def SclSctyNb(self):
		del self._SclSctyNb
		self._SclSctyNb = base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if value is not None else base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AlnRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CstmrNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrvrsLicNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdntyCardNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyrIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PsptNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))