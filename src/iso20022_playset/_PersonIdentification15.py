# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndPlaceOfBirth1
from . import GenericIdentification4
from . import Max256Text
from . import Max35Text

class PersonIdentification15(base_types._BaseFieldType):

	__slots__ = ["_AlnRegnNb", "_CstmrNb", "_Dept", "_DrvrId", "_DrvrLicLctn", "_DrvrLicNb", "_DrvrLicNm", "_DtAndPlcOfBirth", "_EmailAdr", "_IdntyCardNb", "_JobNb", "_MplyeeIdNb", "_MplyrIdNb", "_Othr", "_PsptNb", "_SclSctyNb", "_TaxIdNb"]
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
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if value is not None else base_types.UninitialisedField(self, 'Dept', Max35Text, False)

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = base_types.UninitialisedField(self, 'Dept', Max35Text, False)

	@property
	def DrvrId(self):
		return self._DrvrId

	@DrvrId.setter
	def DrvrId(self, value):
		self._DrvrId = value if value is not None else base_types.UninitialisedField(self, 'DrvrId', Max35Text, False)

	@DrvrId.deleter
	def DrvrId(self):
		del self._DrvrId
		self._DrvrId = base_types.UninitialisedField(self, 'DrvrId', Max35Text, False)

	@property
	def DrvrLicLctn(self):
		return self._DrvrLicLctn

	@DrvrLicLctn.setter
	def DrvrLicLctn(self, value):
		self._DrvrLicLctn = value if value is not None else base_types.UninitialisedField(self, 'DrvrLicLctn', Max35Text, False)

	@DrvrLicLctn.deleter
	def DrvrLicLctn(self):
		del self._DrvrLicLctn
		self._DrvrLicLctn = base_types.UninitialisedField(self, 'DrvrLicLctn', Max35Text, False)

	@property
	def DrvrLicNb(self):
		return self._DrvrLicNb

	@DrvrLicNb.setter
	def DrvrLicNb(self, value):
		self._DrvrLicNb = value if value is not None else base_types.UninitialisedField(self, 'DrvrLicNb', Max35Text, False)

	@DrvrLicNb.deleter
	def DrvrLicNb(self):
		del self._DrvrLicNb
		self._DrvrLicNb = base_types.UninitialisedField(self, 'DrvrLicNb', Max35Text, False)

	@property
	def DrvrLicNm(self):
		return self._DrvrLicNm

	@DrvrLicNm.setter
	def DrvrLicNm(self, value):
		self._DrvrLicNm = value if value is not None else base_types.UninitialisedField(self, 'DrvrLicNm', Max35Text, False)

	@DrvrLicNm.deleter
	def DrvrLicNm(self):
		del self._DrvrLicNm
		self._DrvrLicNm = base_types.UninitialisedField(self, 'DrvrLicNm', Max35Text, False)

	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth1, False)

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth1, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

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
	def JobNb(self):
		return self._JobNb

	@JobNb.setter
	def JobNb(self, value):
		self._JobNb = value if value is not None else base_types.UninitialisedField(self, 'JobNb', Max35Text, False)

	@JobNb.deleter
	def JobNb(self):
		del self._JobNb
		self._JobNb = base_types.UninitialisedField(self, 'JobNb', Max35Text, False)

	@property
	def MplyeeIdNb(self):
		return self._MplyeeIdNb

	@MplyeeIdNb.setter
	def MplyeeIdNb(self, value):
		self._MplyeeIdNb = value if value is not None else base_types.UninitialisedField(self, 'MplyeeIdNb', Max35Text, False)

	@MplyeeIdNb.deleter
	def MplyeeIdNb(self):
		del self._MplyeeIdNb
		self._MplyeeIdNb = base_types.UninitialisedField(self, 'MplyeeIdNb', Max35Text, False)

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
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericIdentification4, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericIdentification4, True)

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
		base_types.FieldEntry(name='AlnRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdntyCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeeIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyrIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PsptNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))