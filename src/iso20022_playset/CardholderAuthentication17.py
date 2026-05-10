from . import base_types
import AuthenticationMethod8Code
import ExternallyDefinedData5
import AuthenticationResult1Code
import Exemption1Code
import ContentInformationType40
import Max5000Binary
import PersonIdentification15
import Max35Text
import OnLinePIN11
import AddressVerification1

class CardholderAuthentication17(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrId", "_AuthntcnRslt", "_AdrVrfctn", "_AuthntcnAddtlInf", "_AuthntcnLvl", "_AuthntcnMtd", "_AuthntcnXmptn", "_CrdhldrOnLinePIN", "_AuthntcnTp", "_PrtctdAuthntcnVal", "_AuthntcnVal"]
	@property
	def CrdhldrId(self):
		return self._CrdhldrId

	@CrdhldrId.setter
	def CrdhldrId(self, value):
		self._CrdhldrId = value if type(value) != auto else self.make_default("CrdhldrId")

	@CrdhldrId.deleter
	def CrdhldrId(self):
		del self._CrdhldrId
		self._CrdhldrId = None

	@property
	def AuthntcnRslt(self):
		return self._AuthntcnRslt

	@AuthntcnRslt.setter
	def AuthntcnRslt(self, value):
		self._AuthntcnRslt = value if type(value) != auto else self.make_default("AuthntcnRslt")

	@AuthntcnRslt.deleter
	def AuthntcnRslt(self):
		del self._AuthntcnRslt
		self._AuthntcnRslt = None

	@property
	def AdrVrfctn(self):
		return self._AdrVrfctn

	@AdrVrfctn.setter
	def AdrVrfctn(self, value):
		self._AdrVrfctn = value if type(value) != auto else self.make_default("AdrVrfctn")

	@AdrVrfctn.deleter
	def AdrVrfctn(self):
		del self._AdrVrfctn
		self._AdrVrfctn = None

	@property
	def AuthntcnAddtlInf(self):
		return self._AuthntcnAddtlInf

	@AuthntcnAddtlInf.setter
	def AuthntcnAddtlInf(self, value):
		self._AuthntcnAddtlInf = value if type(value) != auto else self.make_default("AuthntcnAddtlInf")

	@AuthntcnAddtlInf.deleter
	def AuthntcnAddtlInf(self):
		del self._AuthntcnAddtlInf
		self._AuthntcnAddtlInf = None

	@property
	def AuthntcnLvl(self):
		return self._AuthntcnLvl

	@AuthntcnLvl.setter
	def AuthntcnLvl(self, value):
		self._AuthntcnLvl = value if type(value) != auto else self.make_default("AuthntcnLvl")

	@AuthntcnLvl.deleter
	def AuthntcnLvl(self):
		del self._AuthntcnLvl
		self._AuthntcnLvl = None

	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if type(value) != auto else self.make_default("AuthntcnMtd")

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = None

	@property
	def AuthntcnXmptn(self):
		return self._AuthntcnXmptn

	@AuthntcnXmptn.setter
	def AuthntcnXmptn(self, value):
		self._AuthntcnXmptn = value if type(value) != auto else self.make_default("AuthntcnXmptn")

	@AuthntcnXmptn.deleter
	def AuthntcnXmptn(self):
		del self._AuthntcnXmptn
		self._AuthntcnXmptn = None

	@property
	def CrdhldrOnLinePIN(self):
		return self._CrdhldrOnLinePIN

	@CrdhldrOnLinePIN.setter
	def CrdhldrOnLinePIN(self, value):
		self._CrdhldrOnLinePIN = value if type(value) != auto else self.make_default("CrdhldrOnLinePIN")

	@CrdhldrOnLinePIN.deleter
	def CrdhldrOnLinePIN(self):
		del self._CrdhldrOnLinePIN
		self._CrdhldrOnLinePIN = None

	@property
	def AuthntcnTp(self):
		return self._AuthntcnTp

	@AuthntcnTp.setter
	def AuthntcnTp(self, value):
		self._AuthntcnTp = value if type(value) != auto else self.make_default("AuthntcnTp")

	@AuthntcnTp.deleter
	def AuthntcnTp(self):
		del self._AuthntcnTp
		self._AuthntcnTp = None

	@property
	def PrtctdAuthntcnVal(self):
		return self._PrtctdAuthntcnVal

	@PrtctdAuthntcnVal.setter
	def PrtctdAuthntcnVal(self, value):
		self._PrtctdAuthntcnVal = value if type(value) != auto else self.make_default("PrtctdAuthntcnVal")

	@PrtctdAuthntcnVal.deleter
	def PrtctdAuthntcnVal(self):
		del self._PrtctdAuthntcnVal
		self._PrtctdAuthntcnVal = None

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if type(value) != auto else self.make_default("AuthntcnVal")

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrdhldrId', type=PersonIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnRslt', type=AuthenticationResult1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrVrfctn', type=AddressVerification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnAddtlInf', type=ExternallyDefinedData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnXmptn', type=Exemption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrOnLinePIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAuthntcnVal', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
	))

