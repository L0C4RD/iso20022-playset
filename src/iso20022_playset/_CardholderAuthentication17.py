# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressVerification1
from . import AuthenticationMethod8Code
from . import AuthenticationResult1Code
from . import ContentInformationType40
from . import Exemption1Code
from . import ExternallyDefinedData5
from . import Max35Text
from . import Max5000Binary
from . import OnLinePIN11
from . import PersonIdentification15

class CardholderAuthentication17(base_types._BaseFieldType):

	__slots__ = ["_AdrVrfctn", "_AuthntcnAddtlInf", "_AuthntcnLvl", "_AuthntcnMtd", "_AuthntcnRslt", "_AuthntcnTp", "_AuthntcnVal", "_AuthntcnXmptn", "_CrdhldrId", "_CrdhldrOnLinePIN", "_PrtctdAuthntcnVal"]
	@property
	def AdrVrfctn(self):
		return self._AdrVrfctn

	@AdrVrfctn.setter
	def AdrVrfctn(self, value):
		self._AdrVrfctn = value if value is not None else base_types.UninitialisedField(self, 'AdrVrfctn', AddressVerification1, False)

	@AdrVrfctn.deleter
	def AdrVrfctn(self):
		del self._AdrVrfctn
		self._AdrVrfctn = base_types.UninitialisedField(self, 'AdrVrfctn', AddressVerification1, False)

	@property
	def AuthntcnAddtlInf(self):
		return self._AuthntcnAddtlInf

	@AuthntcnAddtlInf.setter
	def AuthntcnAddtlInf(self, value):
		self._AuthntcnAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnAddtlInf', ExternallyDefinedData5, False)

	@AuthntcnAddtlInf.deleter
	def AuthntcnAddtlInf(self):
		del self._AuthntcnAddtlInf
		self._AuthntcnAddtlInf = base_types.UninitialisedField(self, 'AuthntcnAddtlInf', ExternallyDefinedData5, False)

	@property
	def AuthntcnLvl(self):
		return self._AuthntcnLvl

	@AuthntcnLvl.setter
	def AuthntcnLvl(self, value):
		self._AuthntcnLvl = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnLvl', Max35Text, False)

	@AuthntcnLvl.deleter
	def AuthntcnLvl(self):
		del self._AuthntcnLvl
		self._AuthntcnLvl = base_types.UninitialisedField(self, 'AuthntcnLvl', Max35Text, False)

	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod8Code, False)

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod8Code, False)

	@property
	def AuthntcnRslt(self):
		return self._AuthntcnRslt

	@AuthntcnRslt.setter
	def AuthntcnRslt(self, value):
		self._AuthntcnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnRslt', AuthenticationResult1Code, False)

	@AuthntcnRslt.deleter
	def AuthntcnRslt(self):
		del self._AuthntcnRslt
		self._AuthntcnRslt = base_types.UninitialisedField(self, 'AuthntcnRslt', AuthenticationResult1Code, False)

	@property
	def AuthntcnTp(self):
		return self._AuthntcnTp

	@AuthntcnTp.setter
	def AuthntcnTp(self, value):
		self._AuthntcnTp = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnTp', Max35Text, False)

	@AuthntcnTp.deleter
	def AuthntcnTp(self):
		del self._AuthntcnTp
		self._AuthntcnTp = base_types.UninitialisedField(self, 'AuthntcnTp', Max35Text, False)

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnVal', Max5000Binary, False)

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = base_types.UninitialisedField(self, 'AuthntcnVal', Max5000Binary, False)

	@property
	def AuthntcnXmptn(self):
		return self._AuthntcnXmptn

	@AuthntcnXmptn.setter
	def AuthntcnXmptn(self, value):
		self._AuthntcnXmptn = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnXmptn', Exemption1Code, False)

	@AuthntcnXmptn.deleter
	def AuthntcnXmptn(self):
		del self._AuthntcnXmptn
		self._AuthntcnXmptn = base_types.UninitialisedField(self, 'AuthntcnXmptn', Exemption1Code, False)

	@property
	def CrdhldrId(self):
		return self._CrdhldrId

	@CrdhldrId.setter
	def CrdhldrId(self, value):
		self._CrdhldrId = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrId', PersonIdentification15, False)

	@CrdhldrId.deleter
	def CrdhldrId(self):
		del self._CrdhldrId
		self._CrdhldrId = base_types.UninitialisedField(self, 'CrdhldrId', PersonIdentification15, False)

	@property
	def CrdhldrOnLinePIN(self):
		return self._CrdhldrOnLinePIN

	@CrdhldrOnLinePIN.setter
	def CrdhldrOnLinePIN(self, value):
		self._CrdhldrOnLinePIN = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrOnLinePIN', OnLinePIN11, False)

	@CrdhldrOnLinePIN.deleter
	def CrdhldrOnLinePIN(self):
		del self._CrdhldrOnLinePIN
		self._CrdhldrOnLinePIN = base_types.UninitialisedField(self, 'CrdhldrOnLinePIN', OnLinePIN11, False)

	@property
	def PrtctdAuthntcnVal(self):
		return self._PrtctdAuthntcnVal

	@PrtctdAuthntcnVal.setter
	def PrtctdAuthntcnVal(self, value):
		self._PrtctdAuthntcnVal = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAuthntcnVal', ContentInformationType40, False)

	@PrtctdAuthntcnVal.deleter
	def PrtctdAuthntcnVal(self):
		del self._PrtctdAuthntcnVal
		self._PrtctdAuthntcnVal = base_types.UninitialisedField(self, 'PrtctdAuthntcnVal', ContentInformationType40, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrVrfctn', type=AddressVerification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnAddtlInf', type=ExternallyDefinedData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnRslt', type=AuthenticationResult1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnXmptn', type=Exemption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrId', type=PersonIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrOnLinePIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAuthntcnVal', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
	))