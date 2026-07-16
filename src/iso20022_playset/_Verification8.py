# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ExternalAuthenticationMethod1Code
from . import Max35Text
from . import PINData1
from . import Verification4Code
from . import VerificationEntity3Code
from . import VerificationValue1

class Verification8(base_types._BaseFieldType):

	__slots__ = ["_Data", "_Ntty", "_PINData", "_Rslt", "_RsltDtls", "_SubTp", "_Tp"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', VerificationValue1, True)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', VerificationValue1, True)

	@property
	def Ntty(self):
		return self._Ntty

	@Ntty.setter
	def Ntty(self, value):
		self._Ntty = value if value is not None else base_types.UninitialisedField(self, 'Ntty', VerificationEntity3Code, False)

	@Ntty.deleter
	def Ntty(self):
		del self._Ntty
		self._Ntty = base_types.UninitialisedField(self, 'Ntty', VerificationEntity3Code, False)

	@property
	def PINData(self):
		return self._PINData

	@PINData.setter
	def PINData(self, value):
		self._PINData = value if value is not None else base_types.UninitialisedField(self, 'PINData', PINData1, False)

	@PINData.deleter
	def PINData(self):
		del self._PINData
		self._PINData = base_types.UninitialisedField(self, 'PINData', PINData1, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Verification4Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Verification4Code, False)

	@property
	def RsltDtls(self):
		return self._RsltDtls

	@RsltDtls.setter
	def RsltDtls(self, value):
		self._RsltDtls = value if value is not None else base_types.UninitialisedField(self, 'RsltDtls', ATICALaxProcessing, False)

	@RsltDtls.deleter
	def RsltDtls(self):
		del self._RsltDtls
		self._RsltDtls = base_types.UninitialisedField(self, 'RsltDtls', ATICALaxProcessing, False)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', Max35Text, False)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ExternalAuthenticationMethod1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ExternalAuthenticationMethod1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=VerificationValue1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntty', type=VerificationEntity3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINData', type=PINData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltDtls', type=ATICALaxProcessing, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ExternalAuthenticationMethod1Code, min=0, max=1, mutex_group=None, array=False),
	))