import base_types
import Max35Text
import DateAndPlaceOfBirth1
import Max256Text
import GenericIdentification4

class PersonIdentification15(base_types._BaseFieldType):

	__slots__ = ["_MplyrIdNb", "_SclSctyNb", "_DrvrLicNm", "_TaxIdNb", "_DtAndPlcOfBirth", "_PsptNb", "_DrvrLicLctn", "_MplyeeIdNb", "_CstmrNb", "_AlnRegnNb", "_IdntyCardNb", "_Dept", "_Othr", "_JobNb", "_EmailAdr", "_DrvrLicNb", "_DrvrId"]
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
	def DrvrLicNm(self):
		return self._DrvrLicNm

	@DrvrLicNm.setter
	def DrvrLicNm(self, value):
		self._DrvrLicNm = value if type(value) != auto else self.make_default("DrvrLicNm")

	@DrvrLicNm.deleter
	def DrvrLicNm(self):
		del self._DrvrLicNm
		self._DrvrLicNm = None

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
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if type(value) != auto else self.make_default("DtAndPlcOfBirth")

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = None

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
	def DrvrLicLctn(self):
		return self._DrvrLicLctn

	@DrvrLicLctn.setter
	def DrvrLicLctn(self, value):
		self._DrvrLicLctn = value if type(value) != auto else self.make_default("DrvrLicLctn")

	@DrvrLicLctn.deleter
	def DrvrLicLctn(self):
		del self._DrvrLicLctn
		self._DrvrLicLctn = None

	@property
	def MplyeeIdNb(self):
		return self._MplyeeIdNb

	@MplyeeIdNb.setter
	def MplyeeIdNb(self, value):
		self._MplyeeIdNb = value if type(value) != auto else self.make_default("MplyeeIdNb")

	@MplyeeIdNb.deleter
	def MplyeeIdNb(self):
		del self._MplyeeIdNb
		self._MplyeeIdNb = None

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
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if type(value) != auto else self.make_default("Dept")

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def JobNb(self):
		return self._JobNb

	@JobNb.setter
	def JobNb(self, value):
		self._JobNb = value if type(value) != auto else self.make_default("JobNb")

	@JobNb.deleter
	def JobNb(self):
		del self._JobNb
		self._JobNb = None

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	@property
	def DrvrLicNb(self):
		return self._DrvrLicNb

	@DrvrLicNb.setter
	def DrvrLicNb(self, value):
		self._DrvrLicNb = value if type(value) != auto else self.make_default("DrvrLicNb")

	@DrvrLicNb.deleter
	def DrvrLicNb(self):
		del self._DrvrLicNb
		self._DrvrLicNb = None

	@property
	def DrvrId(self):
		return self._DrvrId

	@DrvrId.setter
	def DrvrId(self, value):
		self._DrvrId = value if type(value) != auto else self.make_default("DrvrId")

	@DrvrId.deleter
	def DrvrId(self):
		del self._DrvrId
		self._DrvrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MplyrIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PsptNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeeIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AlnRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdntyCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='JobNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrLicNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

